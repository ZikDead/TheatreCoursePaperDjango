from django.db import models



class Hall(models.Model):
    number_of_places = models.IntegerField()
    description_of_hall = models.CharField(max_length=100)
    place = models.TextField(default='')
    def __unicode__(self):
        return self.id
    class Meta:
        verbose_name_plural = 'Halls'


class Perfomance(models.Model):
    cost_of_ticket = models.FloatField()
    tittle= models.CharField(max_length=70)


class Program(models.Model):
    time = models.TimeField()
    data = models.DateField()
    perfomance = models.ForeignKey(Perfomance)
    hall = models.ForeignKey(Hall)
    places = models.CharField(max_length=2000)
    #JSON format
    #object = ProgrammManager
    def __unicode__(self):
        return self.id
    # def get_absolute_url(self):
    #     return '/program/%d' % self.id
    class Meta:
        ordering = ['-time']

# class ProgrammtManager(models.Manager):
#     def last_sessions(self):
#         return self.filter(time__gt<fwefw)