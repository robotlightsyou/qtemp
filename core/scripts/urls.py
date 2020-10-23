"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from scripts import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='scripts-index'),
    path('anatomy/', views.anatomy, name='anatomy'),
    path('howto', views.howto, name='howto'),
    path('arm/', views.arm, name='arm'),
    path('addvideo', views.addvideo, name='addvideo'),
    path('batchadjust', views.batchadjust, name='batchadjust'),
    path('bumplower', views.bumplower, name='bumplower'),
    path('fadein', views.fadein, name='fadein'),
    path('projmanager', views.projmanager, name='projmanager'),
    path('uselist', views.uselist, name='uselist'),
]
