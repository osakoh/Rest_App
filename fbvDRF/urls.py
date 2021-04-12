from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv/', include('fbvAPP.urls')),
    path('cbv/', include('cbvAPP.urls')),

]
