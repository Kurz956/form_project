from django.shortcuts import render
from django.http import HttpResponseRedirect
from  .forms import FeedbackForm
from .models import Feedback

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
# Create your views here.

class FeedBackView(View):
    '''Получение информации'''
    def get(self, request):
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})

class FeedBackUpdateView(View):
    '''Обновление информации'''
    def get(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})

class DoneView(TemplateView):
    '''Подтверждение успешности операции'''
    template_name = 'feedback/done.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I.'
        context['date'] = '23/4/2022'
        return context

# class ListFeedBack(TemplateView):        через TemplateView
#     '''Вывод всех отзывов'''
#     template_name = 'feedback/list_feedback.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_feed'] = Feedback.objects.all()
#         return context
class ListFeedBack(ListView):
    '''Вывод всех отзывов'''
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=2)
        return filter_qs

class DetailFeedBack(DetailView): # через DetailView
    '''Инфа по одному отзыву'''
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feedback'

class DetailFeedBack_TemplateView(TemplateView): # через TemplateView
    '''Инфа по одному отзыву'''
    template_name = 'feedback/detail_feedback.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['detailed_feedback'] = Feedback.objects.get(id=kwargs['id_feedback'])
        return context
class DetailFeedBack_View(View): # через View
    '''Инфа по одному отзыву'''
    def get(self, request, id_feedback):
        template_name = 'feedback/detail_feedback.html'
        feed = Feedback.objects.get(id=id_feedback)
        data = {
            'detailed_feedback': feed
        }
        return render(request, template_name=template_name, context=data)


# def index(request):                       переделано под классы
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         # name = request.POST['name']   # формы через ХТМЛ
#         # if len(name) == 0:
#         #     return render(request, 'feedback/feedback.html', context={'form': form})
#         # print(name)
#         # return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})

# def update_feedback(request, id_feedback):         переделано под классы
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})
#
# def done(request):
#     return render(request, 'feedback/done.html')