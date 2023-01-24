from fastapi import FastAPI
from controllers.index import user
app = FastAPI()
app.include_router(user)

