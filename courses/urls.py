from django.urls import path
from . import views

app_name = 'insta'
urlpatterns=[
    path('', views.home, name='home'),
    path('create/', views.create_student, name='create'),
    path('student/<int:student_id>/', views.student_details, name='details'),
    path('student/<int:student_id>/edit/', views.edit_view, name='edit'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:stu_id>/delete/', views.delete_view, name='delete')
]