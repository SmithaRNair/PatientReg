from sqlalchemy.orm import Session
from .import models, schemas

def get_patient(db:Session, patient_id:int):
    return db.query(models.Patient).filter(models.Patient.id==patient_id).first()

def get_patients(db:Session,skip:int=0,limit:int=10):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db:Session,patient:schemas.PatientCreate):
    db_patient=models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit();
    db.refresh(db_patient)
    return db_patient

def update_patient(db:Session,patient_id:int,patient:schemas.PatientUpdate):
    db_patient=get_patient(db,patient_id)
    if db_patient:
        for key,value in patient.model_dump().items():
            setattr(db_patient,key,value)
        db.commit()
    
        db.refresh(db_patient)
    return db_patient

def delete_patient(db:Session,patient_id:int):
    db_patient=get_patient(db,patient_id)
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient     

def patch_patient(db:Session, patient_id:int,patient_update:schemas.PatientPartialUpdate):
    patient=db.query(models.Patient).filter(models.Patient.id==patient_id).first()
    if not patient:
        return None
    update_dict=patient_update.model_dump(exclude_unset=True)
    for key,Value in update_dict.items():
        setattr(patient,key,Value)
    db.commit()
    db.refresh(patient)
    return patient    
      
            