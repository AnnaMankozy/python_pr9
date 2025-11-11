import csv

flag = False

# 📌 Вывод всех данных на экран
try:
    with open("lab9.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print("Country Name: 2010-2019")
        
        for row in reader:
            if len(row) >= 14:
                country_name = row[4].strip()  # ✅ Название страны в колонке 3
                years_data = row[4:14]         # 📊 Данные за 2010–2019
                print(f"{country_name}: {', '.join(years_data)}")
except Exception as e:
    print(f"❌ File lab9.csv not found or reading error: {e}")

# 🔍 Поиск значений выше заданного порога
try:
    with open("lab9.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        indicator = input("\nEnter value to search for indicators above this number: ")

        # 🔒 Проверка, что введено число
        while not indicator.replace('.', '').isdigit():
            indicator = input("Please enter a numeric value: ")
        indicator = float(indicator)

        with open("new_lab9.csv", "w", newline='', encoding='utf-8') as csvfile2:
            writer = csv.writer(csvfile2, delimiter=";")
            writer.writerow(["Country Name", "Year", "Inflation"])

            print("\nCountries with inflation rate higher than entered value:")
            next(reader)  # Пропустить заголовок

            for row in reader:
                if len(row) >= 14:
                    country_name = row[4].strip()  # ✅ Название страны
                    for i, year in enumerate(range(2010, 2020)):
                        value = row[4 + i].strip()
                        if value:
                            try:
                                value_float = float(value)
                                if value_float > indicator:
                                    flag = True
                                    # Вывод в консоль
                                    print(f"Country: {country_name}, Year: {year}, Inflation: {value_float}")
                                    # Запись в файл
                                    writer.writerow([country_name, year, value_float])
                            except ValueError:
                                continue

        if not flag:
            print(f"⚠️ No inflation indicators found that are greater than {indicator}.")
except Exception as e:
    print(f"❌ Error: {e}")



