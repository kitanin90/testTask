from django.urls import path
from .views import *
from . import views

app_name = "assignments"

urlpatterns = [
    # assignments
    path('assignments/', AssignmentView.as_view()),
    path('assignments/<int:pk>', SingleAssignmentView.as_view()),

    #books
    path('books/', BookView.as_view()),
    path('books/<int:pk>', SingleBookView.as_view()),

    #users
    path('users/', UserView.as_view()),
    path('users/<int:pk>', SingleUserView.as_view()),

]

