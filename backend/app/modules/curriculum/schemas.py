from pydantic import BaseModel, ConfigDict


class SubjectResponse(BaseModel):
    subject_id: int
    subject_code: str
    subject_name: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class ExamBoardResponse(BaseModel):
    exam_board_id: int
    board_code: str
    board_name: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class SpecificationTierResponse(BaseModel):
    specification_tier_id: int
    tier_code: str
    tier_name: str

    model_config = ConfigDict(from_attributes=True)


class SubjectSpecificationResponse(BaseModel):
    specification_id: int
    subject_id: int
    exam_board_id: int
    qualification_id: int
    specification_code: str
    specification_name: str
    specification_version: str | None
    is_active: bool
    tiers: list[SpecificationTierResponse] = []

    model_config = ConfigDict(from_attributes=True)