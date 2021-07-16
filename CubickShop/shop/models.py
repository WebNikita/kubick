from django.db import models
from django.urls import reverse


def get_product_url(obj,viewname):
    ct_model = obj.__class__.meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class Category(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):

    MALE = 'M'
    FEMAIL = 'Ж'
    FORALL = 'В'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    
    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    size = models.CharField(max_length=200, db_index=False)
    article = models.CharField(max_length=200, db_index=False)
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,)
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def __str__(self):
        return self.name


class Summer_workwear(Product):

    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')

    class Meta:
        verbose_name = 'Летняя спецодежда'
        verbose_name_plural = 'Летняя спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Winter_workwear(Product):

    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')

    class Meta:
        verbose_name = 'Зимняя спецодежда'
        verbose_name_plural = 'Зимняя спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')

class Winter_workwear(Product):

    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')

    class Meta:
        verbose_name = 'Зимняя спецодежда'
        verbose_name_plural = 'Зимняя спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Medical_workwear(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Медицинская спецодежда'
        verbose_name_plural = 'Медицинская спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Medical_workwear(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Медицинская спецодежда'
        verbose_name_plural = 'Медицинская спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Clothing_for_the_service_sector(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Одежда для сферы услуг'
        verbose_name_plural = 'Одежда для сферы услуг'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Protective_clothing_of_security_structures(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Спецодежда охранных структур'
        verbose_name_plural = 'Спецодежда охранных структур'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Special_workwear(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')
    
    class Meta:
        verbose_name = 'Специальная спецодежда'
        verbose_name_plural = 'Специальная спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Signal_workwear(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')
    
    class Meta:
        verbose_name = 'Сигнал спецодежда'
        verbose_name_plural = 'Сигнал спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Protective_protective_workwear(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Сигнал спецодежда'
        verbose_name_plural = 'Сигнал спецодежда'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')