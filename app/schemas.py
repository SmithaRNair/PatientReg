from pydantic import BaseModel
from typing import Optional

class PatientBase(BaseModel):
    name: str
    age: int
    gender: str
    doctor: str
    disease: str
    phone_no: Optional[str]=None

class PatientCreate(PatientBase):
    pass

class PatientUpdate(PatientBase):
    pass

class PatientPartialUpdate(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    gender:Optional[str]=None
    doctor:Optional[str]=None
    disease:Optional[str]=None
    phone_no:Optional[str]=None
    

class Patient(PatientBase):
    id:int
    class Config:
        orm_mode=True
            
        