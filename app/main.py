from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

# --- Build metadata (for DevOps visibility) ---
GIT_SHA = os.getenv("GIT_SHA", "dev")
BUILD_TIME = os.getenv("BUILD_TIME", "unknown")


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "gcp-postgres"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "appassword"),
    )


@app.get("/")
def read_root():
    return {"message": "Hello from GCP 2-Tier App 🚀"}


@app.get("/health")
def health():
    return {"status": "ok"}


# --- NEW VERSION ENDPOINT ---
@app.get("/version")
def version():
    return {
        "git_sha": GIT_SHA,
        "build_time": BUILD_TIME
    }


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

