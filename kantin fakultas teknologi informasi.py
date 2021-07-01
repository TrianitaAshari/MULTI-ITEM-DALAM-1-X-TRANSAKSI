# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 12:32:24 2021

@author: trianita
"""

"""
Cek nilai Menggunakan Loop 
" Loop CEK Program Kantin Fakultas Teknologi Informasi
" loop run program (ok)
"""
#CEK Program 
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("===============================================")
    print("<<    KANTIN FAKULTAS TEKNOLOGI INFORMASI    >>")
    print("<<          CEK TRANSAKSI PEMBELIAN          >>")
    print("===============================================")
    print("--DAFTAR MENU MAKANAN dan MINUMAN : --")  
    print(" 1. Nasi Goreng          7. Teh dingin/hangat/panas ")
    print(" 2. Lontong Goreng       8. Kopi Dingin  ")
    print(" 3. Bakso Goreng         9. Kopi Teh Panas ")
    print(" 4. Rujak Goreng         10. Coca Cola Dingin ")
    print(" 5. Rujak Bakso          11. Coca cola Panas  ") 
    print(" 6. Rujak Bakso Pecel")
    print("______________________________________________________")
    
    #input nama pembeli    
    pembeli = input("Masukkan nama Pembeli: ")
    print ("Nama Pembeli :", pembeli) 
    
    #input dan hitung menu makanan
    menumakanan = ['Nasi goreng','Lontong goreng','Bakso goreng','rujak goreng','rujak bakso','rujak bakso pecel']
    Hargamakanan = [15000,14900,12900,13000,15000,17000]
    
    pilihan = input(">> Masukkan nomer untuk melihat menu makanan = ")
    #identifikasi pilihan
    if pilihan=="1":
        idx = 0
    elif pilihan=="2":
        idx = 1
    elif pilihan=="3":
        idx = 2
    elif pilihan=="4":
        idx = 3
    elif pilihan=="5":
        idx = 4        
    elif pilihan=="6":
        idx = 5 
    else:
        idx = 7
        print("----------------MENU TIDAK TERDAFTAR---------------------")
        print(">>>           Masukan MENU Yang Sesuai           <<<")  
        
   #cetak tampilan layar
    print(">>> Menu makanan = " + menumakanan[idx])
    print(">>> Harga menu makanan = Rp " + str(Hargamakanan[idx])) 
    makananygdibeli = menumakanan[idx]
    #input porsi makanan
    jumlahporsi=int(input("masukan jumlah porsi makanan yang dibeli = " ))  
    
    #hitung transksi
    Hargamakanan = Hargamakanan[idx]
    total1 = Hargamakanan * jumlahporsi
    #tampilkan total Harga
    print(">>> Total Harga     = Rp " + str(total1))  
          
    #input minuman dan harga minuman
    menuminuman =['teh dingin','kopi dingin','kopi teh panas','Coca cola dingin','Coca cola panas'] 
    hargaminuman =[2500,5000,6500,3500,5000]
    
    pilihan = input(">> Masukkan nomer untuk melihat menu minuman = ")
    #identifikasi pilihan
    if pilihan=="7":
        idx = 0
    elif pilihan=="8":
        idx = 1
    elif pilihan=="9":
        idx = 2
    elif pilihan=="10":
        idx = 3
    elif pilihan=="11":
        idx = 4        
    else:
        idx = 6
        print("----------------MENU TIDAK TERDAFTAR---------------------")
        print(">>>           Masukan MENU Yang Sesuai           <<<") 
        
     #cetak tampilan layar
    print(">>> Menu Minuman = " + menuminuman[idx])
    print(">>> Harga Minuman = Rp " + str(hargaminuman[idx])) 
    
    #input jumlah gelas
    jumlahgelas=int(input("masukan jumlah gelas yang dibeli = " ))  
    #hitung transksi
    hargaminuman = hargaminuman[idx]
    total2 = hargaminuman * jumlahgelas
    #tampilkan total Harga
    print(">>> Total Harga     = Rp " + str(total2)) 
    
    #hitung total semua
    totalsemua= total1 + total2
    print("Total yang harus Dibayar: Rp" + str(totalsemua))
    #pembayaran dan kembalian
    uangpembeli=int(input("Uang Tunai Pembeli: Rp "))
    kembalian= uangpembeli - totalsemua
    print("Kembalian :" + str(kembalian))
    
    print("============================================")
    print("=========  S T R U K   B E L I   ===========")
    print("============================================")
    print (" Nama                       :" + pembeli)
    print (" Menu makanan yang dibeli   :" + makananygdibeli)
    print (" Harga Makanan              :" + str(Hargamakanan))
    print (" jumlah makanan yang dibeli :" + str(jumlahporsi))
    print (" Total Harga Makanan        :" + str(total1))
    print (" Minuman yang dibeli        :" + menuminuman[idx])
    print (" Harga Minuman              :" + str(hargaminuman))
    print (" jumlah minuman yang dibeli :" + str(jumlahgelas))
    print ("  Total Harga Minuman       :" + str(total2))
    print ("_____________________________________________________+")
    print (" Tagihan                    : Rp." + str(totalsemua))
    print (" Uang                       : Rp." + str(uangpembeli))
    print (" Kembalian                  : Rp." + str(kembalian))
    print("=====================================================")
    print("=============   TERIMA KASIH  =======================")
   
    ulangprog = input(">> Cek Transaksi lagi ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break 
   
     
     
    
    