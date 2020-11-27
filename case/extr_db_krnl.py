from ctypes import *

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


class POINT(Structure):
    _fields_ = [("x", c_int),
                ("y", c_int)]


class Test(Structure):
    pass
Test._fields_ = [('x', c_int),
                 ('y', c_char),
                 ('next', POINTER(Test))]


def mount_db_file():
    dll = cdll.LoadLibrary(r'../x64/extr_db_krnl.dll')      # 载入按标准的cdecl调用协议导出的函数
    db_name = c_wchar_p('../data/debug/student.ibd')
    db_type = 0x0A01
    err = None
    dll.extr_db_fun_A.restype = c_long
    db_fh = pointer(c_long(1))
    print(db_fh)
    db_fh = dll.extr_db_fun_A(db_name, db_type, id(err))    # id()函数用于获取对象的内存地址
    print(err)
    print('HANDLE =', db_fh)
    print(type(db_fh))


def main():
    mount_db_file()

if __name__ == '__main__':
    main()
