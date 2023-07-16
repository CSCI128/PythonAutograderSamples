def handle_shipment(_inventory: dict, _item: str, _quantity: int):
    if _item not in _inventory.keys():
        _inventory[_item] = 0

    print(f"OUTPUT Received shipment of {_quantity} {_item}")
    _inventory[_item] += _quantity


def handle_sale(_inventory: dict, _item: str, _quantity: int):

    if _item not in _inventory.keys():
        print(f"OUTPUT ERROR: {_item} not found in inventory")
        return

    if _inventory[_item] < _quantity:
        _quantity = _inventory[_item]

    print(f"OUTPUT Sold {_quantity} {_item}")
    _inventory[_item] -= _quantity


def handle_input(_inventory: dict, _userIn: str):
    chgType, item, quantity = _userIn.split(":")

    if chgType == "sale":
        handle_sale(_inventory, item, quantity)

    if chgType == "shipment":
        handle_shipment(_inventory, item, quantity)


def end_day(_inventory: dict):
    if not _inventory:
        print("OUTPUT No items in _inventory")
        return

    for item, quantity in _inventory.items():
        print(f"OUTPUT {item}: {quantity}")


if __name__ == "__main__":

    userIn = input("INPUT> ")
    inventory: dict = {}

    while userIn != "EOD":
        handle_input(inventory, userIn)

    end_day(inventory)
