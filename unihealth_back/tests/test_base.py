import pytest
import sys
import os.path
import json
from datetime import *
from inspect import getsourcefile
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]
sys.path.insert(0, parent_dir)

from app import create_app
from backend.config.routes import init_routes

app = create_app()
app.testing = True
app.debug = True
init_routes(app)

@pytest.fixture
def client():
    return app.test_client()

