"""
Orders (read-only model)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from db import get_sqlalchemy_session, get_redis_conn
from sqlalchemy import desc
from models.order import Order
from models.user import User

def get_order_by_id(order_id):
    """Get order by ID from Redis"""
    r = get_redis_conn()
    return r.hgetall(order_id)

def get_orders_from_mysql(limit=9999):
    """Get last X orders"""
    session = get_sqlalchemy_session()
    return session.query(Order).order_by(desc(Order.id)).limit(limit).all()

from types import SimpleNamespace
from db import get_redis_conn
from collections import defaultdict

def get_orders_from_redis(limit=9999):
    r = get_redis_conn()
    keys = r.zrevrange("orders", 0, max(0, limit - 1))
    orders = []
    for k in keys:
        doc = r.hgetall(k)  
        orders.append(SimpleNamespace(id=int(doc["id"]), user_id=doc["user_id"], total_amount=float(doc["total_amount"])))
    return orders

def get_user_names():
    session = get_sqlalchemy_session()
    users = session.query(User).all()
    return {str(user.id): user.name for user in users}
    


def get_highest_spending_users():
    """Get report of best selling products"""
    # TODO: écrivez la méthode
    # triez le résultat par nombre de commandes (ordre décroissant)
    orders = get_orders_from_redis(9999)
    expenses_by_user = defaultdict(float)

    for order in orders:
        expenses_by_user[order.user_id] += order.total_amount

    highest_spending_users = sorted(
        expenses_by_user.items(),
        key=lambda item: item[1],
        reverse=True
    )
    user_names = get_user_names()
    enriched = [(user_names.get(uid, f"Utilisateur {uid}"), total) for uid, total in highest_spending_users]


    return enriched[:10]


def get_best_sellers():
    """Retourne les produits les plus vendus selon Redis"""
    r = get_redis_conn()
    keys = r.keys("product:*")

    sales = []
    for k in keys:
        product_id = k.split(":")[1]
        quantity = int(r.get(k))
        sales.append((product_id, quantity))

    sorted_sales = sorted(sales, key=lambda x: x[1], reverse=True)
    return sorted_sales[:10]


    