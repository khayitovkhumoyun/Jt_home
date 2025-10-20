from rest_framework import serializers
from .models import *


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

from rest_framework import serializers
from .models import (
    Content, ContentText, ContentFile, ContentImage, ContentVideo,
    News, NewsText, NewsFile, NewsImage, NewsVideo, NewsType
)

# ======================
#   CONTENT SERIALIZERS
# ======================

class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentText
        fields = '__all__'


class ContentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentFile
        fields = '__all__'


class ContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentImage
        fields = '__all__'


class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentVideo
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    texts = ContentTextSerializer(many=True, read_only=True)
    files = ContentFileSerializer(many=True, read_only=True)
    images = ContentImageSerializer(many=True, read_only=True )
    videos = ContentVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Content
        fields = '__all__'


# ======================
#     NEWS SERIALIZERS
# ======================

class NewsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsType
        fields = '__all__'


class NewsTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsText
        fields = '__all__'


class NewsFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsFile
        fields = '__all__'


class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'


class NewsVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsVideo
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    type = NewsTypeSerializer(read_only=True)
    texts = NewsTextSerializer(many=True, read_only=True)
    files = NewsFileSerializer(many=True, read_only=True)
    images = NewsImageSerializer(many=True, read_only=True)
    videos = NewsVideoSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = '__all__'
