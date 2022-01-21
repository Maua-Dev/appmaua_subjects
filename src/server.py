
from src.main.main import app

from mangum import Mangum


handler = Mangum(app)