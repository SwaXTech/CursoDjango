from django.http import HttpResponse
from datetime import datetime

def hello_world(request):
  return HttpResponse("Hello, world!")

def time(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hs')
  return HttpResponse("Que onda!. La hora es: {}".format(str(now)))