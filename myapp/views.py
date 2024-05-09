from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User  # Import the User model
from myapp.models import Client, User

# Create your views here.
def index(request):
 templates = "index.html"
 return render(request, templates)

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
 return render(request, 'shop.html', {'products': products})

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
 return render(request, 'product.html', {'product':product})
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


def managerdashboard():
 return None

from django.shortcuts import render
from .models import Product

def product_list(request):
 products = Product.objects.select_related('categorie', 'reviews', 'description').all()
 return render(request, 'product_list.html', {'products': products})