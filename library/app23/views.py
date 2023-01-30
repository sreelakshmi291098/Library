from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
from app23.models import Stud_reg,Teacher_reg,Bookdetail,fine
from.import models
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
role=""
roles=""
def login(request):
    global role
    global roles
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        data=User.objects.filter(username=username).values()
        print("userModelData==>",data)
        for i in data:
            id=i['id']
            u_name=i['username']
            print(".............",id,u_name)
 
            da=Stud_reg.objects.filter(user_id=id).values()
            print("studentdata==>",da)
            for i in da:
                roles=i['role']
                statuss=i['status']
                print(roles)

            d=Teacher_reg.objects.filter(user_id=id).values()
            print("teacherdata==>",d)
            for i in d:
                roles=i['role']
                status=i['status']
                print(roles)

            user=authenticate(username=username,password=password)

            if user is not None and roles=='student' and username==u_name and status=="1":
                auth_login(request,user)
                return redirect("student")

            elif roles=='teacher' and username==u_name and status=="1":
                auth_login(request,user)
                return redirect("teacher")

            elif username=="sreelakshmi" and password=="sree123":
                return redirect("adminpage")
            else:pass
        else:
            messages.info(request,'Invalid credentials')
            return redirect("login")
    else:
        return render(request,'login.html')

def adminpage(request):
    return render(request,'admin.html')

def student(request):
    return render(request,'student.html')

def teacher(request):
    return render(request,'teacher.html')

def studreg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        cource=request.POST.get('cource')
        gender=request.POST.get('gender')
        phonenumber=request.POST.get('number')
        status="0"
        role="student"

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("studreg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("studreg")
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                userDetail=models.Stud_reg(user=user,name=name,email=email,age=age,phone_number=phonenumber,cource=cource,gender=gender,status=status,role=role)
                userDetail.save()

                print('user created')
        else:
            messages.info(request,"password is not matching")
            return redirect("studreg")
        return redirect("login")
    else:
        return render(request,'studreg.html')



def pay_fine(request):
    return render(request,'fine.html')

def teach_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        username=request.POST.get('username')
        password1=request.POST.get('password')
        password2=request.POST.get('conformpassword')
        cource=request.POST.get('cource')
        gender=request.POST.get('gender')
        phonenumber=request.POST.get('number')
        status="0"
        role="teacher"

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("teachreg")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("teachreg")
            else:
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                userDetail=models.Teacher_reg(user=user,name=name,email=email,age=age,phone_number=phonenumber,cource=cource,gender=gender,status=status,role=role)
                userDetail.save()

                print('user created')
        else:
            messages.info(request,"password is not matching")
            return redirect("teachreg")
        return redirect("login")
    else:
        return render(request,'teach_reg.html')


def studpending(request):
    data=Stud_reg.objects.all()
    return render(request,'viewstudent.html',{'data':data})

def teachpending(request):
    data=Teacher_reg.objects.all()
    return render(request,'viewteacher.html',{'data':data})

def stud_approve(request,reg_id):
    reg=Stud_reg.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("studpending")

def stud_reject(request,reg_id):
    item=Stud_reg.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("studpending")

def approvedstud(request):
    data=Stud_reg.objects.all()
    return render(request,'approvedstud.html',{'data':data})

def teach_approve(request,reg_id):
    reg=Teacher_reg.objects.get(id=reg_id)
    reg.status=1
    reg.save()
    return redirect("teachpending")

def teach_reject(request,reg_id):
    item=Teacher_reg.objects.get(id=reg_id)
    item.delete()
    messages.info(request,'delete successfull')
    return redirect("teachpending")

def approvedteach(request):
    data=Teacher_reg.objects.all()
    return render(request,'approvedteach.html',{'data':data})

def stud_delete(request,reg_id):
    add=Stud_reg.objects.get(id=reg_id)
    add.delete()
    return redirect('approvedstud')

def teach_delete(request,reg_id):
    dele=Teacher_reg.objects.get(id=reg_id)
    dele.delete()
    return redirect('approvedteach')

def book(request):
    if request.method=='POST':
        user=request.user
        book_id=request.POST.get('id')
        book_title=request.POST.get('title')
        book_author=request.POST.get('author')
        book_cost=request.POST.get('cost')
        status="0"
       
        userDetail=models.Bookdetail(user=user,book_id=book_id,book_title=book_title,book_author=book_author,book_cost=book_cost)
        userDetail.save()
        return redirect("adminpage")
    else:
        return render(request,'book_detail.html')

def viewbook(request):
    data=Bookdetail.objects.all()
    return render(request,'viewbookdetail.html',{'data':data})

def admin_request(request):
    data=Bookdetail.objects.all()
    return render(request,'admin_request_approve.html',{'data':data})

def viewstud(request):
    data=Stud_reg.objects.all()
    return render(request,'viewstuddetail.html',{'data':data})

def teach_book(request):
    data=Bookdetail.objects.all()
    return render(request,'viewteachbook.html',{'data':data})

def pay_fine(request):
    if request.method=='POST':
        book_title=request.POST.get('title')
        name=request.POST.get('name')
        delay=request.POST.get('delay')
        ammount=request.POST.get('ammount')

        userDetail=models.fine(book_title=book_title,name=name,delay=delay,ammount=ammount)
        userDetail.save()
        return redirect("adminpage")
    else:
        return render(request,'fine.html')

def viewfine(request):
    data=fine.objects.all()
    return render(request,'viewfine.html',{'data':data})





