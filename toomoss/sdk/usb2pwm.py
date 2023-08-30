"""
文件说明：USB2XXX PWM操作相关函数集合
更多帮助：www.toomoss.com
"""
from ctypes import *

from toomoss.sdk.usb_device import *

# UTA0101 UTA0201 UTA0301 UTA0302引脚定义参考引脚定义说明文档，主频为200M
# UTA0403 UTA0402 UTA0401  LIN1对应的PWM通道为0x40,LIN2对应的PWM通道为0x80，主频84M
# UTA0503  LIN1对应的PWM通道为0x02,LIN2对应的PWM通道为0x04，主频220M
# UTA0504  LIN1->0x01 LIN2->0x02 LIN3->0x04 LIN4->0x08 DO0->0x10 DO1->0x20,主频240M

# Error code define
PWM_SUCCESS = 0  # success
PWM_ERR_NOT_SUPPORT = -1  # USB2XXX not support
PWM_ERR_USB_WRITE_FAIL = -2  # USB write data error
PWM_ERR_USB_READ_FAIL = -3  # USB read data error
PWM_ERR_CMD_FAIL = -4  # execute function error


# PWM初始化配置参数
class PWM_CONFIG(Structure):
    _fields_ = [
        ("Prescaler", c_ushort * 8),  # 预分频器
        ("Precision", c_ushort * 8),  # 占空比调节精度
        ("Pulse", c_ushort * 8),  # 占空比，实际占空比=(Pulse/Precision)*100%
        ("Phase", c_ushort * 8),  # 波形相位，取值0到Precision-1
        ("Polarity", c_ubyte * 8),  # 波形极性
        ("ChannelMask", c_ubyte),  # 使能的通道号，每个通道对应一个bit位，bit0对应PWM_CH1
    ]


# PWM初始化配置参数
class PWM_CAP_DATA(Structure):
    _fields_ = [("LowValue", c_ushort), ("HighValue", c_ushort)]  # 低电平时间  # 高电平时间


# Initialize pwm
def PWM_Init(DevHandle, pConfig):
    return USB2XXXLib.PWM_Init(DevHandle, pConfig)


# 启动PWM
def PWM_Start(DevHandle, ChannelMask, RunTimeOfUs):
    return USB2XXXLib.PWM_Start(DevHandle, ChannelMask, RunTimeOfUs)


# 停止PWM
def PWM_Stop(DevHandle, ChannelMask):
    return USB2XXXLib.PWM_Stop(DevHandle, ChannelMask)


# 改变脉冲宽度
def PWM_SetPulse(DevHandle, ChannelMask, pPulse):
    return USB2XXXLib.PWM_SetPulse(DevHandle, ChannelMask, pPulse)


# 改变相位
def PWM_SetPhase(DevHandle, ChannelMask, pPhase):
    return USB2XXXLib.PWM_SetPhase(DevHandle, ChannelMask, pPhase)


# 改变频率
def PWM_SetFrequency(DevHandle, ChannelMask, pPrescaler, pPrecision):
    return USB2XXXLib.PWM_SetFrequency(DevHandle, ChannelMask, pPrescaler, pPrecision)


# 初始化
def PWM2_Init(DevHandle, ChannelIndex, Frequency, Polarity, Precision, DutyCycle):
    return USB2XXXLib.PWM2_Init(
        DevHandle, ChannelIndex, Frequency, Polarity, Precision, DutyCycle
    )


# 启动PWM输出
def PWM2_Start(DevHandle, ChannelIndex, RunTimeUs):
    return USB2XXXLib.PWM2_Start(DevHandle, ChannelIndex, RunTimeUs)


# 设置PWM占空比
def PWM2_SetDutyCycle(DevHandle, ChannelIndex, DutyCycle):
    return USB2XXXLib.PWM2_SetDutyCycle(DevHandle, ChannelIndex, DutyCycle)


# 设置频率
def PWM2_SetFrequency(DevHandle, ChannelIndex, Frequency, Precision):
    return USB2XXXLib.PWM2_SetFrequency(DevHandle, ChannelIndex, Frequency, Precision)


# 停止输出
def PWM2_Stop(DevHandle, ChannelIndex):
    return USB2XXXLib.PWM2_Stop(DevHandle, ChannelIndex)


# PWM信号探测初始化
def PWM_CAP_Init(DevHandle, Channel, TimePrecUs):
    return USB2XXXLib.PWM_CAP_Init(DevHandle, Channel, TimePrecUs)


# 获取PWM信号数据
def PWM_CAP_GetData(DevHandle, Channel, pPWMData):
    return USB2XXXLib.PWM_CAP_GetData(DevHandle, Channel, pPWMData)


# 停止PWM探测
def PWM_CAP_Stop(DevHandle, Channel):
    return USB2XXXLib.PWM_CAP_Stop(DevHandle, Channel)
