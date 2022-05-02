from django.db import models
from django.utils.translation import ugettext_lazy as _

class AboutSchool(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True,verbose_name=_('title'))
    image = models.ImageField(blank=True, upload_to='aboutschool',verbose_name=_('image'))
    describtions = models.TextField(verbose_name=_('descriptions'))
    date = models.DateTimeField(auto_now_add=True,verbose_name=_('date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('aboutschool')
        verbose_name_plural = _('aboutchools')


class Managements(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True,verbose_name=_('fullname'))
    pozitions = models.CharField(max_length=200, null=True, blank=True,verbose_name=_('pozitions'))
    image = models.ImageField(null=True, blank=True, upload_to='managements',verbose_name=_('image'))
    phone_number = models.CharField(max_length=20,null=True,blank=True,verbose_name=_('phone_number'))
    biografy = models.TextField(max_length=1000, null=True, blank=True,verbose_name=_('biografy'))
    date = models.DateTimeField(auto_now_add=True,verbose_name=_('date'))

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('management')
        verbose_name_plural = _('managements')


class Staff(models.Model):
    fullname = models.CharField(max_length=200, null=True, blank=True,verbose_name=_('fullname'))
    pozitions = models.CharField(max_length=200, null=True, blank=True,verbose_name=_('pozitions'))
    phone_number = models.CharField(max_length=20, null=True, blank=True,verbose_name=_('phone_number'))
    image = models.ImageField(null=True, blank=True, upload_to='managements',verbose_name=_('image'))
    biografy = models.TextField(max_length=1000, null=True, blank=True,verbose_name=_('biografy'))
    date = models.DateTimeField(auto_now_add=True,verbose_name=_('date'))

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('staff')
        verbose_name_plural = _('staff')

class Author(models.Model):
    author = models.ForeignKey(Staff,on_delete=models.SET_NULL,null=True,verbose_name=_('author'))

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

class News(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True,verbose_name=_('title'))
    short_descriptions = models.CharField(max_length=1000,null=True,blank=True,verbose_name=_('short_descriptions'))
    descriptions = models.TextField(max_length=10000,null=True,blank=True,verbose_name=_('descriptions'))
    image = models.ImageField(upload_to='news',null=True,blank=True,verbose_name=_('image'))
    author = models.CharField(max_length=200,null=True,blank=True,verbose_name=_('author'))
    date = models.DateTimeField(auto_now_add=True,verbose_name=_('date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')


class Contact(models.Model):
    fullname = models.CharField(max_length=200,null=True,blank=True,verbose_name=_('fullname'))
    phone_number = models.CharField(max_length=30,null=True,blank=True,verbose_name=_('phone_number'))
    email = models.EmailField(verbose_name=_('email'))
    text = models.TextField(verbose_name=_('text'))

    def __str__(self):
        return self.fullname or self.email

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

class Banner(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True,verbose_name=_('title'))
    descriptions = models.CharField(max_length=2000, null=True, blank=True,verbose_name=_('descriptions'))
    image = models.ImageField(upload_to='banner',verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')

class Statistics(models.Model):
    science = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('science'))
    students = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('students'))
    teachers = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('teachers'))
    classroom = models.CharField(max_length=50, null=True, blank=True,verbose_name=_('classroom'))

    def __str__(self):
        return self.science

    class Meta:
        verbose_name = _('statistics')
        verbose_name_plural = _('statistic')

class Features(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True,verbose_name=_('title'))
    descriptions = models.TextField(verbose_name=_('descriptions'))
    image = models.ImageField(upload_to='features',verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('feature')
        verbose_name_plural = _('features')

class Gallery(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True,verbose_name=_('title'))
    image = models.ImageField(upload_to='gallery',null=True,blank=True,verbose_name=_('image'))

    def __str__(self):
        return self.title or self.image

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

class Courses(models.Model):
    course_name = models.CharField(max_length=100,null=True,blank=True,verbose_name=_('course_name'))
    fullname = models.CharField(max_length=100,null=True,blank=True,verbose_name=_('fullname'))
    short_description = models.CharField(max_length=1000,null=True,blank=True,verbose_name=_('short_description'))
    description = models.TextField(verbose_name=_('description'))
    day = models.CharField(max_length=19,verbose_name=_('day'))
    price = models.FloatField(verbose_name=_('price'))

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = _('course')
        verbose_name_plural = _('courses')

class Students(models.Model):
    content = models.TextField(verbose_name=_('contact'))
    fullname = models.CharField(max_length=50,verbose_name=_('fullname'))
    image = models.ImageField(upload_to='students',verbose_name=_('image'))
    title = models.CharField(max_length=50,verbose_name=_('title'))

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = _('student')
        verbose_name_plural = _('students')






