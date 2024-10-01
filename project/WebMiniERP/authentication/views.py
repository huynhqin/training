from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from ldap3 import Server, Connection, ALL
from .forms import LoginForm

LDAP_SERVER = 'ldap://10.20.20.191'  
LDAP_BASE_DN = 'dc=acslab,dc=local'

def ldap_authenticate(username, password):
    try:
        # Kết hợp username với domain (vd: acslab.local)
        user_dn = f"{username}@acslab.local"
        
        # Tạo kết nối tới LDAP server
        server = Server(LDAP_SERVER, get_info=ALL)
        conn = Connection(server, user=user_dn, password=password)
        
        # Thực hiện bind để xác thực
        if conn.bind():
            # Nếu xác thực thành công, lấy thêm thông tin người dùng (tùy chọn)
            conn.search(
                search_base=LDAP_BASE_DN,
                search_filter=f"(sAMAccountName={username})",
                search_scope='SUBTREE',
                attributes=['cn', 'mail', 'givenName', 'sn']
            )

            if conn.entries:
                user_info = conn.entries[0]
                user_data = {
                    'username': username,
                    'full_name': user_info.cn.value,
                    'email': user_info.mail.value,
                    'first_name': user_info.givenName.value,
                    'last_name': user_info.sn.value
                }
                conn.unbind()
                return True, user_data
            else:
                conn.unbind()
                return True, None  # Xác thực thành công nhưng không lấy được thông tin người dùng
        else:
            return False, None
    except Exception as e:
        print(f"Lỗi: {e}")
        return False, None

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            is_authenticated, user_data = ldap_authenticate(username, password)
                         
            if is_authenticated:
                # try:
                #     # Kiểm tra nếu user đã tồn tại trong hệ thống
                #     user = User.objects.get(username=username)
                # except User.DoesNotExist:
                #     # Tạo user mới nếu chưa tồn tại, dùng thông tin từ LDAP
                #     user = User.objects.create(
                #         username=username,
                #         first_name=user_data['first_name'] if user_data else '',
                #         last_name=user_data['last_name'] if user_data else '',
                #         email=user_data['email'] if user_data else '',
                #     )
                
                #login(request, user)
                return redirect('dashboard')
            else:                
                return HttpResponse('Sai thông tin đăng nhập', status=401)
    else:
        form = LoginForm()
    
    return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
