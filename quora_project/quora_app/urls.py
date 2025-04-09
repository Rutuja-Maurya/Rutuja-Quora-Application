from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('post-question/', views.post_question, name='post_question'),
    path('question/<int:pk>/', views.question_detail, name='question_detail'),
    path('question/<int:pk>/edit/', views.edit_question, name='edit_question'),
    path('question/<int:pk>/delete/', views.delete_question, name='delete_question'),
    path('answer/<int:pk>/edit/', views.edit_answer, name='edit_answer'),
    path('answer/<int:pk>/delete/', views.delete_answer, name='delete_answer'),
    path('answer/<int:pk>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:pk>/likers/', views.get_likers, name='get_likers'),
] 