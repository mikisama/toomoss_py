"""
文件说明：USB2XXX BMM_LIN操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *

# 定义函数返回错误代码
BMM_LIN_SUCCESS            = (0)   #函数执行成功
BMM_LIN_ERR_NOT_SUPPORT    = (-1)  #设备不支持该函数
BMM_LIN_ERR_USB_WRITE_FAIL = (-2)  #USB发送数据错误
BMM_LIN_ERR_USB_READ_FAIL  = (-3)  #USB读取数据错误
BMM_LIN_ERR_CMD_FAIL       = (-4)  #命令执行失败
BMM_LIN_ERR_CH_NO_INIT     = (-5)  #当前通道未初始化
BMM_LIN_ERR_READ_DATA      = (-6)  #LIN读数据错误
BMM_LIN_ERR_PARAMETER      = (-7)  #函数传入参数错误
BMM_LIN_ERR_WRITE          = (-8)  #LIN发送数据错误
BMM_LIN_ERR_READ           = (-9)  #LIN读数据错误
BMM_LIN_ERR_RESP           = (-10) #数据响应错误
BMM_LIN_ERR_CHECK          = (-11) #数据校验错误

def BMM_LIN_Init(DevHandle,LINIndex,BaudRate):
    return USB2XXXLib.BMM_LIN_Init(DevHandle,LINIndex,BaudRate)
def BMM_LIN_SetPara(DevHandle, LINIndex,BreakBits, InterByteSpaceUs, BreakSpaceUs):
    return USB2XXXLib.BMM_LIN_SetPara(DevHandle, LINIndex,BreakBits, InterByteSpaceUs, BreakSpaceUs)
def BMM_LIN_WriteData(DevHandle,LINIndex,pData, Len):
    return USB2XXXLib.BMM_LIN_WriteData(DevHandle,LINIndex,pData, Len)
def BMM_LIN_ReadData(DevHandle,LINIndex,pData):
    return USB2XXXLib.BMM_LIN_ReadData(DevHandle,LINIndex,pData)
def BMM_LIN_WaitDataNum(DevHandle,LINIndex,DataNum,TimeOutMs):
    return USB2XXXLib.BMM_LIN_WaitDataNum(DevHandle,LINIndex,DataNum,TimeOutMs)
