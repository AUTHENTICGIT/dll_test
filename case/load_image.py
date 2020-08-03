from ctypes import *

def load_image():
    dll = cdll.LoadLibrary(r'../x64/hd.dll')        # 载入按标准的cdecl调用协议导出的函数
    # dll2 = windll.LoadLibrary(r'../x64/hd.dll')   #载入按stdcall调用协议调用其中的函数
    # dll3 = oledll.LoadLibrary(r'../x64/hd.dll')   #也按stdcall调用协议调用其中的函数，并假定函数返回的是Windows HRESULT错误代码，当调用失败时，自动根据代码甩出一个OSEroor异常
    print(dll)
    print(dll.fun_0)

def main():
    load_image()

if __name__ == '__main__':
    main()