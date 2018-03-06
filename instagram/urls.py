from django.conf.urls import url
from .import views 
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.welcome,name='welcome'),
    url('^home/$',views.home,name='home')
]