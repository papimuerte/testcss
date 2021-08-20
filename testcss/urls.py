"""testcss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from testcss import views

urlpatterns = [
    path('',views.login_redirect, name="login_redirect"),
    #path('users/',include('users.urls')),
    path('users/',include(('users.urls','users'), namespace='users')),
    path('admin/', admin.site.urls),
    path('hello_world/',include('hello_world.urls')),
    #path('hello_world/',include(('hello_world.urls','hello_world'), namespace='hello_world')),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
