from .models import *
from .serializers import *
#SET TOPICS HERE: FORMAT: (mqtt_topic, device.data, model)

"""
2025 TOPICS:
- Accelerometer
- Torque Sensor
- Pressure Sensor
- Hall Sensor
"""

topics_list = {
    #Bear 1
    "/Bear_1/Hall_velocity": {
        "name": "bear1.hall_velocity",
        "model": HallVelocityData
    },
    "/Bear_1/Torque_motor": {
        "name": "bear1.torque_motor",
        "model": MotorTorqueData,
    },
    "/Bear_1/Current": {
        "name": "bear1.current",
        "model": CurrentData
    },
    "/Bear_1/Board_Temp": {
        "name": "bear1.board_temp",
        "model": BearBoardTempData
    },
    "/Bear_1/Motor_Temp": {
        "name": "bear1.motor_temp",
        "model": MotorTempData
    },
    "/UI/Motor": {
        "name": "ui.motor",
        "model": UIData,
        "type": "motor"
        
    },
    "/UI/Reverse": {
        "name": "ui.reverse",
        "model": UIData,
        "type": "reverse"
        
    },
    "/HS1/Gyro_x": {
        "name": "hs1.gyro_x",
        "model": GyroData,
        "board": "HS1",
        "axis": "x"
        
    },
    "/HS1/Gyro_y": {
        "name": "hs1.gyro_y",
        "model": GyroData,
        "board": "HS1",
        "axis": "y"
        
    },
    "/HS1/Gyro_z": {
        "name": "hs1.gyro_z",
        "model": GyroData,
        "board": "HS1",
        "axis": "z"
        
    },
    "/HS1/Accel_x": {
        "name": "hs1.accel_x",
        "model": AccelData,
        "board": "HS1",
        "axis": "x"
        
    },
    "/HS1/Accel_y": {
        "name": "hs1.accel_y",
        "model": AccelData,
        "board": "HS1",
        "axis": "y"
        
    },
    "/HS1/Accel_z": {
        "name": "hs1.accel_z",
        "model": AccelData,
        "board": "HS1",
        "axis": "z"
        
    },
    "/HS1/Pressure": {
        "name": "hs1.pressure",
        "model": PressureData,
        "board": "HS1"
        
    },
    "/HS1/Torque_HS": {
        "name": "hs1.torque_hs",
        "model": TorqueData,
        "board": "HS1"
        
    },
    "/HS2/Gyro_x": {
        "name": "hs2.gyro_x",
        "model": GyroData,
        "board": "HS2",
        "axis": "x"
        
    },
    "/HS2/Gyro_y": {
        "name": "hs2.gyro_y",
        "model": GyroData,
        "board": "HS2",
        "axis": "y"
        
    },
    "/HS2/Gyro_z": {
        "name": "hs2.gyro_z",
        "model": GyroData,
        "board": "HS2",
        "axis": "z"
        
    },
    "/HS2/Accel_x": {
        "name": "hs2.accel_x",
        "model": AccelData,
        "board": "HS2",
        "axis": "x"
        
    },
    "/HS2/Accel_y": {
        "name": "hs2.accel_y",
        "model": AccelData,
        "board": "HS2",
        "axis": "y"
        
    },
    "/HS2/Accel_z": {
        "name": "hs2.accel_z",
        "model": AccelData,
        "board": "HS2",
        "axis": "z"
        
    },
    "/HS2/Pressure": {
        "name": "hs2.pressure",
        "model": PressureData,
        "board": "HS2"
        
    },
    "/HS2/Torque_HS": {
        "name": "hs2.torque_hs",
        "model": TorqueData,
        "board": "HS2"
        
    },
    "/HS3/Gyro_x": {
        "name": "hs3.gyro_x",
        "model": GyroData,
        "board": "HS3",
        "axis": "x"
        
    },
    "/HS3/Gyro_y": {
        "name": "hs3.gyro_y",
        "model": GyroData,
        "board": "HS3",
        "axis": "y"
        
    },
    "/HS3/Gyro_z": {
        "name": "hs3.gyro_z",
        "model": GyroData,
        "board": "HS3",
        "axis": "z"
        
    },
    "/HS3/Accel_x": {
        "name": "hs3.accel_x",
        "model": AccelData,
        "board": "HS3",
        "axis": "x"
        
    },
    "/HS3/Accel_y": {
        "name": "hs3.accel_y",
        "model": AccelData,
        "board": "HS3",
        "axis": "y"
        
    },
    "/HS3/Accel_z": {
        "name": "hs3.accel_z",
        "model": AccelData,
        "board": "HS3",
        "axis": "z"
        
    },
    "/HS3/Pressure": {
        "name": "hs3.pressure",
        "model": PressureData,
        "board": "HS3"
        
    },
    "/HS3/Torque_HS": {
        "name": "hs3.torque_hs",
        "model": TorqueData,
        "board": "HS3"
        
    },
    "/HS4/Gyro_x": {
        "name": "hs4.gyro_x",
        "model": GyroData,
        "board": "HS4",
        "axis": "x"
        
    },
    "/HS4/Gyro_y": {
        "name": "hs4.gyro_y",
        "model": GyroData,
        "board": "HS4",
        "axis": "y"
        
    },
    "/HS4/Gyro_z": {
        "name": "hs4.gyro_z",
        "model": GyroData,
        "board": "HS4",
        "axis": "z"
        
    },
    "/HS4/Accel_x": {
        "name": "hs4.accel_x",
        "model": AccelData,
        "board": "HS4",
        "axis": "x"
        
    },
    "/HS4/Accel_y": {
        "name": "hs4.accel_y",
        "model": AccelData,
        "board": "HS4",
        "axis": "y"
        
    },
    "/HS4/Accel_z": {
        "name": "hs4.accel_z",
        "model": AccelData,
        "board": "HS4",
        "axis": "z"
        
    },
    "/HS4/Pressure": {
        "name": "hs4.pressure",
        "model": PressureData,
        "board": "HS4",
        "axis": "z"
        
    },
    "/HS4/Torque_HS": {
        "name": "hs4.torque_hs",
        "model": TorqueData,
        "board": "HS4"
        
    },
    "/FC/Gas": {
        "name": "fc.gas",
        "model": GasData
        
    },
    "/FC/Brake": {
        "name": "fc.brake",
        "model": BrakeData
        
    },
    "/Joule_H/Power": {
        "name": "joule_h.power",
        "model": PowerData,
        "board": "Joule_H"
        
    },
    "/Joule_L/Power": {
        "name": "joule_l.power",
        "model": PowerData,
        "board": "Joule_L"
        
    },
    "/DAQ_Board/Longitude": {
        "name": "daq_board.longitude",
        "model": Location,
        "direction": "longitude"
        
    },
    "/DAQ_Board/Latitude": {
        "name": "daq_board.latitude",
        "model": Location,
        "direction": "latitude"
        
    },
    "/DAQ_Board/Speed": {
        "name": "daq_board.speed",
        "model": SpeedData
        
    },
}
