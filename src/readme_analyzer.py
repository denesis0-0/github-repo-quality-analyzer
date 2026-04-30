from pathlib import Path


README_FILENAMES = {"readme.md", "readme.rst", "readme.txt"}


def find_readme(repo_path: str | Path) -> Path | None:
    repo_path = Path(repo_path)

    for path in repo_path.iterdir():
        if path.is_file() and path.name.lower() in README_FILENAMES:
            return path

    return None


def read_readme(repo_path: str | Path) -> str:
    readme_path = find_readme(repo_path)

    if readme_path is None:
        return ""

    return readme_path.read_text(encoding="utf-8", errors="ignore")


def analyze_readme(repo_path: str | Path) -> dict:
    text = read_readme(repo_path)
    text_lower = text.lower()

    has_description = any(
        keyword in text_lower
        for keyword in ["overview", "description", "описание", "о проекте"]
    )

    has_installation = any(
        keyword in text_lower
        for keyword in [
            "installation",
            "install",
            "setup",
            "requirements",
            "dependencies",
            "pip install",
            "установка",
            "установить",
            "зависимости",
            "настройка",
        ]
    )

    has_usage = any(
        keyword in text_lower
        for keyword in [
            "usage",
            "how to use",
            "quick start",
            "getting started",
            "run",
            "launch",
            "example",
            "examples",
            "demo",
            "пример",
            "примеры",
            "как использовать",
            "как запустить",
            "запустить",
            "запуск",
            "использование",
        ]
    )

    has_technologies = any(
        keyword in text_lower
        for keyword in ["tech stack", "technologies", "tools", "стек", "технологии"]
    )

    has_results = any(
        keyword in text_lower
        for keyword in ["results", "metrics", "roc-auc", "accuracy", "результаты", "метрики"]
    )

    has_images = any(
        marker in text_lower
        for marker in ["![", "<img", ".png", ".jpg", ".jpeg", ".gif"]
    )

    return {
        "readme_length": len(text),
        "has_readme_description": has_description,
        "has_readme_installation": has_installation,
        "has_readme_usage": has_usage,
        "has_readme_technologies": has_technologies,
        "has_readme_results": has_results,
        "has_readme_images": has_images,
    }
