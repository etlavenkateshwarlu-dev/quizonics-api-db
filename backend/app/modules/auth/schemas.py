from datetime import date
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, StringConstraints


# ---------------------------------------------------------
# Subject Enrollment Request
# ---------------------------------------------------------

class SubjectEnrollmentRequest(BaseModel):
    """
    Represents one subject selected during student registration.
    """

    specification_id: int = Field(gt=0)

    tier: Annotated[
        str,
        StringConstraints(strip_whitespace=True, min_length=1, max_length=30),
    ]

    target_grade: Annotated[
        str | None,
        StringConstraints(strip_whitespace=True, max_length=20),
    ] = None


# ---------------------------------------------------------
# Student Registration Request
# ---------------------------------------------------------

class StudentRegistrationRequest(BaseModel):
    """
    Request payload for registering a student account.

    The password must be hashed before being stored in PostgreSQL.
    """

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

    school_year: int | None = Field(default=None, ge=1, le=13)

    school_name: Annotated[
        str | None,
        StringConstraints(strip_whitespace=True, max_length=200),
    ] = None

    date_of_birth: date | None = None

    country_code: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=2,
            max_length=2,
            pattern=r"^[A-Za-z]{2}$",
        ),
    ] = "GB"

    subjects: Annotated[
        list[SubjectEnrollmentRequest],
        Field(min_length=1, max_length=5),
    ]


# ---------------------------------------------------------
# Student Registration Response
# ---------------------------------------------------------

class StudentRegistrationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    student_id: int
    email: EmailStr
    role: str
    status: str
    first_name: str
    last_name: str
    school_year: int | None
    school_name: str | None