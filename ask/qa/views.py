from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

#from ask.qa.models import Question
from qa.models import Question

from ask.qa.forms import AskForm, AnswerForm


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
        if form.is_valid():
            q = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request,
                  'ask_form.html',
                  {'form': form})
