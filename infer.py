import argparse
from ultralytics import YOLO


def main(args):
    model = YOLO(args.weights)

    model.predict(
        source=args.image_path,
        conf=args.conf,
        save=True,
        project="runs/detect",
        name="inference",
        exist_ok=True
    )

    print("Inference completed.")
    print("Saved to runs/detect/inference/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--image_path", type=str, required=True)

    parser.add_argument(
        "--weights",
        type=str,
        default="runs/detect/runs/detect/ppe_yolov8n-2/weights/best.pt"
    )

    parser.add_argument("--conf", type=float, default=0.25)

    args = parser.parse_args()

    main(args)

    