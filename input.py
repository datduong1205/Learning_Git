your_name = input("Hay nhap ten:")
your_great= "Xin chao "

from time import sleep

for a in your_great+your_name:
    print(a, end='', flush=True)
    sleep(0.1)



print("\n__repr__method: %r" %your_name)
