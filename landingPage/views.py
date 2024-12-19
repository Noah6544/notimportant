from django.shortcuts import render, get_list_or_404, redirect

from django.http import HttpResponse, HttpResponseRedirect
from .models import PotentialUser
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'landingPage/index.html')

def coming_soon(request):
    if request.method == 'POST':
            print('request', request)
            print('request.POST', request.POST)
            try:
                email = request.POST['email']
                os = request.POST['os']
                tier = str(request.POST['tier'][0])
                print('os', os)
                print('email', email)
                print('tier', tier)
                
                user = PotentialUser.create(email=email, tier=tier,os=os)
                user.save()
                print('got here...')
                return HttpResponseRedirect(reverse("landingPage:thank-you"))
            except Exception as e:
                print('ERROR', e)
                return render(request, 'landingPage/coming-soon.html', {'error':f'Something Went Wrong: {str(e)} ','messageTitle': "Thank you.", "thank you":'messageTitle', 'messageBody': "Your response has been recorded."})
    else:
        return render(request, 'landingPage/coming-soon.html', {'messageTitle': "Thank you.", "thank you":'messageTitle', 'messageBody': "Your response has been recorded."})

    # print('request', request)
    # form = getUserInfoForm
    # if request.method == 'POST':
    #     # form = getUserInfoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/Thank-You')
    # else:
    #     pass
        

def thank_you(request):
   return render(request, 'landingPage/thank-you.html', {'messageTitle': "Thank you.", "thank you":'messageTitle', 'messageBody': "Your response has been recorded."})