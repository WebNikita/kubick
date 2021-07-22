CT_MODEL_MODEL_CLASS = [
        'summer_workwear',
        'winter_workwear',
        'medical_workwear',
        'clothing_for_the_service_sector',
        'protective_clothing_of_security_structures',
        'special_workwear',
        'signal_workwear',
        'protective_protective_workwear',
        'clothing_for_hunting_and_fishing',
        'knitwearg',
        'hats',
        'summer_shoes',
        'insulated_shoes',
        'special_insulated_shoes',
        'pvc_rubber_shoes',
        'casual_walking_shoes',
        'medical_shoes',
        'head_and_face_protection_products',
        'means_of_protection_of_the_organs_of_vision',
        'protective_equipment_during_welding_operations',
        'hearing_protection_equipment',
        'respiratory_protection_equipment',
        'protective_equipment_during_highrise_works',
        'clothing_with_limited_service_life',
        'dielectric_safety_devices',
        'knitted_gloves',
        'wool_blend_gloves',
        'split_gloves_combined',
        'kragi_vachegi',
        'specialized_gloves',
        'household_gloves_disposable',
        'working_gloves',
        'insulated_mittens',
        'medical_supplies',
        'dermatological_agents',
        'technical_fabrics',
        'detergents_and_household_chemicals',
        'firefighting_equipment_fire_extinguishers',
        'protective_equipment',
        'household_goods',
        'snow_removal_equipment',
        'gardening_tools',
        'bristle_and_brush_products',
        'bed_linen_sets',
        'mattresses',
        'blankets',
        'pillows',
        'bedspreads_blankets',
        'waffle_towels',
        'terry_towels',
        'shoe_accessories',
]


for name in CT_MODEL_MODEL_CLASS:
    print('test')
    file = open(f"C:\\Users\\shvora.n\\Desktop\\Out\\kubick\\CubickShop\\shop\\templates\\shop\\product\\{name}_specification.html", "w+", encoding='utf-8')
    file.write("""
    <div class="block__product_info block__product_info_second">
        <p class="block__product_info_title">Информация о товаре</p>
        <p class="block__product_info_text" style="text-decoration: underline;">{{ product.name }}</p>
        <div class="block__product_info_second_top">
            <p class="block__product_info_text"> {{ product.description }} </p>
        </div>
        <p class="block__product_info_title">Тип манжеты</p>
        <div class="block__product_info_second_top">
            <p class="block__product_info_text"> {{ product.cuff_Type }} </p>
        </div>
    </div>

    <div class="block__product_info block__product_info_third">
    <div class="block__product_info_third_material">
        <p class="block__product_info_title">Материал</p>
        <ul class="block__product_info_text">
            <li>{{ product.material }}</li>
        </ul>
    </div>
    <div class="block__product_info_third_size">
        <p class="block__product_info_title">Соответствует требованиям ФСС</p>
        <ul class="block__product_info_text">
            <li>{{ product.meets_the_requirements_of_the_FSS }}</li>
        </ul>
    </div>
    <div class="block__product_info_third_size">
        <p class="block__product_info_title">Особенности</p>
        <ul class="block__product_info_text">
            <li>{{ product.features }}</li>
        </ul>
    </div>
    </div>
    """)
    file.close()