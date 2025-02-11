from .models import *
#SET TOPICS HERE: FORMAT: (mqtt_topic, device.data, model)

"""
2025 TOPICS:
- Accelerometer
- Torque Sensor
- Pressure Sensor
- Hall Sensor
"""

topics_list = {
    #bear_1
    "/Bear_1/RPM": {
        "name": "bear1.rpm",
        "model": RPMData
        #chart
    },
        "/Bear_1/Motor_State": {
        "name": "bear1.motor_state",
        "model": Motor_StateData,
        "max": 0,
        "min": 0
        #io
    },
        "/Bear_1/Cruise": {
        "name": "bear1.cruise",
        "model": CruiseData
        #ignore
    },
        "/Bear_1/M_Error_Status": {
        "name": "bear1.m_error_status",
        "model": M_Error_StatusData,
        "max": 0,
        "min": 0
        #error 1, check, io
    },
        "/Bear_1/Throttle": {
        "name": "bear1.throttle",
        "model": ThrottleData,
        "max": 1028,
        "min": 0
        #error above 1028: check teensy output range, ignore
    },
    "/Bear_1/Brake": {
        "name": "bear1.brake",
        "model": BrakeData
        #check back, ignore
    },
    "/Bear_1/Meter_Count": {
        "name": "bear1.meter_count",
        "model": Meter_CountData
        #ignore
    },    
#bear_2
    "/Bear_2/RPM": {
        "name": "bear2.rpm",
        "model": RPMData
    },
    "/Bear_2/Motor_State": {
        "name": "bear2.motor_state",
        "model": Motor_StateData
    },

    "/Bear_2/Cruise": {
        "name": "bear2.cruise",
        "model": CruiseData
    },
    "/Bear_2/M_Error_Status": {
        "name": "bear2.m_error_status",
        "model": M_Error_StatusData,
        "max": 0,
        "min": 0
        #error 1, check

    },
    "/Bear_2/Throttle": {
        "name": "bear2.throttle",
        "model": ThrottleData
    },
    "/Bear_2/Brake": {
        "name": "bear2.brake",
        "model": BrakeData
    },
    "/Bear_2/Meter_Count": {
        "name": "bear2.meter_count",
        "model": Meter_CountData
    },

    #UI blinkers
    "/UIMessage/Blink_Left": {
        "name": "uimessage.blink_left",
        "model": Blinker,
    },
    "/UIMessage/Blink_Right": {
        "name": "uimessage.blink_right",
        "model": Blinker,
    },
    #HS Message: for analysis
    "   ": {
        "name": "hsmessage.temperature",
        "model": Temperature,
    },
    "/HSMessage/Gyro_x": {
        "name": "hsmessage.gyro_x",
        "model": Gyro_x
    },
    "/HSMessage/Gyro_y": {
        "name": "hsmessage.gyro_y",
        "model": Gyro_y
    },
    "/HSMessage/Gyro_z": {
        "name": "hsmessage.gyro_z",
        "model": Gyro_z,
    },
    "/HSMessage/Magnetometer": {
        "name": "hsmessage.magnetometer",
        "model": Magnetometer
    },
    "/HSMessage/Accel": {
        "name": "hsmessage.accel",
        "model": Accel,
    },
    #DAQMessage
    "/DAQ/Speed": {
        "name": "daq.speed",
        "model": SpeedData,
    },
    "/DAQ/Longitude": {
        "name": "daq.longitude",
        "model": Location
    },
    "/DAQ/Latitude": {
        "name": "daq.latitude",
        "model": Location
    }
}