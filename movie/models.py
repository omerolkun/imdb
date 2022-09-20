from django.db import models
from django.utils.translation import gettext as _
import datetime
# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(primary_key = True ) 
    name = models.CharField(max_length= 30)
    release_year =models.IntegerField( default = 0) 

    def __str__(self):
        return str(self.movie_id)+ " " +   self.name + " " + str(self.release_year)


class Actor(models.Model):
    actor_id = models.IntegerField(primary_key = True ) 
    name = models.CharField(max_length= 30)
    age=models.IntegerField( default = 0) 

    def __str__(self):
        return str(self.actor_id)+ " " +   self.name + " " + str(self.age)





class Director(models.Model):
    director_id = models.IntegerField(primary_key = True ) 
    name = models.CharField(max_length= 30)
    age=models.IntegerField( default = 0) 

    def __str__(self):
        return str(self.director_id)+ " " +   self.name + " " + str(self.age)


class Movie_Actor(models.Model):
    movie_id = models.ForeignKey( 'Movie' , on_delete=models.CASCADE)
    actor_id = models.ForeignKey(  'Actor', on_delete=models.CASCADE)
     
    def __str__(self):
        return "\nmovie id :" + str( self.movie_id ) + " \nactor id :" + str( self.actor_id )+ "\n"
    class Meta:
        unique_together =( 'movie_id' , 'actor_id' )

    

class Movie_Director(models.Model):
    movie_id = models.ForeignKey( 'Movie', on_delete=models.CASCADE)
    director_id =models.ForeignKey( 'Director', on_delete=models.CASCADE)


    def __str__(self):
        return "movie id:" + str( self.movie_id ) + " director id:" + str( self.director_id ) + "\n"

    class Meta:
        unique_together = ( 'movie_id' , 'director_id')













