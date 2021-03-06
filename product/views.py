from django.shortcuts import render,redirect
from .models import Product,ProductInfo,Clothing,Accessories,Electronics,Footwear
from django.contrib import messages
from .forms import CommentForm
from unicodedata import category
from django.db.models import Q
from django.core.mail import EmailMessage



def home(request):
    womens_product = []
    womens_product.append(Clothing.objects.filter(gender='F',category__iexact='Top').first())
    womens_product.append(Clothing.objects.filter(gender='F',category__iexact='Jeans').first())
    womens_product.append(Clothing.objects.filter(gender='F',category__iexact='Trousers').first())
    womens_product.append(Clothing.objects.filter(gender='F',category__iexact='Kurti').first())
    mens_product = []
    mens_product.append(Clothing.objects.filter(gender='M',category__iexact='T-Shirt').first())
    mens_product.append(Clothing.objects.filter(gender='M',category__iexact='Blazzers').first())
    mens_product.append(Clothing.objects.filter(gender='M',category__iexact='Shirt1').first())
    mens_product.append(Clothing.objects.filter(gender='M',category__iexact='Jeans').first())
    mobile_product = []
    mobile_product.append(Electronics.objects.filter(sub_category='Mobiles').first())
    mobile_product.append(Electronics.objects.filter(sub_category='CasesCovers').first())
    mobile_product.append(Electronics.objects.filter(sub_category='PowerBanks').first())
    mobile_product.append(Electronics.objects.filter(sub_category='Tablets').first())
    computer_product = []
    computer_product.append(Electronics.objects.filter(sub_category='Computer').first())
    computer_product.append(Electronics.objects.filter(sub_category='KeyboardMouse').first())
    computer_product.append(Electronics.objects.filter(sub_category='Laptops').first())
    computer_product.append(Electronics.objects.filter(sub_category='PrintersScanners').first())
    home_appliance_product = []
    home_appliance_product.append(Electronics.objects.filter(sub_category='Television').first())
    home_appliance_product.append(Electronics.objects.filter(sub_category='Speakers').first())
    home_appliance_product.append(Electronics.objects.filter(sub_category='MicrowaveIron').first())
    home_appliance_product.append(Electronics.objects.filter(sub_category='Furniture').first())
    context = {
        'womens_product':womens_product,
        'mens_product':mens_product,
        'mobile_product':mobile_product,
        'computer_product':computer_product,
        'home_appliance_product':home_appliance_product, 
        }
    return render(request,'product/home.html',context=context)


def mens_product(request):
    clothing_product = Clothing.objects.filter(gender = "M")
    accessories_product = Accessories.objects.filter(gender='M')
    footwear_product = Footwear.objects.filter(gender = "M")
    products = clothing_product.union(accessories_product,footwear_product)
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            clothing_product = Clothing.objects.filter(gender = "M",brand__in = brand)
            accessories_product = Accessories.objects.filter(gender='M',brand__in = brand)
            footwear_product = Footwear.objects.filter(gender = "M",brand__in = brand)
            products = clothing_product.union(accessories_product,footwear_product)
        if len(color) > 0:
            clothing_product = Clothing.objects.filter(gender = "M",color__in = color)
            accessories_product = Accessories.objects.filter(gender='M',color__in = color)
            footwear_product = Footwear.objects.filter(gender = "M",color__in = color)
            products = clothing_product.union(accessories_product,footwear_product)
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_shoes_product(request):
    products = Footwear.objects.filter(gender = 'M')
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
            
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_wear_product(request,wear_category):
    print(wear_category)
    products = Clothing.objects.filter(gender = 'M', category__icontains = wear_category)
    #print(products)
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)


def mens_accessories_product(request,wear_category):
    products = Accessories.objects.filter(Q(category__icontains = wear_category) | Q(sub_category__icontains = wear_category))
    products = products.filter(gender = 'M')
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
    context = {'products':products
                }
    return render(request,'product/mens_product.html',context=context)
    

def womens_product(request):
    clothing_product = Clothing.objects.filter(gender = "F")
    accessories_product = Accessories.objects.filter(gender='F')
    footwear_product = Footwear.objects.filter(gender = "F")
    products = clothing_product.union(accessories_product,footwear_product)
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            clothing_product = Clothing.objects.filter(gender = "F",brand__in = brand)
            accessories_product = Accessories.objects.filter(gender='F',brand__in = brand)
            footwear_product = Footwear.objects.filter(gender = "F",brand__in = brand)
            products = clothing_product.union(accessories_product,footwear_product)
        if len(color) > 0:
            clothing_product = Clothing.objects.filter(gender = "F",color__in = color)
            accessories_product = Accessories.objects.filter(gender='F',color__in = color)
            footwear_product = Footwear.objects.filter(gender = "F",color__in = color)
            products = clothing_product.union(accessories_product,footwear_product)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_shoes_product(request):
    products = Footwear.objects.filter(gender = 'F')
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_wear_product(request,wear_category):
    products = Clothing.objects.filter(gender = 'F', category__icontains = wear_category)
    #print(products)
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def womens_accessories_product(request,wear_category):
    products = Accessories.objects.filter(Q(category__icontains = wear_category) | Q(sub_category__icontains = wear_category))
    products = products.filter(gender = 'F')
    if request.method == "POST":
        brand = request.POST.getlist('brand')
        color = request.POST.getlist('color')
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(color) > 0:
            products = products.filter(color__in = color)
    context = {'products':products
                }
    return render(request,'product/womens_product.html',context=context)


def electronics_product(request,sub_category):
    if sub_category.upper() == 'ALL':
        products = Electronics.objects.filter(category__iexact = 'Mobiles and Laptops')
    else:
        products = Electronics.objects.filter(category__iexact = 'Mobiles and Laptops',sub_category__icontains = sub_category)
    if request.method == "POST":
        brand = request.POST.getlist('brand') 
        storage = request.POST.getlist('size')  
        ram = request.POST.getlist('ram')  
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
        if len(storage) > 0:
            products = products.filter(storage__in = storage)
        if len(ram) > 0:
            products = products.filter(ram__in = ram)
    context = {'products':products
                }
    return render(request,'product/electronics_product.html',context=context)


def tv_appliance_product(request,sub_category):
    if sub_category.upper() == 'ALL':
        products = Electronics.objects.filter(category__iexact = 'Tv and Appliances')
    else:
        products = Electronics.objects.filter(category__iexact = 'Tv and Appliances',sub_category__icontains = sub_category)
    if request.method == "POST":
        brand = request.POST.getlist('brand')   
        if len(brand) > 0:
            products = products.filter(brand__in = brand)
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


def search_product(request):
    question = request.POST['question']
    product =  Clothing.objects.filter(Q(product = Product.objects.filter(name__icontains = question).first()) | Q(brand__icontains = question)
                                        | Q(category__icontains = question) | Q(sub_category__icontains = question) | Q(description__icontains = question)
                                        )
    #print(product)
    footwear = Footwear.objects.filter(Q(product = Product.objects.filter(name__icontains = question).first()) | Q(brand__icontains = question)
                                        | Q(category__icontains = question) | Q(sub_category__icontains = question) | Q(description__icontains = question)
                                        | Q(gender__icontains = question))
    #print(footwear)
    accessories = Accessories.objects.filter(Q(product = Product.objects.filter(name__icontains = question).first()) | Q(brand__icontains = question)
                                        | Q(category__icontains = question) | Q(sub_category__icontains = question) | Q(description__icontains = question)
                                        | Q(gender__icontains = question))
    #print(accessories)
    electrnoic_product = Electronics.objects.filter(Q(product = Product.objects.filter(name__icontains = question).first()) | Q(brand__icontains = question)
                                        | Q(category__icontains = question) | Q(sub_category__icontains = question) | Q(description__icontains = question)
                                        )
    #print(electrnoic_product)
    product_list = product.union(footwear,accessories)

    #print(product_list)
    context = {
        'product_list':product_list,
        'electrnoic_product':electrnoic_product,
        }
    return render(request,'product/search_product.html',context=context)

def more(request):
    return render(request,'product/more.html')


def contact(request):
    print("Coming to Contact Views")
    message = ""
    if request.method == "POST":
        message = "\nName : "+request.POST['name']+"\nEmail :  "+request.POST['email']+"\n\nMessage : \n\n"+request.POST['comments']
        email = EmailMessage('ECartSupport', message, to=[request.POST['email']])
        email.send()
        return redirect('product:home')


