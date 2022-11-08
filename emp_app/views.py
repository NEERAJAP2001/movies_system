from django.shortcuts import render, HttpResponse
from .models import Movies, Genre, Theatre, customer1
from datetime import datetime
from django.db.models import Q
from .forms import customerform1

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Movies.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    pass
    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     cost = int(request.POST['cost'])
    #     theatre = int(request.POST['Theatre Name'])
    #     genre = int(request.POST['Genre'])
    #     new_emp = Movies(first_name= first_name, last_name=last_name, cost=cost, theatre_id = theatre,Genre_id = genre, Date_of_release = datetime.now())
    #     new_emp.save()
    #     return HttpResponse('Movies added Successfully')
    # elif request.method=='GET':
    #     return render(request, 'add_emp.html')
    # else:
    #     return HttpResponse("An Exception Occured! Movies Has Not Been Added")


def remove_emp(request, emp_id=0):
    # form3=customerform1()
    # if request.method=='POST':
    #     form3=customerform1(request.POST)
    #     username=request.POST.get('theatre')
    #     if Movies.theatre==username:
    #         l="theatre"+username
    #         temp=Movies.objects.filter(theatre=username).values('genre').distinct()
    #         form4=customerform2()

    #         return render(request,'form.html',{'form3':form3,'l':l,'temp':temp,'form4':form4})

    # form4=customerform2()
    # if request.method=='POST':
    #     form4=customerform2(request.POST)
    #     genre=request.POST.get('genre')
    #     if Movies.genre==genre:
    #         return HttpResponse(genre)
    #     else:
    #         return HttpResponse('An Exception Occurred')

    # return render(request,'form.html',{'form3':form3})

    if emp_id:
        try:
            emp_to_be_removed = Movies.objects.get(id=emp_id)
            if emp_to_be_removed.Remaning_tickets >= 1:
                emp_to_be_removed.Remaning_tickets -= 1
                emp_to_be_removed.save()
            elif emp_to_be_removed.Remaning_tickets == 0:
                emp_to_be_removed.delete()
            elif emp_to_be_removed.Remaning_tickets < 0:
                return HttpResponse("Sorry! Tickets over")
            return render(request, 'book.html')
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Movies.objects.all()
    emps1 = Movies.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)


def filter_mov(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['theatre']
        Genre = request.POST['genre']
        emps = Movies.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name)
                               | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(theatre__name__icontains=dept)
        if Genre:
            emps = emps.filter(genre__name__icontains=Genre)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')


def login(request):
    form3 = customerform1()
    if request.method == 'POST':
        form3 = customerform1(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        l = username
        if customer1.objects.filter(username=username, password=password).exists():
            return render(request, 'index.html')
        else:
            return HttpResponse("<h1>Login Failed PleaseEnter Valid Password or username</h1>")
    return render(request, 'logins.html', {'form3': form3})


def signup(request):
    form1 = customerform1()
    if request.method == 'POST':
        form1 = customerform1(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        customer1.objects.create(username=username, password=password)
        form1.save()
        l = username
        #return render(request, 'logins.html')
        return HttpResponse("<h1>Signup Successful {{l}}</h1>")

    return render(request, 'signup.html', {'form1': form1})
