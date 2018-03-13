from django.conf.urls import url
from django.conf.urls import include
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.welcome,name='welcome'),
    url(r'^home/$',views.home,name='home'),
    url(r'^picture/(\d+)',views.picture,name='picture'),
    url(r'^new/image$', views.new_image, name = 'new-image')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
