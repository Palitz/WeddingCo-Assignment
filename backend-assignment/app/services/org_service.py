from datetime import datetime
from fastapi import HTTPException, status
from app.core.database import get_master_db, db
from app.models.schemas import OrgCreateRequest, OrgResponse, OrgUpdateRequest
from app.core.security import get_password_hash
from app.core.config import settings

class OrganizationService:
    def __init__(self):
        self.master_db = get_master_db()
        self.collection = self.master_db.organizations

    async def create_organization(self, data: OrgCreateRequest) -> OrgResponse:
        # 1. Validate: Check if Org already exists
        existing_org = await self.collection.find_one({"organization_name": data.organization_name})
        if existing_org:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Organization '{data.organization_name}' already exists."
            )

        # 2. Dynamic Collection Name
        # Replaces spaces with underscores for safety
        clean_name = data.organization_name.lower().replace(" ", "_")
        dynamic_collection_name = f"org_{clean_name}"

        # 3. Dynamic Collection Creation (The Requirement)
        # We explicitly create it to ensure it exists and maybe add an index
        try:
            await db.client[settings.MASTER_DB_NAME].create_collection(dynamic_collection_name)
        except Exception as e:
            # Collection might already exist (rare edge case), we log and continue
            print(f"Collection creation note: {e}")

        # 4. Prepare Metadata for Master DB
        org_doc = {
            "organization_name": data.organization_name,
            "email": data.email,
            "password_hash": get_password_hash(data.password),
            "collection_name": dynamic_collection_name,
            "connection_details": settings.MONGO_URL, # Simplified for this assignment
            "created_at": datetime.utcnow(),
            "status": "active"
        }

        # 5. Insert into Master DB
        await self.collection.insert_one(org_doc)

        # 6. Return Clean Response (No Password!)
        return OrgResponse(
            organization_name=org_doc["organization_name"],
            admin_email=org_doc["email"],
            collection_name=org_doc["collection_name"],
            connection_details="Master Cluster (Local)",
            status=org_doc["status"]
        )

    async def get_organization(self, org_name: str):
        org = await self.collection.find_one({"organization_name": org_name})
        if not org:
            raise HTTPException(status_code=404, detail="Organization not found")
        
        return OrgResponse(
            organization_name=org["organization_name"],
            admin_email=org["email"],
            collection_name=org["collection_name"],
            connection_details="Master Cluster",
            status=org.get("status", "active")
        )