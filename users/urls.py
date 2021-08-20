from django.conf.urls import url,include
#from users.views import hello_world

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    #url(r"^hello_world/", hello_world, name="hello_world"),
]
