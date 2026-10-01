"""
Assignment 4 - Basic FastAPI App

"""

from fastapi import FastAPI

app = FastAPI(
    title="My First FastAPI App",
    description="A small beginner API with a root endpoint, a path parameter and a query parameter.",
    version="1.0.0",
)


@app.get("/", summary="Welcome message")
def read_root():
    """Root endpoint - returns a simple welcome message."""
    return {
        "message": "Welcome to my first FastAPI app!",
        "docs": "/docs",
    }


@app.get("/greet/{name}", summary="Greet someone by name (path parameter)")
def greet(name: str):
    """Takes a name from the URL path and returns a personalised greeting."""
    return {
        "name": name,
        "greeting": f"Hello, {name}! Nice to meet you.",
    }


@app.get("/square", summary="Square a number (query parameter)")
def square(number: int = 2):
    """
    Takes a number as a query parameter, e.g. /square?number=5.
    If no number is given, it defaults to 2.
    FastAPI automatically returns a 422 error if the value is not an integer.
    """
    return {
        "number": number,
        "square": number * number,
    }