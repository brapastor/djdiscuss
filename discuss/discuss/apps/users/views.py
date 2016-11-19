from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import ExtraDataForm
from django.views.generic import View


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

# Create your views here.
