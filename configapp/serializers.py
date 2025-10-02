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
    lang = LanguageSerializer(read_only=True)
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset=Language.objects.all(), source="lang", write_only=True
    )

    class Meta:
        model = PageModels
        fields = "__all__"


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
