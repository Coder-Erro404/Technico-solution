from django.shortcuts import render
from django.contrib import  messages
from .models import Contact, product, project  , blog , Document, addnote ,impotantImage
from django.contrib import  messages
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from technico_app.filter import UserFilter

# --------------- MAIN WEB PAGES -----------------------------

def index(request):

	return render(request, 'index.html')

def hardware(request):
    user_list = product.objects.all().order_by('-timeStamp')
    user_filter = UserFilter(request.GET, queryset=user_list)
    user_list = user_filter.qs
    page = request.GET.get('page')
    paginator = Paginator(user_list, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    arg = {'filter':user_filter, 'page_obj':page_obj}  
    return render(request, 'hardware.html', arg)

	




def laptop(request):

	return render(request, 'laptop.html')

def computer(request):

	return render(request, 'computer.html')

def webdesign(request):

	return render(request, 'webdesign.html')

def accessories(request):

	return render(request, 'accessories.html')

def refurbished(request):

	return render(request, 'refurbished.html')

def cctv(request):

	return render(request, 'cctv.html')

def repairing(request):

	return render(request, 'repairing.html')
	 
def newtechnology(request):

	return render(request, 'newtechnology.html')
     
def projects(request):
    data = project.objects.all()
    paginator = Paginator(data, 3) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects.html',{'page_obj': page_obj})
    
def blogs(request):
    user_list = blog.objects.all().order_by('-timeStamp')
    user_filter = UserFilter(request.GET, queryset=user_list)
    user_list = user_filter.qs
    page = request.GET.get('page')
    paginator = Paginator(user_list, 3)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    arg = {'filter':user_filter, 'page_obj':page_obj}  
    return render(request, 'Blogs.html', arg)
# def testingblog(request):
#     data = blog.objects.all()
#     paginator = Paginator(data, 4) # Show 25 contacts per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)  
#     return render(request, 'testingblog.html', {'page_obj': page_obj})
def Notes(request):
    data = addnote.objects.all()
    paginator = Paginator(data, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    return render(request, 'notes.html', {'page_obj': page_obj})
def documents(request):
    data = Document.objects.all()
    paginator = Paginator(data, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    return render(request, 'documents.html', {'page_obj': page_obj})
def impotantImages(request):
    data = impotantImage.objects.all()
    paginator = Paginator(data, 8) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    return render(request, 'impotantImage.html', {'page_obj': page_obj})

# def addblogs(request):
#     data = addblog.objects.all()
#     paginator = Paginator(data, 25)
#     blog = {"sno": data}
#     return render(request, 'addblog.html',blog)

def contact(request):
    if request.method=="POST":
        F_name=request.POST['F_name']
        L_name=request.POST['L_name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(F_name)<2 or len(L_name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(F_name=F_name,L_name=L_name , email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'contact.html')

# -----------------------------------------------------------