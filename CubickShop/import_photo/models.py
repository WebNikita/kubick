from django.db import models

import os
import shutil
from glob import glob
import py7zr


from shop.models import Category, Product, Summer_workwear, Winter_workwear
from shop.models import Medical_workwear, Clothing_for_the_service_sector, Protective_clothing_of_security_structures
from shop.models import Special_workwear, Signal_workwear, Protective_protective_workwear
from shop.models import Clothing_for_hunting_and_fishing, Knitwearg, Hats
from shop.models import Summer_shoes, Insulated_shoes, Special_insulated_shoes
from shop.models import PVC_rubber_shoes, Casual_walking_shoes, Medical_shoes
from shop.models import Shoe_accessories, Head_and_face_protection_products, Means_of_protection_of_the_organs_of_vision
from shop.models import Protective_equipment_during_welding_operations, Hearing_protection_equipment, Respiratory_protection_equipment 
from shop.models import Protective_equipment_during_highrise_works, Clothing_with_limited_service_life, Dielectric_safety_devices
from shop.models import Knitted_gloves, Wool_blend_gloves, Split_gloves_combined
from shop.models import Kragi_vachegi, Specialized_gloves, Household_gloves_disposable
from shop.models import Working_gloves, Insulated_mittens, Medical_supplies
from shop.models import Dermatological_agents, Technical_fabrics, Detergents_and_household_chemicals
from shop.models import Firefighting_equipment_fire_extinguishers, Protective_equipment, Household_goods
from shop.models import Snow_removal_equipment, Gardening_tools, Bristle_and_brush_products
from shop.models import Bed_linen_sets, Mattresses, Blankets, Pillows, Bedspreads_blankets
from shop.models import Waffle_towels, Terry_towels



def extract_zip(path):
    print(path)
    archive = py7zr.SevenZipFile(path, mode='r')
    archive.extractall(path=os.getcwd() + "/CubickShop/media/products")
    archive.close()
    os.remove(path)

def write_to_db(path):
    for slug in os.listdir(path):
        products_query = Category.objects.get(slug=slug).products.all()
        for item in os.listdir(path + "/" +slug):
            print(item)
            if len(Product.objects.filter(article=item.split('.')[0])) != 0:
                product_info = Product.objects.filter(article=item.split('.')[0])[0]
                product_info.image = f"{path}/{slug}/{item}"
                product_info.save()   


class Products_Photo(models.Model):

    class Meta:
        verbose_name = 'Файл с фото'
        verbose_name_plural = 'Файл с фото'

    image = models.FileField (blank=True, verbose_name='Картинки товара')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        
        extract_zip(path = self.image.path)
        write_to_db(path = os.getcwd()  + '/CubickShop/media/products')






