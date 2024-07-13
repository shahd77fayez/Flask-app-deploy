from dotenv import load_dotenv
import os
import redis
load_dotenv()
class ApplicationConfig:
    SECRET_KEY=os.environ["SECRET_KEY"]
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_HOST = os.environ.get("DB_HOST", "")
    REDIS_HOST = os.environ.get("REDIS_HOST", "redis-service")
    

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =True
    SQLALCHEMY_DATABASE_URI =f'postgresql://postgres:{DB_PASSWORD}@{DB_HOST}/truthGuard'

    SESSION_TYPE="redis"
    SESSION_PERMANENT=False
    SESSION_USE_SIGNER=True
    SESSION_REDIS=redis.from_url(f"redis://{REDIS_HOST}:6379")
