from django import forms
from core.models import Service, Project, ProjectImage, GalleryImage, Stat, CompanyInfo, Sustainability


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'short_description': forms.Textarea(attrs={'rows': 3}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 8}),
            'short_description': forms.Textarea(attrs={'rows': 3}),
        }


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ['image', 'caption', 'order']


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'


class StatForm(forms.ModelForm):
    class Meta:
        model = Stat
        fields = '__all__'


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields = '__all__'
        widgets = {
            'about_text': forms.Textarea(attrs={'rows': 6}),
            'mission_text': forms.Textarea(attrs={'rows': 4}),
            'vision_text': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class SustainabilityForm(forms.ModelForm):
    class Meta:
        model = Sustainability
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 8}),
        }
