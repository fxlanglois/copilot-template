#!/usr/bin/env python3
import argparse
import csv
from pathlib import Path


DEFAULT_TOLERANCE = 0.10


def parse_args():
    parser = argparse.ArgumentParser(description="Compare two directories recursively and report matching filenames with similar sizes.")
    parser.add_argument("--config", default="compare_folders.config.txt", help="Path to the config file listing the two folders to compare.")
    parser.add_argument("--output", default="matches.csv", help="CSV file for file matches.")
    parser.add_argument("--folder-output", default="folder_matches.csv", help="CSV file for folder matches.")
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE, help="Acceptable relative size difference, expressed as a decimal fraction.")
    return parser.parse_args()


def load_config(config_path: Path):
    entries = []
    for line in config_path.read_text(encoding="utf-8").splitlines():
        entry = line.strip()
        if not entry or entry.startswith("#"):
            continue
        entries.append(entry)
    if len(entries) != 2:
        raise ValueError("Config file must contain exactly two folder paths or names.")
    return entries


def resolve_directory(entry: str, working_dir: Path):
    path = Path(entry).expanduser()
    if not path.is_absolute():
        path = (working_dir / path).resolve()
    return path


def collect_folders(root: Path):
    folders = set()
    for child in root.rglob("*"):
        if child.is_dir():
            relative = child.relative_to(root).as_posix().lower()
            if relative:
                folders.add(relative)
    return folders


def collect_files(root: Path):
    files = {}
    for child in sorted(root.rglob("*")):
        if child.is_file():
            name = child.name.lower()
            files.setdefault(name, []).append((child.relative_to(root).as_posix(), child.stat().st_size))
    return files


def is_approx_same_size(size_a: int, size_b: int, tolerance: float) -> bool:
    if size_a == size_b:
        return True
    if size_a == 0 and size_b == 0:
        return True
    largest = max(size_a, size_b)
    if largest == 0:
        return True
    relative_difference = abs(size_a - size_b) / largest
    return relative_difference <= tolerance


def write_csv(path: Path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def compare_directories(root_a: Path, root_b: Path, tolerance: float):
    folder_matches = sorted(collect_folders(root_a) & collect_folders(root_b))
    file_matches = []
    files_a = collect_files(root_a)
    files_b = collect_files(root_b)

    for filename in sorted(set(files_a) & set(files_b)):
        for rel_a, size_a in files_a[filename]:
            for rel_b, size_b in files_b[filename]:
                if is_approx_same_size(size_a, size_b, tolerance):
                    file_matches.append(
                        {
                            "alpha_relative_path": rel_a,
                            "beta_relative_path": rel_b,
                            "alpha_size": size_a,
                            "beta_size": size_b,
                            "relative_difference": round(abs(size_a - size_b) / max(size_a, size_b), 4) if max(size_a, size_b) else 0.0,
                        }
                    )

    return folder_matches, file_matches


def main():
    args = parse_args()
    working_dir = Path.cwd()
    config_path = Path(args.config).expanduser()
    if not config_path.is_absolute():
        config_path = (working_dir / config_path).resolve()

    config_values = load_config(config_path)
    root_a = resolve_directory(config_values[0], working_dir)
    root_b = resolve_directory(config_values[1], working_dir)

    if not root_a.exists() or not root_a.is_dir():
        raise FileNotFoundError(f"Folder not found: {root_a}")
    if not root_b.exists() or not root_b.is_dir():
        raise FileNotFoundError(f"Folder not found: {root_b}")

    folder_matches, file_matches = compare_directories(root_a, root_b, args.tolerance)

    folder_rows = [{"folder_name": folder_name} for folder_name in folder_matches]
    write_csv(working_dir / args.folder_output, folder_rows, ["folder_name"])
    write_csv(working_dir / args.output, file_matches, [
        "alpha_relative_path",
        "beta_relative_path",
        "alpha_size",
        "beta_size",
        "relative_difference",
    ])

    print(f"Compared: {root_a} and {root_b}")
    print(f"Folder matches: {len(folder_rows)}")
    print(f"File matches: {len(file_matches)}")
    print(f"File matches written to: {working_dir / args.output}")
    print(f"Folder matches written to: {working_dir / args.folder_output}")


if __name__ == "__main__":
    main()
