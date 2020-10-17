from D1mini import *
while True:
    if polsador():
        print("El boto esta premut.")
    else:
        print("El boto no esta premut.")
    time.sleep(1)
