from django.db import models

# Create your models here.


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Topic(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.CharField()
    
    

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return self.title

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class User(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    password  = models.CharField(max_length=80)
    email = models.EmailField(max_length=100)
    def __str__(self) -> str:
        return self.first_name

class Result(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz_title = models.CharField(max_length=255)
    result_detail =models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.quiz_title
    
class Result_detail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.ForeignKey(Result, on_delete=models.CASCADE)
    quation_name = models.CharField(max_length=255)
    is_solved = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.quation_name