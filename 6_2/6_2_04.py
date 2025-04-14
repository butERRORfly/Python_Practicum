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
    return df[['product', 'price', 'number', 'cost']].reset_index(drop=True)


def discount(cheque_df):
    discounted = cheque_df.copy()
    mask = discounted['number'] > 2
    discounted.loc[mask, 'cost'] = discounted.loc[mask, 'cost'] * 0.5
    discounted['cost'] = discounted['cost'].astype(float)
    return discounted
