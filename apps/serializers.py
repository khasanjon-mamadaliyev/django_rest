from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.serializers import ModelSerializer

from apps.models import Vote, Choice, Poll


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poll
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        user = User(
            email=validate_data["email"],
            username=validate_data["username"]
        )
        user.set_password(validate_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user
