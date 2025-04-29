from ninja import Router, Schema, File
from ninja.files import UploadedFile
from ninja.pagination import paginate
from typing import List, Optional
from django.shortcuts import get_object_or_404

from apps.base.pagination import CustomPagination
from apps.employees.models.cards import Card
from apps.employees.models.employee import Employee
from apps.employees.schemas import CardDataIn, CardDataOut, EmployeeIn, EmployeeOut
from apps.employees.handler.admission_file.admission_extractor import FileAdmissionExtractor


class NoContent(Schema):
    pass

router = Router(tags=['employees'])

@router.post('/', response=EmployeeOut)
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict(exclude_unset=True))
    return employee

@router.get('/', response=List[EmployeeOut])
@paginate(CustomPagination)
def list_employees(request, email: Optional[str] = None, google_user_id: Optional[str] = None):
    if not email and not google_user_id:
        return Employee.objects.active().order_by('id')

    if email:
        employee = Employee.objects.active().filter(email=email).order_by('id')
        return employee

    if google_user_id:
        employee = Employee.objects.active().filter(google_user_id=google_user_id).order_by('id')
        return employee

@router.get('/{employee_id}', response=EmployeeOut)
def get_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    return employee

@router.patch('/{employee_id}', response=EmployeeOut)
def update_employee(request, employee_id: int, payload: EmployeeIn):
    employee = get_object_or_404(Employee, id=employee_id)

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(employee, field, value)

    employee.save()

    return employee

@router.delete('/{employee_id}', response={204: NoContent})
def delete_employee(request, employee_id: int):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return 204

@router.post('/cards/', response=CardDataOut)
def create_card(request, payload: CardDataIn):
    card = Card.objects.create(**payload.dict())
    return card

@router.post('/upload/ficha-admissao')
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    pdf_extractor = FileAdmissionExtractor(data)
    return {"result":pdf_extractor.extract_clt()}
