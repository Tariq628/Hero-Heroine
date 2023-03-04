
from django.contrib.auth import authenticate, login, logout
from .models import Brand, Category, CustomUser, Product, SubUser
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login/')
def profile(request):
    main_user = request.user
    if main_user.is_selected:
        user = request.user
    else:
        user = SubUser.objects.get(parent=main_user, is_selected=True)
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        image = request.FILES['image']
        print(image)
        user.first_name = full_name
        user.phone = phone
        user.gender = gender
        user.age = age
        user.image = image
        user.save()
        return render(request, 'user-profile-edit.html', {'image': user.image, 'name': user.first_name})

    return render(request, 'profile.html')


@login_required(login_url='/login/')
def sub_user(request):
    if request.method == "POST":
        name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        image = request.FILES['image']

        sub_user = SubUser()
        sub_user.parent = request.user
        sub_user.name = name
        sub_user.phone = phone
        sub_user.gender = gender
        sub_user.age = age
        sub_user.image = image
        sub_user.save()
        return render(request, 'user-profile-edit.html', {'image': sub_user.image, 'name': sub_user.name})
    return render(request, 'sub_profile.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(CustomUser.objects.get(username=username))
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/profile/")
    return render(request, 'login.html')


@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def user_info(request):
    context = {}
    user = CustomUser.objects.get(username=request.user.username)
    print("user_ifo")
    print(user.id)
    sub_users = user.subuser_set.all()
    context['user'] = user
    context['sub_users'] = sub_users
    return render(request, 'user-info.html', context)


@login_required(login_url='/login/')
def select_profile(request):

    if request.method == "POST":
        main_user = request.user
        main_user.is_selected = False
        main_user.save()
        main_user.subuser_set.all().update(is_selected=False)

        user_subuser = request.POST.get('user_subuser')
        if isinstance(request.POST.get('id'), list):
            id = int(request.POST.get('id')[0])
        else:
            id = int(request.POST.get('id'))

        if user_subuser == "user":
            user = CustomUser.objects.get(id=id)
        else:
            user = SubUser.objects.get(id=id)
        print(user)
        user.is_selected = True
        user.save()

    return redirect('/brands/')


@login_required(login_url='/login/')
def brands(request):
    main_user = request.user
    if main_user.is_selected:
        user = main_user
    else:
        user = SubUser.objects.get(is_selected=True, parent=main_user)
    brands = Brand.objects.all()
    return render(request, 'brands.html', {'brands': brands})


def category(request, brand_id):
    categories = Category.objects.filter(brand_id=brand_id)
    return render(request, 'category.html', {'categories': categories})


def products(request, cat_id):
    products = Product.objects.filter(category_id=cat_id)
    products_with_images = []
    for product in products:
        first_image = product.product_img.first()  # get the first image for the product
        products_with_images.append({'product': product, 'image': first_image})
    return render(request, 'products.html', {'products_with_images': products_with_images})



@login_required(login_url='/login/')
def user_profile(request):
    main_user = request.user
    context = {}

    if main_user.is_selected:
        user = main_user
        name = user.first_name
    else:
        user = SubUser.objects.get(is_selected=True, parent=main_user)
        name = user.name
    print(user)

    if request.method == "POST":
        height = request.POST.get('height')
        body_size = request.POST.get('body_size')
        user.height = height
        user.body_size = body_size
        user.save()

    context['name'] = name
    context['gender'] = user.gender
    context['height'] = user.height.replace(".", "'")
    context['body_size'] = user.body_size.capitalize()
    return render(request, 'user-profile.html', context)


@login_required(login_url='/login/')
def user_profile_edit(request):
    main_user = request.user
    context = {}

    if main_user.is_selected:
        user = main_user
        name = user.first_name
    else:
        user = SubUser.objects.get(is_selected=True, parent=main_user)
        name = user.name
    return render(request, 'user-profile-edit.html', {'image': user.image, 'name': name})


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        custom_user = CustomUser()
        custom_user.username = username
        custom_user.set_password(password)
        custom_user.save()
        return redirect('/login/')
    return render(request, 'signup.html')


def renewal(request):
    return render(request, 'account-renewal.html')


def user_edit(request, id):
    user = CustomUser.objects.get(id=id)
    context = {}
    context['name'] = user.first_name
    context['image'] = user.image
    return render(request, 'user-profile-edit.html', context)


def subuser_edit(request, id):
    main_user = request.user
    main_user.is_selected = False
    main_user.save()
    main_user.subuser_set.all().update(is_selected=False)

    user = SubUser.objects.get(id=id)
    user.is_selected = True
    user.save()
    context = {}
    context['name'] = user.name
    context['image'] = user.image
    return render(request, 'user-profile-edit.html', context)


def user_delete(request, id):
    user = CustomUser.objects.get(id=id).delete()
    return redirect('/user-info/')


def subuser_delete(request, id):
    SubUser.objects.get(id=id).delete()
    return redirect('/user-info/')


def slider1(request, id):
    context = {}
    product = Product.objects.get(id=id)
    images = product.product_img.all()
    context['product'] = product
    context['images'] = images
    print(len(images))
    return render(request, 'slider1.html', context)
