from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        pass

    def save(self):
        q = Question(**self.cleaned_data)
        q.author_id = self._user.id
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            q = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            q = None

        return q

    def clean(self):
        pass

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer


class SignupForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise ValidationError("Такой пользователь уже существует")
        except User.DoesNotExist:
            pass
        return username

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError('Неправильное имя пользователя или пароль.')
        if not user.check_password(password):
            raise ValidationError('Неправильное имя пользователя или пароль')

