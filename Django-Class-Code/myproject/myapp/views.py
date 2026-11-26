from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime
#

def current_time(request):
    now = datetime.datetime.now()
    return HttpResponse(now)

# 
def hello(request):
    return HttpResponse("Hello World");

def home(request):
    return HttpResponse("""<h1 style='color:red'> 
    Welcome to Home Page</h1>""");

def menuitem(request):
    item = "cake"
    return HttpResponse("The name of the item is "+item);
    # return HttpResponse(f"The name of the item is {item}")

def menuitems(request):
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    content = '<h1>Menu items </h1>'
    for item, description in items.items():
        content+=f'<li>{item}:{description}</li>'
    return HttpResponse(content)
    
def greet(request, name):
    return HttpResponse(f"Hello {name}! Welcome to our website")

def menuitems1(request, dish) :
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    discription = items[dish]
    return HttpResponse(f"<h2>{dish}</h2>" + discription)

def menuitems2(request, dish) :
    items={
        'pizza':'Pizza coast Rs. 500',
        'burger':'Burger costs Rs. 25',
        'noodles':'Noodles cost Rs. 40'
    }
    if dish in items:
        discription = items[dish]
        return HttpResponse(f"<h2>{dish}</h2>" + discription)
    else:
        return HttpResponse(f"<h2>{dish}</h2>" + "Not found in the menu")
    
# Dynamic URL
def recipe(request): # recipe/?food=cake
    food = request.GET.get('food')
    if not food:
        return HttpResponse('Food parameter is missing', status=404)    
    return HttpResponse(f'Recipe is available for {food}')

def addition(request): # /addition/?value1=&value2=4
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')
    result = int(value1) + int(value2)
    return HttpResponse(f'Result of addition is {result}')

def calculate(request):
    operation = request.GET.get('operation')
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')

    # if operation == "+":
    #     result = int(value1) + int(value2) # %2B = +
    # elif operation == "-":
    #     result = int(value1) - int(value2)
    # elif operation == "*":
    #     result = int(value1) * int(value2)
    # elif operation == "/":
    #     result = int(value1) / int(value2)
    # else:
    #     result = "Invalid"

    # return HttpResponse(result)

    try:
        value1 = float(value1)
        value2 = float(value2)
    except ValueError:
        return HttpResponse("Invalid Operation")
    if operation == "add":
        result = value1 + value2
    elif operation == "subtract":
        result = value1 - value2
    elif operation == "multiply":
        result = value1 * value2
    elif operation == "divide":
        result = value1 / value2
    else:
        return HttpResponse("Invalid Operation")
    return HttpResponse(result)

# Regular Expressions
def user_profile(request, username):
    return HttpResponse(f'User profile: {username}')

def item_detail(request, item_id):
    return HttpResponse(f'Item ID: {item_id}')

def restro_detail(request, category, subcategory):
    # if(subcategory == ''):
    if not subcategory:
        return HttpResponse(f'Category: {category} and Subcategory: Not provided')
    return HttpResponse(f'Category: {category} and Subcategory: {subcategory}')

# Templates
def home1(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Dynamic templates
def menu(request):
    menuitem={'name':'Noodles'}
    return render(request, 'menu.html', menuitem)

def menu1(request):
    newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]

    return render(request, 'menu1.html', {'mains': newmenu})

# Template Inheritance
def home2(request):
    return render(request, 'home.html')

def about2(request):
    return render(request, 'about.html')

def menuitems2(request):
    return render(request, 'menuitems.html')

# ------------------ Class Code -----------------------
def details(request):
    name = "Ankit"
    program = "CSE"
    # return HttpResponse("<h2 style='color:blue'>The name of the Student " + name + ". " + " He belongs to " + program + "</h2>");
    return HttpResponse(f"<h2 style='color:blue'>The name of the Student {name}. He belongs to {program} </h2>");

def newdetails(request):
    # return HttpResponse("<h1>This is a Heading</h1>" \
    #                     "<p>This is a paragraph</p>")
    return HttpResponse("""<h1>This is a Heading</h1>
                        <p>This is a paragraph</p>""")

def percent(request):
    course1 = 50
    course2 = 60
    course3 = 70
    course4 = 80 
    course5 = 90
    result = (float(course1 + course2 + course3 + course4 + course5)/500) * 100
    return HttpResponse(f'<h2 style="color:green; border:2px solid blue">Percentage {result} </h2>')

def multiple(request):
    number = 5
    result = ""
    for i in range(1, 11):
        result += f'{number} x {i} = {number * i} <br>'
    return HttpResponse(result)

def grade(request):
    marks = 45

    if marks > 80 and marks <= 100:
        result = "<h1 style=color:green>Grade A </h1>"
    elif marks > 60 and marks <= 80:
        result = "<h1 style=color:blue>Grade B </h1>"
    elif marks > 40 and marks <= 60:
        result = "<h1 style=color:orange>Grade C </h1>"
    else:
        result = "<h1 style=color:red>Fail </h1>"

    return HttpResponse(result)

def food(request):
    fooditems = ["Pizza", "Burger", "Noodles", "Momos"]
    itemcontent = "<h2>The food items available are: </h2>"
    for item in fooditems:
        itemcontent += f"<p>{item}</p>"
    return HttpResponse(itemcontent)

def food1(request):
    fooddetails = {
        "name": "Pizza",
        "Price": 200,
        "Size": "Regular"
    }
    content = "<h1>Food List: </h1>"
    for key, value in fooddetails.items():
        content += f'{key} {value} <br>'
    return HttpResponse(content)

def studentdetails(request):
    studentinfo = [
        ["Ayush", 67],
        ["Manish", 50],
        ["Ankit", 60]
    ]

    content = """
    <table border = 1>
    <tr>
    <th>Name</th>
    <th>Marks</th>
    </tr>
    """
    for i in studentinfo:
        content += f"""
        <tr>
        <td>{i[0]}</td>
        <td>{i[1]}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)

def studentdetails1(request):
    studentinfo = [
        {"Name": "Amit", "Marks": 90, "Course": "Django"},
        {"Name": "Manish", "Marks": 86, "Course": "React"},
        {"Name": "Ritik", "Marks": 76, "Course": "Node"},
        {"Name": "Ankit", "Marks": 96, "Course": "Next.js"},
    ]

    # content = """
    # <table border = 1>
    # <tr>
    # <th>Name</th>
    # <th>Marks</th>
    # <th>Course</th>
    # </tr>
    # """
    # for i in studentinfo:
    #     content += f"""
    #     <tr>
    #         <td>{i["Name"]}</td>
    #         <td>{i["Marks"]}</td>
    #         <td>{i["Course"]}</td>
    #     </tr>
    #     """
    # content += "</table>"
    

    # content = "Student list: <br>"
    # for student in studentinfo:
    #     for key, value in student.items():
    #         content += f"{key} {value} <br>"
    #     content += "<br>"


    content = "<table border = 1>"
    for colnames in studentinfo[0].keys():
        content += f"""
        <th>{colnames}</th>
        """

    for i in studentinfo:
        content += "<tr>"
        for key, value in i.items():
            content += f"""
            <td>{value}</td>
            """
    content += "</tr> </table>"

    return HttpResponse(content)

def studentdetails2(request):
    studentinfo = {
        "Amit": {"Marks": 90, "Course": "Django"},
        "Manish": { "Marks": 86, "Course": "React"},
        "Ritik": {"Marks": 76, "Course": "Node"},
    }

    # content = ""
    # for name, details in studentinfo.items():
    #     content += f"Name: {name}<br>"
    #     content += f"Marks: {details['Marks']}<br>"
    #     content += f"Course: {details['Course']}<br><br>"

    content = """
    <table border = 1 >
    <tr>
    <th>Name</th>
    <th>Marks</th>
    <th>Course</th>
    </tr>
    """
    for key, value in studentinfo.items():
        content += f"""
        <tr>
        <td>{key}</td>
        <td>{value['Marks']}</td>
        <td>{value['Course']}</td>
        </tr>
        """
    content += "</table>"
    return HttpResponse(content)

# ------------------------- Dynamic URL --------------
def greetings(request, name):
    return HttpResponse(f"Welcome, {name}")

def add(request, num1, num2):
    return HttpResponse(f'The result is {num1 + num2}')

def foodie(request, foodvalue):
    # fooditems = ["noodeles", "pizza", "Icecream, Bread"]
    fooditems = {
        "Pizza": "size is regular, price is 50",
        "Burger": "size is medium, price is 100",
        "icecream": "Icecream is large, price is 40"
    }
    if foodvalue not in fooditems:
        return HttpResponse(f"The selected item {foodvalue} is not available")
    # return HttpResponse(fooditems[foodvalue])
    return HttpResponse(f"You have selected {foodvalue}. <h4 style=color:violet> {fooditems[foodvalue]} </h4>")

def calculation(request):
    operation = request.GET.get('operation')
    value1 = request.GET.get('value1')
    value2 = request.GET.get('value2')

    # try:
    #     value1 = int(value1)
    #     value2 = int(value2)
    # except:
    #     return HttpResponse("Enter valid number")
    # result = None

    if operation == "add":
        result = int(value1) + int(value2)
    elif operation == "subtract":
        result = int(value1) - int(value2)
    elif operation == "multiply":
        result = int(value1) * int(value2)
    elif operation == "divide":
        result = int(value1) / int(value2)
    else:
        result = "Invalid"

    return HttpResponse(f"The result of {operation} is {result}")

# --------------- Regular Exprression ---------------
def customer_profile(request, customername):
    return HttpResponse(f'Customer Profile: {customername}')

def user_profile(request, username):
    return HttpResponse(f'User Profile: {username}')

def item_detail2(request, item):
    return HttpResponse(f'Item Id: {item}')

def archive_details(request, year, month):
    return HttpResponse(f'Archive Year: {year}, Month: {month}')


def food_category(request, category, subcategory):
    # if(subcategory == ''):
    if not subcategory:
        return HttpResponse(f'You have choosen category: {category} and You have choosen subcategory: not specified')
    return HttpResponse(f'You have choosen category: {category} and  You have choosen subcategory: {subcategory}')


# Error Handling
# Simulate Error 500 (server error)
def dividebyzero(request):
    a = 10
    result = a/0
    return HttpResponse(result)



# -------------------------- Templates -----------------------
def mytemplate(request):
    data= {'name': 'ayush'}
    return render(request, 'test.html', data)


def fooddata(request):
    newmenu=[
        {'name':'Noodles', 'price':40},
        {'name':'Pizza', 'price':100},
        {'name':'Bread', 'price':'free'},
    ]
    
    return render(request, 'menu.html', {'menu': newmenu})



# image loading

def testimage(request):
    return render(request, 'testimage.html')


def productlist(request):
    products = [
        {'name': 'Product 1','brand':'Brand 1', 'price': 10.99, 'image': 'images/f2.jpg'},
        {'name': 'Product 2', 'brand':'Brand 2', 'price': 19.99, 'image': 'images/ff2.jpg'},
        {'name': 'Product 3', 'brand':'Brand 3', 'price': 5.99, 'image': 'images/l.jpg'},
        {'name': 'Product 4', 'brand':'Brand 4', 'price': 15.99, 'image': 'images/download.jpg'},
        
    ]
    return render(request, 'products.html', {'products': products})


# shoping list 
# this is like this image and name show if i click on it it will show the details of that product

def shoppinglist(request):
    products = [
        {'name': 'Product 1','brand':'Brand 1', 'price': 10.99, 'image': 'images/f2.jpg'},
        {'name': 'Product 2', 'brand':'Brand 2', 'price': 19.99, 'image': 'images/ff2.jpg'},
        {'name': 'Product 3', 'brand':'Brand 3', 'price': 5.99, 'image': 'images/l.jpg'},
        {'name': 'Product 4', 'brand':'Brand 4', 'price': 15.99, 'image': 'images/download.jpg'},
        
    ]
    return render(request, 'shopping.html', {'products': products})


def shoppingdetails(request, product_id):
    products = [
        {'name': 'Product 1','brand':'Brand 1', 'price': 10.99, 'image': 'images/f2.jpg'},
        {'name': 'Product 2', 'brand':'Brand 2', 'price': 19.99, 'image': 'images/ff2.jpg'},
        {'name': 'Product 3', 'brand':'Brand 3', 'price': 5.99, 'image': 'images/l.jpg'},
        {'name': 'Product 4', 'brand':'Brand 4', 'price': 15.99, 'image': 'images/download.jpg'},
        
    ]
    # The URL uses a numeric ID, while the displayed name remains free to contain
    # spaces or other characters.
    if product_id < 1 or product_id > len(products):
        return HttpResponse("Product not found", status=404)

    product = products[product_id - 1]
    return render(request, 'shoppingdetails.html', {'product': product})


def restaurant_detail(request):
    """Display the Pizza Palace restaurant menu used by the ordering screens."""
    restaurant = {
        'name': 'Pizza Palace',
        'cuisines': 'Italian, Pizza, Desserts',
        'rating': '4.7',
        'reviews': '500+ reviews',
        'delivery_time': '25–30 min',
        'distance': '900 m',
        'image': 'images/restaurant-hero.png',
    }
    menu_items = [
        {
            'name': 'Margherita Pizza',
            'description': 'Classic tomato sauce, fresh mozzarella, basil and olive oil.',
            'price': 299,
            'tag': 'Recommended',
            'image': 'images/ff2.jpg',
        },
        {
            'name': 'Pepperoni Feast',
            'description': 'Pepperoni and mozzarella on our signature tomato base.',
            'price': 349,
            'tag': 'Bestseller',
            'image': 'images/f2.jpg',
        },
    ]
    return render(request, 'restaurant_detail.html', {
        'restaurant': restaurant,
        'menu_items': menu_items,
    })


def item_detail(request):
    """Display the selected pizza and its configurable order options."""
    item = {
        'name': 'Margherita Pizza',
        'restaurant': "La Pino'z Pizza",
        'description': 'Cheese, basil and tomato sauce',
        'base_price': 299,
        'image': 'images/ff2.jpg',
        'sizes': [
            {'name': 'Regular', 'price': 299},
            {'name': 'Medium', 'price': 399},
            {'name': 'Large', 'price': 499},
        ],
    }
    return render(request, 'item_detail.html', {'item': item})


def payment(request):
    """Present payment choices for the current demo pizza order."""
    order = {
        'restaurant': 'Pizza Palace',
        'items': [
            {'name': 'Margherita Pizza', 'quantity': 1, 'price': 299},
            {'name': 'Pepperoni Feast', 'quantity': 1, 'price': 349},
        ],
        'item_total': 648,
        'delivery_fee': 49,
        'taxes': 32,
        'total': 729,
    }
    return render(request, 'payment.html', {'order': order})


def tracking(request):
    """Show a delivery-status view for the demo pizza order."""
    order = {
        'number': '#PP-1048',
        'restaurant': 'Pizza Palace',
        'eta': '12 min',
        'address': 'Home · 42 Green Park, New Delhi',
        'rider': 'Arjun Kumar',
        'rider_rating': '4.9',
        'steps': [
            {'title': 'Order confirmed', 'detail': 'Pizza Palace has accepted your order.', 'time': '9:32 PM', 'state': 'complete'},
            {'title': 'Being prepared', 'detail': 'Your pizzas are fresh from the oven.', 'time': '9:36 PM', 'state': 'complete'},
            {'title': 'Out for delivery', 'detail': 'Arjun is on the way to you.', 'time': 'Now', 'state': 'current'},
            {'title': 'Delivered', 'detail': 'Enjoy your meal!', 'time': '', 'state': 'pending'},
        ],
    }
    return render(request, 'tracking.html', {'order': order})


def checkout(request):
    """Review address and items before handing the order to payment."""
    order = {
        'restaurant': 'Pizza Palace',
        'address_name': 'Home',
        'address': '42 Green Park, New Delhi – 110016',
        'phone': '+91 98765 43210',
        'items': [
            {'name': 'Margherita Pizza', 'detail': 'Regular · Qty 1', 'price': 299},
            {'name': 'Pepperoni Feast', 'detail': 'Qty 1', 'price': 349},
        ],
        'item_total': 648,
        'delivery_fee': 49,
        'taxes': 32,
        'total': 729,
    }
    return render(request, 'checkout.html', {'order': order})






    
# template inheritance


def home3(request):
    return render(request, 'home1.html')
def about3(request):
    return render(request, 'about1.html')   
def food3(request):
    return food(request)

def food(request):
    newmenu=[
        {
            'name': 'Hakka Noodles', 'price': 140, 'image': 'images/f2.jpg',
            'description': 'Wok-tossed noodles with crisp vegetables and house sauce.'
        },
        {
            'name': 'Garden Pizza', 'price': 220, 'image': 'images/ff2.jpg',
            'description': 'Stone-baked pizza with mozzarella, basil and seasonal vegetables.'
        },
        {
            'name': 'Artisan Bread Basket', 'price': 80, 'image': 'images/l.jpg',
            'description': 'Freshly baked bread served warm with herbed butter.'
        },
        {
            'name': 'Paneer Butter Masala', 'price': 260, 'image': 'images/paneer-meal.png',
            'description': 'Creamy tomato curry with tender paneer, naan and fragrant rice.'
        },
    ]
    
    return render(request, 'food1.html', {'menu': newmenu})




# external css using 
def testcss(request):
    return render(request, 'testcss.html')



def items(request):
    products = [
        {'name':'laptop'},
        {'name':'mobile'},
        {'name':'tablet'},
        {'name':'desktop'},
    ]
    return render(request, 'items.html', {'products': products})


def itemdetails(request, product_id):
    products = [
        {'name':'laptop', 'price': 50000, 'description': 'A high-performance laptop for work and play.'},
        {'name':'mobile', 'price': 20000, 'description': 'A sleek smartphone with a stunning display.'},
        {'name':'tablet', 'price': 30000, 'description': 'A versatile tablet for entertainment and productivity.'},
        {'name':'desktop', 'price': 40000, 'description': 'A powerful desktop computer for gaming and work.'},
    ]
    
    if product_id < 1 or product_id > len(products):
        return HttpResponse("Product not found", status=404)

    product = products[product_id - 1]
    return render(request, 'itemdetails.html', {'product': product})




# testing in Django

def sampletest(request):
    return HttpResponse("<h1 style='color:blue'>This is a sample test page</h1>")

def sampletest1(request, id):
    return HttpResponse(f"<h1 style='color:blue'>This is a sample test page with id {id}</h1>")




def new(request):
    return HttpResponse("some content")
def old(request):
    return HttpResponse("some content")




# htmlform.html
def htmlform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if name and email and password:
            return HttpResponse(
                f"Form submitted successfully! Name: {name}, Email: {email}"
            )

    return render(request, "htmlform.html")




# validate_form.html
def validate_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        
        name_error = None
        email_error = None
        password_error = None

        if not name:
            name_error = "Name is required."
        if not email:   
            email_error = "Email is required."
        if len(password) < 6:
            password_error = "Password must be at least 6 characters long."
        if name_error or email_error or password_error:
            return render(request, "validate_form.html", {
                "name_error": name_error,
                "email_error": email_error,
                "password_error": password_error,
                "name": name,
                "email": email,
            })    
        submitted_details = {
            "name": name,
            "email": email,
        }

        return render(request, "validate_form.html", {"submitted_details": submitted_details})

    return render(request, "validate_form.html")






# form.py
from .forms import InputForm1
def form_submission(request):
    if request.method == 'POST':
        form = InputForm1(request.POST)
        if form.is_valid():
            return HttpResponse("Form submitted successfully!")
    form = InputForm1()
    return render(request, 'InputForm1.html', {'form': form})    



# form submission using InputForm2
from .forms import InputForm2
def form_submission2(request):
    submitted_details = None
    if request.method == 'POST':
        form = InputForm2(request.POST, request.FILES)
        if form.is_valid():
            submitted_details = form.cleaned_data
    form = InputForm2()        
    return render(request, 'InputForm2.html', {'form': form, 'submitted_details': submitted_details})      



# from .forms import Blogpostform
from .forms import Blogpostform
def insertblogpost(request):
    blog_created = False
    blog_post = None
    if request.method == 'POST':
        form = Blogpostform(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            blog_created = True
    else:
        form = Blogpostform()
        blog_created = False
    return render(request, 'insertblogpost.html', {
        'form': form,
        'blog_created': blog_created,
        'blog_post': blog_post,
    })

from .models import Blogpost
def blogposts(request):
    posts = Blogpost.objects.all()
    return render(request, 'blogposts.html', {'posts': posts})




# cookies
# set cookie
def set_cookie(request):
    response = HttpResponse("Cookie has been set.")
    response.set_cookie('Name', 'Ashutosh', max_age=3600)  # Cookie expires in 1 hour
    response.set_cookie('Age', '25', max_age=3600)  # Cookie expires in 1 hour
    return response


# get cookie
def get_cookie(request):
    value = request.COOKIES.get('Name')
    age = request.COOKIES.get('Age')
    return HttpResponse(f"Cookie value: {value}, Age: {age}")


# delete cookie
def delete_cookie(request):
    response = HttpResponse("Cookie has been deleted.")
    response.delete_cookie('Name')
    return response


# Store the most recently visited page in the Last_page cookie.
def cookiesview1(request):
    response = HttpResponse("You visited Page1.")
    response.set_cookie('Last_page', 'Page1', max_age=3600)  # Cookie expires in 1 hour
    return response


def cookieview2(request):
    response = HttpResponse("You visited Page2.")
    response.set_cookie('Last_page', 'Page2', max_age=3600)  # Cookie expires in 1 hour
    return response


def cookieview3(request):
    response = HttpResponse("You visited Page3.")
    response.set_cookie('Last_page', 'Page3', max_age=3600)  # Cookie expires in 1 hour
    return response


def LastVisitedPage(request):
    last_page = request.COOKIES.get('Last_page', 'No page has been visited yet.')
    # return HttpResponse(f"Last visited page: {last_page}")
    return render(request, 'lvp.html', {'last_page': last_page})




# ----------------------------auth------------------------------
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomerForm


def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        customer_form = CustomerForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return HttpResponse("Registration successful!")

        # Keep the bound forms so their validation errors are shown.
        return render(request, 'register.html', {
            'user_form': user_form,
            'customer_form': customer_form,
        })

    # A GET request needs empty forms and, importantly, an HTTP response.
    user_form = UserCreationForm()
    customer_form = CustomerForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'customer_form': customer_form,
    })
