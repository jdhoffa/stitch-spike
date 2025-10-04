import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

STITCH_API_KEY = os.getenv("STITCH_API_KEY")
STITCH_API_KEY_NAME = "X-API-Key"

api_key_header = APIKeyHeader(name=STITCH_API_KEY_NAME, auto_error=True)


def get_api_key(STITCH_API_KEY: str = Security(api_key_header)):
    if STITCH_API_KEY == STITCH_API_KEY:
        return STITCH_API_KEY
    raise HTTPException(status_code=403, detail="Invalid API Key")
