from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.pt')  # load an official detection model
model = YOLO('yolov8n-seg.pt')  # load an official segmentation model


# Track with the model
results = model.track(source="https://youtu.be/nkOk_P5VnOA", show=True)
results = model.track(source="https://youtu.be/nkOk_P5VnOA", show=True, tracker="bytetrack.yaml")