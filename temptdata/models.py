from django.db import models

class temptdata(models.Model):
    rollnum_1 = models.CharField(max_length=20)
    rollnum_2 = models.CharField(max_length=20)
    name_1 = models.CharField(max_length=100)
    name_2 = models.CharField(max_length=100)
    in_time = models.DateTimeField(max_length=100)
    
     