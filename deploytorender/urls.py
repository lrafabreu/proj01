from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from first.views import main_route

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', include('first.urls')),
    path("", main_route),
]
urlpatterns += staticfiles_urlpatterns()
