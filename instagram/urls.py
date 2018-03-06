from django.conf.urls import url,settings
from .import views 
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.welcome,name='welcome'),
    url('^home/$',views.home,name='home')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
