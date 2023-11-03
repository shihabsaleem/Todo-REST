"""
URL configuration for Rest_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from RestApp import views
from RestApp.views import TaskViewSet, DueTaskViewSet, CompletedTaskViewSet

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register('task', TaskViewSet)
router.register('completed_task', views.CompletedTaskViewSet)
router.register('due_task', views.DueTaskViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(router.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
