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
    file = open(f"C:\\Users\\shvora.n\\Desktop\\Out\\kubick\\CubickShop\\shop\\templates\\shop\\category\\{name}_filter.html", "w+", encoding='utf-8')
    file.write("""
   <ul class="sidebar__list_filter_first">
    <p class="filter_first_one-head">
        Защитные свойства
        <svg class="filter_first_one-button" xmlns="http://www.w3.org/2000/svg" width="10" height="10" fill="none" viewBox="0 0 10 10">
            <path fill="#767676" d="M8.833 1.917L5 5.75 1.167 1.917 0 3.083l5 5 5-5-1.167-1.167z"/>
        </svg>
    </p>
    <ul class="filter_first_one-content filter">
        <li id="f1-1">Кислоты</li>
        <li id="f1-2">Вредные биологические факторы</li>
        <li id="f1-3">Искры, брызги расплавленного металла</li>
        <li id="f1-4">Общие производственные загрязнения</li>
        <li id="f1-5">Тепловое излучение</li>
        <li id="f1-6">Вибрация</li>
        <li id="f1-7">Нагретые поверхности</li>
        <li id="f1-8">Статическое электричество</li>
    </ul>
</ul>
<ul class="sidebar__list_filter_second">
    <p class="filter_first_two-head">    
        Комплектность
        <svg class="filter_first_two-button" xmlns="http://www.w3.org/2000/svg" width="10" height="10" fill="none" viewBox="0 0 10 10">
            <path fill="#767676" d="M8.833 1.917L5 5.75 1.167 1.917 0 3.083l5 5 5-5-1.167-1.167z"/>
        </svg>
    </p>
    <ul class="filter_first_two-content filter">
        <li id="f2-1">Куртка</li>
        <li id="f2-2">Брюки</li>
        <li id="f2-3">Полукомбинезон</li>
        <li id="f2-4">Комбинезон</li>
        <li id="f2-5">Жилет</li>
        <li id="f2-6">Халат</li>
        <li id="f2-7">Костюм</li>
    </ul>
</ul>
<ul class="sidebar__list_filter_third">
    <p class="filter_first_four-head">
        Состав
        <svg class="filter_first_four-button" xmlns="http://www.w3.org/2000/svg" width="10" height="10" fill="none" viewBox="0 0 10 10">
            <path fill="#767676" d="M8.833 1.917L5 5.75 1.167 1.917 0 3.083l5 5 5-5-1.167-1.167z"/>
        </svg>
    </p>
    <ul class="filter_first_four-content filter">
        <li id="f3-1">65%ПЭ/35%ХБ</li>
        <li id="f3-2">80%ХБ/20%ПЭ,антист.нить</li>
        <li id="f3-3">95%ХБ/5%ПА, антистатическая нить</li>
        <li id="f3-4">100% ПЭ</li>
        <li id="f3-5">100% ХБ</li>
        <li id="f3-6">23%ХБ 77%ПЭ</li>
        <li id="f3-7">53%ХБ 47%ПЭ</li>
        <li id="f3-8">35%ХБ 65%ПЭ</li>
        <li id="f3-9">33%ХБ 67%ПЭ</li>
        <li id="f3-10">60%ХБ/40%ПЭ</li>
        <li id="f3-11">80%ХБ/20%ПЭ</li>
        <li id="f3-12">20%ХБ/80%ПЭ</li>
        <li id="f3-13">51%ХБ 49%ПЭ</li>
        <li id="f3-14">100% ПА</li>
        <li id="f3-15">80%ПЭ/20%ХБ</li>
    </ul>
</ul>
<ul class="sidebar__list_filter_fourth">
    <p class="filter_first_three-head"> 
        Класс защиты
        <svg class="filter_first_three-button" xmlns="http://www.w3.org/2000/svg" width="10" height="10" fill="none" viewBox="0 0 10 10">
            <path fill="#767676" d="M8.833 1.917L5 5.75 1.167 1.917 0 3.083l5 5 5-5-1.167-1.167z"/>
        </svg>
    </p>
    <ul class="filter_first_three-content filter">
        <li id="f4-1">2  класс</li>
        <li id="f4-2">3</li>
        <li id="f4-3">1</li>
        <li id="f4-4">1-2</li>
    </ul>
</ul>
    """)
    file.close()