from django.http import HttpRequest,JsonResponse



def product_view(request:HttpRequest)->JsonResponse:
    
    return JsonResponse(data={'ok':'ok'})