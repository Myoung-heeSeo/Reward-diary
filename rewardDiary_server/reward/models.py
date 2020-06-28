from django.db import models

class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    goal = models.CharField(max_length = 150)
    created_t = models.DateTimeField(auto_now_add = True)
    due_datetime = models.DateTimeField()
    complete = models.BooleanField(default = 0)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    diary_id = models.ForeignKey(Diary, )