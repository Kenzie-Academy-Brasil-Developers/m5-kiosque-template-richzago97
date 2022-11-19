from menu import products


def calculate_tab(mesa: list[dict]) -> dict:
    subtotal = 0
    menu = products
    for field in mesa:
        amount = field['amount']
        for menuId in menu:
            if field['_id'] == menuId['_id']:
                subtotal += menuId['price'] * amount
    sub_total_round = round(subtotal, 2)
    result = {'subtotal': f'${sub_total_round}'}
    return result
