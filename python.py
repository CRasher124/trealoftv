from time import * 
print("""

 _            _  _          _                      _          __  _   
| |__    ___ | || |  ___   | |_  _ __  ___   __ _ | |  ___   / _|| |_ 
| '_ \  / _ \| || | / _ \  | __|| '__|/ _ \ / _` || | / _ \ | |_ | __|
| | | ||  __/| || || (_) | | |_ | |  |  __/| (_| || || (_) ||  _|| |_ 
|_| |_| \___||_||_| \___/   \__||_|   \___| \__,_||_| \___/ |_|   \__|

""")


target = input("just show my target:")
print("-----------------------------------")

if target == "":
    print("you have to do something instead of login")

sayac = 0
for k in target:
    if k == " ":
        sayac += 1
    harf_sayisi = len(target)-sayac

if harf_sayisi > 3 and harf_sayisi < 17:

    print("[*]https://instagram.com/",target,'/',sep="")
    sleep(1)
    print("[*]https://facebook.com/",target,'/',sep="")
    
          
else:
    print("you entered the wrong string")
