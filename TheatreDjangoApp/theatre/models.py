from django.db import models


class Hall(models.Model):
    number_of_hall = models.IntegerField()
    number_of_places = models.IntegerField()
    # JSON format
    place = models.TextField(default='')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = 'Halls'


class Perfomance(models.Model):
    cost_of_ticket = models.DecimalField(decimal_places=2)
    tittle = models.CharField(max_length=70)


class Program(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()
    data = models.DateField()

    perfomance = models.ForeignKey(Perfomance)
    hall = models.OneToOneField(Hall)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['-time']
        verbose_name_plural = 'Program'

# class ProgrammtManager(models.Manager):
#     def last_sessions(self):
#         return self.filter(time__gt<fwefw)
# def get_absolute_url(self):
#     return '/program/%d' % self.id