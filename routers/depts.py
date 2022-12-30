import datetime

from fastapi import Depends, APIRouter
import models
from sqlalchemy.orm import Session
from pydantic import BaseModel

from setting import get_db, successful_response, http_exception


class Dept(BaseModel):
    dp_no: int
    dp_name: str
    dp_loc: str


router = APIRouter(
    prefix="/deps",
    tags=["deps"],
    responses={401: {"deps": "Not authorized"}})


@router.get("/")
async def depts_all(db: Session = Depends(get_db)):
    return db.query(models.Depts).all()


@router.post("/")
async def create_dept(dept: Dept, db: Session = Depends(get_db)):
    dept_model = models.Depts()
    dept_model.dp_no = dept.dp_no
    dept_model.dp_name = dept.dp_name
    dept_model.dp_loc = dept.dp_loc

    db.add(dept_model)
    db.commit()

    return successful_response(201)


@router.put("/{dept_id}")
async def update_dept(dept_id: int, dept: Dept, db: Session = Depends(get_db)):
    dept_model = db.query(models.Depts) \
        .filter(models.Depts.id == dept_id).first()

    if dept_model is None:
        raise http_exception()

    dept_model.dp_no = dept.dp_no
    dept_model.dp_name = dept.dp_name
    dept_model.dp_loc = dept.dp_loc

    db.add(dept_model)
    db.commit()

    return successful_response(200)


@router.delete("/{dept_id}")
async def delete_dept(dept_id: int, db: Session = Depends(get_db)):
    dept_model = db.query(models.Depts) \
        .filter(models.Depts.id == dept_id).first()

    if dept_model is None:
        raise http_exception()

    db.query(models.Depts). \
        filter(models.Depts.id == dept_id).delete()

    db.commit()

    return successful_response(200)


@router.get("/{dept_id}")
async def dept_row(dept_id: int, db: Session = Depends(get_db)):
    dept_model = db.query(models.Depts) \
        .filter(models.Depts.id == dept_id).first()

    if dept_model is not None:
        return dept_model
    raise http_exception()
