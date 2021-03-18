from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dob=request.POST['dob']
        email=request.POST['email']
        phone=request.POST['Phone']
        age=request.POST['Age']
        gender=request.POST['gender']
        father_name=request.POST['fathername']
        father_citizen_number=request.POST['fathercitizenshipnumber']
        grand_father_name = request.POST['grandfather']
        fathercitizenship=request.POST['fathercitizenship']



    else:
        return render(request,'pages/index.html')