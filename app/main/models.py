from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 32)
    age = models.IntegerField(default = 12)
    gender = models.CharField(max_length=1, choices=( ('M','Masculine'), ('F', 'Female') ))

class Message(models.Model):
    desc = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)