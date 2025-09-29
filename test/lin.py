from abc import abstractmethod


class LinBus(object):
    def __init__(self, channel=0, bitrate=19200, **kwargs):
        self.channel = channel
        self.bitrate = bitrate
        self.is_shutdown = True

    @abstractmethod
    def send(self, id: int, data: bytes):
        raise NotImplementedError("")

    @abstractmethod
    def recv(self, id: int, dlc=8) -> bytes | None:
        raise NotImplementedError("")

    @abstractmethod
    def set_bitrate(self, baud: int):
        raise NotImplementedError("")

    @abstractmethod
    def wakeup(self):
        raise NotImplementedError("")

    def shutdown(self):
        if self.is_shutdown:
            return
        self.is_shutdown = True
