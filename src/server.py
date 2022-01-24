
from src.main.main import app

from mangum import Mangum


handler = Mangum(app,
                 api_gateway_base_path='appmaua_subjects')
