from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
        path('', views.index, name='index'),path('play_list', views.play_list, name='play_list')]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

