"""
Report view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from views.template_view import get_template, get_param
from queries.read_order import get_highest_spending_users


def show_highest_spending_users():
    """ Show report of highest spending users """
    #return get_template("<h2>Les plus gros acheteurs</h2><p>(TO Liste avec nom, total depensé)</p>")
    print(">>> show_highest_spending_users() CALLED", flush=True)
    top_users = get_highest_spending_users()
    print("DEBUG top_users:", top_users, flush=True)

    user_rows = [f"""
        <tr>
            <td>{rank + 1}</td>
            <td>{user_id}</td>
            <td>${total:.2f}</td>
        </tr>""" for rank, (user_id, total) in enumerate(top_users)]

    return get_template(f"""
        <h2>Rapport : Les plus gros acheteurs</h2>
        <p>Voici les 10 utilisateurs ayant le plus dépensé :</p>
        <table class="table">
            <tr>
                <th>Rang</th>
                <th>Utilisateur</th>
                <th>Total dépensé</th>
            </tr>
            {" ".join(user_rows)}
        </table>
        <a href="/orders">← Retourner à la page des commandes</a>
    """)


from queries.read_order import get_best_sellers


def show_best_sellers():
    """ Show report of best selling products """
    #return get_template("<h2>Les articles les plus vendus</h2><p>(TODO: Liste avec nom, total vendu)</p>")
    print(">>> show_best_selling_products() CALLED", flush=True)
    top_products = get_best_sellers()
    print("DEBUG top_products:", top_products, flush=True)

    product_rows = [f"""
        <tr>
            <td>{rank + 1}</td>
            <td>{product_id}</td>
            <td>{quantity}</td>
        </tr>""" for rank, (product_id, quantity) in enumerate(top_products)]

    return get_template(f"""
        <h2>Rapport : Les articles les plus vendus</h2>
        <p>Voici les {len(top_products)} produits les plus vendus :</p>
        <table class="table">
            <tr>
                <th>Rang</th>
                <th>ID Produit</th>
                <th>Quantité vendueee</th>
            </tr>
            {" ".join(product_rows)}
        </table>
        <a href="/orders">← Retourner à la page des commandes</a>
    """)
