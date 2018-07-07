from django.shortcuts import render,HttpResponse

# Create your views here.
import datetime
from blog import models
def cur_time(request):
    # print(request)
    # return HttpResponse("<h1>ok</h1>")
    times = datetime.datetime.now()
    return render(request,'cur_time.html',{"abc":times})#render渲染一下界面

user_list = []
def userInfo(req):
    if req.method == 'POST':
        u = req.POST.get("username",None)
        s = req.POST.get("sex",None)
        e = req.POST.get("email", None)
        # user = {"username":username,"sex":sex,"email":email}
        # user_list.append(user)
        # print(username)
        # print(sex)
        # print(email)
        models.UserInfo.objects.create(
            username=u,
            sex=s,
            email=e
        )
    user_list = models.UserInfo.objects.all()
        # return render(req,"index.html",{"user_list":user_list})
        # {"user_list": user_list}
    return render(req,"index.html",{"user_list": user_list},)