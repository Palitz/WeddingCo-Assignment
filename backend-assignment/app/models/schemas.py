from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# --- Shared Models ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    org_id: Optional[str] = None

# --- Organization Models ---

# INPUT: What we receive when creating an org
class OrgCreateRequest(BaseModel):
    organization_name: str = Field(..., min_length=2, example="Tesla")
    email: EmailStr = Field(..., example="elon@tesla.com")
    password: str = Field(..., min_length=6, example="securePass123")

# INPUT: What we receive when updating
class OrgUpdateRequest(BaseModel):
    organization_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# OUTPUT: What we return to the client (Never return the password!)
class OrgResponse(BaseModel):
    organization_name: str
    admin_email: str
    collection_name: str
    connection_details: str
    status: str = "active"

# --- Admin Login Models ---
class AdminLoginRequest(BaseModel):
    email: EmailStr
    password: str