from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def admin_home(request):
    return render(request,'admin/adminhome.html')

def admin_signin(request):
    # if request.user.is_authenticated:
    #     print("11111")
    #     return redirect(admin_home)
    if request.method == "POST":
        print("2222")
        username = request.POST['email'],
        
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        print("333")
        if username=='' and password =='':
            messages.error("Invalid Credential")
            return redirect(admin_signin)
        if user is not None:
            print("444")
            if user.is_admin==True:
                login(request,user)

                return redirect(admin_home)
            else:
                messages.error(request,"You are not authorized")
                return redirect(admin_signin)
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect(admin_signin)
    else:

        return render(request,'admin/admin_signin.html')



def admin_signout(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect(admin_signin)