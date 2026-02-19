import os
import psycopg2

def conecta_db():
    database_url = os.getenv("DATABASE_URL")
    con = psycopg2.connect(database_url)
    return con


# def conecta_db():
#     con = psycopg2.connect(host="127.0.0.1",
#                             database="barbearia",
#                             user="postgres",
#                             password="postgres",
#                             port=5432)
#     return con
