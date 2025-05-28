from django.shortcuts import render

def home(request):
    # capture user_name from query params
    name = request.GET.get('user_name', '')  # default empty string
    return render(request, 'home.html', {
        'user_name': name
    })
