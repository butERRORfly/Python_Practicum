import pandas as pd


def process_cities(L, Y):
    df = pd.read_csv('city.csv', encoding='utf-8')
    
    filtered_df = df[(df['geo_lon'] > float(L)) & (df['foundation_year'] <= int(Y))]
    
    filtered_df = filtered_df.sort_values('city', ascending=False)
    
    for _, row in filtered_df.iterrows():
        city_name = row['city']
        population = int(row['population']) if pd.notna(row['population']) else 0
        print(f"{city_name} {population}")


L = input().strip()
Y = input().strip()

process_cities(L, Y)