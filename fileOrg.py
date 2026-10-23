import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".xlsx", ".pptx"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi"},
    "Audio": {".mp3", ".wav", ".flac"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Code": {".py", ".js", ".html", ".css", ".json"},
}


def category_for(path):
    ext = path.suffix.lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return "Other"


def organize(folder, dry_run):
    moved = 0
    for item in folder.iterdir():
        if not item.is_file():
            continue
        target_dir = folder / category_for(item)
        target = target_dir / item.name
        if target.exists():
            print(f"Skipped (already exists): {item.name}")
            continue
        print(f"{item.name} -> {target_dir.name}/")
        if not dry_run:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
        moved += 1
    print(f"\n{'Would move' if dry_run else 'Moved'} {moved} file(s).")


def main():
    parser = argparse.ArgumentParser(description="Sort files into folders by type")
    parser.add_argument("folder", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="show changes without moving anything")
    args = parser.parse_args()

    if not args.folder.is_dir():
        parser.error(f"{args.folder} is not a folder")
    organize(args.folder, args.dry_run)


if __name__ == "__main__":
    main()