from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView

from forms import AddStudentForm



# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        auth_user = User.objects.create_user(username,email)
        auth_user.pass1 = pass1
        auth_user.phone = phone


        auth_user.save()

        messages.success(request, "Your Account has been Successfully Created.")


        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = authenticate(request, username=request.POST.get('email'), password=request.POST.get('pass1'))
        # user = authenticate(email=email,pass1=pass1)

        # if user is not None:
        #     login(request, user)
        #     username = user.username
        #     return render(request, "authentication/index.html", {'username':username})
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Student Login")
                return redirect('student_home')
            else:
                messages.error(request, "Invalid Login!")
                return redirect('signin')
        
        # else:
        #     messages.error(request, "Bad Credentials")
        #     return redirect('home')

    # return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.successs(request, "Logged Out Successfully!")
    return redirect('home')


# to register
def register(request):
    return render(request, '/authentication/signup.html')

class student_register(CreateView):
    model = User
    form_class = AddStudentForm
    template_name = '/authentication/'




#     #my CRUD operations
# def index(request): #read data
#     shelf = Book.objects.all()
#     return render(request, 'athentication/dashboard.html', {'shelf': shelf})

# def upload(request):#create data
#     upload = BookCreate()
#     if request.method == 'POST':
#         upload = BookCreate(request.POST, request.FILES)
#         if upload.is_valid():
#             upload.save()
#             return redirect('index')
#         else:
#             return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
#     else:
#         return render(request, 'book/upload_form.html', {'upload_form':upload})

# def update_book(request, book_id):#update data
#     book_id = int(book_id)
#     try:
#         book_sel = Book.objects.get(id = book_id)
#     except Book.DoesNotExist:
#         return redirect('index')
#     book_form = BookCreate(request.POST or None, instance = book_sel)
#     if book_form.is_valid():
#        book_form.save()
#        return redirect('index')
#     return render(request, 'book/upload_form.html', {'upload_form':book_form})

# def delete_book(request, book_id):#delete data
#     book_id = int(book_id)
#     try:
#         book_sel = Book.objects.get(id = book_id)
#     except Book.DoesNotExist:
#         return redirect('index')
#     book_sel.delete()
#     return redirect('index')