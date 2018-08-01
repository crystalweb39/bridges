from django.db import models
from django.contrib.sites.models import Site

# Create your models here.
class MiscPage(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    active = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    meta_keywords = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/%s.html' %self.slug
    
    class Meta:
        ordering = ('-priority',)
    
class People(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='images/people/', help_text='size:116 X 150', null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    priority = models.IntegerField(default=0)
    linkedin_url = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'People'
        ordering = ('-priority',)
    
class SiteMeta(models.Model):
    site = models.OneToOneField(Site)
    title = models.CharField(max_length=255, null=True, help_text='default page title on each page of the site')
    meta_keywords = models.TextField(help_text='default keywords on each page of the site', default='')
    meta_description = models.TextField(help_text='default description on each page of the site',default='')
    why = models.TextField(blank=True, null=True)
    why_background = models.ImageField(upload_to='images/', help_text='size: 868px X 454px', null=True, blank=True, editable=False)
    service = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.site.domain

class ImageSlider(models.Model):
    image = models.ImageField(upload_to='images/', help_text='size: 868px X 454px', null=True,)
    priority = models.IntegerField(default=0)
    link = models.URLField(blank=True, null=True)
    
    def __unicode__(self):
        return self.image.name
    
    class Meta:
        ordering = ('-priority',)
    
class Enquiry(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True)
    postcode = models.CharField(max_length=20, blank=True, null=True, editable=False)
    comment = models.TextField()
    subscribe = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'Enquires'
        
class Service(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('-priority',)
    
    