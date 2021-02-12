from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
  return HttpResponse("Hello, world!")

def time(request):
  now = datetime.now().strftime('%b %dth, %Y - %H:%M hs')
  return HttpResponse("Que onda!. La hora es: {}".format(str(now)))

def hi(request):
  #import pdb # Add a debugger for request
  #pdb.set_trace()
  return HttpResponse("Hola!!")

def sort_numbers(request):
  numbers = list(eval(request.GET['numbers']))
  numbers.sort() 
  data = {
    'status': 'ok',
    'numbers': numbers,
    'message': 'Integer sorted successfully'
  }
  return HttpResponse(json.dumps(data), content_type = 'application/json')