from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse



class ProductManager:

    @staticmethod
    def get_products_for_main_page(*args,**kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')
            products.extend(model_products)
        return products


class All_products:

    objects = ProductManager()


def get_product_url(obj,viewname):
    print(obj.__class__)
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})



class Category(models.Model):
    
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = '!Категории'

    def get_absolute_url(self):
        return reverse('category_detail', kargs={self: self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):


    class Meta:
        ordering = ('name',)
        verbose_name = 'Позиции'
        verbose_name_plural = 'Позиции'

    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE,
                                verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название товара')
    full_name = models.CharField(max_length=200, db_index=True, verbose_name='Полное название товара')
    slug = models.CharField(max_length=200, db_index=True, verbose_name='Ссылка на товар(не трогать)')
    image = models.FileField (upload_to='products/', blank=True, verbose_name='Картинки товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    article = models.CharField(max_length=200, db_index=False, verbose_name='Артикул')
    
    
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')
    
    def __str__(self):
        return self.name


class Gallery(models.Model):

    class Meta:

        verbose_name = 'Фотографии товара'
        verbose_name_plural = 'Фотографии товара'

    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def get_urls_to_img(self):
        return self.image


class Summer_workwear(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    

    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)

    class Meta:
        verbose_name = 'Летняя спецодежда'
        verbose_name_plural = 'Летняя спецодежда'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Winter_workwear(Product):


    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protection_class = models.CharField(max_length=500, verbose_name='Класс защиты')

    class Meta:
        verbose_name = 'Зимняя спецодежда'
        verbose_name_plural = 'Зимняя спецодежда'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Medical_workwear(Product):


    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Медицинская спецодежда'
        verbose_name_plural = 'Медицинская спецодежда'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Clothing_for_the_service_sector(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Одежда для сферы услуг'
        verbose_name_plural = 'Одежда для сферы услуг'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Protective_clothing_of_security_structures(Product):
    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Спецодежда охранных структур'
        verbose_name_plural = 'Спецодежда охранных структур'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Special_workwear(Product):
    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protective_properties = models.TextField(max_length=500, verbose_name='Защитные свойства')
    protection_class = models.CharField(max_length=500, verbose_name='Класс защиты')
    
    class Meta:
        verbose_name = 'Специальная спецодежда'
        verbose_name_plural = 'Специальная спецодежда'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Signal_workwear(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protection_class = models.CharField(max_length=500, verbose_name='Класс защиты')
    
    class Meta:
        verbose_name = 'Сигнал спецодежда'
        verbose_name_plural = 'Сигнал спецодежда'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Protective_protective_workwear(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protection_class = models.CharField(max_length=500, verbose_name='Класс защиты')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Спецодежда влагозащитная'
        verbose_name_plural = 'Спецодежда влагозащитная'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')



class Clothing_for_hunting_and_fishing(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    season = models.CharField(max_length=500, verbose_name='Сезон')
    
    class Meta:
        verbose_name = 'Одежда для охоты и рыбалки'
        verbose_name_plural = 'Одежда для охоты и рыбалки'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Knitwearg(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    
    class Meta:
        verbose_name = 'Трикотаж'
        verbose_name_plural = 'Трикотаж'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Hats(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)

    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Головные уборы'
        verbose_name_plural = 'Головные уборы'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Summer_shoes(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    
    class Meta:
        verbose_name = 'Обувь летняя,демисезонная'
        verbose_name_plural = 'Обувь летняя,демисезонная'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Insulated_shoes(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    mounting_method = models.CharField(max_length=500, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь утепленная'
        verbose_name_plural = 'Обувь утепленная'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Special_insulated_shoes(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    mounting_method = models.CharField(max_length=500, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь специальная, утепленная'
        verbose_name_plural = 'Обувь специальная, утепленная'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class PVC_rubber_shoes(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    
    class Meta:
        verbose_name = 'Обувь резиновая ПВХ'
        verbose_name_plural = 'Обувь резиновая ПВХ'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Casual_walking_shoes(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=500, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь повседневная, прогулочная'
        verbose_name_plural = 'Обувь повседневная, прогулочная'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Medical_shoes(Product):
    
    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=500, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь медицинская'
        verbose_name_plural = 'Обувь медицинская'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Shoe_accessories(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    insulation_material = models.CharField(max_length=500, verbose_name='Утеплитель')
    
    class Meta:
        verbose_name = 'Аксессуары для обуви'
        verbose_name_plural = 'Аксессуары для обуви'


    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Head_and_face_protection_products(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=500, verbose_name='Метод крепления')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты головы и лица'
        verbose_name_plural = 'Средства защиты головы и лица'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Means_of_protection_of_the_organs_of_vision(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    lens_coating = models.CharField(max_length=500, verbose_name='Покрытие линз')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов зрения'
        verbose_name_plural = 'Средства защиты органов зрения'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Protective_equipment_during_welding_operations(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=500, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты при проведении сварочных работ'
        verbose_name_plural = 'Средства защиты при проведении сварочных работ'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Hearing_protection_equipment(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов слуха'
        verbose_name_plural = 'Средства защиты органов слуха'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Respiratory_protection_equipment(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=500, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов дыхания'
        verbose_name_plural = 'Средства защиты органов дыхания'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Protective_equipment_during_highrise_works(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=500, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты при проведении высотных работ'
        verbose_name_plural = 'Средства защиты при проведении высотных работ'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Clothing_with_limited_service_life(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Одежда с ограниченным сроком эксплуатации'
        verbose_name_plural = 'Одежда с ограниченным сроком эксплуатации'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Dielectric_safety_devices(Product):
    
    class Meta:
        verbose_name = 'Диэлектрические средства безопасности'
        verbose_name_plural = 'Диэлектрические средства безопасности'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')



class Knitted_gloves(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    material = models.CharField(max_length=500, verbose_name='Материал')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=500, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    cuff_Type = models.CharField(max_length=500, verbose_name='Тип манжеты')
    
    class Meta:
        verbose_name = 'Перчатки трикотажные'
        verbose_name_plural = 'Перчатки трикотажные'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Wool_blend_gloves(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    material = models.CharField(max_length=500, verbose_name='Материал')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=500, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    cuff_Type = models.CharField(max_length=500, verbose_name='Тип манжеты')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    insulation_material = models.CharField(max_length=500, verbose_name='Утеплитель')
    сomposition = models.CharField(max_length=500, verbose_name='Состав')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки полушерстяные'
        verbose_name_plural = 'Перчатки полушерстяные'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Split_gloves_combined(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    material = models.CharField(max_length=500, verbose_name='Материал')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    lining = models.CharField(max_length=500, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки спилковые, комбинированные'
        verbose_name_plural = 'Перчатки спилковые, комбинированные'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Kragi_vachegi(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    material = models.CharField(max_length=500, verbose_name='Материал')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    lining = models.CharField(max_length=500, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')

    class Meta:
        verbose_name = 'Краги, вачеги'
        verbose_name_plural = 'Краги, вачеги'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Specialized_gloves(Product):

    MALE = 'м'
    FEMAIL = 'ж'
    FORALL = 'в'

    SEX_CHOICES = [
        (MALE, 'Mужской'),
        (FEMAIL, 'Женский'),
        (FORALL, 'Для всех'),
    ]
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол',
                          null=True)
    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    protection_class = models.CharField(max_length=500, verbose_name='Класс защиты')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    
    class Meta:
        verbose_name = 'Перчатки специализированные'
        verbose_name_plural = 'Перчатки специализированные'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Household_gloves_disposable(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки хозяйственные, одноразовые'
        verbose_name_plural = 'Перчатки хозяйственные, одноразовые'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Working_gloves(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    material = models.CharField(max_length=500, verbose_name='Материал')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    lining = models.CharField(max_length=500, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=500, verbose_name='Вид изделия')
    features = models.CharField(max_length=512, verbose_name='Особенности')
    
    class Meta:
        verbose_name = 'Рукавицы рабочие'
        verbose_name_plural = 'Рукавицы рабочие'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Insulated_mittens(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    features = models.CharField(max_length=512, verbose_name='Особенности')
    appointment = models.CharField(max_length=500, verbose_name='Назначение')
    insulation_material = models.CharField(max_length=500, verbose_name='Утеплитель')
    protective_properties = models.CharField(max_length=500, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Рукавицы утепленные'
        verbose_name_plural = 'Рукавицы утепленные'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Medical_supplies(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Медицинские принадлежности'
        verbose_name_plural = 'Медицинские принадлежности'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Dermatological_agents(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Дерматологические средства'
        verbose_name_plural = 'Дерматологические средства'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Technical_fabrics(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Технические ткани'
        verbose_name_plural = 'Технические ткани'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Detergents_and_household_chemicals(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Моющие средства и бытовая химия'
        verbose_name_plural = 'Моющие средства и бытовая химия'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Firefighting_equipment_fire_extinguishers(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Противопожарные средства,огнетушители'
        verbose_name_plural = 'Противопожарные средства,огнетушители'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Protective_equipment(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Оградительные средства'
        verbose_name_plural = 'Оградительные средства'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Household_goods(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Хозяйственные товары'
        verbose_name_plural = 'Хозяйственные товары'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Snow_removal_equipment(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Снегоуборочный инвентарь'
        verbose_name_plural = 'Снегоуборочный инвентарь'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Gardening_tools(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Садово-огородный инвентарь'
        verbose_name_plural = 'Садово-огородный инвентарь'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Bristle_and_brush_products(Product):

    sub_category = models.CharField(max_length=500, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Щетинно щеточные изделия'
        verbose_name_plural = 'Щетинно щеточные изделия'

    

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Bed_linen_sets(Product):

    class Meta:
        verbose_name = 'Комплекты постельного белья'
        verbose_name_plural = 'Комплекты постельного белья'

    

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Mattresses(Product):

    
    class Meta:
        verbose_name = 'Матрасы'
        verbose_name_plural = 'Матрасы'

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Blankets(Product):

    
    class Meta:
        verbose_name = 'Одеяла'
        verbose_name_plural = 'Одеяла'

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Pillows(Product):

    
    class Meta:
        verbose_name = 'Подушки'
        verbose_name_plural = 'Подушки'

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Bedspreads_blankets(Product):

    
    class Meta:
        verbose_name = 'Покрывала, пледы'
        verbose_name_plural = 'Покрывала, пледы'

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Waffle_towels(Product):

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    class Meta:
        verbose_name = 'Полотенца вафельные'
        verbose_name_plural = 'Полотенца вафельные'

    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')


class Terry_towels(Product):

    
    class Meta:
        verbose_name = 'Полотенца махровые'
        verbose_name_plural = 'Полотенца махровые'

    size = models.TextField(max_length=500, db_index=False, verbose_name='Размер', null=True)
    def get_absolute_url(self):
        return get_product_url(self, 'shop:product_detail')



