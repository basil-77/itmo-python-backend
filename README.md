# itmo-python-backend
# ДЗ 2 - REST API (3 балла)

Реализовать REST + RPC API для выдуманного интернет магазина.

Ресурсы:

корзина (cart)

Пример структуры ресурса:
```
{  
    "id": 123,  // идентификатор корзины  
    "items": [  // список товаров в корзине  
        {  
            "id": 1, // id товара  
            "name": "Туалетная бумага \"Поцелуй\", рулон", // название  
            "quantity": 3, // количество товара в корзине  
            "available": true // доступе ли (не удален ли) товар  
        },   
        {  
            "id": 535,   
            "name": "Золотая цепочка \"Abendsonne\"",   
            "quantity": 1,  
            "available": false,  
        },  
    ],  
    "price": 234.4 // общая сумма заказа  
}
```
товар (item)  

Пример структуры ресурса:  
```
{  
    "id": 321, // идентификатор товара  
    "name": "Молоко \"Буреночка\" 1л.", // наименование товара  
    "price": 159.99, // цена товара  
    "deleted": false // удален ли товар, по умолчанию false  
}
```

Запросы для реализации:  

cart  
```POST cart``` - создание, работает как RPC, не принимает тело, возвращает идентификатор  
```GET /cart/{id}``` - получение корзины по id  
```GET /cart``` - получение списка корзин с query-параметрами  
```offset``` - неотрицательное целое число, смещение по списку (опционально, по-умолчанию 0)  
```limit``` - положительное целое число, ограничение на количество (опционально, по-умолчанию 10)  
```min_price``` - число с плавающей запятой, минимальная цена включительно (опционально, если нет, не учитывает в фильтре)  
```max_price``` - число с плавающей запятой, максимальная цена включительно (опционально, если нет, не учитывает в фильтре)  
```min_quantity``` - неотрицательное целое число, минимальное общее число товаров включительно (опционально, если нет, не учитывается в фильтре)  
```max_quantity``` - неотрицательное целое число, максимальное общее число товаров включительно (опционально, если нет, не учитывается в фильтре)  
```POST /cart/{cart_id}/add/{item_id}``` - добавление в корзину с cart_id предмета с item_id, если товар уже есть, то увеличивается его количество  
item  
```POST /item``` - добавление нового товара  
```GET /item/{id}``` - получение товара по id  
```GET /item``` - получение списка товаров с query-параметрами  
```offset``` - неотрицательное целое число, смещение по списку (опционально, по-умолчанию 0)  
```limit``` - положительное целое число, ограничение на количество (опционально, по-умолчанию 10)  
```min_price``` - число с плавающей запятой, минимальная цена (опционально, если нет, не учитывает в фильтре)  
```max_price``` - число с плавающей запятой, максимальная цена (опционально, если нет, не учитывает в фильтре)  
```show_deleted``` - булевая переменная, показывать ли удаленные товары (по умолчанию False)  
```PUT /item/{id}``` - замена товара по id (создание запрещено, только замена существующего)  
```PATCH /item/{id}``` - частичное обновление товара по id (разрешено менять все поля, кроме deleted)  
```DELETE /item/{id}``` - удаление товара по id (товар помечается как удаленный)  

Способ хранение данных на усмотрение.  

Запуск:  
```uvicorn: hw_2:app```
