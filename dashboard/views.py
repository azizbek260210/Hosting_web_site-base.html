from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='dashboard:log_in')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()
    context = {
        'contacts':contacts
    }
    return render(request,'dashboard/index.html',context)


@login_required(login_url='dashboard:log_in')
def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


@login_required(login_url='dashboard:log_in')
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    context = {'banner':banner}
    return render(request,'dashboard/banner/detail.html',context)


@login_required(login_url='dashboard:log_in')
def edit_banner(request,id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST.get('title')
        banner.body = request.POST.get('body')
        banner.save()
        return redirect('banner_detail', banner.id)
    context = {
            'banner':banner
        }
    return render(request,'dashboard/banner/edit.html',context)


@login_required(login_url='dashboard:log_in')
def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('banner_list')


@login_required(login_url='dashboard:log_in')
def create_about(request):
    if request.method == 'POST':
        body = request.POST.get('body')
        models.AboutUs.objects.create(
            body=body
        )
    return render(request,'dashboard/about/create.html')


@login_required(login_url='dashboard:log_in')
def list_about(request):
    abouts = models.AboutUs.objects.all()
    context = {
        'abouts':abouts
    }
    return render(request,'dashboard/about/list.html',context)


@login_required(login_url='dashboard:log_in')
def detail_about(request,id):
    about = models.AboutUs.objects.get(id=id)
    context = {'about':about}
    return render(request,'dashboard/about/detail.html',context)


@login_required(login_url='dashboard:log_in')
def edit_about(request,id):
    about = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        about.body = request.POST.get('body')
        about.save()
        return redirect('about_list')
    context = {'about':about}
    return render(request,'dashboard/about/edit.html',context)


@login_required(login_url='dashboard:log_in')
def delete_about(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('about_list')


@login_required(login_url='dashboard:log_in')
def create_price(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        body = request.POST.get('body')
        models.Price.objects.create(
            title=title,
            price=price,
            body=body
        )
    return render(request,'dashboard/price/create.html')


@login_required(login_url='dashboard:log_in')
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request,'dashboard/price/list.html',context)


@login_required(login_url='dashboard:log_in')
def detail_price(request,id):
    price = models.Price.objects.get(id=id)
    context = {'price':price}
    return render(request,'dashboard/price/detail.html',context)


@login_required(login_url='dashboard:log_in')
def edit_price(request,id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST)
        price.title = request.POST.get('title')
        price.body = request.POST.get('body')
        price.price = request.POST.get('price')
        price.save()
        return redirect('price_list')
    context = {'price':price}
    return render(request,'dashboard/price/edit.html',context)


@login_required(login_url='dashboard:log_in')
def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('price_list')


@login_required(login_url='dashboard:log_in')
def create_service(request):
    if request.method == 'POST' and request.FILES['file']:
        name = request.POST.get('name')
        body = request.POST.get('body')
        icon = request.FILES.get('file')
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon
        )
    return render(request,'dashboard/service/create.html')


@login_required(login_url='dashboard:log_in')
def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'dashboard/service/list.html',context)


@login_required(login_url='dashboard:log_in')
def detail_service(request,id):
    service = models.Service.objects.get(id=id)
    context = {'service':service}
    return render(request,'dashboard/service/detail.html',context)


@login_required(login_url='dashboard:log_in')
def edit_service(request,id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.body = request.POST.get('body')
        if request.FILES:
            service.icon = request.FILES.get('icon')
        service.save()
        return redirect('service_list')
    
    context = {'service':service}

    return render(request,'dashboard/service/edit.html',context)


@login_required(login_url='dashboard:log_in')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('service_list')
    

@login_required(login_url='dashboard:log_in')
def list_contact(request):
    contacts = models.Contact.objects.all()
    context = {'contacts':contacts}
    return render(request,'dashboard/contact/list.html',context)


@login_required(login_url='dashboard:log_in')
def detail_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    context = {'contact':contact}
    return render(request,'dashboard/contact/detail.html',context)


@login_required(login_url='dashboard:log_in')
def edit_contact(request,id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.is_show = bool(int(request.POST.get('is_show')))
        print(request.POST)
        contact.save()
        return redirect('contact_list')
    context = {'contact':contact}
    return render(request,'dashboard/contact/edit.html',context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            User.objects.create_user(
                username = username,
                password = password
            )
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = User.objects.get(username=username)
        user = authenticate(
            username = username, 
            password = password
            )
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            ...

    return render(request, 'dashboard/auth/login.html')



@login_required(login_url='dashboard:log_in')
def log_out(request):
    logout(request)
    return redirect('main:index')