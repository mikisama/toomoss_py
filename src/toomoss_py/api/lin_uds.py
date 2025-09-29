"""
文件说明：USB2XXX LIN UDS操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *

# CAN UDS地址定义
class LIN_UDS_ADDR(Structure):
    _fields_ = [
        ("ReqID",c_ubyte),       # 请求报文ID。
        ("ResID",c_ubyte),       # 应答报文ID。
        ("NAD",c_ubyte),       # 节点地址
        ("CheckType",c_ubyte),# 0-标准校验, 1-增加校验。一般为标准校验
        ("STmin",c_ubyte),    # 连续帧时间间隔，单位为毫秒
    ]


# 函数返回错误代码定义
LIN_UDS_OK           = 0
LIN_UDS_TRAN_USB     = -98
LIN_UDS_TRAN_LIN     = -99
LIN_UDS_TIMEOUT_A    = -100
LIN_UDS_TIMEOUT_Bs   = -101
LIN_UDS_TIMEOUT_Cr   = -102
LIN_UDS_WRONG_SN     = -103
LIN_UDS_INVALID_FS   = -104
LIN_UDS_UNEXP_PDU    = -105
LIN_UDS_WFT_OVRN     = -106
LIN_UDS_BUFFER_OVFLW = -107
LIN_UDS_ERROR        = -108

def LIN_UDS_Request(DevHandle,LINIndex,pUDSAddr,pReqData,DataLen):
    return USB2XXXLib.LIN_UDS_Request(DevHandle,LINIndex,pUDSAddr,pReqData,DataLen)

def LIN_UDS_Response(DevHandle,LINIndex,pUDSAddr,pResData,TimeOutMs):
    return USB2XXXLib.LIN_UDS_Response(DevHandle,LINIndex,pUDSAddr,pResData,TimeOutMs)

def LIN_UDS_GetMsgFromUDSBuffer(DevHandle,LINIndex,pLINMsg,BufferSize):
    return USB2XXXLib.LIN_UDS_GetMsgFromUDSBuffer(DevHandle,LINIndex,pLINMsg,BufferSize)

