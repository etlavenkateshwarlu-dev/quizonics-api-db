from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints
from typing import Annotated


class UserCreateRequest(BaseModel):
    first_name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=100),
    ]

    last_name: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=100),
    ]

    email: EmailStr

    password: Annotated[
        str,
        StringConstraints(min_length=8, max_length=128),
    ]


class UserCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: UUID
    email: EmailStr
    role: str
    status: str
    first_name: str
    last_name: str