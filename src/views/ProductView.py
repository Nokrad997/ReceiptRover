class ProductView:
    """
    Represents a view for displaying product information.

    Args:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.
    """

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
