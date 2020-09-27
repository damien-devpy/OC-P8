from products_app.management.commands.load_db.sort import Sort
from .raw_json_data import product


def test_sort_take_a_dict_and_return_a_list():
    data_sorted = Sort(dict())

    assert isinstance(data_sorted.products, list)


def test_sort_take_raw_json_data_and_return_expected_data():
    data_sorted = Sort(product)

    expected_informations = {
        'barre_code': '3274080005003',
        'name': 'Eau de source',
        'nutriscore': 'a',
        'pict_product': 'https://static.openfoodf…003/front_fr.556.400.jpg',
        'pict_nutriments': 'https://static.openfoodf…nutrition_fr.591.400.jpg',
        'energy_kj': '0',
        'energy_kcal': '0',
        'lipid': '4',
        'glucid ': '0',
        'fiber': '0',
        'protein': '0',
        'salt': '0.0275',
    }

    expected_categories = ['Boissons',
                           'Eaux',
                           'Eaux de sources',
                           'Eaux minérales',
                           'Boissons sans sucre ajouté',
                           ]

    assert data_sorted.products[0]['informations'] == expected_informations
    assert data_sorted.products[0]['categories'] == expected_categories
