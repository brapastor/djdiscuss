from django.views.generic import ListView
from discuss.apps.discuss.models import Question
from discuss.apps.users.models import User

class IndexView(ListView):
    template_name = 'index.html'
    # con model jalamos todo el objeto
    # model = Question

    context_object_name = 'question_list'

    # pero nosotros queremos algo mas personalizado para esto vamos a usar queryset =
    # Jalo todos los obejetos, pero que me devuelva los 5 ultimos
    queryset = Question.objects.all()[:5]

    # Ahora necesitamos los tags de cada pregunta
    # con esta funcion obtengo el querySet de la contulta queryset = Question.objects.all()[:5]
    def get_queryset(self):
        # self.queryset devuelve toda la lista que devuelve la consulta queryset = Question.objects.all()[:5]
        # Lista tags donde se almacena los tags
        tags = [question.tag.all() for question in self.queryset]
        # Retornamos un zip esto manda a la el objeto a la vista
        return zip(self.queryset, tags)

    # mandamos contexto extra
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['total_question'] = Question.objects.count()
        context['total_users'] = User.objects.exclude(is_superuser= True).count()
        return context


