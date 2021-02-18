from datetime import date
from posts.models import User

users = [

  {
    'email': 'cvander@platzi.com',
    'first_name': 'Christian',
    'last_name': 'Van der Henst',
    'password': '123456789',
    'is_admin': True
  },

  {
    'email': 'freddier@platzi.com',
    'first_name': 'Freddy',
    'last_name': 'Vega',
    'password': '123456789',
  },

  {
    'email': 'yesica@platzi.com',
    'first_name': 'Yésica',
    'last_name': 'Cortés',
    'password': '123456789',
    'birthdate': date(1990, 12, 19)
  },

  {
    'email': 'arturo@platzi.com',
    'first_name': 'Arturo',
    'last_name': 'Martínez',
    'password': '123456789',
    'is_admin': True,
    'birthdate': date(1981, 11, 6),
    'bio': 'The path of the righteous man is beset on all sides by the iniquities of the selfish...'
  },
]

for user in Users:
  obj = User.objects.create(**user)
  print("Object #{}: Added Successfully".format(obj.pk))