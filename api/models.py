from django.db import models

# Create your models here.


class Subject(models.Model):
    name =models.TextField(max_length=30)
    
    def __str__(self) -> str:
        return self.name

class Quizes(models.Model):
    True_ans = models.TextField(max_length=250)
    False_ans1 = models.TextField(max_length=250)
    False_ans1 = models.TextField(max_length=250)
    False_ans1 = models.TextField(max_length=250)
    
    def __str__(self) -> str:
        return self.True_ans
    
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.username