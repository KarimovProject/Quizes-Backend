from .models import Quiz, Question, Option, User, Detail, Result_detail
from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
        model = Question
        fields = '__all__'

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
        model = Option
        # fields = '__all__'
        exclude = ('is_correct','question')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        model = Detail
        fields = '__all__'
        
class ResultDetailSerializer(serializers.ModelSerializer):
    class Meta:
        user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
        detail = serializers.PrimaryKeyRelatedField(queryset=Detail.objects.all())
        model = Result_detail
        fields = '__all__'
        