from rest_framework import serializers
from .models import (
    Language, PageModels, Content,
    ContentText, ContentFile, ContentImage, ContentVideo
)


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class PageModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = PageModels
        fields = ['id','icon','title','lang','url','sub','dic']
        extra_kwargs = {
            'icon': {'required': False, 'allow_null': True},
            'sub': {'required': True, 'allow_null': True},
            'dic': {'required': False, 'allow_null': True},
        }

class ContentSerializer(serializers.ModelSerializer):
    page = PageModelsSerializer(read_only=True)
    page_id = serializers.PrimaryKeyRelatedField(
        queryset=PageModels.objects.all(), source="page", write_only=True
    )

    class Meta:
        model = Content
        fields = "__all__"


class ContentTextSerializer(serializers.ModelSerializer):
    content = ContentSerializer(read_only=True)
    content_id = serializers.PrimaryKeyRelatedField(
        queryset=Content.objects.all(), source="content", write_only=True
    )

    class Meta:
        model = ContentText
        fields = "__all__"


class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = "__all__"


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = "__all__"


class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = "__all__"

from rest_framework import serializers
from .models import PageModels


class SubCategorySerializer(serializers.ModelSerializer):
    """Subcategory (eng ichki daraja)"""
    class Meta:
        model = PageModels
        fields = ['id', 'title', 'url']


class CategorySerializer(serializers.ModelSerializer):
    """Har bir Category ichida subcategorylarni olish"""
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = PageModels
        fields = ['id', 'title', 'url', 'subcategories']

    def get_subcategories(self, obj):
        subcats = PageModels.objects.filter(sub=obj.id)
        return SubCategorySerializer(subcats, many=True).data


class PageSerializer(serializers.ModelSerializer):
    """Page ichida categorylar va ularning subcategorylari"""
    categories = serializers.SerializerMethodField()

    class Meta:
        model = PageModels
        fields = ['id', 'title', 'url', 'categories']

    def get_categories(self, obj):
        cats = PageModels.objects.filter(sub=obj.id)
        return CategorySerializer(cats, many=True).data
