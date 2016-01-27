from rest_framework import serializers
from .models import Account, User, Skill
from rest_framework.authtoken.models import Token


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    skills = serializers.PrimaryKeyRelatedField(many=True, required=False, queryset=Skill.objects.all())

    class Meta:
        model = User
        fields = '__all__'



class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Account
        fields = '__all__'
        depth = 2

    # def save(self):
    #     user_data = self.validated_data.pop("user")
    #     u = User.objects.get(user_data["id"])
    #     account = Account.objects.create(user=u, **self.validated_data)
    #     return account
    #
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        u = User.objects.create(**user_data)
        token = Token.objects.get(user_id=u.id)
        account = Account.objects.create(token=token, user=u, **validated_data)
        return account

    def update(self, instance, validated_data):
        print(validated_data)
        instance.password = validated_data["password"]
        instance.user.password = validated_data["password"]
        instance.save()
        return instance

