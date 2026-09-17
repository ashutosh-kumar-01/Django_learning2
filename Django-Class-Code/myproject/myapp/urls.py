from django.http import HttpResponse
from django.urls import path, re_path
from . import views

urlpatterns = [

    #
    path('', views.home),
    path('favicon.ico', lambda request: HttpResponse(status=204)),
    path('curr_time/', views.current_time),
    # 

    path('hello/', views.hello),
    path('home/', views.home),
    path('dish/', views.menuitem),
    path('dishes/', views.menuitems),
    path('details/', views.details),

    # Dynamic URLs (Route Parameter)
    path('greet/<str:name>', views.greet),
    path('menuitems1/<str:dish>', views.menuitems1),
    path('menuitems2/<str:dish>', views.menuitems2),

    # Dynamic URLs (Query Parameter)
    path('recipe/', views.recipe),
    path('addition/', views.addition),
    path('calculate/', views.calculate),

    # Regular Expressions
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile),
    # re_path(r'^item/(?P<item_id>[0-9]+)/$', views.item_detail),
    # re_path(r'^item/(?P<item_id>\d+)/$', views.item_detail),
    # re_path(r'^item/(?P<item_id>\d{4})/$', views.item_detail),
    #  re_path(r'^item/(?P<item_id>\d{2,4})/$', views.item_detail),
    re_path(r'^item/(?P<item_id>[\w-]+)/$', views.item_detail),
    re_path(r'^restaurant/(?P<category>[\w\s%&-]+)/(?P<subcategory>[\w-]*)/?$', views.restro_detail),

    # Templates
    path('home1/', views.home1),
    path('about/', views.about),
    path('menu/', views.menu),
    path('menu1/', views.menu1),

    # Template Inheritance
    path('home2/', views.home2, name='home2'),
    path('about2/', views.about2, name='about2'),
    path('menuitems2/', views.menuitems2, name='menuitems'),

    # ----------------------- Class Code ----------------------------
    path('newdetails/', views.newdetails),
    path('percent/', views.percent),
    path('multiple/', views.multiple),
    path('grade/', views.grade),
    path('food/', views.food),
    path('food1/',views.food1),
    path('studentdetails/', views.studentdetails),
    path('studentdetails1/', views.studentdetails1),
    path('studentdetails2/', views.studentdetails2),

    # Dynamic URLs (Route Parameter)
    path('greet/<str:name>', views.greetings),
    path('add/<int:num1>/<int:num2>', views.add),
    path('foodie/<str:foodvalue>', views.foodie),
    path('calculation/', views.calculation),

    # Regular Exprression:- Matches URLs like /cutomer/Alice/ or /customer/Bob/ 
    # re_path(r'^customer/(?P<customername>[a-zA-Z]+)/$', views.customer_profile),
    re_path(r'^customer/(?P<customername>[\w \s -]+)/$', views.customer_profile),

    # Matches URLs like /user/Alice/ or /user/
    re_path(r'^user/(?P<username>[a-zA-Z]*)/?$', views.user_profile),

    # Matches URLs like /item/123
    # re_path(r'^item/(?P<item_id>\d+)/$', views.item_detail2),
    re_path(r'^item/(?P<item_id>[0-9]+)/$', views.item_detail2),

    # Matches URLs like /archive/1992/12/
    re_path(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive_details),

    # re_path(r'^restaurant1/(?P<category>[\w\s%&-]+)/(?P<subcategory>[\w-]*)/?$', views.food_category),
    re_path(r'^restaurant1/(?P<category>[\w \s]+)/(?P<subcategory>[\w \s]*)/?$', views.food_category),
    # re_path(r'^restaurant1/(?P<category>[a-zA-Z0-9]+)/(?P<subcategory>[\w \s]*)/?$', views.food_category),

    # re_path(r'^blog(?:/(?P<post_slug>[\w-]+))*/$', views.blog_details),


    path('dividebyzero/',views.dividebyzero),
    
    
    
    
     # -----------------------------------template tags-----------------------------------
    path('mytemplate/', views.mytemplate),
    path('fooddata/', views.fooddata),
    
    # image loading
    path('testimage/', views.testimage),
    path('productlist/', views.productlist),
    
    
    # for show details of the product
    path('shoppinglist/', views.shoppinglist, name='shoppinglist'),
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('shoppingdetails/<int:product_id>/', views.shoppingdetails, name='shoppingdetails'),
    
    
    
    
    
    # template inheritance
    path('home3/', views.home3, name='home3'),
    path('about3/', views.about3, name='about3'),   
    path('food3/', views.food3, name='food3'),
    
    
    
]



    
