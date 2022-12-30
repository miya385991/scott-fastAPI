import datetime

from fastapi import FastAPI, Depends, APIRouter
import models
from sqlalchemy.orm import Session
from pydantic import BaseModel

from setting import successful_response, http_exception, get_db

router = APIRouter(
    prefix="/emps",
    tags=["emps"],
    responses={401: {"emps": "Not authorized"}})


class Emp(BaseModel):
    em_no: int
    em_name: str
    em_job: str
    em_mgr: int
    em_hiredate: datetime.date
    em_sal: int
    dept_id: int


@router.get("/emps")
async def emps_all(db: Session = Depends(get_db)):
    return db.query(models.Emps).all()


@router.post('/emps')
async def create_emp(emp: Emp, db: Session = Depends(get_db)):
    emp_model = models.Emps()
    emp_model.em_no = emp.em_no
    emp_model.em_name = emp.em_name
    emp_model.em_job = emp.em_job
    emp_model.em_mgr = emp.em_mgr
    emp_model.em_hiredate = emp.em_hiredate
    emp_model.em_sal = emp.em_sal
    emp_model.dept_id = emp.dept_id

    db.add(emp_model)
    db.commit()

    return successful_response(201)


@router.get("/emps/{emp_id}")
async def emps_row(emp_id: int, db: Session = Depends(get_db)):
    emp_model = db.query(models.Emps).filter(models.Emps.id == emp_id).first()

    if emp_model is not None:
        return emp_model
    raise http_exception()


@router.put("/emps/{emp_id}")
async def update_emp(emp_id: int, emp: Emp, db: Session = Depends(get_db)):
    emp_model = db.query(models.Emps) \
        .filter(models.Emps.id == emp_id).first()

    if emp_model is None:
        raise http_exception()

    emp_model.em_no = emp.em_no
    emp_model.em_name = emp.em_name
    emp_model.em_job = emp.em_job
    emp_model.em_mgr = emp.em_mgr
    emp_model.em_hiredate = emp.em_hiredate
    emp_model.em_sal = emp.em_sal
    emp_model.dept_id = emp.dept_id

    db.add(emp_model)
    db.commit()

    return successful_response(200)


@router.delete("/emps/{emp_id}")
async def delete_emp(emp_id: int, db: Session = Depends(get_db)):
    emp_model = db.query(models.Emps) \
        .filter(models.Emps.id == emp_id).first()

    if emp_model is None:
        raise http_exception()

    db.query(models.Emps). \
        filter(models.Emps.id == emp_id).delete()

    db.commit()

    return successful_response(200)
