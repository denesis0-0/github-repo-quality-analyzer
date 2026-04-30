from pathlib import Path

from src.file_scanner import scan_repository
from src.readme_analyzer import analyze_readme
from src.recommendations import generate_recommendations
from src.repo_loader import TemporaryRepository
from src.scoring import calculate_scores


def build_report(repo_path: str | Path) -> dict:
    scan_result = scan_repository(repo_path)
    readme_result = analyze_readme(repo_path)

    scores = calculate_scores(scan_result, readme_result)
    recommendations = generate_recommendations(scan_result, readme_result, scores)

    return {
        "scan_result": scan_result,
        "readme_result": readme_result,
        "scores": scores,
        "recommendations": recommendations,
    }


def analyze_local_repository(repo_path: str | Path) -> dict:
    return build_report(repo_path)


def analyze_github_repository(repo_url: str) -> dict:
    with TemporaryRepository(repo_url) as repo_path:
        return build_report(repo_path)
