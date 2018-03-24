"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from blog.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/$', views.article, name='article'),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'loginlogout/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'loginlogout/logout.html'}),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
