from django.shortcuts import render



# View Functions:

# Home
def home(request):
    return render(request, 'home.html')

