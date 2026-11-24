import os
import shutil
from pathlib import Path


def organize_folder(folder_path: str) -> None:
  target_dir = Path(folder_path)
  if not target_dir.exists() or not target_dir.is_dir():
    print("المسار غير موجود أو ليس مجلداً.")
    return

  for item in target_dir.iterdir():
    if item.is_file():
      ext = item.suffix.lower().lstrip(".") or "no_extension"
      dest_folder = target_dir / ext
      dest_folder.mkdir(exist_ok=True)
      shutil.move(str(item), str(dest_folder / item.name))

  print("تم تنظيم الملفات بنجاح.")


if __name__ == "__main__":
  folder = input("أدخل مسار المجلد المراد تنظيمه: ").strip()
  organize_folder(folder)
