from django.conf.urls import url

import discuss
from .views import QuestionListView, QuestionCreateView, QuestionDetailView
urlpatterns = [
    url(r'^preguntas/', QuestionListView.as_view(), name='questions'),
    url(r'^preguntar/', QuestionCreateView.as_view(), name='create_question'),
    url(r'^pregunta/(?P<slug>[-\w]+)/', QuestionDetailView.as_view(), name='detail_question'),
    url(r'^buscar-ajax/', discuss.apps.discuss.views.BuscarAjax, name='buscar'),
]
