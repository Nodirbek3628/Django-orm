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
        "create_at":product.create_at.strftime('%d/%m/%Y, %H:%M:%S.%f')[:-3],
        "update_at":product.update_at.strftime('%d/%m/%Y, %H:%M:%S.%f')[:-3]   #DateTimeni stringga o'zgarib beradi

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

    if request.method == "GET":
        params = request.GET
    # products = Product.objects.filter(active=True).order_by('create_at') # ASC -> o'sish bulsa 
    # products = Product.objects.filter(active=True).order_by('-create_at')  DESC -> kamayish bulsa_> oldiga - ishora quysak kamayish tartibida malumot sortledi
    # products = Product.objects.order_by('price')
    
     
        products = Product.objects.all()

    # products = products.reverse()  # bu order_by bilan tartiblab olingan bulsa reverse() teskarisiga o'girb beradi 
    # products = Product.objects.create(name='ali',category='ali',price=10,quantity=15,rating=5)

        # products.save()

        # print(products)

        name = params.get('name')

        if name:
            products=products.filter(name=name)


        category = params.get('category')
        if category:
            products = products.filter(category=category)
        
        price = params.get('price')

        if price:
            products = products.exclude(price__gte=price)  #exclude filterni NOT() inkori

        max_price = params.get('max_price')
        min_price = params.get('min_price')

        # if max_price and min_price:
        #     products = products.filter(price__gte=min_price, price__lte=max_price)
        #     product = products.filter()

        rating = params.get('rating')

        if rating:
            products = products.filter(rating__gt=rating)



        result = []

        for product in products:
            result.append(to_json(product))

        return JsonResponse(data={'count':len(result),'result':result})

    return JsonResponse(data={})