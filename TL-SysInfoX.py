import os
import platform
import subprocess
import pyfiglet

def tampilkan_logo():
    logo = pyfiglet.figlet_format("TL-SysInfoX")
    print(logo)

def tampilkan_info_jaringan():
    print("Informasi Jaringan:")
    print(os.popen("ip addr show").read())

def tampilkan_info_keamanan():
    print("Informasi Keamanan:")
    print("Password:", os.popen("passwd -S").read())

def tampilkan_info_sistem():
    print("Informasi Sistem:")
    print("CPU:", os.popen("cat /proc/cpuinfo").read())
    print("Memori:", os.popen("cat /proc/meminfo").read())
    print("Penyimpanan:", os.popen("df -h").read())

def tampilkan_info_penyimpanan_termux():
    print("Informasi Penyimpanan Termux:")
    print("Penyimpanan yang digunakan:", os.popen("du -sh /data/data/com.termux/files").read())
    print("Penyimpanan yang tersedia:", os.popen("df -h /data/data/com.termux/files").read())

def atur_ip_address():
    interface = input("Masukkan nama interface (contoh: wlan0): ")
    ip_address = input("Masukkan IP address yang ingin diatur (contoh: 192.168.1.100/24): ")
    subprocess.run(["ip", "addr", "add", ip_address, "dev", interface])

def memindai_port():
    host = input("Masukkan host yang ingin dipindai (contoh: 192.168.1.1): ")
    subprocess.run(["nmap", host])

def atur_jaringan():
    while True:
        print("Atur Jaringan:")
        print("1. Atur IP Address")
        print("2. Memindai Port")
        print("3. Kembali")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            atur_ip_address()
        elif pilihan == "2":
            memindai_port()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid")

def main():
    tampilkan_logo()
    while True:
        print("TL-SysInfoX")
        print("1. Informasi Jaringan")
        print("2. Informasi Keamanan")
        print("3. Informasi Sistem")
        print("4. Informasi Penyimpanan Termux")
        print("5. Atur Jaringan")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_info_jaringan()
        elif pilihan == "2":
            tampilkan_info_keamanan()
        elif pilihan == "3":
            tampilkan_info_sistem()
        elif pilihan == "4":
            tampilkan_info_penyimpanan_termux()
        elif pilihan == "5":
            atur_jaringan()
        elif pilihan == "6":
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
