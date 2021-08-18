from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, request
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from cart.forms import CartAddProductForm

from .mixins import CategoryDetailMixin


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




def main_page(request):
    return render(request, 'shop/main.html')


class SearchResultsView(ListView):
    
    model = Product
    template_name = 'shop/search/search_results.html'
    
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Product.objects.filter(name__icontains=query)
        return object_list

class CategoryDetailView(CategoryDetailMixin, DetailView):

    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'shop/category/category_detail.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self): # новый
        query = self.request.GET.dict()
        if len(query) != 0:
            slug = self.kwargs['slug']
            print(self.queryset)
            object_list = Category.get(name=slug).products
            print(object_list)
            return object_list
        else:
            print(self.queryset)
            return self.queryset

# class FilterProductView(DetailView):
#     model = Product
#     template_name = 'shop/category/category_detail.html'

#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         object_list = Product.objects.filter(name__icontains='Ку')
#         print(object_list)
#         return object_list
        

    # def get_pagination(self):
    #     paginator = Paginator(self.queryset, 2)
    #     page = self.request.GET.get('page')

    #     try:
    #         products = paginator.page(page)
    #     except PageNotAnInteger:
    #         products = paginator.page(1)
    #     except EmptyPage:
    #         products = paginator.page(paginator.num_pages)
    #     print('!!!!!')
    #     print(products, page)

    #     return page, products




class ProductDetailView(DetailView):

    CT_MODEL_MODEL_CLASS = {
        'summer_workwear': Summer_workwear,
        'winter_workwear': Winter_workwear,
        'medical_workwear': Medical_workwear,
        'clothing_for_the_service_sector': Clothing_for_the_service_sector,
        'protective_clothing_of_security_structures': Protective_clothing_of_security_structures,
        'special_workwear': Special_workwear,
        'signal_workwear': Signal_workwear,
        'protective_protective_workwear': Protective_protective_workwear,
        'clothing_for_hunting_and_fishing': Clothing_for_hunting_and_fishing,
        'knitwearg': Knitwearg,
        'hats': Hats,
        'summer_shoes': Summer_shoes,
        'insulated_shoes': Insulated_shoes,
        'special_insulated_shoes': Special_insulated_shoes,
        'pvc_rubber_shoes': PVC_rubber_shoes,
        'casual_walking_shoes': Casual_walking_shoes,
        'medical_shoes': Medical_shoes,
        'shoe_accessories': Shoe_accessories,
        'head_and_face_protection_products': Head_and_face_protection_products,
        'means_of_protection_of_the_organs_of_vision': Means_of_protection_of_the_organs_of_vision,
        'protective_equipment_during_welding_operations': Protective_equipment_during_welding_operations,
        'hearing_protection_equipment': Hearing_protection_equipment,
        'respiratory_protection_equipment': Respiratory_protection_equipment,
        'protective_equipment_during_highrise_works': Protective_equipment_during_highrise_works,
        'clothing_with_limited_service_life': Clothing_with_limited_service_life,
        'dielectric_safety_devices': Dielectric_safety_devices,
        'knitted_gloves': Knitted_gloves,
        'wool_blend_gloves': Wool_blend_gloves,
        'split_gloves_combined': Split_gloves_combined,
        'kragi_vachegi': Kragi_vachegi,
        'specialized_gloves': Specialized_gloves,
        'household_gloves_disposable': Household_gloves_disposable,
        'working_gloves': Working_gloves,
        'insulated_mittens': Insulated_mittens,
        'medical_supplies': Medical_supplies,
        'dermatological_agents': Dermatological_agents,
        'technical_fabrics': Technical_fabrics,
        'detergents_and_household_chemicals': Detergents_and_household_chemicals,
        'firefighting_equipment_fire_extinguishers': Firefighting_equipment_fire_extinguishers,
        'protective_equipment': Protective_equipment,
        'household_goods': Household_goods,
        'snow_removal_equipment': Snow_removal_equipment,
        'gardening_tools': Gardening_tools,
        'bristle_and_brush_products': Bristle_and_brush_products,
        'bed_linen_sets': Bed_linen_sets,
        'mattresses': Mattresses,
        'blankets': Blankets,
        'pillows': Pillows,
        'bedspreads_blankets': Bedspreads_blankets,
        'waffle_towels': Waffle_towels,
        'terry_towels': Terry_towels,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    
    
    context_object_name = 'product'
    template_name = 'shop/product/detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        return context
    


    



