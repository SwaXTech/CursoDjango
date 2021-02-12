from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
  return HttpResponse("Hello, world!")

def time(request):
  now = datetime.now()
  return HttpResponse("Que onda!. La hora es: {}".format(str(now)))