import pandas as pd


def cheque(price_list, **purchases):
    items = []
    for product, number in purchases.items():
        if product in price_list.index:
            price = price_list[product]
            items.append({
                'product': product,
                'price': price,
                'number': number,
                'cost': price * number
            })

    df = pd.DataFrame(items)
    df = df.sort_values('product')

    df = df[['product', 'price', 'number', 'cost']]

    return df.reset_index(drop=True)
