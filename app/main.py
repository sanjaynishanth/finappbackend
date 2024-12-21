from fastapi import FastAPI
from app.routers import auth
from app.db.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
#app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
