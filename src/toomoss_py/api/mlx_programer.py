"""
文件说明：USB2XXX LIN MLX芯片烧写操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *

# 函数返回错误代码定义
MLX_SUCCESS            = 0     # 函数执行成功
MLX_ERR_OPEN_DEV       = -1    # 打开设备失败
MLX_ERR_INIT_DEV       = -2    # 初始化设备失败
MLX_ERR_FILE_FORMAT    = -3    # 文件格式错误
MLX_ERR_BEGIN_PROG     = -4    # 开始编程失败
MLX_ERR_CMD_FAIL       = -5    # 函数执行失败
MLX_ERR_WRITE_FLASH    = -6    # 写数据到FLASH失败

def MLX_ProgInit(DeviceHandle, LINChannel,BaudRateOfKbps,UseFastLIN):
    return USB2XXXLib.MLX_ProgInit(DeviceHandle, LINChannel,BaudRateOfKbps,UseFastLIN)

def MLX_ProgNVRAM (DeviceHandle, LINChannel, nvramFileName, nad):
    return USB2XXXLib.MLX_ProgNVRAM (DeviceHandle, LINChannel, nvramFileName, nad)

def MLX_ProgFlash (DeviceHandle, LINChannel, LoaderFileName, AppFileName, nad):
    return USB2XXXLib.MLX_ProgFlash (DeviceHandle, LINChannel, LoaderFileName, AppFileName, nad)


