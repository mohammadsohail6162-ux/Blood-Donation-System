# Blood/views.py - COMPLETE REPLACEMENT CODE
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import User, Donor, BloodRequest
from datetime import datetime

# 🏠 Home Page
def home(request):
    return render(request, 'Blood/index.html')

# ℹ️ About Page
def about(request):
    return render(request, 'Blood/about.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            
            if user.check_password(password):
                # ✅ FIX: Add backend explicitly
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request, f"Welcome back, {user.name}!")  # ✅ Success message
                return redirect('home')  # ✅ Redirect to HOME instead of profile
            else:
                messages.error(request, "Invalid password!")
                
        except User.DoesNotExist:
            messages.error(request, "No account found with this email!")
    
    return render(request, 'Blood/login.html')
# 📝 User Signup - SIMPLIFIED
def user_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Signup attempt: {name}, {email}")  # Debug

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
        else:
            try:
                user = User.objects.create_user(
                    email=email, 
                    name=name, 
                    password=password
                )
                messages.success(request, "Account created! Please login.")
                return redirect('user_login')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
    
    return render(request, 'Blood/signup.html')

# 👤 User Profile - ADD THIS
@login_required
def user_profile(request):
    return render(request, 'Blood/user_profile.html', {'user': request.user})

# 🚪 User Logout
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

# 🩸 Donor Registration
def donor_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        blood_group = request.POST.get('blood_group')
        email = request.POST.get('email')
        city = request.POST.get('city')
        
        Donor.objects.create(
            name=name, age=age, blood_group=blood_group,
            email=email, city=city
        )
        
        request.session['donor_name'] = name
        request.session['donation_date'] = datetime.now().strftime("%d %B, %Y")
        
        messages.success(request, 'Donor registered successfully! ❤️')
        return redirect('donor_success')
    
    return render(request, 'Blood/donor.html')

# ✅ Donor Success
def donor_success(request):
    return render(request, 'Blood/donor_success.html')

# 🏥 Blood Request
def blood_request(request):
    return render(request, 'Blood/request.html')

def submit_request(request):
    if request.method == 'POST':
        BloodRequest.objects.create(
            patient_name=request.POST.get('patient_name'),
            blood_group=request.POST.get('blood_group'),
            city=request.POST.get('city'),
            hospital_name=request.POST.get('hospital_name'),
            contact_number=request.POST.get('contact_number')
        )
        messages.success(request, "Blood request submitted!")
        return redirect('blood_request')
    return redirect('blood_request')

# 📜 Certificate
def certificate(request):
    context = {
        'donor_name': request.session.get('donor_name', 'Anonymous Donor'),
        'donation_date': request.session.get('donation_date', 'Unknown Date'),
    }
    return render(request, 'Blood/certificate.html', context)

# 👨‍💼 Admin Functions
def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username == "Mohammad Sohail" and password == "9801686031":
            request.session["isAdmin"] = True
            messages.success(request, "Admin login successful!")
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid admin credentials!")
    
    return render(request, "Blood/admin_login.html")

def admin_dashboard(request):
    if not request.session.get("isAdmin"):
        return redirect("admin_login")
    
    context = {
        'donors': Donor.objects.all(),
        'requests': BloodRequest.objects.all(),
        'inventory': [
            {'blood_group': 'A+', 'available_units': 15, 'total_donated': 45},
            {'blood_group': 'A-', 'available_units': 8, 'total_donated': 22},
            {'blood_group': 'B+', 'available_units': 12, 'total_donated': 38},
            {'blood_group': 'B-', 'available_units': 6, 'total_donated': 18},
            {'blood_group': 'AB+', 'available_units': 4, 'total_donated': 12},
            {'blood_group': 'AB-', 'available_units': 2, 'total_donated': 8},
            {'blood_group': 'O+', 'available_units': 20, 'total_donated': 55},
            {'blood_group': 'O-', 'available_units': 10, 'total_donated': 28},
        ]
    }
    return render(request, "Blood/admin.html", context)

def admin_logout(request):
    request.session.flush()
    messages.success(request, "Admin logged out!")
    return redirect('admin_login')
