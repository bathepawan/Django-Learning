from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    qlist = ' '.join(q.question_text for q in latest_question_list)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')

    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):

    return HttpResponse('Results:You are looking at the results of {}'.format(question_id))


def vote(request, question_id):
    return HttpResponse('Voting: You are voting on question_id {}'.format(question_id))


