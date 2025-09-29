"""
文件说明：USB2XXX LIN LDF文件解析相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *

# 定义函数返回错误代码
LDF_PARSER_OK               =   0 #没有错误
LDF_PARSER_FILE_OPEN        = (-1)#打开文件出错
LDF_PARSER_FILE_FORMAT      = (-2)#文件格式错误
LDF_PARSER_DEV_DISCONNECT   = (-3)#设备未连接
LDF_PARSER_HANDLE_ERROR     = (-4)#LDF Handle错误
LDF_PARSER_GET_INFO_ERROR   = (-5)#获取解析后的数据出错
LDF_PARSER_DATA_ERROR       = (-6)#数据处理错误
LDF_PARSER_SLAVE_NACK       = (-7)#从机未响应数据

def LDF_ParserFile(DevHandle, LINIndex, isMaster, pLDFFileName):
    USB2XXXLib.LDF_ParserFile.restype = c_uint64
    return USB2XXXLib.LDF_ParserFile(DevHandle, LINIndex, isMaster, pLDFFileName)
def LDF_GetProtocolVersion(LDFHandle):
    return USB2XXXLib.LDF_GetProtocolVersion(LDFHandle)
def LDF_GetLINSpeed(LDFHandle):
    return USB2XXXLib.LDF_GetLINSpeed(LDFHandle)
def LDF_GetFrameQuantity(LDFHandle):
    return USB2XXXLib.LDF_GetFrameQuantity(LDFHandle)
def LDF_GetFrameName(LDFHandle, index, pFrameName):
    return USB2XXXLib.LDF_GetFrameName(LDFHandle, index, pFrameName)
def LDF_GetFrameSignalQuantity(LDFHandle, pFrameName):
    return USB2XXXLib.LDF_GetFrameSignalQuantity(LDFHandle, pFrameName)
def LDF_GetFrameSignalName(LDFHandle, pFrameName, index, pSignalName):
    return USB2XXXLib.LDF_GetFrameSignalName(LDFHandle, pFrameName, index, pSignalName)
def LDF_SetSignalValue(LDFHandle, pFrameName, pSignalName, Value):
    return USB2XXXLib.LDF_SetSignalValue(LDFHandle, pFrameName, pSignalName, Value)
def LDF_GetSignalValue(LDFHandle, pFrameName, pSignalName, pValue):
    return USB2XXXLib.LDF_GetSignalValue(LDFHandle, pFrameName, pSignalName, pValue)
def LDF_GetSignalValueStr(LDFHandle, pFrameName, pSignalName, pValueStr):
    return USB2XXXLib.LDF_GetSignalValueStr(LDFHandle, pFrameName, pSignalName, pValueStr)
def LDF_SetFrameRawValue(LDFHandle, pFrameName, pRawData):
    return USB2XXXLib.LDF_SetFrameRawValue(LDFHandle, pFrameName, pRawData)
def LDF_SyncMsgToValue(LDFHandle, pLINMsg, MsgLen):
    return USB2XXXLib.LDF_SyncMsgToValue(LDFHandle, pLINMsg, MsgLen)
def LDF_GetFrameRawValue(LDFHandle, pFrameName, pRawData):
    return USB2XXXLib.LDF_GetFrameRawValue(LDFHandle, pFrameName, pRawData)
def LDF_GetFramePublisher(LDFHandle, pFrameName, pPublisher):
    return USB2XXXLib.LDF_GetFramePublisher(LDFHandle, pFrameName, pPublisher)
def LDF_GetMasterName(LDFHandle, pMasterName):
    return USB2XXXLib.LDF_GetMasterName(LDFHandle, pMasterName)
def LDF_GetSchQuantity(LDFHandle):
    return USB2XXXLib.LDF_GetSchQuantity(LDFHandle)
def LDF_GetSchName(LDFHandle, index, pSchName):
    return USB2XXXLib.LDF_GetSchName(LDFHandle, index, pSchName)
def LDF_GetSchFrameQuantity(LDFHandle, pSchName):
    return USB2XXXLib.LDF_GetSchFrameQuantity(LDFHandle, pSchName)
def LDF_GetSchFrameName(LDFHandle, pSchName, index, pFrameName):
    return USB2XXXLib.LDF_GetSchFrameName(LDFHandle, pSchName, index, pFrameName)
def LDF_ExeFrameToBus(LDFHandle, pFrameName, FillBitValue):
    return USB2XXXLib.LDF_ExeFrameToBus(LDFHandle, pFrameName, FillBitValue)
def LDF_ExeSchToBus(LDFHandle, pSchName, FillBitValue):
    return USB2XXXLib.LDF_ExeSchToBus(LDFHandle, pSchName, FillBitValue)
def LDF_SetSchToTable(LDFHandle, pSchName, FillBitValue):
    return USB2XXXLib.LDF_SetSchToTable(LDFHandle, pSchName, FillBitValue)
def LDF_GetRawMsg(LDFHandle, pLINMsg, BufferSize):
    return USB2XXXLib.LDF_GetRawMsg(LDFHandle, pLINMsg, BufferSize)
def LDF_Release(LDFHandle):
    return USB2XXXLib.LDF_Release(LDFHandle)

