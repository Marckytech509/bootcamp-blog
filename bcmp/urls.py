from django.conf.urls import url,include
from . import views

app_name = 'bcmp'

urlpatterns = [
    url(r'^Acceuil/$', views.pageA, name='pageA'),
    url(r'^A-propos/$', views.about, name='about'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
    url(r'^Inscrire/$', views.register, name='register'),
    url(r'^Connecter/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
    url(r'^Newsletter/Success/$', views.newsletter_subscribe, name='newsletter'),
    url(r'^Contact/$', views.contact, name='contact'),
]

