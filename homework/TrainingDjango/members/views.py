from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from members.forms import MemberForm
from .models import Member

def viewall(request):
  objs = Member.objects.filter(firstname__isnull=False, lastname__isnull=False).exclude(firstname='', lastname='')
  temp = loader.get_template('index.html')
  context = {
    'mymembers': objs,
  }
  return HttpResponse(temp.render(context, request))

def detail(request, id):
  obj = Member.objects.get(id=id)
  temp = loader.get_template('detail.html')
  context = {
    'mymember': obj,
  }
  return HttpResponse(temp.render(context, request))

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu thông tin thành viên vào cơ sở dữ liệu
            return redirect('view all members')  # Sau khi thêm thành công, chuyển hướng về trang danh sách thành viên
    else:
        form = MemberForm()

    return render(request, 'add_member.html', {'form': form})