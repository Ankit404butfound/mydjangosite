from django.db import models

# Create your models here.
class joinus(models.Model): 
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=33)
    user_id = models.CharField(max_length=15)
    skills = models.CharField(max_length=400)
    date = models.DateField()



    def __str__(self):
        return self.username
    