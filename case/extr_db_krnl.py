from ctypes import *
from ctypes.wintypes import *

'''*****************************************************************************************************************
    被测数据库：      SQL Server 2017 /MySQL5.7

    测试数据准备：

    被测模块：        文件模式

    接口：
                    # 装载数据库文件接口
                    HANDLE extr_db_fun_A(wchar_t *db_name, DWORD db_type, DWORD &err, HANDLE hSnapshot = nullptr, wchar_t *fSampleDb = nullptr);
    参数：
                    db_name     # 数据库路径
                    db_type     # 数据库类型
                    err         # 【输出】错误码
                    nullptr     # 文件快照句柄（结构化存储进度及解析结果）
                    fSampleDb   # 样本数据库，默认情况可以不传
    返回：
                    数据库装载句柄
*****************************************************************************************************************'''


def mount_db_file():
    dll = windll.LoadLibrary(r'../x64/extr_db_krnl.dll')       # 载入按stdcall调用协议调用其中的函数
    db_name = r'C:\\Users\\XLY_LR\\PycharmProjects\\dll_test\\data\\debug\\score.ibd'
    db_type = 0x0A01
    err = c_ulong()
    dll.extr_db_fun_A.argtypes = [c_wchar_p, DWORD, POINTER(DWORD)]
    dll.extr_db_fun_A.restype = HANDLE
    db_fh = dll.extr_db_fun_A(db_name, db_type, byref(err))    # byref()函数用于获取对象的内存地址，db_fh是<class 'int'>

    # dll = cdll.LoadLibrary(r'..\x64\extr_db_krnl.dll')  # 载入按标准的cdecl调用协议导出的函数
    # db_name = c_wchar_p(r'..\data\debug\score.ibd')
    # db_type = DWORD(0x0A01)
    # err = c_ulong()
    # db_fh = HANDLE(dll.extr_db_fun_A(db_name, db_type, byref(err)))    # byref()函数用于获取对象的内存地址，db_fh是<class 'ctypes.c_void_p'>

    # dll = cdll.LoadLibrary(r'..\x64\extr_db_krnl.dll')  # 载入按标准的cdecl调用协议导出的函数
    # db_name = r'..\data\debug\score.ibd'
    # db_type = 0x0A01
    # err = c_ulong()
    # db_fh = HANDLE(dll.extr_db_fun_A(db_name, db_type, byref(err)))    # id()函数用于获取对象的内存地址，db_fh是<class 'ctypes.c_void_p'>

    print(err)
    print('HANDLE =', db_fh)
    print(type(db_fh))


def main():
    mount_db_file()

if __name__ == '__main__':
    main()
