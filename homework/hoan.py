mylist = [{"ID" : "5002447", "Name" : "Châu Thanh Hoán"}, {"ID" : "5007966", "Name" : "Phùng Nguyễn Đào Hoàng Anh"}, {"ID" : "5007872", "Name" : "Nguyễn Tấn Thành"}]

def menu():
    print("\n")
    print("***********************************")
    print("1. Xem danh sach nhan vien\n2. Tao nhan viên\n3. Cap nhat\n4. Xoa\n5. Thoat")
    print("***********************************")

def DSNV():
    for y in mylist:
            print(str((mylist.index(y))+1) + ". " + y['Name'] + " | " + y['ID'])

def create():
    i = 1
    while i == 1:
        print("\n")
        print("Nhập họ tên và mã nhân viên cần tạo:")
        stID = input('ID: ')
        stName = input('Name: ')
        print('\n=> ' + stID + " | " + stName)
        new_dict = {
            "ID" : stID, "Name" : stName
        }
        mylist.append(new_dict)
        q = input("\nTạo tiếp (Yes/No): ")
        if (q == "No"):
            break

def select():
    x = input('\nChọn mục cần thực hiện (0: Menu): ')
    if (x == '0'):
        menu()
    if (x == '1'):
        if(len(mylist) > 0):
            print("\n")
            DSNV()
        else:
            print("\nDanh sách trống!")
            q = input('\nBạn có muốn tạo nhân viên không?? (Yes/No): ')
            if(q == "Yes"):
                create()
            menu()
    elif (x == '2'):
        create()
    elif (x == '3'):
        print("\n")
        DSNV()
        y = input('\nNhập STT nhân viên cần cập nhật: ')
        i = int(y)-1
        uID = input("|" + mylist[i]["ID"] + "| => ")
        if(uID == ""):
            uID = mylist[int(y)]["ID"]
        uName = input("|" + mylist[i]["Name"] + "| => ")
        if(uName == ""):
            uName = mylist[i]["Name"]
        update_dict = {"ID" : uID, "Name" : uName}        
        mylist[i] = update_dict
    elif (x == '4'):
        print("\n")
        DSNV()
        y = input('\nNhập STT nhân viên muốn xóa: ')
        i = int(y)-1
        stName = mylist[i]["Name"]
        mylist.pop(i)
        print("\nĐã xóa nhân viên " + stName)
    elif (x == '5'):
        quit()
    select()

menu()
select()