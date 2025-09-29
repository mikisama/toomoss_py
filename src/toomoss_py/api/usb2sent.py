"""
文件说明：USB2XXX SENT操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *
import platform
from .usb_device import *
from enum import Enum

# 定义函数返回错误代码
SENT_SUCCESS            = (0)   # 函数执行成功
SENT_ERR_NOT_SUPPORT    = (-1)  # 适配器不支持该函数
SENT_ERR_USB_WRITE_FAIL = (-2)  # USB写数据失败
SENT_ERR_USB_READ_FAIL  = (-3)  # USB读数据失败
SENT_ERR_CMD_FAIL       = (-4)  # 命令执行失败
SENT_ERR_PARAMETER      = (-5)  # 函数参数传入有误
SENT_ERR_MSG_TYPE       = (-6)  # 当前函数不支持该消息类型
# SENT主从模式
SENT_MASTER         = 1       # 主机模式，用于模拟主节点发送数据
SENT_SLAVE          = 0       # 从机模式，用于监控SENT主机发送出来的数据
SENT_SPC            = 0x80    # 使能SPC模式
SENT_SPC_SLAVE_TX   = 0x40    #使能SPC从机模式发送数据

# SENT帧类型
SENT_MSGTYPE_ERROR        = 0 # 错误帧，比如CRC错误，数据不完整等
SENT_MSGTYPE_FAST         = 1 # 快速通道数据,数据存放在Data[0]~Data[7]里面，Status的高4位代表数据有效半字节数
SENT_MSGTYPE_SLOW_SHORT   = 2 # 慢速通道，简短型串行信息,Data[0]为ID,Data[1]为数据
SENT_MSGTYPE_SLOW_ENH1    = 3 # 慢速通道，增强型串行信息,12位数据+8位ID,Data[0]为ID，Data[1]为高4位数据,Data[2]为低8位数据
SENT_MSGTYPE_SLOW_ENH2    = 4 # 慢速通道，增强型串行信息,16位数据+4位ID,Data[0]为ID，Data[1]为高8位数据,Data[2]为低8位数据
SENT_MSGTYPE_TX           =  0x80    #当前帧为发送数据帧
SENT_MSGTYPE_SPC          =  0x08    #当前帧为SPC模式帧

# SENT总线空闲电平
SENT_IDLE_LOW     = 0  # 总线空闲时为高电平，数据输出低电平脉冲
SENT_IDLE_HIGH	  = 1	# 总线空闲时为低电平，数据输出高电平脉冲

# 设置从模式下ID操作模式
class SENT_CONFIG(Structure):
    _fields_ = [
        ("TicksTimeUs",c_ubyte),    #Ticks时间，单位为us，一般为3
        ("MasterMode",c_ubyte),     #0-从机模式，用于监控SENT总线数据，1-主机模式，用于发送SENT总线数据
        ("LowTicks",c_ubyte),       #低电平输出Ticks数，低电平输出时间=TicksTimeUs*LowTicks，推荐设置为5
        ("PausePulseTicks",c_ubyte),#暂停脉冲数，0-不输出，1~64对应12Ticks~768Ticks
        ("NibbleNum",c_ubyte),      #快速通道半字节数，不包含CRC，从机模式若是0则自动匹配，主机模式Status高4位代表要发送的有效半字节数
        ("IdleLevel",c_ubyte),      #总线空闲状态，0-空闲低电平，1-空闲高电平
        ("DataFormat",c_ubyte),     #数据格式
        ("SensorType",c_ubyte),     #传感器类型
    ]

# 设置从模式下ID操作模式
class SENT_MSG(Structure):
    _fields_ = [
        ("Timestamp",c_uint),     #接收到信息帧时的时间标识，从SENT控制器初始化开始计时，单位为100us。发送数据时为帧间隔时间，单位为ms
        ("TimestampHigh",c_ubyte),#接收数据时为时间戳高位,发送帧时为该帧发送次数
        ("MsgType",c_ubyte),      #帧类型，具体可以参考帧类型定义
        ("Status",c_ubyte),       #高4位代表Data有效字节数，低4位代表Status
        ("Data",c_ubyte*8),       #根据帧类型存储不同的数据
        ("crc",c_ubyte),          #MsgType若为增强型串行信息，则是6bit有效CRC，其他的为4bit有效CRC，bit7-当前帧为错误帧
        ("Tmtr",c_short),         #Total trigger time，单位为0.01tick
        ("Tmlow",c_short),        #触发字段,SPC模式时用到,Master low time，单位为0.01tick
    ]
# SENT帧数据格式定义
class SENT_DATA_FORMATS(Enum):
    H0 = 0  #未定义
    H1 = 1  #CH1=(byte[0]<<8)|(byte[1]<<4)|byte[2],CH2=(byte[5]<<8)|(byte[4]<<4)|byte[3]
    H2 = 2  #CH1=(byte[0]<<8)|(byte[1]<<4)|byte[2]
    H3 = 3  #CH1=(byte[0]<<9)|(byte[1]<<6)|(byte[2]<<3)|byte[3]
    H4 = 4  #CH1=(byte[0]<<8)|(byte[1]<<4)|byte[2],CH2(Counter)=(byte[3]<<4)|byte[4]
    H5 = 5  #CH1=(byte[0]<<8)|(byte[1]<<4)|byte[2],CH2=0
    H6 = 6  #CH1=(byte[0]<<10)|(byte[1]<<6)|(byte[2]<<2)|(byte[3]>>2),CH2=(byte[5]<<6)|(byte[4]<<2)|(byte[3]&0x03)
    H7 = 7  #CH1=(byte[0]<<12)|(byte[1]<<8)|(byte[2]<<4)|byte[3],CH2==(byte[5]<<4)|byte[4]
    H8 = 8  #Data Frames with one multiplexed fast channel and 12-bit sensor data (F1.5); 1-16 Frame Controls (FC)

#初始化配置SENT总线，必须调用，否则无法正常工作
def SENT_Init(DevHandle,Channel,pConfig):
    return USB2XXXLib.SENT_Init(DevHandle,Channel,pConfig)
#配置SENT总线Tick时间
def SENT_SetTickTime(DevHandle, Channel, TickTimeUs):
    return USB2XXXLib.SENT_SetTickTime(DevHandle,Channel,TickTimeUs)
#主机模式下手动发送SENT消息
def SENT_SendMsg(DevHandle, Channel, pSentMsg,MsgNum):
    return USB2XXXLib.SENT_SendMsg(DevHandle, Channel, pSentMsg,MsgNum)
#设置并启动SENT快速通道帧发送列表
def SENT_StartFastMsgTable(DevHandle,Channel,pSentMsg,MsgNum,SendTimes):
    return USB2XXXLib.SENT_StartFastMsgTable(DevHandle,Channel,pSentMsg,MsgNum,SendTimes)
#更新SENT快速通道发送列表中的帧
def SENT_UpdateFastMsgTable(DevHandle, Channel, StartMsgIndex,pSentMsg, MsgNum):
    return USB2XXXLib.SENT_UpdateFastMsgTable(DevHandle,Channel,StartMsgIndex,pSentMsg,MsgNum)
#停止正在发送的SENT帧列表
def SENT_StopFastMsgTable(DevHandle,Channel):
    return USB2XXXLib.SENT_StopFastMsgTable(DevHandle,Channel)
#设置并启动SENT SPC帧发送列表
def SENT_StartSPCMsgTable(DevHandle, Channel, pSentMsg, MsgNum, SendTimes):
    return USB2XXXLib.SENT_StartSPCMsgTable(DevHandle,Channel,pSentMsg,MsgNum,SendTimes)
#更新SENT SPC快速通道发送列表中的帧
def ENT_UpdateSPCMsgTable(DevHandle, Channel, StartMsgIndex,pSentMsg, MsgNum):
    return USB2XXXLib.SENT_UpdateSPCMsgTable(DevHandle,Channel,StartMsgIndex,pSentMsg,MsgNum)
#停止正在发送的SENT帧列表
def SENT_StopSPCMsgTable(DevHandle, Channel):
    return USB2XXXLib.SENT_StopSPCMsgTable(DevHandle,Channel)
#设置并启动SENT慢速通道帧发送列表，调用该函数后数据不会立即发送，它是在发送快速数据的时候才通过Status域发送，所以需要发送慢速通道帧数据，需要同时启动快速帧发送列表
def SENT_StartSlowMsgTable(DevHandle,Channel,pSentMsg,MsgNum,SendTimes):
    return USB2XXXLib.SENT_StartSlowMsgTable(DevHandle,Channel,pSentMsg,MsgNum,SendTimes)
#更新慢速通道发送列表中的帧
def SENT_UpdateSlowMsgTable(DevHandle, Channel, StartMsgIndex,pSentMsg, MsgNum):
    return USB2XXXLib.SENT_UpdateSlowMsgTable(DevHandle,Channel,StartMsgIndex,pSentMsg,MsgNum)
#停止正在发送的SENT帧列表
def SENT_StopSlowMsgTable(DevHandle,Channel):
    return USB2XXXLib.SENT_StopSlowMsgTable(DevHandle,Channel)
#主机模式获取已发成功发送出去的帧，从机模式获取监控到的帧
def SENT_GetMsg(DevHandle,Channel,pSentMsg):
    return USB2XXXLib.SENT_GetMsg(DevHandle,Channel,pSentMsg)
#主机模式获取已发成功发送出去的帧，从机模式获取监控到的帧
def SENT_GetMsgWithSize(DevHandle, Channel, pSentMsg, BufSize):
    return USB2XXXLib.SENT_GetMsgWithSize(DevHandle,Channel,pSentMsg,BufSize)
#获取SENT起始时间戳，该时间戳可以转换成实际的时间
def SENT_GetStartTime(DevHandle,Channel):
    return USB2XXXLib.SENT_GetStartTime(DevHandle,Channel)
#复位时间戳，复位后起始时间戳为当前时间
def SENT_ResetStartTime(DevHandle,Channel):
    return USB2XXXLib.SENT_ResetStartTime(DevHandle,Channel)
#停止SENT总线功能
def SENT_Stop(DevHandle, Channel):
    return USB2XXXLib.SENT_Stop(DevHandle,Channel)
#将快速通道原始SENT数据解析成实际数据，注意只解析快速通道帧数据
def SENT_MsgDecode(DataFormat,pSentMsg,MsgNum,pDataCh1,  pDataCh2):
    return USB2XXXLib.SENT_MsgDecode(DataFormat,pSentMsg,MsgNum,pDataCh1,pDataCh2)
