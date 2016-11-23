
from django.conf.urls import url
from discuss.apps.users.views import LogOut
from .views import ExtraDataView, UserDetailView
urlpatterns = [
    url(r'^log-out/', LogOut, name='logout'),
    url(r'^extra-data/', ExtraDataView.as_view(), name='extra_data'),
    url(r'^usuario/(?P<slug>[-\w]+)/', UserDetailView.as_view(), name='user_detail'),

]
