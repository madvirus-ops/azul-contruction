from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Project, ProjectImage, GalleryImage, Stat, CompanyInfo, Sustainability, ContactMessage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    fields = ['image', 'caption', 'order']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'location', 'status', 'completion_year', 'featured', 'image_preview']
    list_filter = ['status', 'featured', 'services']
    search_fields = ['title', 'client', 'location']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Details', {
            'fields': ('client', 'location', 'status', 'completion_year', 'services')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Display', {
            'fields': ('featured',)
        }),
    )

    def image_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" style="max-height:50px"/>', obj.featured_image.url)
        return '-'
    image_preview.short_description = 'Image'


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'order', 'featured', 'image_preview']
    list_editable = ['order', 'featured']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height:50px"/>', obj.image.url)
        return '-'
    image_preview.short_description = 'Preview'


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'order']
    list_editable = ['order']


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not CompanyInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Sustainability)
class SustainabilityAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'created_at', 'read']
    list_filter = ['read']
    readonly_fields = ['name', 'email', 'phone', 'message', 'created_at']
    ordering = ['-created_at']
