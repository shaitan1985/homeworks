# ORM - Object-Relational Mapping

from datetime import datetime
from time import sleep
import os

from pony.orm import (
    Database,
    Required, Optional, Set, PrimaryKey,
    LongStr,
    set_sql_debug, show, db_session, select, JOIN
)

try:
    os.remove('estore.sqlite')
except:
    pass
db = Database('sqlite', 'estore.sqlite', create_db=True)
# db.bind()


class Category(db.Entity):
    """Категория товара"""
    title = Required(str, 50)
    description = Optional(LongStr)
    parent = Optional('Category', reverse='categories')
    media = Set('Media')
    products = Set('Product')
    categories = Set('Category', reverse='parent')


class Product(db.Entity):
    """Товар"""
    title = Required(str, 255)
    price = Required(float)
    description = Optional(LongStr)
    categories = Set(Category)
    comments = Set('Comment')
    media = Set('Media')
    order_items = Set('OrderItem')
    cart_items = Set('CartItem')

class Customer(db.Entity):
    """Покупатель"""
    phone = Required(str, 20, unique=True)
    email = Optional(str, 100)
    name = Optional(str, 255)
    discount = Optional(float, default=1) # размер скидки
    orders = Set('Order')
    cart = Optional('Cart')

class Order(db.Entity):
    """Заказ"""
    customer = Required(Customer)
    status = Required('Status')
    created = Optional(datetime, default=datetime.now)
    # created = Optional(datetime)
    order_items = Set('OrderItem')

    # def before_insert(self):
    #     super().before_insert()
    #     self.created = datetime.now()

class Status(db.Entity):
    """Справочник статус"""
    name = PrimaryKey(str, 50)
    orders = Set('Order')

class OrderItem(db.Entity):
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    order = Required(Order)

class Cart(db.Entity):
    """Корзина"""
    customer = Optional(Customer, nullable=True)
    cart_items = Set('CartItem')

class CartItem(db.Entity):
    """Продукт в корзине"""
    product = Required(Product)
    amount = Optional(int, default=1, min=1)
    cart = Required('Cart')

class Media(db.Entity):
    """Мультимедиа ресурс"""
    categories = Set('Category')
    products = Set('Product')

class Comment(db.Entity):
    """Комментарии"""
    product = Required('Product')


# class Sale(object):
#     """Размер скидок, промокод"""


set_sql_debug(True)
db.generate_mapping(create_tables=True)


with db_session:
    Customers = select(c for c in Customer)[:]
    if not Customers:
        customer1 = Customer(name='Vasia', phone='+79992100246')
        customer2 = Customer(name='Petia', phone='+79997777777')
        customer3 = Customer(name='Masha', phone='+77777777777')

with db_session:
    statuses = select(s for s in Status)[:]
    if not statuses:
        status_tmp = Status(name='tmp')
        status_prc = Status(name='processing')
        status_done = Status(name='done')


with db_session:
    categories = select(c for c in Category)[:]
    if not categories:
        category1 = Category(title='clothes')
        category2 = Category(title='technics')
        category3 = Category(title='books')


clothes = ['t-shirt', 'pants', 'coat']
technics = ['tv', 'iphone', 'tablet']
books = [
    "hitchhiker's guide to the galaxy",
    'Do Androids Dream of Electric Sheep?',
    'Player one get ready!'
]
prod = {'clothes': clothes,'technics': technics, 'books': books}

with db_session:
    products = select(p for p in Product)[:]
    if not products:
        for key, value in prod.items():
            category = Category.get(title=key)
            for item in value:
                product = Product(
                    title=item,
                    price=10.0,
                    categories=[category])





with db_session:
    cart = select(o for o in Cart)[:]
    if not cart:
        customers = select(c for c in Customer)[:]
        for customer in customers:
            cart = Cart(customer=customer)
            cart_items = select(oi for oi in CartItem)[:]
            if not cart_items:
                cat = Category[customers.index(customer)+1]
                for i in select(p for p in Product if cat in p.categories):
                    CartItem(product=i, cart=cart)

tables = [Customer, Category, Product, Cart, CartItem, Order, OrderItem]

@db_session
def show_all():
    for item in tables:
        show(select(o for o in item))


show_all()

print('*********************************')

@db_session
def move_to_order():
    for adv_cart in select(c for c in Cart):
        order = Order(
            customer=adv_cart.customer,
            status=Status['tmp'])

        for cart_item in select(c for c in CartItem if c.cart.customer == adv_cart.customer):
            OrderItem(
                product=cart_item.product,
                amount=cart_item.amount,
                order=order)
            cart_item.delete()
        adv_cart.delete()


move_to_order()

tables = [Customer, Category, Product, Cart, CartItem, Order, OrderItem]



show_all()

