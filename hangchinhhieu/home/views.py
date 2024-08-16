from django.shortcuts import get_object_or_404, redirect, render
from Product.models import Product, Category, Banner, Brand, BackGroundSale
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

class Data:
    def __init__(self) -> None:
        self.banner   = Banner.objects.all()
        self.brand    = Brand.objects.all()
        self.category = Category.objects.all()
        self.product  = Product.objects.all()
        self.background = BackGroundSale.objects.all()
        self.ProductDetail  = ''
        self.search   = []
        self.ProductCart = {}

    def getAllProductByBrand(brandName):
        brand = get_object_or_404(Brand, BrandName__icontains=brandName)
        cateName = get_object_or_404(Category,brandname=brand)
        return get_object_or_404(Product, category=cateName)

    def getAllCategoryByBrand(brandName):
        brand = get_object_or_404(Brand, BrandName=brandName)
        return get_object_or_404(Category, SubCategory=brand)

    def getAllProductByCategory(categoryName):
        cateName = get_object_or_404(Category, SubCategory__icontains=categoryName)
        return get_object_or_404(Product, category=cateName)
    
    def getProductByCode(productCode):
        return get_object_or_404(Product, ProductCode=productCode)

data = Data()

class renderHome:
    
    def base(request):
        return render(request,'home/base.html', {'data': data})

    def home(request):
        print(data.__dict__)
        return render(request,'home/index.html', {'data': data})

    def cart(request):
        return render(request, 'home/cart.html', {'data': data})

    def checkouts(request):
        return render(request, 'home/checkouts.html', {'data': data})

    def account(request):
        return render(request, 'home/account.html', )    

    def searchProduct(request):
        return render (request, 'home/product.type.html', {'data': data})  

    def search(request):
        if request.method == 'GET':
            query = request.GET.get('q', None)
            if query:
                Data.search = Product.objects.filter(Q(ProductName__icontains=query) | Q(ProductCode__icontains=query))
                data = Data
                
                if len(Data.search) < 1:
                    Data.search=Data.getAllProductByCategory(query)
                    data = Data

        return render(request, 'home/product.type.html', {'data': data, 'search':query})

    def Login(request):
        if request.method == 'POST':
            Email = request.POST.get('email')
            PassWord = request.POST.get('password')
            user = authenticate(request, username = Email, password = PassWord)
            if user is not None:
                login(request, user)
                return render(request, 'home/product.type.html', {'data': data})
            print(Email, PassWord)

        return redirect('home', {'data': data, 'user': Email, 'password': PassWord})


