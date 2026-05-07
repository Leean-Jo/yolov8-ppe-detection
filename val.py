from ultralytics import YOLO


def main():
    model = YOLO("runs/detect/runs/detect/ppe_yolov8n-2/weights/best.pt")
    metrics = model.val(data="data.yaml")

    print("mAP50:", metrics.box.map50)
    print("mAP50-95:", metrics.box.map)
    print("Precision:", metrics.box.mp)
    print("Recall:", metrics.box.mr)


if __name__ == "__main__":
    main()