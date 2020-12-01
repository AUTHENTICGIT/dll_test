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
    接口：
                    # 装载数据库文件接口
                    void extr_db_fun_B(HANDLE &hMntDB);
    参数：
                    hMntDB      # 数据库装载句柄
    返回：
                    无
*****************************************************************************************************************'''


class MountAndUnmount:
    def __init__(self):
        self.dll = windll.LoadLibrary(r'../x64/extr_db_krnl.dll')   # 载入按stdcall调用协议调用其中的函数
        self.db_name = r'C:\Users\XLY_LR\PycharmProjects\dll_test\data\debug\score.ibd'
        self.db_type = 0x0A01
        self.err = DWORD(111)
        self.db_fh = HANDLE()

    def mount(self):
        # 第一种：argtypes\regtype独立声明实参、返回值为wintypes类型，句柄类型int（绝对路径句柄较长）
        # TODO: 路径不存在也返回句柄
        # dll = windll.LoadLibrary(r'../x64/extr_db_krnl.dll')       # 载入按stdcall调用协议调用其中的函数
        # db_name = r'C:\\Users\\XLY_LR\\PycharmProjects\\dll_test\\data\\debug\\score.ibd'
        # db_type = 0x0A01
        # err = DWORD(111)
        self.dll.extr_db_fun_A.argtypes = [c_wchar_p, DWORD, POINTER(DWORD)]
        self.dll.extr_db_fun_A.restype = HANDLE
        self.db_fh = self.dll.extr_db_fun_A(self.db_name, self.db_type, byref(self.err))    # byref()函数用于获取对象的内存地址，db_fh是<class 'int'>，用pointer()也可

        # 第二种：跟函数使用过程一起转换全部实参、返回值为wintypes的类型，句柄类型ctypes.c_void_p
        # TODO: 路径不存在也返回句柄，无法写卸载
        # dll = cdll.LoadLibrary(r'..\x64\extr_db_krnl.dll')  # 载入按标准的cdecl调用协议导出的函数
        # db_name = c_wchar_p(r'..\data\debug\score.ibd')
        # db_type = DWORD(0x0A01)
        # err = c_ulong()
        # db_fh = HANDLE(dll.extr_db_fun_A(db_name, db_type, byref(err)))    # byref()函数用于获取对象的内存地址，db_fh是<class 'ctypes.c_void_p'>

        # 第三种：只声明实参err、返回值为wintypes类型，句柄类型ctypes.c_void_p
        # TODO: 路径不存在也返回句柄，无法写卸载
        # dll = cdll.LoadLibrary(r'..\x64\extr_db_krnl.dll')  # 载入按标准的cdecl调用协议导出的函数
        # db_name = r'..\data\debug\score.ibd'
        # db_type = 0x0A01
        # err = c_ulong()
        # db_fh = HANDLE(dll.extr_db_fun_A(db_name, db_type, byref(err)))

        # 第四种：argtypes\regtype独立声明实参、返回值为wintypes类型，句柄类型int（相对路径句柄较短、有负值）
        # TODO: 路径不存在也返回句柄，无法写卸载
        # dll = cdll.LoadLibrary(r'../x64/extr_db_krnl.dll')       # 载入按cdecl调用协议调用其中的函数
        # db_name = r'..\data\debug\score.ibd'
        # db_type = 0x0A01
        # err = c_ulong()
        # db_fh = dll.extr_db_fun_A(db_name, db_type, byref(err))

        print('ERROR = ', self.err)
        print('HANDLE =', self.db_fh)
        print(type(self.db_fh))
        print("Mount Success!")
        return self.err, self.db_fh

    def unmount(self):
        self.dll.extr_db_fun_B.argtypes = [POINTER(HANDLE)]
        self.dll.extr_db_fun_B(byref(HANDLE(self.db_fh)))
        print("Unmount Success!")


def main():
    m = MountAndUnmount()
    err, db_fh = m.mount()
    print(db_fh)
    m.unmount()


if __name__ == '__main__':
    main()
