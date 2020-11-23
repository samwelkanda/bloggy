from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique_for_date='created')
    author = models.ForeignKey(User,
                            related_name='blog_posts',
                            on_delete=models.CASCADE)
    body = models.TextField()
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now) 

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title