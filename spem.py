import os, sys, json, os, sys, time
def cls():
	if os.name=="posix":
		os.system("clear")
	if os.name=="nt":
		os.system("cls")
try:
	import requests
except:
	print("Đang Cài Thư Viện Requests")
	os.system("pip install requests")
	print("\nĐã cài Xong Vui Lòng Chạy Lại Tools")
	exit()
try:
	import NongHoangVu
except:
	print("Đang Cài Thư Viện NongHoangVu")
	os.system("pip install NongHoangVu")
	print("\nĐã cài Xong Vui Lòng Chạy Lại Tools")
	exit()
from datetime import datetime, timedelta
from NongHoangVu import Center, Anime, Colors, Colorate
a="""\033[1;96m
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║                                    .::!!!!!!!:.    ║
    ║   .!!!!!:.                        .:!!!!!!!!!!!!   ║
    ║   ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$   ║
    ║       :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P   ║
    ║       $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#    ║
    ║       $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*      ║
    ║       ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"        ║
    ║         "*$bd$$$$      '*$$$$$$$$$$$o+#"           ║
    ║              ''''          '''''''                 ║
    ║           _____       _   _                        ║
    ║          |  __ \     | | | |                       ║
    ║          | |__) |___ | |_| |__  _   _              ║
    ║          |  _  // _ \| __| '_ \| | | |             ║
    ║          | | \ \ (_) | |_| |_) | |_| |             ║
    ║          |_|  \_\___/ \__|_.__/ \__, |             ║
    ║                                  __/ |             ║
    ║                                 |___/              ║
    ║ Copy nhớ ghi nguồn                                 ║
    ║ Zalo: 0843217283            Editor:Bùi Quang Hiệu  ║
    ╚════════════════════════════════════════════════════╝
    ============⟩⟩⟩⟩⟩⟩⟩ Tools Spam Momo ⟨⟨⟨⟨⟨⟨============\n\n   """
Anime.Fade(Center.Center(a), Colors.green_to_yellow, Colorate.Vertical, enter=True)
Anime.Fade(Center.Center(a), Colors.blue_to_red, Colorate.Vertical, enter=True)

cls()
print(a)
sđt=input("  \033[1;94mNhập SĐT: \033[1;95m")
if sđt=="0387640248":
	print("  \033[1;91m\n Ă à à thì ra mầy chọn cái chít :)))")
	exit()
stt=0
dem=0
while True:
	stt=stt+1
	tg = datetime.now().strftime("%H:%M")
	momo=requests.get(f"https://danganhduy.io/login-momo.php?phone={sđt}").json()
	viettelpay=requests.get(f"https://danganhduy.io/login-vtpay.php?phone={sđt}")
	if momo==0:
		print("  \033[1;91mSĐT này được chủ web bảo vệ")
		exit()
	status=momo["status"]
	msg=momo["msg"]
	if "success" in status:
		dem=dem+1
		print(f"  \033[1;95mMoMo \033[0m| \033[1;32mThành Công ", end="\r")
		time.sleep(1)
		print(f"  \033[1;96m{tg} \033[0m| \033[1;32mSTT: \033[1;96m{dem} \033[0m| \033[1;32mSĐT: \033[1;96m{sđt} \033[0m | \033[1;95mMoMo      ")
		print(f"  \033[1;95mViettelPay \033[0m| \033[1;32mThành Công", end="\r")
		time.sleep(1)
		print(f"  \033[1;96m{tg} \033[0m| \033[1;32mSTT: \033[1;96m{dem} \033[0m| \033[1;32mSĐT: \033[1;96m{sđt} \033[0m | \033[1;95mViettelPay")
	if "error" in status:
		print(f"  \033[1;91m{stt} \033[0m| SPAM Quá Nhanh, 1 Lúc Nữa Mới SEND ĐC", end="\r")
		continue