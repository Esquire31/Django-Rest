from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview),
    path('courses/', views.get_courses, name="ViewCourses"),
    path('courses/add/', views.add_courses, name="AddCourse"),
    path('courses/<str:id>/update', views.update_courses, name="UpdateCourses"),
    path('courses/<str:id>/delete', views.delete_courses, name="DeleteCourses"),
]