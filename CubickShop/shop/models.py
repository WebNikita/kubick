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
        verbose_name_plural = '!Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):


    class Meta:
        ordering = ('name',)
        verbose_name = 'Позиции'
        verbose_name_plural = 'Позиции'

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
                                on_delete=models.CASCADE,
                                verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название товара')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Ссылка на товар(не трогать)')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Картинка на главной')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    size = models.CharField(max_length=200, db_index=False, verbose_name='Размер')
    article = models.CharField(max_length=200, db_index=False, verbose_name='Артикул')
    sex = models.CharField(max_length=1, 
                          choices=SEX_CHOICES,
                          default=MALE,
                          verbose_name='Пол')
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
    
    def __str__(self):
        return self.name


class Gallery(models.Model):

    class Meta:

        verbose_name = 'Фотографии товара'
        verbose_name_plural = 'Фотографии товара'

    image = models.ImageField(upload_to='gallproducts/%Y/%m/%d', verbose_name='Фото')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')


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
        verbose_name = 'Спецодежда влагозащитная'
        verbose_name_plural = 'Спецодежда влагозащитная'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')



class Clothing_for_hunting_and_fishing(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    season = models.CharField(max_length=255, verbose_name='Сезон')
    
    class Meta:
        verbose_name = 'Одежда для охоты и рыбалки'
        verbose_name_plural = 'Одежда для охоты и рыбалки'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Knitwearg(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    
    class Meta:
        verbose_name = 'Трикотаж'
        verbose_name_plural = 'Трикотаж'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Hats(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    
    class Meta:
        verbose_name = 'Головные уборы'
        verbose_name_plural = 'Головные уборы'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Summer_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    
    class Meta:
        verbose_name = 'Обувь летняя,демисезонная'
        verbose_name_plural = 'Обувь летняя,демисезонная'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Insulated_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    mounting_method = models.CharField(max_length=255, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь утепленная'
        verbose_name_plural = 'Обувь утепленная'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Special_insulated_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    mounting_method = models.CharField(max_length=255, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь специальная, утепленная'
        verbose_name_plural = 'Обувь специальная, утепленная'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class PVC_rubber_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    
    class Meta:
        verbose_name = 'Обувь резиновая ПВХ'
        verbose_name_plural = 'Обувь резиновая ПВХ'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Casual_walking_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=255, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь повседневная, прогулочная'
        verbose_name_plural = 'Обувь повседневная, прогулочная'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Medical_shoes(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=255, verbose_name='Метод крепления')
    
    class Meta:
        verbose_name = 'Обувь медицинская'
        verbose_name_plural = 'Обувь медицинская'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Shoe_accessories(Product):

    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    insulation_material = models.CharField(max_length=255, verbose_name='Утеплитель')
    
    class Meta:
        verbose_name = 'Аксессуары для обуви'
        verbose_name_plural = 'Аксессуары для обуви'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Head_and_face_protection_products(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    mounting_method = models.CharField(max_length=255, verbose_name='Метод крепления')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты головы и лица'
        verbose_name_plural = 'Средства защиты головы и лица'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Means_of_protection_of_the_organs_of_vision(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    lens_coating = models.CharField(max_length=255, verbose_name='Покрытие линз')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов зрения'
        verbose_name_plural = 'Средства защиты органов зрения'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Protective_equipment_during_welding_operations(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=255, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты при проведении сварочных работ'
        verbose_name_plural = 'Средства защиты при проведении сварочных работ'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Hearing_protection_equipment(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов слуха'
        verbose_name_plural = 'Средства защиты органов слуха'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Respiratory_protection_equipment(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=255, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты органов дыхания'
        verbose_name_plural = 'Средства защиты органов дыхания'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Protective_equipment_during_highrise_works(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=255, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Средства защиты при проведении высотных работ'
        verbose_name_plural = 'Средства защиты при проведении высотных работ'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Clothing_with_limited_service_life(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Одежда с ограниченным сроком эксплуатации'
        verbose_name_plural = 'Одежда с ограниченным сроком эксплуатации'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Dielectric_safety_devices(Product):
    
    class Meta:
        verbose_name = 'Диэлектрические средства безопасности'
        verbose_name_plural = 'Диэлектрические средства безопасности'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')



class Knitted_gloves(Product):

    material = models.CharField(max_length=255, verbose_name='Материал')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=255, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    cuff_Type = models.CharField(max_length=255, verbose_name='Тип манжеты')
    
    class Meta:
        verbose_name = 'Перчатки трикотажные'
        verbose_name_plural = 'Перчатки трикотажные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Wool_blend_gloves(Product):

    material = models.CharField(max_length=255, verbose_name='Материал')
    meets_the_requirements_of_the_FSS = models.CharField(max_length=255, verbose_name='Соответствует требованиям ФСС')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    cuff_Type = models.CharField(max_length=255, verbose_name='Тип манжеты')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    insulation_material = models.CharField(max_length=255, verbose_name='Утеплитель')
    сomposition = models.CharField(max_length=255, verbose_name='Состав')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки полушерстяные'
        verbose_name_plural = 'Перчатки полушерстяные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Split_gloves_combined(Product):

    material = models.CharField(max_length=255, verbose_name='Материал')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    lining = models.CharField(max_length=255, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки спилковые, комбинированные'
        verbose_name_plural = 'Перчатки спилковые, комбинированные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Kragi_vachegi(Product):

    material = models.CharField(max_length=255, verbose_name='Материал')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    lining = models.CharField(max_length=255, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')

    class Meta:
        verbose_name = 'Краги, вачеги'
        verbose_name_plural = 'Краги, вачеги'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Specialized_gloves(Product):

    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    protection_class = models.CharField(max_length=255, verbose_name='Класс защиты')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    
    class Meta:
        verbose_name = 'Перчатки специализированные'
        verbose_name_plural = 'Перчатки специализированные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Household_gloves_disposable(Product):

    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Перчатки хозяйственные, одноразовые'
        verbose_name_plural = 'Перчатки хозяйственные, одноразовые'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Working_gloves(Product):

    material = models.CharField(max_length=255, verbose_name='Материал')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    lining = models.CharField(max_length=255, verbose_name='Подкладка')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    product_type = models.CharField(max_length=255, verbose_name='Вид изделия')
    features = models.CharField(max_length=255, verbose_name='Особенности')
    
    class Meta:
        verbose_name = 'Рукавицы рабочие'
        verbose_name_plural = 'Рукавицы рабочие'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Insulated_mittens(Product):

    features = models.CharField(max_length=255, verbose_name='Особенности')
    appointment = models.CharField(max_length=255, verbose_name='Назначение')
    insulation_material = models.CharField(max_length=255, verbose_name='Утеплитель')
    protective_properties = models.CharField(max_length=255, verbose_name='Защитные свойства')
    
    class Meta:
        verbose_name = 'Рукавицы утепленные'
        verbose_name_plural = 'Рукавицы утепленные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Medical_supplies(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Медицинские принадлежности'
        verbose_name_plural = 'Медицинские принадлежности'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Dermatological_agents(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Дерматологические средства'
        verbose_name_plural = 'Дерматологические средства'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Technical_fabrics(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Технические ткани'
        verbose_name_plural = 'Технические ткани'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Detergents_and_household_chemicals(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Моющие средства и бытовая химия'
        verbose_name_plural = 'Моющие средства и бытовая химия'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Firefighting_equipment_fire_extinguishers(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Противопожарные средства,огнетушители'
        verbose_name_plural = 'Противопожарные средства,огнетушители'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Protective_equipment(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Оградительные средства'
        verbose_name_plural = 'Оградительные средства'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Household_goods(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Хозяйственные товары'
        verbose_name_plural = 'Хозяйственные товары'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Snow_removal_equipment(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Снегоуборочный инвентарь'
        verbose_name_plural = 'Снегоуборочный инвентарь'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Gardening_tools(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Садово-огородный инвентарь'
        verbose_name_plural = 'Садово-огородный инвентарь'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bristle_and_brush_products(Product):

    sub_category = models.CharField(max_length=255, verbose_name='Подкатегория')
    
    class Meta:
        verbose_name = 'Щетинно щеточные изделия'
        verbose_name_plural = 'Щетинно щеточные изделия'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bed_linen_sets(Product):

    
    class Meta:
        verbose_name = 'Комплекты постельного белья'
        verbose_name_plural = 'Комплекты постельного белья'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Mattresses(Product):

    
    class Meta:
        verbose_name = 'Матрасы'
        verbose_name_plural = 'Матрасы'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Blankets(Product):

    
    class Meta:
        verbose_name = 'Одеяла'
        verbose_name_plural = 'Одеяла'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Pillows(Product):

    
    class Meta:
        verbose_name = 'Подушки'
        verbose_name_plural = 'Подушки'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Bedspreads_blankets(Product):

    
    class Meta:
        verbose_name = 'Покрывала, пледы'
        verbose_name_plural = 'Покрывала, пледы'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Waffle_towels(Product):

    
    class Meta:
        verbose_name = 'Полотенца вафельные'
        verbose_name_plural = 'Полотенца вафельные'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Terry_towels(Product):

    
    class Meta:
        verbose_name = 'Полотенца махровые'
        verbose_name_plural = 'Полотенца махровые'

    def __str__(self):
        return f"{self.category.name} : {self.title}"

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')
