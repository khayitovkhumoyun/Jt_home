from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from yaml import serialize

from .models import (
    Language, PageModels, Content,
    ContentText, ContentFile, ContentImage, ContentVideo
)

from .serializers import (
    LanguageSerializer, PageModelsSerializer, ContentSerializer,
    ContentTextSerializer, ContentFileSerializer, ContentImageSerializer, ContentVideoSerializer, PageSerializer
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

    @swagger_auto_schema(request_body=LanguageSerializer)
    def put(self, request, pk):
        lang = get_object_or_404(Language, pk=pk)
        serializer = LanguageSerializer(lang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=LanguageSerializer)
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

"""
    Page → Category → Subcategory tuzilmasini JSON formatda qaytaradi.
    """
class PageApi(APIView):

    def get(self, request,lan_pk):
        # Agar URL orqali aniq page so‘ralgan bo‘lsa
        lans = Language.objects.all()
        serialize_lan =LanguageSerializer(lans,many=True)
        try:
            page = PageModels.objects.filter(lang=lan_pk).first()
            serializer = PageSerializer(page)
            content={
                "lans":serialize_lan.data,
                "page":serializer.data
            }
            return Response(content)
        except PageModels.DoesNotExist:
            context={
                "data":None,
                "status":False
            }
            return Response(data=context)


class PageDetailAPIView(APIView):
    def get(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        serializer = PageModelsSerializer(page)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PageModelsSerializer)
    def put(self, request, pk):
        page = get_object_or_404(PageModels, pk=pk)
        serializer = PageModelsSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PageModelsSerializer)
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

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import (
    Content, ContentText, ContentFile, ContentImage, ContentVideo,
    News, NewsText, NewsFile, NewsImage, NewsVideo, NewsType
)
from .serializers import (
    ContentSerializer, ContentTextSerializer, ContentFileSerializer,
    ContentImageSerializer, ContentVideoSerializer,
    NewsSerializer, NewsTextSerializer, NewsFileSerializer,
    NewsImageSerializer, NewsVideoSerializer, NewsTypeSerializer
)


# =====================
#     CONTENT VIEWS
# =====================

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all().order_by('-created_ed')
    serializer_class = ContentSerializer
    permission_classes = [AllowAny]


class ContentTextViewSet(viewsets.ModelViewSet):
    queryset = ContentText.objects.all().order_by('position')
    serializer_class = ContentTextSerializer
    permission_classes = [AllowAny]


class ContentFileViewSet(viewsets.ModelViewSet):
    queryset = ContentFile.objects.all().order_by('position')
    serializer_class = ContentFileSerializer
    permission_classes = [AllowAny]


class ContentImageViewSet(viewsets.ModelViewSet):
    queryset = ContentImage.objects.all().order_by('position')
    serializer_class = ContentImageSerializer
    permission_classes = [AllowAny]


class ContentVideoViewSet(viewsets.ModelViewSet):
    queryset = ContentVideo.objects.all().order_by('position')
    serializer_class = ContentVideoSerializer
    permission_classes = [AllowAny]


# =====================
#       NEWS VIEWS
# =====================

class NewsTypeViewSet(viewsets.ModelViewSet):
    queryset = NewsType.objects.all()
    serializer_class = NewsTypeSerializer
    permission_classes = [AllowAny]


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_ed')
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class NewsTextViewSet(viewsets.ModelViewSet):
    queryset = NewsText.objects.all().order_by('position')
    serializer_class = NewsTextSerializer
    permission_classes = [AllowAny]


class NewsFileViewSet(viewsets.ModelViewSet):
    queryset = NewsFile.objects.all().order_by('position')
    serializer_class = NewsFileSerializer
    permission_classes = [AllowAny]


class NewsImageViewSet(viewsets.ModelViewSet):
    queryset = NewsImage.objects.all().order_by('position')
    serializer_class = NewsImageSerializer
    permission_classes = [AllowAny]


class NewsVideoViewSet(viewsets.ModelViewSet):
    queryset = NewsVideo.objects.all().order_by('position')
    serializer_class = NewsVideoSerializer
    permission_classes = [AllowAny]
