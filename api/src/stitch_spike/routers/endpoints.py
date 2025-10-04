from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from ..models.sql_models import Scenario, Organization
from ..services.db import get_db, engine


endpoints = APIRouter()


# Router to get all tables in the database
@endpoints.get("/tables")
def get_tables(db=Depends(get_db)):
    return {"tables": get_tables_from_db()}


# Function to fetch table names using SQLAlchemy inspect
def get_tables_from_db():
    inspector = inspect(engine)  # Use the SQLAlchemy engine to inspect the database
    return inspector.get_table_names(
        schema="poc"
    )  # Get table names in the 'poc' schema


# Router to get the entire scenarios table
@endpoints.get("/scenarios")
def get_scenarios(db: Session = Depends(get_db)):
    # Query the scenarios
    scenarios = db.query(Scenario).all()
    if not scenarios:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenarios


# Router to get scenarios by scenario_id
@endpoints.get("/scenarios/{scenario_id}")
def get_scenario_by_id(scenario_id: int, db: Session = Depends(get_db)):
    # Query the Scenarios table by primary key (scenario_id)
    scenario = db.query(Scenario).get(scenario_id)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return scenario


# Router to get the entire organizations table
@endpoints.get("/organizations")
def get_organization(db: Session = Depends(get_db)):
    # Query the organizations
    organizations = db.query(Organization).all()
    if not organizations:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organizations


# Router to get organization by organization_id
@endpoints.get("/organizations/{organization_id}")
def get_organization_by_id(organization_id: int, db: Session = Depends(get_db)):
    # Query the Organizations table by primary key (organization_id)
    organization = db.query(Organization).get(organization_id)
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization

@endpoints.get("/search", summary="Search organizations by name")
def search_organizations_by_name(
    q: str = Query(..., description="Free text search query"),
    db: Session = Depends(get_db)):
    """
    Search for organizations by name using PostgreSQL full-text search.
    """
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' is required.")

    # Perform the full-text search dynamically on the `name` field
    query = text("""
        SELECT id, name
        FROM poc.organizations
        WHERE to_tsvector('english', name) @@ to_tsquery(:query)
        ORDER BY ts_rank(to_tsvector('english', name), to_tsquery(:query)) DESC
    """)
    results = db.execute(query, {"query": q}).fetchall()

    # Format the results
    items = [{"id": row.id, "name": row.name} for row in results]
    return {
        "total_count": len(items),
        "items": items
    }
