from django.urls import path
from .views import  FeedBackView, FeedBackUpdateView, DoneView, ListFeedBack, DetailFeedBack # index, update_feedback, done,

urlpatterns = [
    path('done/', DoneView.as_view()),
    path('', FeedBackView.as_view(), name='index'),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('list/', ListFeedBack.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
]