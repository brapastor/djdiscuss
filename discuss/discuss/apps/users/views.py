from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ExtraDataForm
from django.views.generic import View, DetailView
from .models import User
from discuss.apps.discuss.models import Question


class ExtraDataView(View):
    def get(self,request, *args, **kwargs):
        if request.user.status or request.user.email:
            return redirect('/')
        else:
            return render(request, 'extra_data.html')

    def post(self,request,*args,**kwargs):
        form = ExtraDataForm(request.POST)

        if form.is_valid():
            request.user.username = request.POST['username']
            request.user.email = request.POST['email']
            request.user.status = True
            request.user.save()
            # send_email(request)
            return redirect('/')

        else:
            error_username = form['username'].errors.as_text()
            error_email = form['email'].errors.as_text()
            ctx = {'error_username': error_username, 'error_email':error_email}
            return render(request, 'extra_data.html', ctx)


def LogOut(request):
    logout(request)
    return redirect('/')

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user'

    slug_field = 'username'

    # Enviar mas contexto a detail: El contexto que retorna se envia automaticamente a template
    def get_context_data(self, **kwargs):
        # Ejecutar el metodo padre que es DetailView
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # Vamos a traer cada pregunta que hizo este usuario con sus respectivo tag
        # context['object'] trae el objecto que viene con DetailView el objeto del uaurio en donde me encuentro
        questions = Question.objects.filter(user= context['user']).order_by('created')
        # Traer todos los all de cada pregunta
        tags = [question.tag.all() for question in questions]

        # enviamos mas contexto   context['user'] objeto del usuario al cual estoy mostrando el detalle
        facebook = context['object'].social_auth.filter(provider='facebook')
        if facebook:
            context['facebook'] = facebook[0].extra_data['id']

        twitter = context['object'].social_auth.filter(provider='twitter')
        if twitter:
            context['twitter'] = twitter[0].extra_data['access_token']['screen_name']

        # Uniendo la dos listas
        context['ques_tags'] = zip(questions, tags)
        return context

