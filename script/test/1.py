from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color', resolution='1080p')
    oak.visualize([color])
    oak.start(blocking=False)

    while oak.running():
        oak.poll()
        # this code is executed while the pipeline is running
