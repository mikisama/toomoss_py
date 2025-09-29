"""
文件说明：USB2XXX CAN操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *
# 函数返回错误值宏定义
MELIBU_SUCCESS           =  (0)   # 函数执行成功
MELIBU_ERR_NOT_SUPPORT   =  (-1)  # 适配器不支持该函数
MELIBU_ERR_USB_WRITE_FAIL=  (-2)  # USB写数据失败
MELIBU_ERR_USB_READ_FAIL =  (-3)  # USB读数据失败
MELIBU_ERR_CMD_FAIL      =  (-4)  # 命令执行失败
MELIBU_ERR_PARAMETER     =  (-5)  # 参数错误

# 设备工作模式
MELIBU_MASTER    =  0x01    # 设备工作在主机模式，可以控制总线收发数据
MELIBU_SLAVE     =  0x00    # 设备工作在从机模式，可以用于监听总线数据

# 帧收发方向定义
MELIBU_TX      = 0x00    # 主机发送数据给从机
MELIBU_RX      = 0x01    # 主机向从机读数据

# 帧状态定义
MELIBU_STATUS_NACK  = 0x01    # 写无应答(非广播帧)
MELIBU_STATUS_RNRES = 0x02    # 读数据无应答
MELIBU_STATUS_ECRC  = 0x04    # CRC校验错误
MELIBU_STATUS_FERR  = 0x08    # 帧异常，实际字节数跟规定的不匹配
MELIBU_STATUS_DLEN  = 0x10    # 实际数据字节数跟帧头字节数不匹配
MELIBU_STATUS_PERR  = 0x20    # P0 P1错误


# MELIBU帧结构定义
class MELIBU_MSG(Structure):
    _fields_ = [
        ("DataLen",c_ubyte),      # Data域中有效数据字节数
        ("BreakBits",c_ubyte),    # 发送同步间隔宽度，一般为13
        ("Status",c_ubyte),       # 当前帧状态指示，接收时有效，指示帧异常状态
        ("ACKValue",c_ubyte),     # 应答值，发送数据时存储对方应答数据
        ("MsgMode",c_ubyte),      # 0-普通模式，1-扩展模式
        ("TimeStampHigh",c_ubyte),# 时间戳高位
        ("MsgSendTimes",c_ushort),# 当前帧发送次数
        ("TimeStamp",c_uint),     # 接收帧时为时间戳低位，单位为10us，发送数据时为跟下一帧的间隔时间，单位为微秒(us)
        ("ID",c_ushort),          # ID值，可以通过调用 @ref MeLiBu_GetID 函数获取
        ("Crc16",c_ushort),       # 发送数据时不用填，底层会自动计算，接收时代表接收到的CRC值
        ("Data",c_ubyte*128)      # 数据存储数组，里面包含的有效数据字节数由DataLen决定
    ]

# MELIBU调度表信息
class MELIBU_SCH_INFO(Structure):
    _fields_ = [
        ("SchSendTimes",c_uint), # 调度表发送次数，若为0xFFFFFFFF,表示一直循环发送
        ("SchSendIndex",c_uint), # 当前调度表发送次数
        ("MsgSendIndex",c_uint), # 当前帧发送次数索引
        ("AllMsgLen",c_uint),    # 调度表里面包含帧数
        ("MsgIndex",c_ushort),   # 当前发送帧在调度表里面的索引模式
        ("RunFlag",c_ubyte),     # 调度表运行标志
        ("SaveTxMsg",c_ubyte)
    ]

# 接口函数定义

def MeLiBu_Init(DevHandle, Index, BaudRate, MasterMode, ResEnable):
    return USB2XXXLib.MeLiBu_Init(DevHandle, Index, BaudRate, MasterMode, ResEnable)

def MeLiBu_SetRevTime(DevHandle, Index, TimeUs):
    return USB2XXXLib.MeLiBu_SetRevTime(DevHandle, Index, TimeUs)

def MeLiBu_MasterStartSch(DevHandle, Index, pMsg, MsgLen, SendTimes, ReadBackFlag):
    return USB2XXXLib.MeLiBu_MasterStartSch(DevHandle, Index, pMsg, MsgLen, SendTimes, ReadBackFlag)

def MeLiBu_GetMsg(DevHandle, Index, pMsg, BufferSize):
    return USB2XXXLib.MeLiBu_GetMsg(DevHandle, Index, pMsg, BufferSize)

def MeLiBu_GetID(MsgMode, SlaveAddr, RT, F, dlc, InstrExt):
    return USB2XXXLib.MeLiBu_GetID(MsgMode, SlaveAddr, RT, F, dlc, InstrExt)

def MeLiBu_MasterStopSch(DevHandle, Index):
    return USB2XXXLib.MeLiBu_MasterStopSch(DevHandle, Index)

def MeLiBu_Stop(DevHandle, Index):
    return USB2XXXLib.MeLiBu_Stop(DevHandle, Index)

def MeLiBu_GetStartTime(DevHandle, Index):
    return USB2XXXLib.MeLiBu_GetStartTime(DevHandle, Index)

def MeLiBu_GetSchInfo(DevHandle, Index, pSchInfo):
    return USB2XXXLib.MeLiBu_GetSchInfo(DevHandle, Index, pSchInfo)
