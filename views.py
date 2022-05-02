from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import *
from .form import ContactForm
from django.urls import reverse

class HomeTemplateViews(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['banner'] = Banner.objects.order_by('-pk')
        context['statistics'] = Statistics.objects.order_by('-pk')
        context['features'] = Features.objects.order_by('-pk')[:3]
        context['courses'] = Courses.objects.order_by('-pk')[:3]
        context['students'] = Students.objects.order_by('-pk')[:3]
        context['managements'] = Managements.objects.order_by('-pk')[:4]
        context['staff'] = Managements.objects.order_by('-pk')[:4]
        context['news'] = News.objects.order_by('-pk')[:3]

        return context


class ErrorTemplateViews(TemplateView):
    template_name = '404.html'


class AboutTemplateViews(TemplateView):
    template_name = 'about.html'


class NewsListView(ListView):
    template_name = 'news.html'
    queryset = News.objects.order_by('-pk')


class NewsDetailView(DetailView):
    model = News
    template_name = 'details.html'


class ManagementsListView(ListView):
    model = Managements
    paginate_by = 3
    template_name = 'management.html'


class StaffListView(ListView):
    model = Staff
    template_name = 'staff.html'


class GalleryListView(ListView):
    model = Gallery
    paginate_by = 6
    template_name = 'galeries.html'


class CoursesDetailView(DetailView):
    model = Courses
    template_name = 'course_details.html'


# def contact_views(request):
#     form = ContactForm()
#     context = {'form' : form}
#     return render(request, 'contact.html', context)

class ContactCreateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse('schools220:contact')
