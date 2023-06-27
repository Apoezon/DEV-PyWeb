import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from store.models import Products, Category

if __name__ == '__main__':
    category = Category.objects.get(name='Vegetables')
    obj = Products(name = 'Carrot', description='Морковка сладкая, вкусная',
                   price=120, image='static/products/product-7.jpg', category=category)

    obj.save()

    obj = Products.objects.create(name='Fruit Juice', description='Мультифрукт-укт', image='static/products/product-9.jpg', category = Category.objects.get(name = 'Juice'))

    data = (
        {'name': 'Onion',
         'price': 120.00,
         'description': 'Лук',
         'image': 'static/products/product-9.jpg',
         'category': 'Vegetables'
        },
        {'name': 'Apple',
         'price': 120.00,
         'description': 'Яблоко',
         'image': 'static/products/product-10.jpg',
         'category': 'Fruits'
         },
        {'name': 'Garlic',
         'price': 120.00,
         'description': 'Чеснок',
         'image': 'static/products/product-9.jpg',
         'category': 'Vegetables'
         },
    )

    categ = {'Fruits': Category.objects.get(name='Fruits'),
             'Vegetables': Category.objects.get(name='Vegetables'),
             }
    objects_to_create = [Products(name=val['name'],
                                  description=val['description'],
                                  price=val['price'],
                                  category=categ[val['category']]) for val in data]

    Products.objects.bulk_create(objects_to_create)