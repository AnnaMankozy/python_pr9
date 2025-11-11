import csv
import os

flag = False

try:
    csvfile = open("lab9.csv","r")
    reader = csv.reader(csvfile, delimiter=',')
    
    print("Country Name: 2010-2019")
    
    for row in reader:
        if len(row) >= 14: 
            country_name = row[2]
            years_data = row[4:14] 
            
            print(f"{country_name}: {', '.join(years_data)}")
    
    csvfile.close()
    
except Exception as e:
    print(f"Файл lab9.csv не знайдено або помилка читання: {e}")

try:
    csvfile = open("lab9.csv","r", encoding='utf-8')
    reader = csv.reader(csvfile, delimiter=',')

    indicator = input("\nВведіть будь-яке значення, щоб знайти показники, які більші, ніж значення, яке ви ввели: ")
    while indicator.isalpha():
        indicator = input("Введіть значення ще раз, так як повинна бути цифра: ")

    indicator = float(indicator)

    with open("new_lab9.csv","w", newline='', encoding='utf-8') as csvfile2:
        writer = csv.writer(csvfile2, delimiter = ";")
        writer.writerow(["Country Name", "Year", "Inflation"])

        print("\nКраїни з показником інфляції вище за введене:")
        for row in reader:
            if len(row) >= 14:
                country_name = row[2]

                for i, year in enumerate(range(2010, 2020)):
                    value = row[4+i]
                    try:
                        value_float = float(value)
                        if value_float > indicator:
                            flag = True
                            print(f"{country_name}: {value_float} (рік {year})")
                            writer.writerow([country_name, year, value_float])
                    except ValueError:
                        continue

    csvfile.close()

    if not flag:
        print(f"Показників, які більші, ніж значення, яке ви ввели ({indicator}) - немає.")

except Exception as e:
    print(f"Помилка: {e}")