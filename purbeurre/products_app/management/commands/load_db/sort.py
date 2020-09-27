import pdb
from .configuration import FIELDS_PRODUCT, FIELDS_NUTRIMENTS, VALUE_REQUIRED, PRODUCT_TEMPLATE

class Sort:
    """Sort out raw json data from OpenFoodFacts API."""

    def __init__(self, raw_json_data):
        """Create a sort object.

        Argument:

        raw_json_data (dict): Data from OFF API.

        Attr:

        products (list): List of dict containing products informations and
            categories which each one belong to.

        """
        self.normalize_products = []
        self.products = self._sort(raw_json_data)


    def _sort(self, raw_json_data):
        """Private method.

        Sort out raw json data. Only keep fields needed and products complete.

        """
        if bool(raw_json_data):
            for product in raw_json_data['products']:

                # If all fields required are present and contains expected values
                if all((value in str(product.get(key)))
                       for key, value in VALUE_REQUIRED.items()
                       ):

                    new_product = PRODUCT_TEMPLATE
                    # Get all categories to which belong current product
                    new_product['categories'] = [category.strip() for category
                                                 in product.get('categories').split(',')
                                                 ]

                    # Get all fields required
                    # Switching for more convienient keywords
                    new_product['informations'].update(
                        {key: str(product.get(value))
                         for key, value in FIELDS_PRODUCT.items()
                         }
                    )
                    # Get all nutriments fields required
                    # Switching for more convienient keywords
                    new_product['informations'].update(
                        {key: str(product.get('nutriments').get(value))
                         for key, value in FIELDS_NUTRIMENTS.items()
                         }
                    )
                    self.normalize_products.append(new_product)

                else:
                    continue

        return self.normalize_products
