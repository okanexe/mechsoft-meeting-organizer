from django.db import models


# Create your models here.
class Meeting(models.Model):
    meeting_name = models.CharField(max_length=500)
    meeting_link = models.URLField(max_length=2000)

    start_time = models.TimeField(default='12:00:00')
    end_time = models.TimeField(default='12:00:00')

    meeting_day = models.CharField(max_length=500, default = "monday")

    participants = models.CharField(max_length=5000, default = "noone")


    def __str__(self):
        return self.meeting_name


