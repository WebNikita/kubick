from import_export import resources

from .models import Summer_workwear, Winter_workwear
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



class Summer_workwearResource(resources.ModelResource):

    class Meta:
        model = Summer_workwear



class Winter_workwearResource(resources.ModelResource):

   class Meta:
        model = Winter_workwear
        # exclude = ("product_ptr", 'category','slug','image')
        # fields = ('name','description','price','size','article','sex','protective_properties','product_type','сomposition','protection_class')


class Medical_workwearResource(resources.ModelResource):

    class Meta:
        model = Medical_workwear

class Clothing_for_the_service_sectorResource(resources.ModelResource):

    class Meta:
        model = Clothing_for_the_service_sector


class Protective_clothing_of_security_structuresResource(resources.ModelResource):

    class Meta:
        model = Protective_clothing_of_security_structures


class Special_workwearResource(resources.ModelResource):

    class Meta:
        model = Special_workwear


class Signal_workwearResource(resources.ModelResource):

    class Meta:
        model = Signal_workwear


class Protective_protective_workwearResource(resources.ModelResource):

    class Meta:
        model = Protective_protective_workwear


class Clothing_for_hunting_and_fishingResource(resources.ModelResource):

    class Meta:
        model = Clothing_for_hunting_and_fishing


class KnitweargResource(resources.ModelResource):

    class Meta:
        model = Knitwearg


class HatsResource(resources.ModelResource):

    class Meta:
        model = Hats


class Summer_shoesResource(resources.ModelResource):

    class Meta:
        model = Summer_shoes


class Insulated_shoesResource(resources.ModelResource):

    class Meta:
        model = Insulated_shoes


class Special_insulated_shoesResource(resources.ModelResource):

    class Meta:
        model = Special_insulated_shoes


class PVC_rubber_shoesResource(resources.ModelResource):

    class Meta:
        model = PVC_rubber_shoes


class Casual_walking_shoesResource(resources.ModelResource):

    class Meta:
        model = Casual_walking_shoes


class Medical_shoesResource(resources.ModelResource):

    class Meta:
        model = Medical_shoes


class Shoe_accessoriesResource(resources.ModelResource):

    class Meta:
        model = Shoe_accessories
        # exclude = ('product_ptr','id','category')


class Head_and_face_protection_productsResource(resources.ModelResource):

    class Meta:
        model = Head_and_face_protection_products


class Means_of_protection_of_the_organs_of_visionResource(resources.ModelResource):

   class Meta:
        model = Means_of_protection_of_the_organs_of_vision


class Protective_equipment_during_welding_operationsResource(resources.ModelResource):

    class Meta:
        model = Protective_equipment_during_welding_operations


class Hearing_protection_equipmentResource(resources.ModelResource):

    class Meta:
        model = Hearing_protection_equipment


class Respiratory_protection_equipmentResource(resources.ModelResource):

    class Meta:
        model = Respiratory_protection_equipment


class Protective_equipment_during_highrise_worksResource(resources.ModelResource):

    class Meta:
        model = Protective_equipment_during_highrise_works


class Clothing_with_limited_service_lifeResource(resources.ModelResource):

    class Meta:
        model = Clothing_with_limited_service_life


class Dielectric_safety_devicesResource(resources.ModelResource):
    
    class Meta:
        model = Dielectric_safety_devices



class Knitted_glovesResource(resources.ModelResource):

    class Meta:
        model = Knitted_gloves


class Wool_blend_glovesResource(resources.ModelResource):

    class Meta:
        model = Wool_blend_gloves


class Split_gloves_combinedResource(resources.ModelResource):

    class Meta:
        model = Split_gloves_combined


class Kragi_vachegiResource(resources.ModelResource):

    class Meta:
        model = Kragi_vachegi


class Specialized_glovesResource(resources.ModelResource):

    class Meta:
        model = Specialized_gloves


class Household_gloves_disposableResource(resources.ModelResource):

    class Meta:
        model = Household_gloves_disposable


class Working_glovesResource(resources.ModelResource):

    class Meta:
        model = Working_gloves


class Insulated_mittensResource(resources.ModelResource):

    class Meta:
        model = Insulated_mittens


class Medical_suppliesResource(resources.ModelResource):

    class Meta:
        model = Medical_supplies

class Dermatological_agentsResource(resources.ModelResource):

    class Meta:
        model = Dermatological_agents


class Technical_fabricsResource(resources.ModelResource):

    class Meta:
        model = Technical_fabrics


class Detergents_and_household_chemicalsResource(resources.ModelResource):

    class Meta:
        model = Detergents_and_household_chemicals

class Firefighting_equipment_fire_extinguishersResource(resources.ModelResource):

    class Meta:
        model = Firefighting_equipment_fire_extinguishers


class Protective_equipmentResource(resources.ModelResource):

    class Meta:
        model = Protective_equipment


class Household_goodsResource(resources.ModelResource):

    class Meta:
        model = Household_goods


class Snow_removal_equipmentResource(resources.ModelResource):

    class Meta:
        model = Snow_removal_equipment


class Gardening_toolsResource(resources.ModelResource):

    class Meta:
        model = Gardening_tools


class Bristle_and_brush_productsResource(resources.ModelResource):

    class Meta:
        model = Bristle_and_brush_products


class Bed_linen_setsResource(resources.ModelResource):

    
    class Meta:
        model = Bed_linen_sets


class MattressesResource(resources.ModelResource):

    
    class Meta:
        model = Mattresses


class BlanketsResource(resources.ModelResource):

    
    class Meta:
        model = Blankets


class PillowsResource(resources.ModelResource):

    
    class Meta:
        model = Pillows


class Bedspreads_blanketsResource(resources.ModelResource):

    
    class Meta:
        model = Bedspreads_blankets


class Waffle_towelsResource(resources.ModelResource):

    
    class Meta:
        model = Waffle_towels


class Terry_towelsResource(resources.ModelResource):

    
    class Meta:
        model = Terry_towels
