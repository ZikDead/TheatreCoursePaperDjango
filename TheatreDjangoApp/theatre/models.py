from django.db import models
from datetime import date, timedelta

class Hall(models.Model):
    number_of_hall = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Halls'


class Performance(models.Model):
    cost_of_ticket = models.DecimalField(max_digits=10, decimal_places=2)
    tittle = models.CharField(max_length=70)
    img = models.ImageField(verbose_name="Path to post-img", upload_to='post-img/', blank=False,
                            default='post-img/default.jpg')

    def __str__(self):
        return str(self.tittle)


# class EventListManager(models.Manager):
#     def get_last_events(self, limit: int):
#         events = self.distinct('date')
#         events = events.order_by('date')
#         today = date.today()
#         events = [events.filter(date__lte=today + timedelta(days=int(limit)), date__gte=today)]
#
#
#         weekdays = {
#             '0': 'Monday',
#             '1': 'Tuesday',
#             '2': 'Wednesday',
#             '3': 'Thursday',
#             '4': 'Friday',
#             '5': 'Sunday',
#             '6': 'Saturday'
#         }
#
#         for i in range(len(events)):
#             events[i] = [events[i], events[i].date.weekday()]
#
#         print(events)
#         return events


class EventList(models.Model):
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

    performance = models.ForeignKey(Performance)
    hall = models.ForeignKey(Hall)

    # object = EventListManager()
    # JSON format
    place = models.TextField(default='', blank=True)

    @staticmethod
    def get_last_days(limit: int):

        weekdays_dict = {
            '0': 'Monday',
            '1': 'Tuesday',
            '2': 'Wednesday',
            '3': 'Thursday',
            '4': 'Friday',
            '5': 'Sunday',
            '6': 'Saturday'
        }

        today = date.today()
        weekdays = []
        for i in range(int(limit)):
            date_text = today + timedelta(days=i)
            weekday_id = date_text.weekday()
            weekdays.append([str(date_text), weekdays_dict[str(weekday_id)]])

        return weekdays

    def __str__(self):
        return str(self.performance.tittle) + ' ' + str(self.date) + ' ' + str(self.time_start)

    class Meta:
        ordering = ['-date', '-time_start']
        verbose_name_plural = 'EventList'





#def get_absolute_url(self):
 #   return '/program/%d' % self.id