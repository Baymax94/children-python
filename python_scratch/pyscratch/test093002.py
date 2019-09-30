import scratch


class ScratchReceiver(object):
    @staticmethod
    def broadcast_handler(message):
        print('[receive] broadcast:', message)

    @staticmethod
    def sensor_update_handler(**sensor_data):
        for name, value in sensor_data.items():
            print('[receive] sensor-update:', name, value)


rsc = scratch.RemoteSensorConnection(
    ScratchReceiver.broadcast_handler, ScratchReceiver.sensor_update_handler)
rsc.connect()
rsc.send_broadcast('connected')
rsc.send_sensor_update(test_sensor=100)
rsc.disconnect()
