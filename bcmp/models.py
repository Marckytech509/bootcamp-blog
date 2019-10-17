from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.FileField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):  # __unicode__ for Python 2
        return self.user.username 


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),('published', 'Published'),)

    title = models.CharField(max_length=250)
    post_logo = models.FileField()
    slug = models.SlugField(max_length=250,unique_for_date='created_on')
    author = models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='published')
    objects = models.Manager()
    published = PublishedManager()
    
    class Meta:
        ordering = ('-created_on',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bcmp:post_detail',args=[self.created_on.year,self.created_on.strftime('%m'),self.created_on.strftime('%d'),self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    reply_to = models.ForeignKey('self', related_name='replies',null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_added = models.DateField(auto_now_add=True)
 
    def __str__(self):
        return self.name + "-" +  self.name

class NewsUsers(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "NewsUser"
        verbose_name_plural = "NewsUsers"
        def __str__(self):
            return self.email