from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def showcategory(request):
    category=Category.objects.all()
    branch=Branch.objects.all()
    return render(request, 'index.html', {"Category" : category,"Branch" : branch})



def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.jsp.html')

def contact(request):
    return render(request, 'contactus.jsp.html')



def feedback(request):
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    contact = request.POST["telnum"]
    email = request.POST["emailid"]
    
    feed = request.POST["feedback"]

    send_feedback = model_feedback(firstname = firstname, lastname = lastname, contact = contact, email = email, feed = feed)

    send_feedback.save()
    return render(request, 'contactus.jsp.html')



def FindCollege(request):
    r = int(request.POST["rank"])
    dbranch = (request.POST["dbranch"])
    dcategory = (request.POST["dcategory"])
    print(r,dbranch,dcategory)

    b=Branch.objects.get(name=dbranch)
    c=Category.objects.get(name=dcategory)
    print(b.id,c.name)
    Mp=Mapping.objects.filter(branchid=b.id,categoryid=c.id,rank__gte=r).order_by('rank')
    print(Mp)
    if(len(Mp)==0):
        check=False
    else:
        check=True
    d=[]
    for i in range(len(Mp)):
        d.append([Mp[i],i+1])
    return render(request,'output.jsp',{'b':b, 'c':c, 'r':r, 'obj':d, 'l':check})


   

