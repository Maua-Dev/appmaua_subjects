
from src.main.main import app

from mangum import Mangum


handler = Mangum(app,api_gateway_endpoint_url='appmaua_subjects')
