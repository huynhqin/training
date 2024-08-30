NhanViens = []

def ContinueMethod():
    print("/---------------------------------/")    
    choice = input("Bạn có muốn tiếp tục không (y/n)? ")
    if choice.lower() == "y":
        return True
    else:
        return False

def CreateEmployee():
    print("/************************************/")
    print("Màn hình tạo nhân viên")
    while True:
        NhanVien = dict()
        id = int(input("Nhập id: "))
        ten = input("Nhập tên: ")
        NhanVien[id] = ten
        NhanViens.append(NhanVien)
        if not ContinueMethod():
            break

def ReadEmployee():
    print("***********************")
    print("* Danh sách nhân viên *")
    print(f"{'Mã số':<10} | {'Tên nhân viên'}")
    for nv in NhanViens:
        for id, ten in nv.items():
            print(f"{id:<10} | {ten}")        
    print("* Kết thúc danh sách  *")    

def UpdateEmployee():
    print("/************************************/")
    print("Màn hình cập nhật nhân viên")
    while True:        
        id = int(input("Nhập id: "))
        found = False
        for manv in NhanViens:
            if id in manv:
                tenmoi = input("Nhập tên mới: ")
                manv[id] = tenmoi
                found = True
                print(f"Nhân viên có mã số {id} đã được cập nhật.")
                break
        if not found:
            print("Không tồn tại nhân viên có mã số này!")
        if not ContinueMethod():
            break

def DeleteEmployee():
    print("/************************************/")
    print("Màn hình xóa nhân viên")
    while True:        
        id = int(input("Nhập id: "))
        found = False
        for manv in NhanViens:
            if id in manv:                
                NhanViens.remove(manv)
                found = True
                print(f"Nhân viên có mã số {id} đã được xóa.")
                break
        if not found:
            print("Không tồn tại nhân viên có mã số này!")
        if not ContinueMethod():
            break

choice = 0

while choice != 5:
    print("*********************************************")
    print("* Hãy chọn thao tác bạn muốn thực hiện      *")
    print("*   1. Tạo nhân viên                        *")
    print("*   2. Đọc toàn bộ nhân viên                *")
    print("*   3. Cập nhật thông tin nhân viên         *")
    print("*   4. Xóa thông tin nhân viên              *")
    print("*   5. Thoát chương trình                   *")
    print("*********************************************")
    choice = int(input("Nhập lựa chọn của bạn: "))
    if choice == 1:
        CreateEmployee()
    elif choice == 2:
        ReadEmployee()
    elif choice == 3: 
        UpdateEmployee()
    elif choice == 4:
        DeleteEmployee()
    elif choice == 5:
        exit()