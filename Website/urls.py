from django.shortcuts import render
import sqlite3
from django.http import JsonResponse
import binascii
import base64
from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse

Email = ''
First_name = ''
Last_name = ''
Designation = ''
Department = ''
Joining_Date = ''
Institution = ''
Contact = ''
Qualification = ''
Experience = ''
Profile_Image_base64 = ''
TimeTable_base64 = ''
main = ''
context = {}

def index(request):
    global context,Username,Email
    Email = ''
    Username = ''
    context = {}
    return render(request, 'index.html')

def choice(request):
    return render(request, 'choice.html')

def meetourteam(request): 
    return render(request, 'meetourteam.html')

def institute_login(request): 
    return render(request, 'institute_login.html')

def welcome(request): 
    return render(request, 'welcome.html')

def reachus(request): 
    return render(request, 'reachus.html')


def login_faculty(request):
    global context,Email,First_name,Last_name,Designation,Department,Joining_Date,Institution,Contact,Qualification,Experience,Profile_Image
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * FROM login, faculty WHERE login.user_id=faculty.id AND Email=? AND Passwords=?"
        cursor.execute(query, (email, password))
        row = cursor.fetchone()
        if row is not None:
            Email = row[1]
            First_name = row[4]
            Last_name = row[5]
            Designation = row[6]
            Department = row[7]
            Joining_Date = row[8]
            Institution = row[9]
            Contact = row[10]
            Qualification = row[11]
            Experience = row[12]
            Profile_Image = row[13]
            Profile_Image_base64 = base64.b64encode(Profile_Image).decode('utf-8')
            cursor.close()
            # query = "SELECT * from TimeTable where Department=?;"
            # cursor.execute(query, (Department,))
            # row = cursor.fetchone()
            # if row is not None:
            #     TimeTable = row[1]
            #     TimeTable_base64 = base64.b64encode(TimeTable).decode('utf-8')
            context = {
                'Email' : Email,
                'First_name' : First_name,
                'Last_name' : Last_name,
                'Designation' : Designation,
                'Department' : Department,
                'Joining_Date' : Joining_Date,
                'Institution' : Institution,
                'Contact' : Contact,
                'Qualification' : Qualification,
                'Experience' : Experience,
                'Profile_Image' : Profile_Image_base64,
                
            }
            return JsonResponse({'success': True,'Designation': Designation})
        else:
            error_message = "Incorrect email or password. Please try again."
            return JsonResponse({'success': False, 'error_message': error_message})
    return render(request, 'login_faculty.html')

def profile_faculty(request):
    global context 
    return render(request, 'profile_faculty.html', context)

# def profile(request):
#     global context
#     return render(request, 'profile.html', context)

def timetable_faculty(request):
    global context, Department
    if request.method == 'GET' :
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * from TimeTable where Department=?;"
        cursor.execute(query, (Department,))
        row1 = cursor.fetchone()
        cursor.close()
        if row1 is not None:
            TimeTable = row1[1]
            TimeTable_base64 = base64.b64encode(TimeTable).decode('utf-8')
    return render(request, 'timetable_faculty.html', {'TimeTable': TimeTable_base64})
    
def create_leave_application(request):
    global context, Department,First_name ,Last_name
    if request.method == 'POST':
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "INSERT INTO Leave_Application (first_name, last_name, Department, description, start_date, end_date,status) VALUES (?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (First_name , Last_name, Department, description, start_date, end_date, 'Pending',))
        connection.commit()  # Commit the transaction
        return JsonResponse({'success': True})
    return render(request, 'create_leave_application.html')

def leave_application_faculty(request):
    global context, Department,main 
    if request.method == 'GET':
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * from Leave_Application where first_name=? And last_name=? And Department=?;"
        cursor.execute(query, (First_name, Last_name, Department))
        row2 = cursor.fetchone()
        main = [row2] + cursor.fetchall()  # Fetch remaining rows
        cursor.execute("PRAGMA table_info(Leave_Application)")
        columns = cursor.fetchall()
        num_columns = len(columns)
    elif request.method == 'POST':
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        status = request.POST.get("status")
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "DELETE From Leave_Application where first_name=? And last_name=? And Department=? And description=? And start_date=? And end_date=? And status=?  ;"
        cursor.execute(query, (First_name ,Last_name, Department, description, start_date, end_date,status))
        connection.commit()
        row2 = cursor.fetchone()
        main = [row2] + cursor.fetchall()
        print(main)
        return JsonResponse({'success': True})
    return render(request, 'leave_application_faculty.html', {'main': main})

def tools_faculty(request):
    return render(request, 'tools_faculty.html')

def chatroom_faculty(request):
    return render(request, 'chatroom_faculty.html')




def profile_hod(request):
    global context 
    return render(request, 'profile_hod.html', context)

def leave_application_hod(request):
    global context, Department,main 
    if request.method == 'GET':
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * from Leave_Application where Department=? And status=?;"
        cursor.execute(query, ( Department,'Pending'))
        row2 = cursor.fetchone()
        main = [row2] + cursor.fetchall()  # Fetch remaining rows
        cursor.execute("PRAGMA table_info(Leave_Application)")
        columns = cursor.fetchall()
        num_columns = len(columns)
    elif request.method == 'POST':
        first_name  = request.POST.get("first_name")
        last_name  = request.POST.get("last_name")
        description = request.POST.get("description")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        status = request.POST.get("status")
        print(status,first_name,last_name,description,start_date,end_date)
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "Update Leave_Application Set status=? where first_name=? And last_name=? And Department=? And description=? And start_date=? And end_date=?;"
        cursor.execute(query, (status, first_name ,last_name, Department, description, start_date, end_date))
        connection.commit()
        return JsonResponse({'success': True})
    return render(request, 'leave_application_hod.html', {'main': main})

def timetable_hod(request):
    global context, Department
    if request.method == 'GET' :
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        query = "SELECT * from TimeTable where Department=?;"
        cursor.execute(query, (Department,))
        row1 = cursor.fetchone()
        cursor.close()
        if row1 is not None:
            TimeTable = row1[1]
            TimeTable_base64 = base64.b64encode(TimeTable).decode('utf-8')
    return render(request, 'timetable_hod.html', {'TimeTable': TimeTable_base64})

def chatroom_hod(request):
    return render(request, 'chatroom_hod.html')

def tools_hod(request):
    return render(request, 'tools_hod.html')

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
