from appTwo.models import User
from django.shortcuts import render
from appTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'frst_app/index.html')


def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("error form invalid")
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    # return render(request,'frst_app/users.html',context=user_dict)
    #render(request, 'frst_app/users.html',context=user_dict)
    return  render(request,'frst_app/users.html',{'form':form})


    #user_list = User.objects.order_by('first_name')
    #user_dict = {'users':user_list}
    #return render(request,'frst_app/users.html',context=user_dict)
