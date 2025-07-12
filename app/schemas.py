from pydantic import BaseModel

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    doctor: str
    disease: str

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class Patient(PatientBase):
    id:int
    class Config:
        orm_mode=True
            
        