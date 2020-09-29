from .configuration import FIELDS_PRODUCT, FIELDS_NUTRIMENTS, VALUE_REQUIRED


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
        self.products = self._sort(raw_json_data)

    def _sort(self, raw_json_data):
        """Private method.

        Sort out raw json data. Only keep fields needed and products complete.

        """
        normalize_products = []

        for product in raw_json_data['products']:
            new_product = {'informations': {},
                           'categories': [],
                           }

            # If all fields required are present and contains expected values
            if all((value in str(product.get(key)))
                   for key, value in VALUE_REQUIRED.items()
                   ):

                # Get all categories to which belong current product
                categories = (category.strip() for category
                              in product.get('categories').split(',')
                              )
                new_product['categories'].extend(categories)

                # Get all fields required
                # Switching for more convienient keywords
                informations = {key: product.get(value)
                                for key, value in FIELDS_PRODUCT.items()
                                }
                new_product['informations'].update(informations)

                # Get all nutriments fields required
                # Switching for more convienient keywords
                nutriments = {key: product.get('nutriments').get(value)
                if product.get('nutriments').get(
                    value) != None else 'Valeur inconnue'
                              for key, value in FIELDS_NUTRIMENTS.items()
                              }

                new_product['informations'].update(nutriments)

                # Get rid of products with missing important informations
                if (None in new_product.values()
                        or
                        None in new_product['informations'].values()
                ):
                    continue
                else:
                    normalize_products.append(new_product)

            else:
                continue

        return normalize_products
