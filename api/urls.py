from django.urls import path
from .views import CreateOption, CreateQuestion, Createquiz, CreateTopic, CreateUser, CreateResult,CreateResultDetail,  QuizListView, QuestionListView, UserListView

urlpatterns = [
    path('QuizListView/', QuizListView.as_view()),
    path('QuestionListView/', QuestionListView.as_view()),
    path('CreateOption/',CreateOption.as_view()),
    path('CreateQuestion/', CreateQuestion.as_view()),
    path('Createquiz/', Createquiz.as_view()),
    path('CreateTopic', CreateTopic.as_view()),
    path('CreateUser',CreateUser.as_view()),
    path('CreateResult', CreateResult.as_view()),
    path('CreateResultDetail', CreateResultDetail.as_view()),
    path('UserListView/', UserListView.as_view())
]