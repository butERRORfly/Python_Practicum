def main():
    v1 = int(input())
    v2 = int(input())
    v3 = int(input())

    dict_of_places = {'Петя': v1, 'Вася': v2, 'Толя': v3}
    sorted_people = sorted(dict_of_places.items(), key=lambda item: item[1], reverse=True)

    print(f'''          {sorted_people[0][0]}          
      {sorted_people[1][0]}  
                      {sorted_people[2][0]}  
       II      I      III   ''')

if __name__ == '__main__':
    main()