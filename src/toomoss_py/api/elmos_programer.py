"""
文件说明：USB2XXX LIN ELMOS芯片烧写操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *


# 函数返回错误代码定义
ELMOS_SUCCESS            = 0     # 函数执行成功
ELMOS_ERR_OPEN_DEV       = -1    # 打开设备失败
ELMOS_ERR_INIT_DEV       = -2    # 初始化设备失败
ELMOS_ERR_FILE_FORMAT    = -3    # 传入文件格式错误
ELMOS_ERR_BEGIN_PROG     = -4    # 开始编程出错
ELMOS_ERR_CMD_FAIL       = -5    # 命令执行失败
ELMOS_ERR_PRG_FAILD      = -6    # 编程失败
ELMOS_ERR_FIND_CHIP      = -7    # 寻找芯片失败

def ELMOS_SetSpeed (DeviceHandle, LINChannel, SpeedHz):
    return USB2XXXLib.ELMOS_SetSpeed (DeviceHandle, LINChannel, SpeedHz)

def ELMOS_StartProg (DeviceHandle, LINChannel,AppFileName):
    return USB2XXXLib.ELMOS_StartProg (DeviceHandle, LINChannel,AppFileName)
    

