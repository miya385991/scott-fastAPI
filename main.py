import datetime

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

# CORSオリジン設定
origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def http_exception():
    return HTTPException(status_code=404, detail="depts not found")


def successful_response(status_code: int):
    return {
        'status': status_code,
        'transaction': 'Successful'
    }


class Dept(BaseModel):
    dp_no: int
    dp_name: str
    dp_loc: str


class Emp(BaseModel):
    em_no: int
    em_name: str
    em_job: str
    em_mgr: int
    em_hiredate: datetime.date
    em_sal: int
    dept_id: int


@app.get("/depts")
async def depts_all(db: Session = Depends(get_db)):
    return db.query(models.Depts).all()


@app.post("/depts")
async def create_dept(dept: Dept, db: Session = Depends(get_db)):
    dept_model = models.Depts()
    dept_model.dp_no = dept.dp_no
    dept_model.dp_name = dept.dp_name
    dept_model.dp_loc = dept.dp_loc

    db.add(dept_model)
    db.commit()

    return successful_response(201)


@app.put("/depts/{dept_id}")
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


@app.delete("/depts/{dept_id}")
async def delete_dept(dept_id: int, db: Session = Depends(get_db)):
    dept_model = db.query(models.Depts) \
        .filter(models.Depts.id == dept_id).first()

    if dept_model is None:
        raise http_exception()

    db.query(models.Depts). \
        filter(models.Depts.id == dept_id).delete()

    db.commit()

    return successful_response(200)


@app.get("/depts/{dept_id}")
async def dept_row(dept_id: int, db: Session = Depends(get_db)):
    dept_model = db.query(models.Depts) \
        .filter(models.Depts.id == dept_id).first()

    if dept_model is not None:
        return dept_model
    raise http_exception()


@app.get("/emps")
async def emps_all(db: Session = Depends(get_db)):
    return db.query(models.Emps).all()


@app.post('/emps')
async def create_emp(emp:Emp,  db: Session = Depends((get_db))):

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


@app.get("/emps/{emp_id}")
async def emps_row(emp_id:int, db: Session = Depends(get_db)):
    emp_model = db.query(models.Emps).filter(models.Emps.id == emp_id).first()

    if emp_model is not None:
        return emp_model
    raise http_exception()


@app.put("/emps/{emp_id}")
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

@app.delete("/emps/{emp_id}")
async def delete_emp(emp_id: int, db: Session = Depends(get_db)):
    emp_model = db.query(models.Emps) \
        .filter(models.Emps.id == emp_id).first()

    if emp_model is None:
        raise http_exception()

    db.query(models.Emps). \
        filter(models.Emps.id == emp_id).delete()

    db.commit()

    return successful_response(200)

