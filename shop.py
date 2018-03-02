# ORM - Object-Relational Mapping

from datetime import datetime
from time import sleep

from pony.orm import (
    Database,
    Required, Optional, Set, PrimaryKey,
    LongStr,
    set_sql_debug, show, db_session, select
)


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


with db_session:
    products = select(p for p in Product)[:]
    if not products:
        category1 = Category.get(title='clothes')
        product1 = Product(
            title='t-shirt',
            price=10.0,
            categories=category1)
        product2 = Product(
            title='pants',
            price=10.0,
            categories=category1)
        product3 = Product(
            title='coat',
            price=10.0,
            categories=category1)
        category2 = Category.get(title='technics')
        product1 = Product(
            title='tv',
            price=10.0,
            categories=category2)
        product2 = Product(
            title='iphone',
            price=10.0,
            categories=category2)
        product3 = Product(
            title='tablet',
            price=10.0,
            categories=category2)
        category3 = Category.get(title='books')
        product1 = Product(
            title="hitchhiker's guide to the galaxy",
            price=10.0,
            categories=category3)
        product2 = Product(
            title='Do Androids Dream of Electric Sheep?',
            price=20.0,
            categories=category3)
        product3 = Product(
            title='Player one get ready!',
            price=10.0,
            categories=category3)





    # customer = Customer[1]
    # # customer.phone = '+79110016527'
    # show(customer)
    # status = Status['In beginning...']

    # sleep(5)
    #
    # order = Order(customer=customer,
    #               status=status)
    # show(order)
    #
    # sleep(5)

    # order = Order(customer=customer,
    #               status=status)
    # show(order)


with db_session:
    order = select(o for o in Order)[:]
    if not order:
        status = Status['tmp']
        Customers = select(c for c in Customer)[:]
        for customer in Customers:
            order = Order(customer=customer, status=status)
            order_items = select(oi for oi in OrderItem)[:]
            if not order_items:
                cat = Category[1]
                print(cat)
                for i in select(p for p in Product if cat in p.categories):
                    OrderItem(product=i, order=order)



tables = [Customer, Category, Product, Order, OrderItem]


@db_session
def show_all():
    for item in tables:
        show(select(o for o in item))

show_all()