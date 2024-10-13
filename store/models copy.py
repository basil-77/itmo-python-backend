from dataclasses import dataclass

@dataclass(slots=True)
class Item:
    id: int
    name: str
    price: float
    deleted: bool

@dataclass(slots=True)
class Items:
    items: dict[
        'id': int,
        'item': Item
    ]
    def add_item(self, item: Item):
        _item = {'id': item.id, 'item': item}
        self.items[item.id] = _item
    def get_item(self, id: int):
        res = self.items[id] if id in self.items.keys else None
        return res
    def replace_item(self, id: int, new_item: Item):
        res = False
        if id in self.items.keys:
            new_item.id = id
            self.items[id] = new_item
            res = True
        return res
    def update_item(self, id: int, new_item: Item):
        res = False
        if id in self.items.keys:
            new_item.deleted = self.items[id].deleted
            self.items[id] = new_item
            res = True
        return res
    def delete_item(self, id: int):
        res = False
        if id in self.items.keys:
            self.items[id].deleted = True
        return res
    
@dataclass(slots=True)
class CartItems:
    id: int
    name: str
    quantity: int
    available: bool

@dataclass(slots=True)
class Cart:
    id: int
    items: list
    price: float

    def add_item(self, item: Item, quantity: int):
        _item = {'id': item.id, 'name': item.name, 'quantity': quantity, 'available': not item.deleted}
        self.items.append(_item)    

@dataclass(slots=True)
class Carts:
    carts: dict[
        'id': int,
        'cart': Cart
    ]
    def get_cart(self, id: int):
        res =  None
        if id in self.carts.keys:
            res = self.carts[id]
        return res

    def add_cart(self, cart: Cart):
        self.carts[cart.id] = cart

