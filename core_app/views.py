from django.shortcuts import render
from .models import Dashboard, Stories, Products, Team


def home_view(request):

    company = Dashboard.objects.get()
    team = Team.objects.filter(is_manager=False, first_member=False)
    # stories = Stories.objects.get()


    try:
        manager = Team.objects.get(is_manager=True)
        first_member = Team.objects.get(first_member=True)
    except Exception as e:
        manager = None
        first_member = None

    context = {
        'dashboard': company,
        # 'story': stories,
        # 'products': products,
        'team': team,
        'manager': manager,
        'first_member': first_member

    }

    return render(request, "index.html", context)


def co_details(request):
    return render(request, "About.html")


def services(request):
    return render(request, "services.html")


def products(request):
    products = Products.objects.all()
    print(products)
    context = {
        'products': products
    }
    return render(request, "products.html", context)


def mining(request):
    return render(request, "mining.html")


def contactUS(request):
    return render(request, "contactUS.html")


def productDetails(request):
    return render(request, "productDetails.html")


def storyDetail(request):
    return render(request, "Story-details.html")


def aboutView(request):
    return render(request, "about.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")


def activeamail(request):
    return render(request, "active-email.html")


def cart(request):
    return render(request, "cart.html")


def verifyEmail(request):
    return render(request, "verify-the-email.html")
