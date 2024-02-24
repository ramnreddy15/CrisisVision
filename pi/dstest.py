from src import ds
import time


if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 100

    distance_sensor1 = ds.DistanceSensor({
        "pins": {
            "echo": 23,
            "trigger": 24
        }
    })

    distance_sensor2 = ds.DistanceSensor({
        "pins": {
            "echo": 17,
            "trigger": 27
        }
    })

    start_time = time.time()
    while time.time() - start_time < total_seconds:

        loop_start = time.time()

        print(1, distance_sensor1.distance, distance_sensor2.distance)
        time.sleep(max(0, 1/sample_hz - (time.time() - loop_start)))
