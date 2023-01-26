from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic, Webpage, User
from . import forms
from first_app.forms import NewUserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html', context=date_dict)

# Used for Display users
def showusers(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'first_app/showusers.html', context=user_dict)

# Used for Ask for user info and update DB
def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print('Haha')
        # if form is valid,save the form and take the user to the index page
        if form.is_valid():
            form.save(commit=True)
            return showusers(request)

        else:
            print('ERROR FORM INVALID')

    return render(request,'first_app/users.html',{'form':form})





def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do somthing code
            print("Validation Success!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(request,'first_app/form_page.html',{'form':form})


# Create your views here.
