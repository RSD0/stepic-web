from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qa.models import Question
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    except TypeError:
        page = 1
    limit = 10
    paginator = Paginator(qs, limit)
    page = paginator.page(page)
    return page.object_list


def index(request, *args, **kwargs):
    p = paginate(request, Question.objects.all().order_by('-id'))
    return render(request,
                  'list.html',
                  {'questions': paginate(request, p)})


def popular(request, *args, **kwargs):
    p = paginate(request, Question.objects.all().order_by('-rating'))
    return render(request,
                  'list.html',
                  {'questions': paginate(request, p)})


def question(request, *args, **kwargs):
    try:
        q = Question.objects.get(id=kwargs['num'])
    except Question.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})
    return render(request,
                  'question.html',
                  {'question': q,
                   'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request,
                  'ask_form.html',
                  {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request,
                  'signup.html',
                  {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active():
                    login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request,
                  'login.html',
                  {'form': form})
