from django.db import models
from django.utils import timezone

class Post(models.Model):

	title = models.CharField(max_length=250, verbose_name='Название')


	slug = models.SlugField(max_length=250,unique_for_date='publish')
	img = models.ImageField(null = True, blank = True,verbose_name='Превью изображение')
	previev_text = models.TextField(verbose_name='Текст превью', null = True)
	body = models.TextField(verbose_name='Текст статьи', null = False)
	publish = models.DateTimeField(default=timezone.now, verbose_name='Дата')

	bject = models.Manager()      # Стандарный менаджер

	# def get_absolute_url(self):
	# 	return reverse('ctpo:post_detail', args=[self.publish.year,
	# 		self.publish.month, self.publish.day, self.slug])
	
	def __str__(self):
		return self.title
