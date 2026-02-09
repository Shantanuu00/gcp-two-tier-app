from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
    )

@app.get("/")
def read_root():
    return {"message": "Hello from GCP 2-Tier App 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db")
def db_check():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"db": "connected", "result": result[0]}
    except Exception as e:
        return {"db": "error", "detail": str(e)}

@app.post("/db/init")
def db_init():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    return {"db": "initialized"}

@app.post("/db/visit")
def db_visit():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id;")
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"inserted_id": new_id}

@app.get("/db/visits")
def db_visits():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"visits": count}

