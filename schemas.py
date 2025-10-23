from pydantic import BaseModel

class CustomerCreate(BaseModel):
    name: str
    phone: str
    email: str | None = None

class CustomerRead(BaseModel):
    id: int
    name: str
    phone: str
    email: str | None = None

    class Config:
        orm_mode = True
