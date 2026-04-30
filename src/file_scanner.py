from pathlib import Path


def scan_repository(repo_path: str | Path) -> dict:
    repo_path = Path(repo_path)

    if not repo_path.exists():
        raise FileNotFoundError(f"Repository path does not exist: {repo_path}")

    files = [path for path in repo_path.rglob("*") if path.is_file()]
    relative_files = [path.relative_to(repo_path) for path in files]

    file_names = {path.name.lower() for path in relative_files}
    top_level_dirs = {
        path.parts[0].lower()
        for path in relative_files
        if len(path.parts) > 1
    }

    python_files = [path for path in relative_files if path.suffix == ".py"]
    notebooks = [path for path in relative_files if path.suffix == ".ipynb"]

    return {
        "has_readme": any(name.startswith("readme") for name in file_names),
        "has_requirements": "requirements.txt" in file_names,
        "has_pyproject": "pyproject.toml" in file_names,
        "has_gitignore": ".gitignore" in file_names,
        "has_src_dir": "src" in top_level_dirs,
        "has_tests_dir": "tests" in top_level_dirs,
        "has_notebooks_dir": "notebooks" in top_level_dirs,
        "has_app_dir": "app" in top_level_dirs,
        "python_file_count": len(python_files),
        "notebook_count": len(notebooks),
        "total_file_count": len(relative_files),
    }
