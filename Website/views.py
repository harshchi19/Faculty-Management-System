from django.shortcuts import render
import sqlite3
from django.http import JsonResponse

Email = ''
Passwords = ''
Username = ''
context = {}

def index(request):
    global Email, Passwords, Username, context
    if request.method == 'POST':
        m = sqlite3.connect('db.sqlite3')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                Email = value
            if key == 'password':
                Passwords = value
        c = "Select * from Login where Email=? and Passwords=?"
        cursor.execute(c, (Email, Passwords))
        row = cursor.fetchone()
        if row is not None:
            Username = row[0]
            context = {
                'Username': Username,
                'variable2': 'IT'
            }
            return JsonResponse({'success': True})
        else:
            error_message = "Incorrect email or password. Please try again."
            return JsonResponse({'success': False, 'error_message': error_message})
    return render(request, 'index.html')


def profile(request):
    global context
    return render(request, 'profile.html', context)

def manage(request):
    global context
    return render(request, 'manage.html', context)
