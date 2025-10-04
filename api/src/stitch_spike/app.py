from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .routers.health import health_router
from .routers.endpoints import endpoints


def create_app(title, description, version):
    """Create and configure the FastAPI application."""

    # Create FastAPI app with metadata
    app = FastAPI(
        title=title,
        description=description,
        version=version,
        contact={
            "name": "RMI",
            "url": "https://github.com/RMI",
        },
        license_info={
            "name": "MIT",
            "url": "https://github.com/RMI/stitch-spike/blob/main/LICENSE.txt",
        },
    )

    # Configure CORS
    origins = [
        "http://localhost",
        "http://localhost:3000",
        "http://0.0.0.0",
        "http://0.0.0.0:3000",
        "null",
    ]  # "null" is necessary for a request from a local file

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Root endpoint redirects to docs
    @app.get("/")
    async def redirect():
        response = RedirectResponse(url="/docs")
        return response

    # Include routers
    app.include_router(health_router)
    app.include_router(endpoints)

    return app
