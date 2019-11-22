from django.urls import path
from .views import AssignmentView, BookView, UserView

app_name = "assignments"

urlpatterns = [
    # assignments
    path('assignments/', AssignmentView.as_view()),
    path('assignments/<int:pk>', AssignmentView.as_view()),

    #books
    path('books/', BookView.as_view()),
    path('books/<int:pk>', BookView.as_view()),

    #users
    path('users/', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
]