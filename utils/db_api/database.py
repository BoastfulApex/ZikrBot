from typing import List, Any
from asgiref.sync import sync_to_async
from backend.models import *
import random
from sql_update import *
import datetime


@sync_to_async
def get_users() -> List[User]:
    try:
        users = User.objects.all()
        ids = []
        for i in users:
            ids.append(i.user_id)
        return users
    except Exception as err:
        print("ERROR ->>>>", err)
        return None


@sync_to_async
def get_users_count() -> List[User]:
    try:
        users = User.objects.all()
        ids = []
        for i in users:
            ids.append(i.user_id)
        return len(users)
    except Exception as err:
        print("ERROR ->>>>", err)
        return None


def check_data():
    now = datetime.datetime.now()
    if now.weekday() == 3 and  now.hour >= 13 or now.weekday() == 4 and  now.hour <= 13:
        return True
    else:
        return False


@sync_to_async
def get_zikr() -> List[Zikr]:
    try:
        if not check_data():
            text = "<b>📿 10 marotaba istig'for ayting</b>\n\n"
            zikrlar = Zikr.objects.filter(send=True).all()
            zikr = random.choice(zikrlar) 
            if zikr.zikr_arabic:
                    text +=f"<b style=\"text-align: left;\">{zikr.zikr_arabic}</b>\n\n"
            text += f"<i>{zikr.zikr}</i> "
            if zikr.zikr_mean:
                text += f"\n\n <b>{zikr.zikr_mean}</b> "
            # text += "\n\n<b style=\"text-align: left;\"> Arabic </b>"
            # text += "✨ Payg'ambarimiz sollallohu alayhi vasallam shunday marhamat qiladilar: \"<b>Qiyomat junida ummatlarimning menga eng yaqini, menga ularning salovotni eng ko'p aytuvchilardir</b>\""
            text += "\n\n💫 Zikrlaringizni o'z vaqtida qilishga odatlaning. Zero Alloh ishni mukammal qilib bajarguvchilarni sevadi."
            return text
        else:
            text = "<b>📿 10 ta salovat ayting</b>\n\n"
            text += f"<b>Allohumma solli  va sallim 'ala sayyidina Muhammad</b> \n\n"
            text += "✨ <b>Payg'ambarimiz sollallohu alayhi vasallam shunday marhamat qiladilar: \"Qiyomat kunida ummatlarimning menga eng yaqini, menga ularning salovotni eng ko'p aytuvchilardir.</b>\""
            return text
    except Exception as err:
        print("ERROR ->>>>", err)
        return None


@sync_to_async
def add_user(user_id, name):
    try:
        user, created = User.objects.get_or_create(user_id=user_id, name=name)
        user.save()
        return user
    except:
        return ''


@sync_to_async
def get_update():
    try:
        users = all_users()
        for urs in users:
            user, created = User.objects.get_or_create(user_id=urs[0], name=urs[1])
            user.save()
    except Exception as err:
        print("ERROR ->>>>", err)
        return None


# @sync_to_async
# def get_doctor(password):
#     try:
#         user = Doctor.objects.filter(unique_password=password).first()
#         return user
#     except:
#         return None


# @sync_to_async
# def get_product(kash):
#     try:
#         product = Product.objects.filter(kod=kash).first()
#         return product
#     except:
#         return None


# @sync_to_async
# def add_order(product_kod, doctor):
#     try:
#         product = Product.objects.filter(kod=product_kod).first()
#         doctor = Doctor.objects.filter(unique_password=doctor).first()
#         return Order(product=product, doctor=doctor, count=1, summa=product.keshbek).save()
#     except Exception as err:
#         print(err)


# @sync_to_async
# def get_orders() -> List[Order]:
#     try:
#         users = Order.objects.all()
#         return users
#     except Exception as err:
#         print("ERROR ->>>>", err)
#         return None


# @sync_to_async
# def add_category(name):
#     try:
#         return Category(speciality=name).save()
#     except Exception as err:
#         print(err)


# @sync_to_async
# def add_product(product_name, category1, kod, keshbek):
#     try:
#         category = Category.objects.filter(speciality=category1).first()
#         if not category:
#             category = Category.objects.create(speciality=category1)
#             category.save()
#         return Product(product_name=product_name, category=category, kod=kod, keshbek=keshbek).save()
#     except Exception as err:
#         pass


# @sync_to_async
# def get_categories() -> List[Category]:
#     try:
#         users = Category.objects.all()
#         return users
#     except Exception as err:
#         print("ERROR ->>>>", err)
#         return None


# @sync_to_async
# def get_orders() -> List[Order]:
#     try:
#         users = Order.objects.all()
#         return users
#     except Exception as err:
#         print("ERROR ->>>>", err)
#         return None


# @sync_to_async
# def get_category_by_name(name):
#     try:
#         category = Category.objects.filter(speciality=name).first()
#         return category
#     except:
#         return None


# @sync_to_async
# def get_order_by_product(name):
#     try:
#         orders = []
#         products = Product.objects.filter(product_name=name)
#         ords = Order.objects.all()
#         for product in products:
#             for order in ords:
#                 if order.product.product_name == product.product_name:
#                     orders.append(order)
#         return orders
#     except:
#         return None
