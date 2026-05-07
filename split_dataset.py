from pathlib import Path
import random
import shutil

SOURCE = Path("construction safety.yolov8/train")
TARGET = Path("dataset")

random.seed(42)

image_dir = SOURCE / "images"
label_dir = SOURCE / "labels"

images = [x for x in image_dir.glob("*") if x.suffix.lower() in [".jpg", ".jpeg", ".png"]]

random.shuffle(images)

n = len(images)

train_split = int(n * 0.8)
val_split = int(n * 0.1)

splits = {
    "train": images[:train_split],
    "val": images[train_split:train_split + val_split],
    "test": images[train_split + val_split:]
}

for split in splits:
    (TARGET / "images" / split).mkdir(parents=True, exist_ok=True)
    (TARGET / "labels" / split).mkdir(parents=True, exist_ok=True)

    for img_path in splits[split]:
        label_path = label_dir / f"{img_path.stem}.txt"

        shutil.copy2(img_path, TARGET / "images" / split / img_path.name)

        if label_path.exists():
            shutil.copy2(label_path, TARGET / "labels" / split / label_path.name)

print("Done.")
print(f"Total images: {n}")
print(f"Train: {len(splits['train'])}")
print(f"Val: {len(splits['val'])}")
print(f"Test: {len(splits['test'])}")