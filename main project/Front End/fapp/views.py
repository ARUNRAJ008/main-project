from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about_us.html')

def admin_addAccount(request):
    return render(request, 'admin_addAccount.html')

def admin_database(request):
    return render(request, 'admin_database.html')

def admin_home(request):
    return render(request, 'admin_home.html')

def admin_event(request):
    return render(request, 'admin_event.html')

def admin_book(request):
    return render(request, 'admin_book.html')

def admin_db_client(request):
    return render(request, 'admin_db_client.html')

def admin_db_owner(request):
    return render(request, 'admin_db_owner.html')

def admin_db_tonment(request):
    return render(request, 'admin_db_tonment.html')

def login(request):
    return render(request, 'login.html')

def payment(request):
    return render(request, 'payment.html')

def profile_edit(request):
    return render(request, 'profile_edit.html')

def profile(request):
    return render(request, 'profile.html')

def profile_feedback(request):
    return render(request, 'profile_feedback.html')

def sigup(request):
    return render(request, 'sigup.html')

def slotBooking(request):
    return render(request, 'slotBooking.html')
def next(request):
    return render(request, 'next.html')
