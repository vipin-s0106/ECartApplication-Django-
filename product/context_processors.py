'''
Why it is required -
Some vale that is required to pass in every template with context object
so we have to render the value in html every time
In order to avoid this we have to write the context_processor without passing those value with template rendering
we can directly use in template with help of context processor

for example I want to display on application that How many product has this application on template

context processor we have to define in Template section of settings.py file
'''

'''
Be careful while creating this context processor bcz this is calculated in all
the request so it should be light weighted
'''


from .models import Product


def product_count(request):
    count = Product.objects.count()
    return {"product_count":count}


'''
Now for testing in every html pages type

{{ product_count }}
'''