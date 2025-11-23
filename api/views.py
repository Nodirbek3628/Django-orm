import json

from django.http import HttpRequest,JsonResponse
from .models import Product

def to_json(product:Product)->dict:
    return {
        "id":product.id,
        "name":product.name,
        "category":product.category,
        "price": product.price,
        "quantity":product.quantity,
        "rating":product.rating,
        "active":product.active,
        "create_at":product.create_at.strftime('%d/%m/%Y, %H:%M:%S'),
        "update_at":product.update_at.strftime('%d/%m/%Y, %H:%M:%S')   #DateTimeni stringga o'tgarib beradi

}


def product_view(request:HttpRequest)->JsonResponse:

    if request.method == "POST":
        result = []

        data = json.loads(request.body.decode())
        for item in data:

        
            new_product = Product(
                name = item.get('name', ''),
                category = item.get('category', ''),
                price  = item.get('price', 0),
                quantity = item.get('quantity', 0),
                rating = item.get('rating', 0)
            )
            new_product.save()
            result.append(to_json(new_product))

        return JsonResponse(data={'result':result, 'count':len(result)},status=201)

    
    return JsonResponse(data={})