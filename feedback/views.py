from django.shortcuts import render
from django.http import HttpResponseRedirect
from  .forms import FeedbackForm
from .models import Feedback

from django.views import View
# Create your views here.

class FeedBackView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        # name = request.POST['name']   # формы через ХТМЛ
        # if len(name) == 0:
        #     return render(request, 'feedback/feedback.html', context={'form': form})
        # print(name)
        # return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})

def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})

def done(request):
    return render(request, 'feedback/done.html')