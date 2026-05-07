from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="data.yaml",
        epochs=10,
        imgsz=416,
        batch=8,
        patience=10,
        project="runs/detect",
        name="ppe_yolov8n",
        pretrained=True
    )


if __name__ == "__main__":
    main()
