from django.forms import ModelChoiceField
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Category, Product, Summer_workwear, Winter_workwear
from .models import Medical_workwear, Clothing_for_the_service_sector, Protective_clothing_of_security_structures
from .models import Special_workwear, Signal_workwear, Protective_protective_workwear
from .models import Clothing_for_hunting_and_fishing, Knitwearg, Hats
from .models import Summer_shoes, Insulated_shoes, Special_insulated_shoes
from .models import PVC_rubber_shoes, Casual_walking_shoes, Medical_shoes
from .models import Shoe_accessories, Head_and_face_protection_products, Means_of_protection_of_the_organs_of_vision
from .models import Protective_equipment_during_welding_operations, Hearing_protection_equipment, Respiratory_protection_equipment 
from .models import Protective_equipment_during_highrise_works, Clothing_with_limited_service_life, Dielectric_safety_devices
from .models import Knitted_gloves, Wool_blend_gloves, Split_gloves_combined
from .models import Kragi_vachegi, Specialized_gloves, Household_gloves_disposable
from .models import Working_gloves, Insulated_mittens, Medical_supplies
from .models import Dermatological_agents, Technical_fabrics, Detergents_and_household_chemicals
from .models import Firefighting_equipment_fire_extinguishers, Protective_equipment, Household_goods
from .models import Snow_removal_equipment, Gardening_tools, Bristle_and_brush_products
from .models import Bed_linen_sets, Mattresses, Blankets, Pillows, Bedspreads_blankets
from .models import Waffle_towels, Terry_towels, Gallery

from .resources import Summer_workwearResource, Winter_workwearResource
from .resources import Medical_workwearResource, Clothing_for_the_service_sectorResource, Protective_clothing_of_security_structuresResource
from .resources import Special_workwearResource, Signal_workwearResource, Protective_protective_workwearResource
from .resources import Clothing_for_hunting_and_fishingResource, KnitweargResource, HatsResource
from .resources import Summer_shoesResource, Insulated_shoesResource, Special_insulated_shoesResource
from .resources import PVC_rubber_shoesResource, Casual_walking_shoesResource, Medical_shoesResource
from .resources import Shoe_accessoriesResource, Head_and_face_protection_productsResource, Means_of_protection_of_the_organs_of_visionResource
from .resources import Protective_equipment_during_welding_operationsResource, Hearing_protection_equipmentResource, Respiratory_protection_equipmentResource 
from .resources import Protective_equipment_during_highrise_worksResource, Clothing_with_limited_service_lifeResource, Dielectric_safety_devicesResource
from .resources import Knitted_glovesResource, Wool_blend_glovesResource, Split_gloves_combinedResource
from .resources import Kragi_vachegiResource, Specialized_glovesResource, Household_gloves_disposableResource
from .resources import Working_glovesResource, Insulated_mittensResource, Medical_suppliesResource
from .resources import Dermatological_agentsResource, Technical_fabricsResource, Detergents_and_household_chemicalsResource
from .resources import Firefighting_equipment_fire_extinguishersResource, Protective_equipmentResource, Household_goodsResource
from .resources import Snow_removal_equipmentResource, Gardening_toolsResource, Bristle_and_brush_productsResource
from .resources import Bed_linen_setsResource, MattressesResource, BlanketsResource, PillowsResource, Bedspreads_blanketsResource
from .resources import Waffle_towelsResource, Terry_towelsResource


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Summer_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    
    resource_class = Summer_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='summer_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    


@admin.register(Winter_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Winter_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='winter_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Medical_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Medical_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='medical_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Clothing_for_the_service_sector)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Clothing_for_the_service_sectorResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='clothing_for_the_service_sector'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Protective_clothing_of_security_structures)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Protective_clothing_of_security_structuresResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='protective_clothing_of_security_structures'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Special_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Special_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='special_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Signal_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Signal_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='signal_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Protective_protective_workwear)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Protective_protective_workwearResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='protective_protective_workwear'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Knitwearg)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = KnitweargResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='knitwearg'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Hats)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = HatsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='hats'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Summer_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Summer_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='summer_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Insulated_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Insulated_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='insulated_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Special_insulated_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Special_insulated_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='special_insulated_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(PVC_rubber_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = PVC_rubber_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='pvc_rubber_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Casual_walking_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Casual_walking_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='casual_walking_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Medical_shoes)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Medical_shoesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='medical_shoes'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Shoe_accessories)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Shoe_accessoriesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='shoe_accessories'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Head_and_face_protection_products)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Head_and_face_protection_productsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='head_and_face_protection_products'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Means_of_protection_of_the_organs_of_vision)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Means_of_protection_of_the_organs_of_visionResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='means_of_protection_of_the_organs_of_vision'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Protective_equipment_during_welding_operations)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Protective_equipment_during_welding_operationsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='protective_equipment_during_welding_operations'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Hearing_protection_equipment)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Hearing_protection_equipmentResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            inlines = [GalleryInline,]
            return ModelChoiceField(Category.objects.filter(slug='hearing_protection_equipment'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Respiratory_protection_equipment)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Respiratory_protection_equipmentResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='respiratory_protection_equipment'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Protective_equipment_during_highrise_works)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Protective_equipment_during_highrise_worksResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='protective_equipment_during_highrise_works'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Clothing_with_limited_service_life)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Clothing_with_limited_service_lifeResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='clothing_with_limited_service_life'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Dielectric_safety_devices)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Dielectric_safety_devicesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='dielectric_safety_devices'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Clothing_for_hunting_and_fishing)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Clothing_for_hunting_and_fishingResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='clothing_for_hunting_and_fishing'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Knitted_gloves)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Knitted_glovesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='knitted_gloves'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Wool_blend_gloves)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Wool_blend_glovesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='wool_blend_gloves'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Split_gloves_combined)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Split_gloves_combinedResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='split_gloves_combined'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Kragi_vachegi)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Kragi_vachegiResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='kragi_vachegi'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Specialized_gloves)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Specialized_glovesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='specialized_gloves'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Household_gloves_disposable)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Household_gloves_disposableResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='household_gloves_disposable'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Working_gloves)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Working_glovesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='working_gloves'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Insulated_mittens)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Insulated_mittensResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='insulated_mittens'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Medical_supplies)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Medical_suppliesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='medical_supplies'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

#########################
@admin.register(Dermatological_agents)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Dermatological_agentsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='dermatological_agents'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Technical_fabrics)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Technical_fabricsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='technical_fabrics'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Detergents_and_household_chemicals)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Detergents_and_household_chemicalsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='detergents_and_household_chemicals'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Firefighting_equipment_fire_extinguishers)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Firefighting_equipment_fire_extinguishersResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='firefighting_equipment_fire_extinguishers'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Protective_equipment)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Protective_equipmentResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='protective_equipment'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Household_goods)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Household_goodsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='household_goods'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Snow_removal_equipment)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Snow_removal_equipmentResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='snow_removal_equipment'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Gardening_tools)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Gardening_toolsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='gardening_tools'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Bristle_and_brush_products)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Bristle_and_brush_productsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bristle_and_brush_products'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Bed_linen_sets)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Bed_linen_setsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bed_linen_sets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Mattresses)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = MattressesResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='mattresses'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Blankets)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = BlanketsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='blankets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Pillows)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = PillowsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='pillows'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Bedspreads_blankets)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Bedspreads_blanketsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='bedspreads_blankets'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Waffle_towels)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Waffle_towelsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='waffle_towels'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Terry_towels)
class ProductAdmin(ImportExportModelAdmin):
    inlines = [GalleryInline,]
    list_display = ['name', 'slug', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

    resource_class = Terry_towelsResource

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='terry_towels'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


