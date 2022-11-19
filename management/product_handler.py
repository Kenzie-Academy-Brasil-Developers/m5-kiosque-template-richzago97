from menu import products


def get_product_by_id(id: int):
    if type(id) != int:
        raise TypeError('product id must be an int')
    for product in products:
        if id == product['_id']:
            return product
    return {}


def get_products_by_type(tipo: str):
    tipo_Produto = []
    if type(tipo) != str:
        raise TypeError('product type must be a str')
    for product in products:
        if tipo == product['type']:
            tipo_Produto.append(product)
    return tipo_Produto


def menu_report():
    contagem_de_produtos = len(products)
    valorTotal = 0
    for product in products:
        valorTotal = valorTotal + product['price']
    preco_medio = round(valorTotal / contagem_de_produtos, 2)
    typeCount = {}
    for product in products:
        productType = product['type']
        if productType in typeCount:
            typeCount[productType] += 1
        else:
            typeCount[productType] = 1
    sortedType = sorted(typeCount.items(), key=lambda x: x[1], reverse=True)
    return f"Products Count: {contagem_de_produtos} - Average Price: ${preco_medio} - Most Common Type: {sortedType[0][0]}"


def add_product(menu, **kwargs):
    id = 0
    for products in menu:
        if products['_id'] > id:
            id = products['_id']
    id += 1
    kwargs['_id'] = id
    menu.append(kwargs)
    return menu[-1]
