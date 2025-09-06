from pruebaa.asgi import application
from mangum import Mangum

handler = Mangum(application)
