from django.urls import path
from .views import  FeedBackView, FeedBackUpdateView, DoneView, ListFeedBack, DetailFeedBack, FeedBackViewUpdate,FeedBackDeleteView # index, update_feedback, done,

urlpatterns = [
    path('done/', DoneView.as_view()),
    path('', FeedBackView.as_view(), name='index'),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
    path('list/', ListFeedBack.as_view(), name='feedback-list'),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
    path('update/<int:pk>', FeedBackViewUpdate.as_view(), name='update-feedback'),
    path('delete/<int:pk>', FeedBackDeleteView.as_view(), name='delete-feedback'),
]