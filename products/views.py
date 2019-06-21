from django.shortcuts import render

# Create your views here.


def product_list(request):
    return render(request, 'product_list.html')


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        app_name = request.POST['APP名称']
        intro = request.POST['介绍']
        url = request.POST['APP链接']
        iron = request.FILES['APP图标']
        image = request.FILES['大图']
        return render(request, 'publish.html')

