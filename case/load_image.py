from ctypes import *

def load_image():
    dll = cdll.LoadLibrary(r'../x64/hd.dll')
    print(dll)

def main():
    load_image()

if __name__ == '__main__':
    main()