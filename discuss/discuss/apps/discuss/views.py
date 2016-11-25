from django.views.generic import ListView, CreateView, DetailView
from braces.views import LoginRequiredMixin
from .models import Question,Tag
from .forms import CreateQuestionForm

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
       context = super(QuestionListView, self).get_context_data(**kwargs)
       context['tags'] = Tag.objects.all()
       return context


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'
    context_object_name = 'question'

    # def post(self, request, *args,**kwargs):









class QuestionCreateView(LoginRequiredMixin,CreateView):
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
