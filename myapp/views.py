from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User  # Import the User model
from myapp.models import Client, User
from django.http import JsonResponse
from django.template.loader import render_to_string
from myapp.models import Categorie
from .models import Categorie


# Create your views here.
#def index(request):
# templates = "index.html"
# return render(request, templates)

def index(request):
    # Get the last 6 products added
    latest_products = Product.objects.order_by('-id')[:8]
    return render(request, 'index.html', {'latest_products': latest_products})


def about(request):
    templates = "about.html"
    return render(request, templates)


def cart(request):
    templates = "cart.html"
    return render(request, templates)


def compare(request):
    templates = "compare.html"
    return render(request, templates)


def contacts(request):
    templates = "contacts.html"
    return render(request, templates)


def faq(request):
    templates = "faq.html"
    return render(request, templates)


def news(request):
    templates = "news.html"
    return render(request, templates)


def post(request):
    templates = "post.html"
    return render(request, templates)


def product(request):
    product_id = request.GET.get('id')  # Get the product ID from the URL
    product = get_object_or_404(Product, pk=product_id)  # Fetch the product from the database
    return render(request, 'product.html', {'product': product})  # Pass the product to the template


def shop(request):
    products = Product.objects.all()  # get all products
    categories = Categorie.objects.all()  # get all categories

    # Get all unique effects
    effects = set(effect for product in products for effect in product.effects.split(','))
    top = Product.objects.order_by('-salesnumber')[:4]
    return render(request, 'shop.html', {'products': products, 'categories': categories, 'effects': effects, 'top': top})

def team(request):
    templates = "team.html"
    return render(request, templates)


def wishlist(request):
    templates = "wishlist.html"
    return render(request, templates)


def err(request):
    templates = "404.html"
    return render(request, templates)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product})


def product_view(request):
    product_id = request.GET.get('id')
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})


############################################################################################################


from django.shortcuts import render, redirect


def registration(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('user-name')
        password = request.POST.get('user-password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        # address = request.POST.get('address')

        # Create a new client object
        client = Client.objects.create(
            nom=username,
            password=password,
            email=email,
            tel=phone_number,
            # address=address,
            username=username,
            account_creation_date=timezone.now(),
            role='regular'  # Default role is set to 'regular'
        )

        # Save the client object
        client.save()

        # Redirect to a success page or any other page after successful registration
        return render(request, 'index.html/')  # Change this to your desired URL
    return render(request, 'register.html')


#login with email and password
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email, password=password)
            if user.role == 'regular':
                # Redirect to index.html
                return redirect('index')
            elif user.role == 'regular_manager':
                # Redirect to managerdashboard.html
                return redirect('managerdashboard')
            else:
                # Handle other roles or scenarios
                pass
        except User.DoesNotExist:
            # Handle invalid credentials
            pass
    return render(request, 'login.html')


def loginpage(request):
    return render(request, 'login.html')


def managerdashboard(request):
    return render(request, 'managerdashboard.html')





def product_list(request):
    # Retrieve the last 6 products ordered by their primary key (assuming the primary key is the ID)
    latest_products = Product.objects.order_by('-id')[:6]
    return render(request, 'product_list.html', {'latest_products': latest_products})


def product_list(request):
    products = Product.objects.select_related('categorie', 'reviews', 'description').all()
    return render(request, 'product_list.html', {'products': products})


from django.shortcuts import render
from .models import Product


def product_list(request):
    # Retrieve the last 6 products ordered by their primary key (assuming the primary key is the ID)
    latest_products = Product.objects.order_by('-id')[:6]
    return render(request, 'product_list.html', {'latest_products': latest_products})


def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(nom__icontains=query)
    # Render the products using a template
    products_html = render_to_string('products_partial.html', {'products': products})
    # Return the rendered HTML as JSON response
    return JsonResponse({'products_html': products_html})

from django.http import JsonResponse
from .models import Product

from django.shortcuts import render
from .models import Product, Categorie

def get_products(request):
    # Get the selected category from the query parameters
    category_name = request.GET.get('category')
    category = Categorie.objects.get(nom=category_name)

    # Get the products for the selected category
    products = Product.objects.filter(categorie=category)

    # Render the products to HTML
    return render(request, 'products_partial.html', {'products': products})

def get_products_by_effect(request):
    # Get the selected effect from the query parameters
    effect = request.GET.get('effect')

    # Get the products for the selected effect
    products = Product.objects.filter(effects__contains=effect)

    # Render the products to HTML
    return render(request, 'products_partial.html', {'products': products})