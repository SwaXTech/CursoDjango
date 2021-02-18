from django.db import models # Nos permite interactuar con el ORM

# Definimos una tabla a través de la clase

class User(models.Model):

  email       = models.EmailField(unique = True)
  password    = models.CharField(max_length = 100)
  first_name  = models.CharField(max_length = 100)
  last_name   = models.CharField(max_length = 100)
  bio         = models.TextField(blank = True)
  birthdate   = models.DateField(blank = True, null = True)
  created     = models.DateTimeField(auto_now_add = True) # Fecha en la que se agregó
  modified    = models.DateTimeField(auto_now = True)    # Fecha en la que se editó


  ## Posterior a la creación de esta clase, es necesario realizar la migración. (python manage.py makemigrations)





