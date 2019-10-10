from django.conf.urls import url,include
from . import views

app_name = 'bcmp'

urlpatterns = [
    url(r'^Acceuil/$', views.pageA, name='pageA'),
    url(r'^Actualites/$', views.post_list, name='blog'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    url(r'^Inscrire/$', views.register, name='register'),
    url(r'^Connecter/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
]

