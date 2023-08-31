from depthai_sdk import OakCamera

with OakCamera() as oak:
    color = oak.create_camera('color', resolution='1080p')
    # List of models that are supported out-of-the-box by the SDK:
    # https://docs.luxonis.com/projects/sdk/en/latest/features/ai_models/#sdk-supported-models
    yolo = oak.create_nn('yolov6n_coco_640x640', input=color)

    oak.visualize([color, yolo])
    oak.start(blocking=True)
