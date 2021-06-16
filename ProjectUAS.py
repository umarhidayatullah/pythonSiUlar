#fungsi
def garis1():
    print(35*"-")
def garis2():
    print(73*"-")
def garis3():
    print(55*"-")
def daftar():
    #Input
    garis1()
    print("\tPembelian Playsation GameStop")
    garis1()
    print("kode.  Jenis PS    Storange")
    print("1.     PS3          1TB")
    print("2.     PS4          1TB")
    garis1()
    pilih = input("Masukkan Kode Yang Diinginkan : ")
    if pilih == '1':
        ps3()
    elif pilih == '2':
        ps4()
    else:
        print("Kode salah")
        daftar()
def ps3():
    #Input
    garis1()
    print("\t\tSilahkan Pilih PS3")
    garis1()
    print("Kode.  Jenis PS3           Harga")
    garis1()
    print("1.   PS3 Fat         Rp.1.500.000")
    print("2.   PS3 Slim        Rp.2.000.000")
    print("3.   PS3 SuperSlim   Rp.2.500.000")
    garis1()
    jnsps = input("Masukan Kode PS3 Yang Diingikan : ") 
    if jnsps == '1':
        ply = "PS3 Fat"
        harga = 2500000
    elif jnsps == "2":
        ply = "PS3 Slim"
        harga = 3000000
    elif jnsps == "3":
        ply = "PS3 SuperSlim"
        harga = 3500000
    else:
        print("kode salah")
        ps3()
    garis3()
    print("\t\t\tSilahkan Pilih Games PS3")
    garis3()
    print("Kode     Games                            Harga")
    garis3()
    print("1.   Grand Thef Auto V                 Rp.250.000")
    print("2.   The last Of US                    Rp.200.000")
    print("3.   Read Dead Redemption              Rp.270.000")
    print("4.   Grand Turismo 6                   Rp.190.000")
    print("5.   Need For Speed Most Wanted        Rp.150.000")
    garis3()
    ls_games = []
    ls_harga = []
    jnsgms = int(input("Jumlah Games Yang Ingin Dibeli : "))
    for data in range(jnsgms):
        print("Game Ke - :", data + 1)
        games = input("Masukkan Kode Games :")
        if games == "1":
            dgms = "Grand thef Auto V "
            hrggms = 250000
        elif games == '2':
            dgms = "The last Of Us "
            hrggms = 200000
        elif games == "3":
            dgms = 'Read Dead Redemption'
            hrggms = 270000
        elif games == "4":
            dgms = "Grand Turismo 6"
            hrggms = 190000
        elif games == "5":
            dgms = "Need For Speed Most Wanted"
            hrggms = 150000
        else:
            print("Kode salah")
            ps3()
        ls_games.append(dgms)
        ls_harga.append(hrggms)
    #Output
    garis2()
    print("\t\t\t\tDaftar Total Pembelian PS GameStop ")
    garis2()
    print("No.              Barang                    Harga       ")
    print('{0:^4} {1:<35} {2:>0}{3:<0}'.format(1,ply,"Rp.",format(round(harga), ',d')))
    garis2()
    print("                 Games                     Harga       ")
    garis2()
    for i in range(jnsgms):
        total_harga = (sum(ls_harga)) + harga
        if jnsgms > 2:
            total_tagihan = total_harga - (((sum(ls_harga)) + harga) * 0.2)
            disc = "20%"
        else:
            total_tagihan = (sum(ls_harga)) + harga
            disc = "0"
        print('{0:^4} {1:<35} {2:>0}{3:<0}'.format(i + 2, ls_games[i],"Rp.",format(round(ls_harga[i]),',d')))
    garis2()
    print("\t\t\t\t\t\t Total Beli    : Rp.",format(round(total_harga), ',d'))
    print("\t\t\t\t\t\t Discount      : "+ str(disc),)
    print("\t\t\t\t\t\t Total Bayar   : Rp.",format(round(total_tagihan), ',d'))
    garis2()
def ps4():
    #Input
    garis1()
    print("\t\tSilahkan Pilih PS4")
    garis1()
    print("Kode.  Jenis PS4           Harga")
    garis1()
    print("1.   PS4 Standart    Rp.3.000.000")
    print("2.   PS4 Slim        Rp.3.500.000")   
    print("3.   PS4 Pro         Rp.4.000.000")
    garis1()
    jnsps = input("Masukan Kode PS4 Yang Diingikan : ")
    if jnsps == '1':
        ply = "PS4 Standart"
        harga = 2500000
    elif jnsps == "2":
        ply = "PS4 Slim"
        harga = 3000000
    elif jnsps == "3":
        ply = "PS4 Pro"
        harga = 3500000
    else:
        print("kode salah")
        ps4()
    garis3()
    print("\t\tSilahkan Pilih Games PS4")
    garis3()
    print("Kode     Games                           Harga")
    garis3()
    print("1.   Death Stranding                   Rp.250.000")
    print("2.   Monster Hunter world Iceborne     Rp.600.000")
    print("3.   God Of War                        Rp.200.000")
    print("4.   Spiderman Miles Morales           Rp.700.000")
    print("5.   Assassin's Creed Valhalla         Rp.650.000")
    garis3()
    ls_games = []
    ls_harga = []
    jnsgms = int(input("Jumlah Games Yang Ingin Dibeli : "))
    for data in range(jnsgms):
        print("Game Ke - :", data + 1)
        games = input("Masukkan Kode Games :")
        if games == "1":
            dgms = "Death Stranding"
            hrggms = 250000
        elif games == '2':
            dgms = "Monster Hunter World Iceborne"
            hrggms = 600000
        elif games == "3":
            dgms = 'God Of War'
            hrggms = 200000
        elif games == "4":
            dgms = "Spiderman Miles Morales"
            hrggms = 700000
        elif games == "5":
            dgms = "Assassin's Creed Valhalla"
            hrggms = 650000
        else:
            print("Kode salah")
            ps4()
        ls_games.append(dgms)
        ls_harga.append(hrggms)
    #Output
    garis2()
    print("\t\t\t\t\tDaftar Total Pembelian PS GameStop ")
    garis2()
    print("No.              Barang                    Harga       ")
    garis2()
    print('{0:^4} {1:<35} {2:>0}{3:<0}'.format(1,ply,"Rp.",format(round(harga),',d')))
    garis2()
    print("                 Games                     Harga       ")
    garis2()
    total_harga = (sum(ls_harga)) + harga
    for i in range(jnsgms):
        if jnsgms>2:
            total_tagihan = total_harga - (((sum(ls_harga)) + harga) * 0.2)
            disc = "20%"
        else:
            total_tagihan = ((sum(ls_harga)) + harga)
            disc = "0"
        print('{0:^4} {1:<35} {2:>0}{3:<0}'.format(i+2,ls_games[i],"Rp.",format(round(ls_harga[i]), ',d')))
    garis2()
    print("\t\t\t\t\t\t\t  Total    : Rp.",format(round(total_harga),',d'))
    print("\t\t\t\t\t\t\t  Discount :",(disc))
    print("\t\t\t\t\t\t\t  Total    : Rp.",format(round(total_tagihan),',d'))
    garis2()
def ulang():
    ulg=input("Masukkan ulang ? [Y/N] :")
    if ulg == 'Y'or ulg == 'y':
        daftar()
        ulang()
    else:
        print('''"Terimakasih"''')
        exit()
#pemanggilan fungsi
daftar()
ulang()