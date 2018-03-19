from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404

from ask.qa.models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        page = int(request.GET.get('page'))
    except ValueError:
        page = 1
    limit = 10
    paginator = Paginator(qs, limit)
    page = paginator.page(page)
    return page.object_list


def index(request, *args, **kwargs):
    p = paginate(request, Question.objects.new())
    return render(request,
                  'list.html',
                  {'questions': p})


def popular(request, *args, **kwargs):
    p = Question.objects.popular()
    return render(request,
                  'list.html',
                  {'questions': p})


def question(request, *args, **kwargs):
    try:
        q = Question.objects.get(id=kwargs['num'])
    except Question.DoesNotExist:
        raise Http404

    return render(request,
                  'question.html',
                  {'question': q})
