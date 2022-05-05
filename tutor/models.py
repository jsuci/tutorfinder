from distutils.command.upload import upload
from html.entities import name2codepoint
from django.db import models
from django.core.files import File

from io import BytesIO
from PIL import Image

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Tutor(models.Model):
    category = models.ForeignKey(Category, related_name='tutors', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    profileImage = models.ImageField(upload_to='uploads/', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-dateAdded', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://localhost:8000' + self.thumbnail.url
        else:
            if self.profileImage:
                self.thumbnail = self.make_thumbnail(self.profileImage)
                self.save()
            
                return 'http://localhost:8000' + self.thumbnail.url
            else:
                return ''

    def make_thumbnail(self, profileImage, size=(300, 200)):
        imgObj = Image.open(profileImage)
        imgObj.convert('RGB')
        imgObj.thumbnail(size)

        thumbIO = BytesIO()
        imgObj.save(thumbIO, 'JPEG', quality=85)

        thumbnail = File(thumbIO, name=profileImage.name)
    
        return thumbnail