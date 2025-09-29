"""
文件说明：USB2DIO操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *

# 函数返回值错误定义
DIO_SUCCESS             =(0)   # 函数执行成功
DIO_ERR_NOT_SUPPORT     =(-1)  # 适配器不支持该函数
DIO_ERR_USB_WRITE_FAIL  =(-2)  # USB写数据失败
DIO_ERR_USB_READ_FAIL   =(-3)  # USB读数据失败
DIO_ERR_CMD_FAIL        =(-4)  # 命令执行失败
DIO_ERR_ARG             =(-5)  # 传入函数参数异常

# DIO引脚定义
DIO_PIN_LIN1    = 0x0001
DIO_PIN_LIN2    = 0x0002
DIO_PIN_LIN3    = 0x0004
DIO_PIN_LIN4    = 0x0008
DIO_PIN_DI0     = 0x0010
DIO_PIN_DI1     = 0x0020
DIO_PIN_DI2     = 0x0040
DIO_PIN_DI3     = 0x0080
DIO_PIN_DO0     = 0x0100
DIO_PIN_DO1     = 0x0200
DIO_PIN_DO2     = 0x0400
DIO_PIN_DO3     = 0x0800

# 初始化DIO,将对应引脚初始化为DIO功能
def DIO_Init(DevHandle, PinMask):
    return USB2XXXLib.DIO_Init(DevHandle, PinMask)

# 控制DIO引脚输出高电平
def DIO_SetPins(DevHandle, PinMask):
    return USB2XXXLib.DIO_SetPins(DevHandle, PinMask)

# 控制DIO引脚输出低电平
def DIO_ResetPins(DevHandle, PinMask):
    return USB2XXXLib.DIO_ResetPins(DevHandle, PinMask)

# 设置PWM相位参数值
def DIO_ReadPins(DevHandle, PinMask):
    return USB2XXXLib.DIO_ReadPins(DevHandle, PinMask)


