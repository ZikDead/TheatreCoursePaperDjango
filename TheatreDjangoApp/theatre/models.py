from django.db import models



class Hall(models.Model):
    number_of_places = models.IntegerField()
    description_of_hall = models.TextField(max_length=100)


class Perfomance(models.Model):
    cost_of_ticket = models.FloatField()
    tittle= models.CharField(max_length=70)
    #JSON format
    time_array = models.CharField(max_length=100)


class Program(models.Model):
    time = models.TimeField()
    perfomance = models.ForeignKey(Perfomance)
    hall = models.ForeignKey(Hall)
    places = models.CharField(max_length=2000)



