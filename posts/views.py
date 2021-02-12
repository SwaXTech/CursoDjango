from django.http import HttpResponse
from datetime import datetime

posts = [
  {
    'name': 'Mont Blac',
    'user': "Yésica Cortéz",
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture':  'https://picsum.photos/200/200/?image=1036'
  },

  {
    'name': 'Vía Lactea',
    'user': "C. Vander",
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture': 'https://picsum.photos/200/200/?image=903'
  },

  {
    'name': 'Nuevo Auditorio',
    'user': "Thespianartist",
    'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hs'),
    'picture': 'https://picsum.photos/200/200/?image=1076'
  }
]

def list_posts(request):
  content = []
  for post in posts:
    content.append("""
    
      <p><strong>{name}</strong></p>
      <p><small>{user} - <i>{timestamp}</i></small></p>
      <figure><img src="{picture}"/></figure>
    """.format(**post))

  return HttpResponse('<br>'.join(content))

