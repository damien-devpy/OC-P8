from products_app.management.commands.load_db.sort import Sort

from .raw_json_data import product_complete, product_incomplete, \
    product_key_missing, product_with_none_nutriments


def test_sort_take_raw_json_data_and_return_expected_data():
    data_sorted = Sort(product_complete)

    expected_informations = {
        'barre_code': '3274080005003',
        'name': 'Eau de source',
        'nutriscore': 'a',
        'pict_product': 'https://static.openfoodfacts.org/images/products/327/408/000/5003/front_fr.556.400.jpg',
        'pict_nutriments': 'https://static.openfoodfacts.org/images/products/327/408/000/5003/nutrition_fr.591.400.jpg',
        'energy_kj': 0,
        'energy_kcal': 0,
        'lipid': 4,
        'glucid': 0,
        'fiber': 0,
        'protein': 0,
        'salt': 0.0275,
    }

    expected_categories = ['Boissons',
                           'Eaux',
                           'Eaux de sources',
                           'Eaux minérales',
                           'Boissons sans sucre ajouté',
                           ]

    assert data_sorted.products[0]['informations'] == expected_informations
    assert data_sorted.products[0]['categories'] == expected_categories


def test_sort_take_raw_json_and_not_return_incomplete_product():
    data_sorted = Sort(product_incomplete)

    assert data_sorted.products == []


def test_sort_exlude_product_with_None_value():
    data_sorted = Sort(product_key_missing)

    assert data_sorted.products == []


def test_sort_return_unkown_value_for_missing_nutriments_keys():
    data_sorted = Sort(product_with_none_nutriments)

    expected_informations = {
        'barre_code': '3274080005003',
        'name': 'Eau de source',
        'nutriscore': 'a',
        'pict_product': 'https://static.openfoodfacts.org/images/products/327/408/000/5003/front_fr.556.400.jpg',
        'pict_nutriments': 'https://static.openfoodfacts.org/images/products/327/408/000/5003/nutrition_fr.591.400.jpg',
        'energy_kj': 0,
        'energy_kcal': 0,
        'lipid': 4,
        'glucid': 0,
        'fiber': 'Valeur inconnue',  # Missing informations for fibers
        'protein': 0,
        'salt': 'Valeur inconnue',  # Missing informations for salt
    }

    assert data_sorted.products[0]['informations'] == expected_informations
