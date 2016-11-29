from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from braces.views import LoginRequiredMixin
from .models import Question, Tag, Answer
from .forms import CreateQuestionForm
from django.core import serializers
from django.http import HttpResponse, Http404
from django.core.cache import cache


class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tags'] = tags
        return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    def get_answers(self,question):
        answers = Answer.objects.filter(question=question)
        return answers

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        # question=context['object']) Esto viene del detail
        context['answers'] = self.get_answers(context['object'])
        return context

    def post(self, request, *args, **kwargs):
        answer = Answer()
        # Aca capruramos e usuaario que esta logueado o respindiendo
        answer.user = request.user
        # texto que me mandan por el formulario
        answer.description = request.POST['description']
        # A que pregunta va dirigido
        # enviar el objeto de la pregunta en la que se esta respondiendo
        # kwargs['slug'] esto trae el slug de la pregunta donde me encuentro
        answer.question = Question.objects.get(slug=kwargs['slug'])
        # Guardamos el objeto

        answer.save()
        answers = self.get_answers(answer.question)
        return render(request, 'question_detail.html', {'question': answer.question, 'answers': answers})


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'question_form.html'
    # fields = '__all__'
    form_class = CreateQuestionForm
    # Esta variable es donde se redirige la vista una vez guardado el formulario
    success_url = '/'
    # login_url que valida que si no esta logueado que le redirection a cualquier url ej: uno donde se puedan registrar
    login_url = '/'

    def form_valid(self, form):
        print("valido")
        # Aca el usuario no puede ir en null ya que es llave foranea y para esto tendremos que jalar el usuario logueado
        form.instance.user = self.request.user

        return super(QuestionCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print("invalido")
        return super(QuestionCreateView, self).form_invalid(form)

# PAsamos la peticion request
def BuscarAjax(request):
    if request.is_ajax():
        # con esto estamos trayendo el objeto tag que esta enviando el ajax
        tag = Tag.objects.get(id=request.GET['id'])
        # Traer todas las preguntas referentes a esto
        # Trae una lista de preguntas del tag que le hice click
        # A esta lista tengo que serailizarla y pasarla a un objeto json para devolverselo al ajax
        question = Question.objects.filter(tag= tag)

        # fields que campos quiere que serialize
        data = serializers.serialize('json', question,
                                     fields = {'title','description', 'modified', 'slug'})

        #retornamos una respuesta al ajax
        # content_type que tipo de data estoy respondiendo
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404




