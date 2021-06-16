def tagihan(lamapakai):
    if (lamapakai > 5):
        return (5000*lamapakai)-(5000*lamapakai*0.1)
    else:
        return (5000*lamapakai)
def potongan(lamapakai):
    if (lamapakai > 5):
        return (5000*lamapakai*0.1)
    else:
        return 0
def garis():
    print("="*35)

j = "y"
while (j=="y"):
    jmldt=int(input("Jumlah Data: "))
    list_nokomp=[]
    list_namapakai=[]
    list_lamapakai=[]
    for i in range(jmldt):
        garis()
        print("       PROGRAM TAGIHAN WARNET")
        print("              KOMPUTER       ")
        garis()
        print("DATA KE: ", i + 1)
        nokomp    = input("Nomor Komputer       : ")
        list_nokomp.append(nokomp)
        namapakai = input("Nama Pemakai         : ")
        list_namapakai.append(namapakai)
        lamapakai = int(input("Lama Pakai (jam)     : "))
        list_lamapakai.append(lamapakai)
        garis()
        print("\n")


    print('=================================================================================')
    print("                         DAFTAR TAGIHAN WARNET KOMPUTER                          ")
    print('=================================================================================')
    print('   No    NoKomp   Nama Pakai      Lama Pakai       Potongan      Total Tagihan   ')
    print('=================================================================================')
    for data in range(jmldt):
        x = print('{:5}'.format(data + 1),'{:>10}'.format(list_nokomp[data]),'{:>12}'.format(list_namapakai[data]),'{:>15}'.format(list_lamapakai[data]),'{:>15}'.format(potongan(list_lamapakai[data])),'{:>15}'.format(tagihan(list_lamapakai[data])))
    print('=================================================================================')
    print("\n")

    j = input("ULANGI LAGI [y/t]?")
    if j == "t":
        j = input("ULANGI LAGI [y/t]?")

