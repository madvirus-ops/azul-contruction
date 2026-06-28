from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Service, Project, GalleryImage, Stat, CompanyInfo, Sustainability


def home(request):
    company = CompanyInfo.objects.first()
    services = Service.objects.all()
    stats = Stat.objects.all()
    featured_projects = Project.objects.filter(featured=True)[:6]
    gallery = GalleryImage.objects.filter(featured=True)[:8]
    return render(request, 'core/home.html', {
        'company': company,
        'services': services,
        'stats': stats,
        'featured_projects': featured_projects,
        'gallery_images': gallery,
    })


class ServicesView(ListView):
    model = Service
    template_name = 'core/services.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'core/service_detail.html'
    context_object_name = 'service'


class ProjectsView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'
    paginate_by = 12


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'core/project_detail.html'
    context_object_name = 'project'


class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = CompanyInfo.objects.first()
        context['stats'] = Stat.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company'] = CompanyInfo.objects.first()
        return context

    def post(self, request, *args, **kwargs):
        from django.contrib import messages
        from django.shortcuts import redirect
        from .models import ContactMessage
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('message', '')
        if name and email and msg:
            ContactMessage.objects.create(name=name, email=email, phone=phone, message=msg)
            messages.success(request, 'Thank you for your message. We will get back to you shortly.')
        return redirect('contact')


class SustainabilityView(ListView):
    model = Sustainability
    template_name = 'core/sustainability.html'
    context_object_name = 'entries'


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'gallery_images': images})
