from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import (
    Language, PageModels, Content,
    ContentText, ContentFile, ContentImage, ContentVideo
)

from .serializers import (
    LanguageSerializer, PageModelsSerializer, ContentSerializer,
    ContentTextSerializer, ContentFileSerializer, ContentImageSerializer, ContentVideoSerializer
)


# -------- LANGUAGE API --------
class LanguageAPIView(APIView):
    def get(self, request):
        langs = Language.objects.all()
        serializer = LanguageSerializer(langs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=LanguageSerializer)
    def post(self, request):
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LanguageDetailAPIView(APIView):
    def get(self, request, pk):
        lang = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(lang)
        return Response(serializer.data)

    def put(self, request, pk):
        lang = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(lang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        lang = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(lang, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        lang = get_object_or_404(Language, pk=pk)
        lang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- PAGE MODELS API --------
class PageModelsAPIView(APIView):
    def get(self, request):
        pages = PageModels.objects.all()
        serializer = PageModelsSerializer(pages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PageModelsSerializer)
    def post(self, request):
        serializer = PageModelsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetailAPIView(APIView):
    def get(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        serializer = PageModelsSerializer(page)
        return Response(serializer.data)

    def put(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        serializer = PageModelsSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        serializer = PageModelsSerializer(page, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- CONTENT API --------
class ContentAPIView(APIView):
    def get(self, request):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentSerializer)
    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentDetailAPIView(APIView):
    def get(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentSerializer(content)
        return Response(serializer.data)

    def put(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentSerializer(content, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        serializer = ContentSerializer(content, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        content = get_object_or_404(Content, pk=pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- CONTENT TEXT API --------
class ContentTextAPIView(APIView):
    def get(self, request):
        texts = ContentText.objects.all()
        serializer = ContentTextSerializer(texts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentTextSerializer)
    def post(self, request):
        serializer = ContentTextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContentTextDetailAPIView(APIView):
    def get(self, request, pk):
        text = get_object_or_404(ContentText, pk=pk)
        serializer = ContentTextSerializer(text)
        return Response(serializer.data)

    def put(self, request, pk):
        text = get_object_or_404(ContentText, pk=pk)
        serializer = ContentTextSerializer(text, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        text = get_object_or_404(ContentText, pk=pk)
        serializer = ContentTextSerializer(text, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        text = get_object_or_404(ContentText, pk=pk)
        text.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------- CONTENT FILE API --------
class ContentFileAPIView(APIView):
    def get(self, request):
        files = ContentFile.objects.all()
        serializer = ContentFileSerializer(files, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentFileSerializer)
    def post(self, request):
        serializer = ContentFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------- CONTENT IMAGE API --------
class ContentImageAPIView(APIView):
    def get(self, request):
        images = ContentImage.objects.all()
        serializer = ContentImageSerializer(images, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentImageSerializer)
    def post(self, request):
        serializer = ContentImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------- CONTENT VIDEO API --------
class ContentVideoAPIView(APIView):
    def get(self, request):
        videos = ContentVideo.objects.all()
        serializer = ContentVideoSerializer(videos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ContentVideoSerializer)
    def post(self, request):
        serializer = ContentVideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
