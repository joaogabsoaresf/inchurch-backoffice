from ninja.pagination import paginate, PageNumberPagination
from ninja import Router, Schema
from typing import List
from django.shortcuts import get_object_or_404
from apps.employees.schemas import EmployeeIn, EmployeeOut
from apps.employees.models.employee import Employee
from apps.base.pagination import CustomPagination

class NoContent(Schema):
    pass

router = Router(tags=['employees'])

@router.post('/', response=EmployeeOut)
def create_employee(request, payload: EmployeeIn):
    employee = Employee.objects.create(**payload.dict(exclude_unset=True))
    return employee

@router.get('/', response=List[EmployeeOut])
@paginate(CustomPagination)
def list_employees(request):
    qs = Employee.objects.active().order_by('id')
    return qs

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