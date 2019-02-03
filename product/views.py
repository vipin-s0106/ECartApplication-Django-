from django.shortcuts import render,redirect
from .models import Product,ProductInfo,Clothing,Accessories,Electronics,Footwear
from django.contrib import messages
from .forms import CommentForm
from unicodedata import category
from django.db.models import Q

def home(request):
    return render(request,'product/home.html')


def mens_product(request):
    clothing_product = Clothing.objects.filter(gender = "M")
    accessories_product = Accessories.objects.filter(gender='M')
    footwear_product = Footwear.objects.filter(gender = "M")
    products = clothing_product.union(accessories_product,footwear_product)
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_shoes_product(request):
    products = Footwear.objects.filter(gender = 'M')
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_wear_product(request,wear_category):
    print(wear_category)
    products = Clothing.objects.filter(gender = 'M', category__icontains = wear_category)
    #print(products)
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_accessories_product(request,wear_category):
    products = Accessories.objects.filter(Q(category__icontains = wear_category) | Q(sub_category__icontains = wear_category))
    products = products.filter(gender = 'M')
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)
    

def womens_product(request):
    clothing_product = Clothing.objects.filter(gender = "F")
    accessories_product = Accessories.objects.filter(gender='F')
    footwear_product = Footwear.objects.filter(gender = "F")
    products = clothing_product.union(accessories_product,footwear_product)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_shoes_product(request):
    products = Footwear.objects.filter(gender = 'F')
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_wear_product(request,wear_category):
    products = Clothing.objects.filter(gender = 'F', category__icontains = wear_category)
    #print(products)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_accessories_product(request,wear_category):
    products = Accessories.objects.filter(Q(category__icontains = wear_category) | Q(sub_category__icontains = wear_category))
    products = products.filter(gender = 'F')
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def electronics_product(request,sub_category):
    if sub_category.upper() == 'ALL':
        products = Electronics.objects.filter(category__iexact = 'Mobiles and Laptops')
    else:
        products = Electronics.objects.filter(category__iexact = 'Mobiles and Laptops',sub_category__icontains = sub_category)
    context = {'products':products
                }
    return render(request,'product/electronics_product.html',context=context)


def tv_appliance_product(request,sub_category):
    if sub_category.upper() == 'ALL':
        products = Electronics.objects.filter(category__iexact = 'Tv and Appliances')
    else:
        products = Electronics.objects.filter(category__iexact = 'Tv and Appliances',sub_category__icontains = sub_category)
    context = {'products':products
                }
    return render(request,'product/tv_appliance_product.html',context=context)


def product_detail(request,product_id):
    form = CommentForm()
    if request.method == "POST":
        pass
    if Clothing.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Clothing.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Footwear.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Footwear.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Accessories.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Accessories.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    elif Electronics.objects.filter(product = Product.objects.filter(id = product_id).first()).first() is not None:
        product = Electronics.objects.filter(product = Product.objects.filter(id = product_id).first()).first()
    else:
        pass
                        
    product_reviews = ProductInfo.objects.filter(product = product.product)
    average_rating = 0
    rating5 = rating4 = rating3 = rating2 = rating1 = 0 
    if product_reviews.count() > 0:
        sum_rating = 0
        for review in product_reviews:
            if review.rating == 5:
                rating5 += 1
            elif review.rating == 4:
                rating4 += 1
            elif review.rating == 3:
                rating3 += 1
            elif review.rating == 2:
                rating2 += 1
            elif review.rating == 1:
                rating1 += 1
            else:
                pass
            sum_rating += review.rating
        average_rating = round(sum_rating/product_reviews.count())
        
    
    context = { 'product':product,
                'product_reviews':product_reviews,
                'average_rating':average_rating,
                'ratings_count':[rating5,rating4,rating3,rating2,rating1],
                'rating_range':range(5),
                'form':form
        }
    
    return render(request,'product/product_detail.html',context=context)


def write_reviews(request,product_id):
    if request.user.is_authenticated:
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            comment = form.save(commit=False)
            if 'review_image2' in request.FILES:
                comment.review_image2 = request.FILES['review_image2']
            comment.product = Product.objects.filter(id = product_id).first()
            comment.user = request.user
            comment.save()
            return redirect('product:product_detail',product_id)
    else:
        messages.warning(request,"Please login")
        return redirect("user:user_login")

