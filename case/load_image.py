from ctypes import *


def load_image():
    dll = cdll.LoadLibrary(r'../x64/hd.dll')        # 载入按标准的cdecl调用协议导出的函数
    # dll2 = windll.LoadLibrary(r'../x64/hd.dll')   #载入按stdcall调用协议调用其中的函数
    # dll3 = oledll.LoadLibrary(r'../x64/hd.dll')   #也按stdcall调用协议调用其中的函数，并假定函数返回的是Windows HRESULT错误代码，当调用失败时，自动根据代码甩出一个OSEroor异常
    print(dll)
    # 接口
    dll.fun_0()
    # 打开磁盘 HANDLE fun_1(BYTE dsk_num);
    dll.fun_1()
    # 打开一个存在的文件 HANDLE fun_2(LPCTSTR szName);
    dll.fun_2()
    # 总是创建一个新的文件 ANDLE fun_3(LPCTSTR szName);
    dll.fun_3()
    # 读扇区 DWORD fun_4(HANDLE hFile, PVOID pBuf, DWORD64 startBlock, DWORD blocks);
    dll.fun_4()
    # 写扇区 DWORD fun_5(HANDLE hFile, PVOID  pBuf, DWORD64 startBlock, DWORD blocks);
    dll.fun_5()
    # 读文件 DWORD fun_6(HANDLE hFile, DWORD64 offBytes, DWORD bytes, PVOID pBuf);
    dll.fun_6()
    # 写文件 DWORD fun_7(HANDLE hFile, DWORD64 offBytes, DWORD bytes, PVOID pBuf);
    dll.fun_7()
    # 磁盘镜像 DWORD fun_8(lpfn_callback_dsk_image lpfn, PDSK_IMAGE_PARAMETER_INFO pimgInfo);
    dll.fun_8()
    # 停止镜像 void fun_9(int nStatus); nstatus -停止参数:1-执行,2-暂停,3-停止
    dll.fun_9()
    # 通过盼复获取磁盘号 DWORD fun_10(BYTE &disk_num, BYTE disk_letter);
    dll.fun_10()
    # 磁盘数据擦除 DWORD fun_11(lpfn_callback_dsk_image lpfn,PDSK_FILL_SECTOR_INFO_EX pfsi_ex);
    dll.fun_11()


def main():
    load_image()

if __name__ == '__main__':
    main()
