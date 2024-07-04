from django.core.checks import messages
from django.utils import timezone
from django.contrib.auth.models import User  # Import the User model
from myapp.models import Client, User
from django.template.loader import render_to_string
from django.shortcuts import redirect
from .models import Post
from django.shortcuts import render
from .models import Product, Categorie, Cart
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required




def index(request):
    # Get the last 8 products added
    latest_products = Product.objects.order_by('-id')[:8]
    # Get the last 3 posts
    latest_posts = Post.objects.order_by('-date')[:3]
    # Get all items in the cart
    cart_items = Cart.objects.all()

    # Calculate the total price of items in the cart
    total_price = sum(item.product.prix * item.quantity for item in cart_items)

    context = {
        'latest_products': latest_products,
        'latest_posts': latest_posts,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'index.html', context)





def about(request):
    templates = "about.html"
    return render(request, templates)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Check if the product is already in the cart
    cart_item, created = Cart.objects.get_or_create(product=product)

    if created:
        messages.success(request, f"{product.nom} added to cart.")
    else:
        messages.info(request, f"{product.nom} is already in the cart.")

    return redirect('shop')



def cart(request):
    cart_items = Cart.objects.all()  # Existing cart items
    # Assuming 'salesnumber' is stored in Product and is a measure of sales popularity
    top_sales_products = Product.objects.order_by('-salesnumber')[:5]  # Get top 5 selling products

    context = {
        'cart_items': cart_items,
        'top_sales_products': top_sales_products  # Add this line to pass top sales products to the template
    }
    return render(request, 'cart.html', context)



def add_to_compare(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    compare_list = request.session.get('compare_list', [])
    if product_id not in compare_list:
        compare_list.append(product_id)
        request.session['compare_list'] = compare_list
    return redirect('compare')

def remove_from_compare(request, product_id):
    compare_list = request.session.get('compare_list', [])
    if product_id in compare_list:
        compare_list.remove(product_id)
        request.session['compare_list'] = compare_list
    return redirect('compare')

def compare(request):
    compare_list = request.session.get('compare_list', [])
    compared_products = Product.objects.filter(id__in=compare_list)

    viewed_product_ids = request.session.get('viewed_products', [])
    recently_viewed_products = Product.objects.filter(id__in=viewed_product_ids)

    context = {
        'compared_products': compared_products,
        'recently_viewed_products': recently_viewed_products
    }
    return render(request, 'compare.html', context)


def clear_compare(request):
    request.session['compare_list'] = []
    return redirect('compare')


def contacts(request):
    templates = "contacts.html"
    return render(request, templates)


def faq(request):
    templates = "faq.html"
    return render(request, templates)


def news(request):
    posts = Post.objects.all()
    return render(request, 'news.html', {'posts': posts})


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


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist = request.session.get('wishlist', [])
    if product_id not in wishlist:
        wishlist.append(product_id)
    request.session['wishlist'] = wishlist
    return redirect('wishlist')

def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    products = Product.objects.filter(id__in=wishlist)
    return render(request, 'wishlist.html', {'products': products})


def err(request):
    templates = "404.html"
    return render(request, templates)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Get the list of recently viewed product IDs from the session
    viewed_products = request.session.get('viewed_products', [])

    # Add current product_id to the list if it's not already included
    if product_id not in viewed_products:
        viewed_products.append(product_id)
        if len(viewed_products) > 5:  # Limit the list to last 5 viewed items
            viewed_products.pop(0)

    # Update the session
    request.session['viewed_products'] = viewed_products

    return render(request, 'product.html', {'product': product})



def product_view(request):
    product_id = request.GET.get('id')
    product = Product.objects.get(id=product_id)
    return render(request, 'product.html', {'product': product})


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


#def product_list(request):
    # Retrieve the last 6 products ordered by their primary key (assuming the primary key is the ID)
    #latest_products = Product.objects.order_by('-id')[:6]
    #return render(request, 'product_list.html', {'latest_products': latest_products})


def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(nom__icontains=query)
    # Render the products using a template
    products_html = render_to_string('products_partial.html', {'products': products})
    # Return the rendered HTML as JSON response
    return JsonResponse({'products_html': products_html})



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



def get_latest_posts():
    # Fetch the latest posts, you can customize the number of posts here
    return Post.objects.order_by('-date')[:3]

def get_previous_post(post):
    return Post.objects.filter(date__lt=post.date).order_by('-date').first()

# Function to get the next post
def get_next_post(post):
    return Post.objects.filter(date__gt=post.date).order_by('date').first()

# View to list all posts
def post_list(request):
    posts = Post.objects.all()
    latest_posts = get_latest_posts()
    return render(request, 'news.html', {'posts': posts, 'latest_posts': latest_posts})

# View to display a specific post's content
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    tags = post.tags.split(',')
    latest_posts = get_latest_posts()

    previous_post = get_previous_post(post)
    next_post = get_next_post(post)

    return render(request, 'post.html', {
        'post': post,
        'tags': tags,
        'latest_posts': latest_posts,
        'previous_post': previous_post,
        'next_post': next_post
    })

