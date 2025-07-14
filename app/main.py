from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Sessionlocal, Base

Base.metadata.create_all(bind=engine)

app=FastAPI()

def  get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/patients/",response_model=schemas.Patient)  
def create_patient(patient:schemas.PatientCreate,db:Session=Depends(get_db)):
    return crud.create_patient(db,patient)  

@app.get("/patients/",response_model=list[schemas.Patient]) 
def read_patients(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    return crud.get_patients(db,skip=skip,limit=limit)   

@app.get("/patients/{patient_id}",response_model=schemas.Patient)
def read_patient(patient_id:int, db:Session=Depends(get_db)):
    db_patient=crud.get_patient(db,patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404,detail="Patient Not Found")
    return db_patient

@app.put("/patients/{patient_id}",response_model=schemas.Patient)
def update_patient(patient_id:int, patient:schemas.PatientUpdate, db:Session=Depends(get_db)):
    db_patient=crud.update_patient(db,patient_id,patient)
    if db_patient is None:
        raise HTTPException(status_code=404,detail="Patient Not Found")
    return db_patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id:int, db:Session=Depends(get_db)):
    db_patient=crud.delete_patient(db,patient_id)
    if db_patient is None:
        raise HTTPException(status_code=404,detail="Patient Not Found")
    return {'message':"Deleted Successfully"}
         
@app.patch("/patients/{patient_id}",response_model=schemas.Patient)   
def update_partial_patient(patient_id:int,patient_update:schemas.PatientPartialUpdate,db:Session=Depends(get_db)):
    updated_patient=crud.patch_patient(db,patient_id,patient_update)
    if updated_patient is None:
        raise HTTPException(status_code=404,detail="Patient Not Found")
    return updated_patient         
