from django.core.asgi import get_asgi_application
from mangum import Mangum

application = get_asgi_application()
handler = Mangum(application)

