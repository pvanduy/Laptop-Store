import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from urllib3 import HTTPResponse

from home.views import Data

# Create your views here.

data = Data

class renderProduct:

    def productDetail(request, ProductCode):
        Data.ProductDetail = Data.getProductByCode(ProductCode)
        data = Data
        return render (request, 'home/product.detail.html', {'product': data.ProductDetail,'data':data} )

    def productType(request, brandName):
        return render (request, 'home/product.type.html', {'data': data, 'search': brandName})  

    def addToCart(request):
        cart = []   
        if request.method == 'POST':
            if 'cart' in request.session:
                cart = request.session['cart']
                totalPrice = (request.session['totalPrice'])
            updateCart = []
            updatePrice=[]
            inCart = False
            for productCart in cart:
                currentCode = data.ProductDetail.ProductCode
                if currentCode == productCart['code']:
                    inCart = True
                    quality, ItemPrice = int(productCart['quality']), int(productCart['ItemPrice'])
                    quality = quality + 1
                    ItemPrice = ItemPrice * quality
                    productCart['quality']= str(quality)
                    productCart['ItemPrice']= str(ItemPrice)
                updateCart.append(productCart)
                        
            if not inCart:
                updateCart.append({
                'code':data.ProductDetail.ProductCode,
                'price': str(data.ProductDetail.ProductPrice),
                'title': data.ProductDetail.ProductTitle,
                'Img': str(data.ProductDetail.ProductImg1),
                'ItemPrice': str(data.ProductDetail.ProductPrice),
                'quality': '1',
                })
                updatePrice.append({'totalPrice':str(data.ProductDetail.ProductPrice)})
            
            request.session['cart'] = updateCart
            request.session['totalPrice'] = updatePrice

        return redirect('product', ProductCode=data.ProductDetail.ProductCode)
        
    def DeleteCartItem(request, ProductCode):
        if 'cart' in request.session:
            cart = request.session['cart']
            for productCart in cart:
                currentCode = productCart.get('code')
                if currentCode == ProductCode:
                    print(currentCode)
                    cart.remove(productCart)
        request.session['cart'] = cart
        return redirect('product', ProductCode=data.ProductDetail.ProductCode)
