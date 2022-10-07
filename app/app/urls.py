from django.contrib import admin
from rest_framework import routers
from django.urls import include, path
from django.conf.urls import url
from main import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]