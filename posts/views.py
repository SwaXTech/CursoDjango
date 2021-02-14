from django.shortcuts import render
from datetime import datetime

posts = [
  {
    'title': 'Mont Blac',
    'user': {
      'name': "Yésica Cortéz",
      'picture': 'https://picsum.photos/60/60/?image=1027'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture':  'https://picsum.photos/800/600/?image=1036'
  },

  {
    'title': 'Vía Lactea',
    'user': {
      'name': "Christian Van der Henst",
      'picture': 'https://picsum.photos/60/60/?image=1005'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture': 'https://picsum.photos/800/600/?image=903'
  },

  {
    'title': 'Nuevo Auditorio',
    'user': {
      'name': "Uriel (thespianartist)",
      'picture': 'https://picsum.photos/60/60/?image=883'
    },
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture': 'https://picsum.photos/800/600/?image=1076'
  }
]

def list_posts(request):
  return render(request, 'feed.html', {
    
    'posts': posts

  })

