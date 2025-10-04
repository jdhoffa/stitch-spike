from stitch_spike import create_app
from uvicorn import run
from importlib.metadata import metadata
from os import getenv
from dotenv import load_dotenv

# import .env settings
load_dotenv()
STITCH_API_PORT = int(getenv("STITCH_API_PORT", 8000))
STITCH_API_LOG_LEVEL = getenv("STITCH_API_LOG_LEVEL", "info").lower()

# Validate log level
valid_log_levels = ["critical", "error", "warning", "info", "debug", "trace"]
if STITCH_API_LOG_LEVEL not in valid_log_levels:
    print(f"Warning: Invalid log level '{STITCH_API_LOG_LEVEL}'. Defaulting to 'info'.")
    STITCH_API_LOG_LEVEL = "info"

meta = metadata("stitch_spike")

app = create_app(
    title="POC API", description=meta["summary"], version=meta["version"]
)

if __name__ == "__main__":
    print(f"Starting POC API on port {STITCH_API_PORT} with log level '{STITCH_API_LOG_LEVEL}'")
    run("main:app", host="0.0.0.0", port=STITCH_API_PORT, log_level=STITCH_API_LOG_LEVEL)
