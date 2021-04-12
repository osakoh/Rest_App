from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', include('fbvAPP.urls')),
    path('student/', include('cbvAPP.urls')),

]
