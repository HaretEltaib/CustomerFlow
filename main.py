from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas

# إنشاء الجداول في قاعدة البيانات
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ClientBook API")

# Dependency للحصول على جلسة قاعدة البيانات
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# إضافة عميل جديد
@app.post("/customers/", response_model=schemas.CustomerRead)
def add_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = models.Customer(name=customer.name, phone=customer.phone, email=customer.email)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# عرض كل العملاء
@app.get("/customers/", response_model=list[schemas.CustomerRead])
def get_customers(db: Session = Depends(get_db)):
    return db.query(models.Customer).all()

# البحث عن عميل بالاسم أو الهاتف
@app.get("/customers/search/", response_model=list[schemas.CustomerRead])
def search_customer(keyword: str, db: Session = Depends(get_db)):
    results = db.query(models.Customer).filter(
        (models.Customer.name.contains(keyword)) | 
        (models.Customer.phone.contains(keyword))
    ).all()
    return results

# تحديث بيانات العميل
@app.put("/customers/{customer_id}", response_model=schemas.CustomerRead)
def update_customer(customer_id: int, customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db_customer.name = customer.name
    db_customer.phone = customer.phone
    db_customer.email = customer.email
    db.commit()
    db.refresh(db_customer)
    return db_customer

# حذف العميل
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)
    db.commit()
    return {"message": f"Customer {db_customer.name} deleted successfully"}
