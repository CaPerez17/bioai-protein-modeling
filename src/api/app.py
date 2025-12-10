"""
FastAPI application for protein modeling API.
"""

from fastapi import FastAPI

app = FastAPI(title="BioAI Protein Modeling API")


@app.get("/")
def root():
    """
    Root endpoint.
    
    Returns:
        Welcome message
    """
    return {"message": "BioAI Protein Modeling API"}


@app.get("/health")
def health_check():
    """
    Health check endpoint.
    
    Returns:
        API status
    """
    return {"status": "healthy"}