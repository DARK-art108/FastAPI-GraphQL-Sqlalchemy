from fastapi import FastAPI
from controllers.index import user, index
app = FastAPI()
app.include_router(user)

