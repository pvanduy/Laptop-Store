from django.db import models

class Banner(models.Model):
	BannerImg=models.ImageField(upload_to='image')
	BannerAlt=models.CharField(max_length=300)

	def __str__(self):
        	return self.BannerAlt

class BackGroundSale(models.Model):
	BackGroundSaleImg=models.ImageField(upload_to='image')
	BackGroundSaleImgAlt=models.CharField(max_length=300)

	def __str__(self):
        	return self.BackGroundSaleImgAlt

class Brand(models.Model):
	BrandName = models.CharField(primary_key = True, max_length=30)

	def __str__(self):
        	return self.BrandName

class Category(models.Model):
    SubCategory = models.CharField(primary_key= True,max_length=50)
    brandname = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        	return self.SubCategory

class Product(models.Model):
    ProductID = models.AutoField(primary_key= True)
    ProductCode = models.CharField(max_length=50)
    ProductName = models.CharField(max_length=50)
    ProductTitle = models.CharField(max_length=50)
    ProductPrice = models.DecimalField(max_digits=30, decimal_places=0)
    ProductInfo = models.TextField(blank = True)
    ProductStatus = models.CharField(max_length=30)
    ProductImg1 = models.ImageField(upload_to='image', blank= True)
    ProductImg2 = models.ImageField(upload_to='image', blank= True)
    ProductImg3 = models.ImageField(upload_to='image', blank= True)
    ProductImg4 = models.ImageField(upload_to='image', blank= True)
    ProductImg5 = models.ImageField(upload_to='image', blank= True)
    ProductImg6 = models.ImageField(upload_to='image', blank= True)
    ProductImg7 = models.ImageField(upload_to='image', blank= True)
    ProductImg8 = models.ImageField(upload_to='image', blank= True)
    ProductImg9 = models.ImageField(upload_to='image', blank= True)	
    ProductImg10 = models.ImageField(upload_to='image', blank= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
            return self.ProductName

    