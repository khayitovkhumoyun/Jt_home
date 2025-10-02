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
    sub = models.IntegerField(default=None)
    url = models.CharField(max_length=500)
    position = models.IntegerField(default=None)
    dic = models.TextField(default=None)

    def __str__(self):
        return self.title




class Content(Base):
    page = models.ForeignKey(PageModels, on_delete=models.CASCADE, related_name="contents")
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title


class ContentText(Base):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="texts")
    title = models.TextField()
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} (pos: {self.position})"


class ContentFile(Base):
    title = models.CharField(max_length=255)
    file = models.FileField(default=None, upload_to='files/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class ContentImage(Base):
    title = models.CharField(max_length=255)
    file = models.ImageField(default=None, upload_to='photo/%Y/%m/%d')
    position = models.IntegerField()
    sub = models.BooleanField(default=False)


class ContentVideo(Base):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to="videos/")  # yuklangan video shu yerda saqlanadi
    position = models.IntegerField()
    sub = models.BooleanField(default=False)

    def __str__(self):
        return self.title