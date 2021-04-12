from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.StudentList.as_view()),
    path('<int:id>/', views.StudentDetail.as_view()),
]
