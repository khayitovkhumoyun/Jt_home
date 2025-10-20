from django.db import models


class Base(models.Model):
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.created_ed


class Language(Base):
    title = models.CharField(max_length=50, unique=True)


class PageModels(Base):
    icon = models.ImageField(upload_to="home/icons/", blank=True, null=True)
    title = models.CharField(max_length=255)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    sub = models.IntegerField(blank=True,default=0)
    url = models.CharField(max_length=500,unique=True,null=True,blank=True)
    dic = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title




class Content(Base):
    page = models.ForeignKey(PageModels, on_delete=models.CASCADE, related_name="contents")
    title = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return self.title


class ContentText(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_texts")
    title = models.TextField()
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (pos: {self.position})"


class ContentFile(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_files")
    title = models.CharField(max_length=255)
    file = models.FileField(default=None, upload_to='files/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class ContentImage(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_images")
    title = models.CharField(max_length=255)
    file = models.ImageField(default=None, upload_to='photo/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)


class ContentVideo(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="content_video")
    title = models.CharField(max_length=100,unique=True,null=True,blank=True)
    file = models.URLField(null=True,blank=True)  # yuklangan video shu yerda saqlanadi
    position = models.IntegerField(null=True,blank=True)
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class NewsType(Base):
    title = models.CharField(unique=True,null=True,blank=True)

class News(Base):
    page = models.ForeignKey(PageModels, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(NewsType,on_delete=models.CASCADE,related_name="news")

class NewsText(Base):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="texts")
    title = models.TextField()
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (pos: {self.position})"


class NewsFile(Base):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="files")
    title = models.CharField(max_length=255)
    file = models.FileField(default=None, upload_to='files/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class NewsImage(Base):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="image")
    title = models.CharField(max_length=255)
    file = models.ImageField(default=None, upload_to='photo/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)


class NewsVideo(Base):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="video")
    title = models.CharField(max_length=100,unique=True,null=True,blank=True)
    file = models.URLField(null=True,blank=True)  # yuklangan video shu yerda saqlanadi
    position = models.IntegerField(null=True,blank=True)
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title