from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)


    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, verbose_name='URL', unique=True)


    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']




class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Post', )
    slug = models.SlugField(max_length=255, verbose_name='URL', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True, verbose_name='Published')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Count views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')


    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
