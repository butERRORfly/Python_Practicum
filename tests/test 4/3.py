import pandas as pd


def process_cities(L, Y):
    df = pd.read_csv('city.csv', encoding='utf-8')
    
    df['longitude'] = df['координаты центра'].str.split(',').str[1].astype(float)
    
    df['год основания'] = pd.to_numeric(df['год основания'], errors='coerce')
    
    filtered_df = df[(df['longitude'] > L) & (df['год основания'] <= Y)]
    
    result_df = filtered_df.sort_values('название города', ascending=False)
    
    for _, row in result_df.iterrows():
        print(f"{row['название города']} {row['население']}")


L = float(input().strip())
Y = int(input().strip())

process_cities(L, Y)