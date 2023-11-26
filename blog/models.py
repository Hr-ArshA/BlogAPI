import uuid
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from extentions.name_fixer import upload_img_path
from accounts.models import Profile, IPAddress
from django.shortcuts import reverse


# Create your models here.


class Category(models.Model):
    '''
    A class for categorizing blog posts
    '''
    parent = models.ForeignKey(
        'self', 
        default=None, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL,
        related_name='childeren'             
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True)
    position = models.IntegerField()

    class Meta:
        verbose_name = "category"
        verbose_name_plural = 'categories'
        ordering = ["parent__id", "position"]

    def __str__(self):
        return self.title
    

class Post(models.Model):
    class STATUS(models.IntegerChoices):
        draft = 0
        publish = 1
        investigation = 2
        returned = 3
    
    title = models.CharField(_('title'), max_length=256)
    slug = models.SlugField(_('slug'), unique=True)
    category = models.ManyToManyField(Category, related_name='posts', blank=True, null=True)
    author = models.ForeignKey(Profile, related_name='posts', on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(_('content'))
    description = models.CharField(_('description'), max_length=256)
    publish = models.DateTimeField(_("publish"), default=timezone.now)
    cover = models.ImageField(_('cover'), upload_to=upload_img_path)
    is_special = models.BooleanField(_("is special"), default=False)
    views = models.ManyToManyField(IPAddress, through='PostViews', blank=True, related_name='seen',)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    status = models.IntegerField(_('status'), choices=STATUS.choices, default=0)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        ordering = ["-created", "-updated"]

    
    def get_api_url(self):
        try:
            return reverse("api:post_detail", kwargs={'slug': self.slug})
        except:
            None


    @property
    def get_view_count(self):
        return self.views.count()
    
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter(parent=instance)
        return qs
    

class PostViews(models.Model):
    '''
    A class for counting post views
    '''
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    parent = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created", "-updated"]