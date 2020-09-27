ENDPOINT = "https://fr.openfoodfacts.org/cgi/search.pl?"

TAGS = {
    'action': 'process',
    'sort_by': 'unique_scans_n',
    'page_size': '',
    'page': '1',
    'json': 'true',
}

# 'Field_of_the_product_model': 'Field_in_raw_json_data'
FIELDS_PRODUCT = {
    'barre_code': 'code',
    'name': 'product_name_fr',
    'nutriscore': 'nutrition_grade_fr',
    'pict_product': 'image_url',
    'pict_nutriments': 'image_nutrition_url',
}

FIELDS_NUTRIMENTS = {
    'energy_kj': 'energy-kj_100g',
    'energy_kcal': 'energy-kcal_100g',
    'lipid': 'fat_100g',
    'glucid ': 'sugars_100g',
    'fiber': 'fiber_100g',
    'protein': 'proteins_100g',
    'salt': 'salt_100g',
}

FIELDS_CATEGORIES = {
    'name': 'categories',
}

# 'key_looking_for_in_json_data': 'value_required'
VALUE_REQUIRED = {
    'complete': '1',
    'countries': 'France',
    'countries_lc': 'fr',
}

PRODUCT_TEMPLATE = {'informations': {},
                    'categories': [],
                    }
