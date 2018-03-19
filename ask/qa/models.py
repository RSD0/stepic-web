from django.contrib.auth.models import User
from django.db import models
from django.db.models import CharField, IntegerField, TextField, ForeignKey, ManyToManyField, DateTimeField, \
    OneToOneField
from django.urls import reverse

from ask.qa import views


class QuestionManager(models.Manager):
    def new(self):
        self.order_by('-added_at')

    def popular(self):
        self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = CharField(max_length=255, default="")
    text = TextField(default="")
    added_at = DateTimeField(blank=True, auto_now_add=True)
    rating = IntegerField(default=0)
    author = ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = ManyToManyField(User, related_name="q_likes_set")

    def __str__(self):
        return self.title

    def get_url(self):
        return '/question/{}/'.format(self.id)


class Answer(models.Model):
    text = TextField(default="")
    added_at = DateTimeField(null=True, auto_now_add=True)
    question = ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text
