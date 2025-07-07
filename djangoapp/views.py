from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def get_dealerships(request):
    # dummy data for now
    dealerships = [
        {"id": 1, "full_name": "Badal Honda", "city": "Delhi", "state": "DL"},
        {"id": 2, "full_name": "Sunrise Motors", "city": "Mumbai", "state": "MH"},
    ]
    from django.http import JsonResponse
    return JsonResponse(dealerships, safe=False)
