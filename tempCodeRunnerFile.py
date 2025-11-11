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
