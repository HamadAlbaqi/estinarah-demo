from fastapi import FastAPI
from .models import QueryRequest
from .vanna import query_vanna
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# origins = [
#     "http://localhost:5173", 
#     "http://127.0.0.1:3000", 
#     "http://localhost:5174" 
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,  
#     allow_credentials=True,
#     allow_methods=["*"],  
#     allow_headers=["*"],  
# )

@app.get("/")
def read_root():
    return {"Hello": "Welcome to Estinarah application!"}

@app.post("/query/")
async def process_query(query: QueryRequest):
    sql_query, data = query_vanna(query.question)
    data = data.to_dict('list')
    print(sql_query)
    print(data)
    return sql_query, data

# uvicorn app.main:app --reload