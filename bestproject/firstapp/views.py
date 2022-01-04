
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import Users, Webpages,Userprofile
from django.urls import reverse
from .forms import ContactForm,WebForm,FormProfile,Userprofileinfo

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def index(request):
    
    if request.method == 'POST':
        form=ContactForm(request.POST)

        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname=form.cleaned_data['lastname']
            email=form.cleaned_data['email']



            form=Users.objects.create(firstname=firstname,lastname=lastname,email=email)
            form.save()



    else:


        form=ContactForm()
    return render(request,'index.html',context={'userform':form})





def textpage(request):
    form=WebForm()
   
    if request.method == 'POST':
        form=WebForm(request.POST)

        if form.is_valid():
            topic=form.cleaned_data['topic']
            name=form.cleaned_data['name']
            url=form.cleaned_data['url']

            form=Webpages.objects.create(topic=topic,name=name,url=url)
            form.save()
    else:
        WebForm()

    
    # context={'forms':form}

    return render(request,'textfile.html',context={'forms':form})


@login_required
def special(request):
    return HttpResponse("You are login")

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_user(request):
     if request.method=='POST':
         username=request.POST.get('username')
         password=request.POST.get('password')

         user=authenticate(username=username,password=password)
         if user:
             if user.is_active:
                 login(request,user)
                 return HttpResponseRedirect(reverse('index'))
             else:
                return HttpResponse("Account not <strong> activated </strong>")
         else:
            print("someone tried to login and failed")
            print(f"username: {username} and password {password}")
     else:

         return render(request,"loginpage.html",context={})


def contact(request):
   registered=False
  
   if request.method == 'POST':
       userform=FormProfile(data=request.POST)
       profileform=Userprofileinfo(data=request.POST)
       if userform.is_valid() and profileform.is_valid():
           user=userform.save()
           user.set_password(user.password)
           user.save()
      

           profile=profileform.save(commit=False)
           profile.user=user   

           if 'profile_pic ' in request.FILES:
               profile.profile_pic=request.FILES
           profile.save() 
           registered=True
           return redirect('firstapp:index')
   else:

       userform=FormProfile()
       profileform=Userprofileinfo()
   context={


       'userdetail':userform,
       'profilepics':profileform,
       'checkreg':registered

   }


   return render(request,'contact.html',context)
         