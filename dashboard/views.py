from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count
from core.models import Service, Project, ProjectImage, GalleryImage, Stat, CompanyInfo, Sustainability, ContactMessage
from .forms import (
    ServiceForm, ProjectForm, ProjectImageForm,
    GalleryImageForm, StatForm, CompanyInfoForm,
    SustainabilityForm
)


def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser, login_url='dashboard_login')(view_func)


def dashboard_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('dashboard_home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_superuser:
            login(request, user)
            return redirect('dashboard_home')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')


@login_required(login_url='dashboard_login')
@superuser_required
def dashboard_home(request):
    context = {
        'project_count': Project.objects.count(),
        'project_in_progress': Project.objects.filter(status='in_progress').count(),
        'service_count': Service.objects.count(),
        'gallery_count': GalleryImage.objects.count(),
        'stat_count': Stat.objects.count(),
        'recent_projects': Project.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/index.html', context)


# --- SERVICES ---
@login_required(login_url='dashboard_login')
@superuser_required
def service_list(request):
    services = Service.objects.all()
    return render(request, 'dashboard/services/list.html', {'services': services})


@login_required(login_url='dashboard_login')
@superuser_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service created.')
            return redirect('dashboard_services')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/services/form.html', {'form': form, 'title': 'Add Service'})


@login_required(login_url='dashboard_login')
@superuser_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated.')
            return redirect('dashboard_services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/services/form.html', {'form': form, 'title': 'Edit Service', 'service': service})


@login_required(login_url='dashboard_login')
@superuser_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Service deleted.')
    return redirect('dashboard_services')


# --- PROJECTS ---
@login_required(login_url='dashboard_login')
@superuser_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'dashboard/projects/list.html', {'projects': projects})


@login_required(login_url='dashboard_login')
@superuser_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            messages.success(request, 'Project created.')
            return redirect('dashboard_project_edit', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'dashboard/projects/form.html', {'form': form, 'title': 'Add Project'})


@login_required(login_url='dashboard_login')
@superuser_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.gallery_images.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated.')
            return redirect('dashboard_project_edit', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'dashboard/projects/form.html', {
        'form': form, 'title': 'Edit Project', 'project': project, 'images': images
    })


@login_required(login_url='dashboard_login')
@superuser_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    messages.success(request, 'Project deleted.')
    return redirect('dashboard_projects')


@login_required(login_url='dashboard_login')
@superuser_required
def project_image_add(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = ProjectImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.project = project
            img.save()
            messages.success(request, 'Image added.')
    return redirect('dashboard_project_edit', pk=project.pk)


@login_required(login_url='dashboard_login')
@superuser_required
def project_image_delete(request, pk):
    image = get_object_or_404(ProjectImage, pk=pk)
    project_pk = image.project.pk
    image.delete()
    messages.success(request, 'Image deleted.')
    return redirect('dashboard_project_edit', pk=project_pk)


# --- GALLERY ---
@login_required(login_url='dashboard_login')
@superuser_required
def gallery_list(request):
    images = GalleryImage.objects.all()
    return render(request, 'dashboard/gallery/list.html', {'images': images})


@login_required(login_url='dashboard_login')
@superuser_required
def gallery_create(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added.')
            return redirect('dashboard_gallery')
    else:
        form = GalleryImageForm()
    return render(request, 'dashboard/gallery/form.html', {'form': form, 'title': 'Add Image'})


@login_required(login_url='dashboard_login')
@superuser_required
def gallery_edit(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated.')
            return redirect('dashboard_gallery')
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'dashboard/gallery/form.html', {'form': form, 'title': 'Edit Image'})


@login_required(login_url='dashboard_login')
@superuser_required
def gallery_delete(request, pk):
    image = get_object_or_404(GalleryImage, pk=pk)
    image.delete()
    messages.success(request, 'Image deleted.')
    return redirect('dashboard_gallery')


@login_required(login_url='dashboard_login')
@superuser_required
def gallery_bulk_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        caption = request.POST.get('caption', '')
        featured = request.POST.get('featured') == 'on'
        count = 0
        last_order = GalleryImage.objects.count()
        for i, f in enumerate(files):
            if f:
                GalleryImage.objects.create(
                    image=f,
                    caption=caption,
                    featured=featured,
                    order=last_order + i,
                )
                count += 1
        messages.success(request, f'{count} image{"s" if count != 1 else ""} uploaded successfully.')
        return redirect('dashboard_gallery')
    return redirect('dashboard_gallery')


# --- STATS ---
@login_required(login_url='dashboard_login')
@superuser_required
def stat_list(request):
    stats = Stat.objects.all()
    return render(request, 'dashboard/stats/list.html', {'stats': stats})


@login_required(login_url='dashboard_login')
@superuser_required
def stat_create(request):
    if request.method == 'POST':
        form = StatForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stat created.')
            return redirect('dashboard_stats')
    else:
        form = StatForm()
    return render(request, 'dashboard/stats/form.html', {'form': form, 'title': 'Add Stat'})


@login_required(login_url='dashboard_login')
@superuser_required
def stat_edit(request, pk):
    stat = get_object_or_404(Stat, pk=pk)
    if request.method == 'POST':
        form = StatForm(request.POST, instance=stat)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stat updated.')
            return redirect('dashboard_stats')
    else:
        form = StatForm(instance=stat)
    return render(request, 'dashboard/stats/form.html', {'form': form, 'title': 'Edit Stat'})


@login_required(login_url='dashboard_login')
@superuser_required
def stat_delete(request, pk):
    stat = get_object_or_404(Stat, pk=pk)
    stat.delete()
    messages.success(request, 'Stat deleted.')
    return redirect('dashboard_stats')


# --- COMPANY INFO ---
@login_required(login_url='dashboard_login')
@superuser_required
def company_edit(request):
    company = CompanyInfo.objects.first()
    if not company:
        company = CompanyInfo.objects.create()
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company info updated.')
            return redirect('dashboard_home')
    else:
        form = CompanyInfoForm(instance=company)
    return render(request, 'dashboard/company/form.html', {'form': form, 'company': company})


# --- SUSTAINABILITY ---
@login_required(login_url='dashboard_login')
@superuser_required
def sustainability_list(request):
    entries = Sustainability.objects.all()
    return render(request, 'dashboard/sustainability/list.html', {'entries': entries})


@login_required(login_url='dashboard_login')
@superuser_required
def sustainability_create(request):
    if request.method == 'POST':
        form = SustainabilityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry created.')
            return redirect('dashboard_sustainability')
    else:
        form = SustainabilityForm()
    return render(request, 'dashboard/sustainability/form.html', {'form': form, 'title': 'Add Entry'})


@login_required(login_url='dashboard_login')
@superuser_required
def sustainability_edit(request, pk):
    entry = get_object_or_404(Sustainability, pk=pk)
    if request.method == 'POST':
        form = SustainabilityForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entry updated.')
            return redirect('dashboard_sustainability')
    else:
        form = SustainabilityForm(instance=entry)
    return render(request, 'dashboard/sustainability/form.html', {'form': form, 'title': 'Edit Entry'})


@login_required(login_url='dashboard_login')
@superuser_required
def sustainability_delete(request, pk):
    entry = get_object_or_404(Sustainability, pk=pk)
    entry.delete()
    messages.success(request, 'Entry deleted.')
    return redirect('dashboard_sustainability')


# --- CONTACT MESSAGES ---
@login_required(login_url='dashboard_login')
@superuser_required
def contact_messages(request):
    msgs = ContactMessage.objects.all()
    return render(request, 'dashboard/contact_messages/list.html', {'contact_messages': msgs})


@login_required(login_url='dashboard_login')
@superuser_required
def contact_message_detail(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if not msg.read:
        msg.read = True
        msg.save()
    return render(request, 'dashboard/contact_messages/detail.html', {'contact_msg': msg})


@login_required(login_url='dashboard_login')
@superuser_required
def contact_message_delete(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.delete()
    messages.success(request, 'Message deleted.')
    return redirect('dashboard_contact_messages')
