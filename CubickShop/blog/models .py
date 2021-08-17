from django.db import models
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
	def ger_qeryser(self):
		return super().get_queryset().filter(status='published')


class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'В работе'),
		('published', 'Опубликована'),
		)
	
	title = models.CharField(max_length=250, verbose_name='Название')

	slug = models.SlugField(max_length=250,unique_for_date='publish')
	img = models.ImageField(null = True, blank = True,verbose_name='Превью изображение')
	main_img = models.ImageField(null = True, blank = True,verbose_name='Главное изображение')
	previev_text = models.TextField(verbose_name='Текст превью', null = True)
	body = models.TextField(verbose_name='Текст статьи', null = False)
	publish = models.DateTimeField(default=timezone.now, verbose_name='Дата')
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft', verbose_name='Статус')

	object = models.Manager()
	published = PublishedManager()      # Стандарный менаджер

	def get_absolute_url(self):
		return reverse('blog:blog_detail', args=[self.publish.year,
			self.publish.month, self.publish.day, self.slug])
	
	def __str__(self):
		return self.title
