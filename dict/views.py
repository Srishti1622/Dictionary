from django.shortcuts import render

# Create your views here.
def homePage(request):
    if request.method=='POST':
        keyword=request.POST.get('keyword')
        print(keyword)
    return render(request,'dict/home.html',{})
