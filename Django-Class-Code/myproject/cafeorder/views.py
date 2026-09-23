from django.shortcuts import render



ORDERS = [
    {"order_id": 101, "customer_name": "Aarav", "item_name": "Veg Sandwich", "quantity": 2, "price_per_item": 60, "status": "ready"},
    {"order_id": 102, "customer_name": "Diya", "item_name": "Cold Coffee", "quantity": 1, "price_per_item": 80, "status": "preparing"},
    {"order_id": 103, "customer_name": "Kabir", "item_name": "Paneer Roll", "quantity": 3, "price_per_item": 70, "status": "cancelled"},
    {"order_id": 104, "customer_name": "Meera", "item_name": "Masala Maggi", "quantity": 1, "price_per_item": 50, "status": "ready"},
    {"order_id": 105, "customer_name": "Rohan", "item_name": "French Fries", "quantity": 2, "price_per_item": 90, "status": "preparing"},
]


def order_list(request):
    selected_status = request.GET.get("status", "").lower()
    orders = ORDERS
    if selected_status:
        orders = [order for order in ORDERS if order["status"] == selected_status]

    return render(request, "cafeorder/order_list.html", {
        "orders": orders,
        "selected_status": selected_status,
    })


def order_detail(request, order_id):
    order = next((item for item in ORDERS if str(item["order_id"]) == order_id), None)
    if order is None:
        return render(request, "cafeorder/order_not_found.html", status=404)

    order = order.copy()
    order["total_amount"] = order["quantity"] * order["price_per_item"]
    return render(request, "cafeorder/order_detail.html", {"order": order})
