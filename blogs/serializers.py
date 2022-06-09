
from rest_framework import serializers
from account.models import User
from blogs.models import Blog, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
        ]


class BlogSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()

    @staticmethod
    def get_tag(self):
        if self.id is None:
            return None
        # user = User.objects.get(id=)
        return TagSerializer(self.tag,many= True).data
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'author',
            'body',
            'tag',
            'image1',
            'image2',
            'image3',
            'created_at',
            'updated_at',

        ]
