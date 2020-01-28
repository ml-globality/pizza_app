"""
Entrypoint module for WSGI containers.

"""
from slice.app import create_app


app = create_app().app
