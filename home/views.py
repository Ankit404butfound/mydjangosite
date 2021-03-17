from django.shortcuts import render, HttpResponse
from home.models import joinus 
from datetime import datetime
import smtplib
# Create your views here.
def home(request):
    #return HttpResponse("This is a home page")
    return render(request, 'index.html')

def joinuss(request):

    
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        user_id = request.POST.get('user_id')
        skills = request.POST.get('skills')
        joined = joinus(name=name, username=username, user_id=user_id, skills=skills, date = datetime.today())
        joined.save()
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login("hchardcorecommunity@gmail.com", "divyam123")
        server.sendmail("hchardcorecommunity@gmail.com", name,  "Hey, \n \n  Thanks for applying for HardCore Community. \n You will get a reply soon about your selection. \n \n Thanks! \n Team HardCore")
        server.sendmail("hchardcorecommunity@gmail.com", "hchardcoreowner@gmail.com", skills + user_id + name  + username )
        server.quit()
        return render(request, 'applied.html')
        

    
    return render(request, 'joinus.html')
  
    
def contactus(request):
    return render(request, 'contactus.html')
def verifiedusers(request):
    return render(request, 'verifiedusers.html')
def rulesguidelines(request):
    return render(request, 'rules&guidelines.html')
