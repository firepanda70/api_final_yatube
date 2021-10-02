from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    pub_date = serializers.DateTimeField(read_only=True,
                                         format='%Y-%m-%dT%H:%M:%SZ')

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')
    following = serializers.SlugRelatedField(slug_field='username',
                                             queryset=User.objects)

    class Meta:
        model = Follow
        fields = ('user', 'following', )

    def create(self, validated_data):
        user = self.context['request'].user
        following = validated_data['following']
        if user == following:
            raise APIException(code=status.HTTP_400_BAD_REQUEST,
                               detail='Нельзя подписаться на самого себя')
            # Ошибки поднимаются неправильно, в Postman указан код 500,
            # нужна подсказка
        if len(Follow.objects.filter(user=user, following=following)) != 0:
            raise APIException(code=status.HTTP_400_BAD_REQUEST,
                               detail='Вы уже подписаны')
        return Follow.objects.create(user=user, following=following)
