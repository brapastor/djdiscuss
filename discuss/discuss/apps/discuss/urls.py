from django.conf.urls import url
from .views import QuestionListView
urlpatterns = [
    url(r'^preguntas/', QuestionListView.as_view(), name='questions'),
]
