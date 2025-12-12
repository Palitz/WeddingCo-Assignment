from fastapi import APIRouter, Depends
from app.models.schemas import OrgCreateRequest, OrgResponse
from app.services.org_service import OrganizationService

router = APIRouter(prefix="/org", tags=["Organization"])

# Dependency Injection for the Service
def get_service():
    return OrganizationService()

@router.post("/create", response_model=OrgResponse)
async def create_org(
    request: OrgCreateRequest, 
    service: OrganizationService = Depends(get_service)
):
    """
    Creates a new organization, a dynamic collection, and an admin user.
    """
    return await service.create_organization(request)

@router.get("/get/{org_name}", response_model=OrgResponse)
async def get_org(
    org_name: str,
    service: OrganizationService = Depends(get_service)
):
    """
    Fetch organization details by name.
    """
    return await service.get_organization(org_name)