from src import cam as camera_module
import time

if __name__ == '__main__':

    total_seconds = 60
    sample_hz = 10

    camera = camera_module.Camera({
        "show_preview": False
    })
    start_time = time.time()

    while time.time() - start_time < total_seconds:
        camera.capture()
        print(camera.image_array)

        time.sleep(max(0, 1/sample_hz -
                       (time.time() - start_time)))
