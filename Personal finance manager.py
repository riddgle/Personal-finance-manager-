danh_sach_giao_dich=[]
def menu():
    print("==========PERSONAL FINANCIAL MANAGER==========")
    print("1. Them giao dich")
    print("2. Xem tat ca giao dich")
    print("3. Xem tong thu")
    print("4.Xem tong chi")
    print("5. Xem so du")
    print("6.Xoa giao dich")
    print("0.Thoat")
def nhap_lua_chon():
    while True:
        try:
            lua_chon=int(input("Chon mot so:"))
            return lua_chon
        except:
            print('Vui long nhap so:')
menu()
def tao_giao_dich():
    giao_dich= {
    "ngay": input("Nhap ngay:"),
    "loai":input("Nhap loai(thu/chi)"),
    "danh muc": input("Nhap danh muc:"),
    "noi dung":input("Nhap noi dung:"),
    "so tien":int(input("Nhap so tien:")),
    "dia diem":input("Nhap dia diem:"),
    }
    return giao_dich
    
def them_giao_dich():
    giao_dich_chinh= tao_giao_dich()
    danh_sach_giao_dich.append(giao_dich_chinh)
    print(danh_sach_giao_dich)
def xem_giao_dich():
    for giao_dich in danh_sach_giao_dich:
       print("========DANH SACH GIAO DICH========")
       print(giao_dich["ngay"])
       print(giao_dich["loai"])
       print(giao_dich["danh muc"])
       print(giao_dich["noi dung"])
       print(giao_dich["so tien"])
       print(giao_dich["dia diem"])
       print("==============================")
def xem_tong_thu():
    tong_thu=0
    for giao_dich in danh_sach_giao_dich:
        if giao_dich["loai"]=="thu":
            tong_thu += giao_dich["so tien"]
    return tong_thu
def xem_tong_chi():
    tong_chi=0
    for giao_dich in danh_sach_giao_dich:
        if giao_dich["loai"]=="chi":
            tong_chi += giao_dich["so tien"]
    return tong_chi
def xem_so_du():
    tong_thu=xem_tong_thu()
    tong_chi=xem_tong_chi()
    so_du= tong_thu - tong_chi  
    print("so_du:", so_du)
def  xoa_giao_dich():
    if len(danh_sach_giao_dich) == 0:
        print("Chua co giao dich de xoa!")
        return
    for stt, giao_dich in enumerate(danh_sach_giao_dich,1):
        print(stt,giao_dich["danh muc"],giao_dich["so tien"])
    stt_can_xoa= int(input("Nhap stt can xoa:"))
    if stt_can_xoa>=1 and stt_can_xoa<=len(danh_sach_giao_dich):
        danh_sach_giao_dich.pop(stt_can_xoa - 1)
        print("Da xoa giao dich!")
    else:
        print("stt khong hop le!")
lua_chon=nhap_lua_chon()
while lua_chon!=0:
    if lua_chon==1:
        them_giao_dich()
    elif lua_chon==2:
        xem_giao_dich()
    elif lua_chon==3:
        print(xem_tong_thu())
    elif lua_chon==4:
        print(xem_tong_chi())
    elif lua_chon==5:
        xem_so_du()
    elif lua_chon==6:
        xoa_giao_dich()
    else:
        print("Vui long chon lai")
    try:
        lua_chon=int(input("Chon mot so:"))
    except:
        print("Vui long chon so!")
if lua_chon==0:
   print("Thanks for using the app")

                
            
    
       
        
        
        
    
