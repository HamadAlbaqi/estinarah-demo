from vanna.remote import VannaDefault
from .config import Settings
from .database import connection
import pandas as pd

def run_sql(sql: str) -> pd.DataFrame:
    df = pd.read_sql_query(sql, connection)
    return df

def query_vanna(question):

    try:
        answer = vn.ask(question, print_results=False)
        print(answer)
        sql_query = answer[0]
        data = answer[1]
        # vis = answer[2]
        return sql_query, data
    except Exception as e:
        print(e)

vn = VannaDefault(
    model=Settings.model_name,
    api_key=Settings.api_key
)

vn.run_sql = run_sql
vn.run_sql_is_set=True