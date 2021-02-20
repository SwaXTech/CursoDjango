from django.db import models # Nos permite interactuar con el ORM

# Definimos una tabla a través de la clase

class User(models.Model):


  # Django ya agrega un id

  email       = models.EmailField(unique = True)
  password    = models.CharField(max_length = 100)
  first_name  = models.CharField(max_length = 100)
  last_name   = models.CharField(max_length = 100)
  bio         = models.TextField(blank = True)
  birthdate   = models.DateField(blank = True, null = True)
  created     = models.DateTimeField(auto_now_add = True) # Fecha en la que se agregó
  modified    = models.DateTimeField(auto_now = True)    # Fecha en la que se editó
  is_admin    = models.BooleanField(default = False)
  country     = models.CharField(max_length = 30, null = True)
  city        = models.CharField(max_length = 30, null = True)


  ## Posterior a la creación de esta clase, es necesario realizar la migración. (python manage.py makemigrations) 
  ## Luego migrar a la base con python manage.py migrate
  ## Se creará un archivo de migración (0001_initial.py) que permite trackear los cambios en la base

  ## Makemigrations --> Busca los cambios en nuestro modelo y lo pasa a un archivo
  ## Migrate --> Implementa los cambios a la DB


  def __str__(self):
    return self.email




