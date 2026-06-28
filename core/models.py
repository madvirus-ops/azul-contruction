from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g. 'fa-solid fa-building'")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('upcoming', 'Upcoming'),
    ]

    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=400, blank=True)
    description = models.TextField()
    client = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=300, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    completion_year = models.PositiveIntegerField(blank=True, null=True)
    featured_image = models.ImageField(upload_to='projects/')
    services = models.ManyToManyField(Service, related_name='projects', blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.caption or f"Gallery Image {self.pk}"


class Stat(models.Model):
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.label}"


class CompanyInfo(models.Model):
    name = models.CharField(max_length=200, default='Azul Environmental Engineering Services')
    tagline = models.CharField(max_length=500, blank=True)
    about_text = models.TextField(blank=True)
    mission_text = models.TextField(blank=True)
    vision_text = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    hero_image = models.ImageField(upload_to='company/', blank=True, null=True)

    class Meta:
        verbose_name = 'Company Info'
        verbose_name_plural = 'Company Info'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Sustainability(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='sustainability/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Sustainability'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, help_text='Optional — international format e.g. +1 555 234 5678')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'{self.name} - {self.email}'
