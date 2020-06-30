from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration
from .forms import CustomerSignup


# Create your views here.
def Index(request):
    
    return render(request,'FoodyApp/home.html')

def recipes1(request):

    return render(request,'FoodyApp/recipes.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        request.session['sessionname']=name
        request.session['sessionemail']=email
        return redirect('showresult')


    return render(request,'FoodyApp/contact.html')

def showresult(request):
    name=request.session['sessionname']
    email=request.session['sessionemail']
    return render(request,'FoodyApp/show.html',{'name':name,'email':email})

def about(request):

    return render(request,'FoodyApp/about.html')


def reserve(request):

    return render(request,'FoodyApp/reserve.html')



# def ReserveForm(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         guests = request.POST.get('guests')
#         phone = request.POST.get('phone')
#         time = request.POST.get('time')
#         request.session['sessionName']=name
#         request.session['sessionGuests']=guests
#         request.session['sessionPhone']= phone
#         request.session['sessionTime']=time

#         return redirect('showSession')
#     return render(request,'FoodyApp/reserve.html')

# def showSession(request):
#     name = request.session['sessionName']
#     guests =request.session['sessionGuests']
#     phone =request.session['sessionPhone']
#     time =request.session['sessionTime']

#     return render(request,'FoodyApp/acknowledgement.html',{
#         'name':name,
#         'guests':guests,
#         'phone':phone,
#         'time':time
#     })


def signup(request):
    form = CustomerSignup()
    if request.method == 'POST':
        form=CustomerSignup(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            guests = form.cleaned_data['guests']
            time = form.cleaned_data['time']
            order = form.cleaned_data['orders']
            password = form.cleaned_data['password']
            
            register=Registration()

            register.name=name
            register.address=address
            register.phone=phone
            register.guests=guests
            register.time=time
            register.orders = order
            register.password=password
            register.save()
            return redirect('registered')

    return render(request,'FoodyApp/reserve.html',{'form':form})

def registered(request):
    return render(request,'FoodyApp/registered.html')

def login(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        phone=request.POST.get('phone')
        password= request.POST.get('password')

        print(name,password)

        data= Registration.objects.filter(name= name, password= password, phone= phone)

        if data:

            form = CustomerSignup()

            request.session['name']= name
            request.session['phone']= phone
            request.session['password']= password

            Customer = request.session['name']
            Mobile = request.session['phone']
            password=request.session['password']
           
            return render(request,'FoodyApp/acknowledgement.html', {'name': Customer, 'phone': Mobile })

    return render(request,'FoodyApp/customerlogin.html')


# def acknowledge(request):
#     return redirect('acknowledge')


def register(request):
    return render(request,'FoodyApp/register.html')