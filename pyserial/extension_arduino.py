import serial
import platform
from codelab_adapter.core_extension import Extension
from codelab_adapter.utils import ui_error


class ArduinoExtension(Extension):
    def __init__(self):
        name = type(self).__name__  # class name
        super().__init__(name)
        self.TOPIC = "eim/arduino"

    def connect_to_arduino(self):
        # 根据平台不同找到port(类似microbit的发现机制), 或者提供选择积木
        # 参考 https://github.com/Scratch3Lab/codelab_adapter_extensions/blob/master/extension_ubtrobot.py
        ser = None
        if platform.system() == "Linux":
            try:
                ser = serial.Serial(
                    "/dev/ttyUSB0", 115200,
                    timeout=1)  # Ubuntu sudo chmod 666 /dev/ttyUSB0
            except:
                ser = None
        '''
        if platform.system() == "Windows":
            # 分别处理win7和win10 没必要 platform.release()
            # win7会存贮之前的连接信息
            win_ports = []
            for port in ports:
                # ServiceGUID
                # 00010039_PID win7需要这个
                if ("00001101-0000-1000-8000-00805f9b34fb" in port[2].lower()) and ("00010039_pid" in port[2].lower()):
                    # 旧的port会被系统留着
                    win_ports.append(str(port[0]))
                    ser = sorted(win_ports)[-1]  # 选择最大的
        '''

        if platform.system() == "Windows":
            ser = serial.Serial()
            ser.baudrate = 9600
            # 修改端口
            ser.port = 'COM7'

        return ser

    def run(self):
        # 建立与arduino的连接
        ser = self.connect_to_arduino()
        if not ser:
            ui_error("error", "无法连接arduino")

        while self._running:
            message = self.read(
            )  # todo 停止插件后，这里仍可能处于阻塞，以至于ser.close()无法释放（需要前端再多发一条消息才能跳出while）
            self.logger.debug(message)
            topic = message.get("topic")
            if topic == self.TOPIC:
                python_code = message.get("payload")
                self.logger.debug("run python code:{}".format(message))
                try:
                    # 单一入口，传递源码
                    # 为了安全性, 做一些能力的牺牲, 放弃使用exec
                    output = eval(python_code)
                except Exception as e:
                    output = e
                message = {
                    "topic": self.TOPIC,
                    "payload": str(output).rstrip()
                }
                self.publish(message)
        ser.close()


export = ArduinoExtension
