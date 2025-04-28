from datetime import date, datetime
from typing import List, Optional

from ninja import Schema


class EmployeeIn(Schema):
    google_user_id: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    team: List[str] = None  # type: ignore
    is_onboarded: Optional[bool] = None
    document_number: Optional[str] = None
    birthday: Optional[date] = None
    phone: Optional[str] = None
    address: Optional[dict] = None
    hire_date: Optional[date] = None
    firement_date: Optional[date] = None


class EmployeeOut(Schema):
    id: int
    google_user_id: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    role: Optional[str] = None
    team: List[str] = None  # type: ignore
    is_onboarded: Optional[bool] = None
    document_number: Optional[str] = None
    birthday: Optional[date] = None
    phone: Optional[str] = None
    address: Optional[dict] = None
    hire_date: Optional[date] = None
    firement_date: Optional[date] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime


class CardDataIn(Schema):
    title: str
    description: str
    request_type: str
    recipient: str
    status: str
    created_by: str


class CardDataOut(Schema):
    id: int
    title: str
    description: str
    request_type: str
    recipient: str
    status: str
    created_at: datetime
    created_by: str
