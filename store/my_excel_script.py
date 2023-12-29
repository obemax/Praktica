import pandas as pd
from products.models import Product, ProductCategory



def import_data_from_excel(file_path):
    # Чтение данных из Excel-файла
    data = pd.read_excel(file_path)

    current_category = None

    for index, row in data.iterrows():
        if not pd.isna(row['Наименование']):
            # Если строка содержит наименование категории, создаем или получаем категорию
            current_category, created = ProductCategory.objects.get_or_create(
                name=row['Наименование'],
                defaults={'description': ''}
            )
        else:
            # Создаем продукт в текущей категории
            product = Product.objects.create(
                name=row['Наименование'],
                price=row['Цена'],
                quantity=row['Остаток'],
                # Добавьте другие поля модели, такие как description и image, если они есть в вашем Excel-файле
                category=current_category
            )
        product.save()

file_path = 'C:/Users/Максим/Desktop/kat.xlsx'
import_data_from_excel(file_path)

