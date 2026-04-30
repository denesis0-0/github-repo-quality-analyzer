def generate_recommendations(scan_result: dict, scores: dict) -> list[str]:
    recommendations = []

    if not scan_result["has_readme"]:
        recommendations.append("Add a README.md with project description and usage instructions.")

    if not scan_result["has_requirements"] and not scan_result["has_pyproject"]:
        recommendations.append("Add requirements.txt or pyproject.toml to make the project reproducible.")

    if not scan_result["has_gitignore"]:
        recommendations.append("Add .gitignore to avoid committing virtual environments, cache files, and local artifacts.")

    if not scan_result["has_src_dir"]:
        recommendations.append("Move reusable code into a src/ directory.")

    if not scan_result["has_tests_dir"]:
        recommendations.append("Add tests/ directory with basic unit tests.")

    if not scan_result["has_notebooks_dir"]:
        recommendations.append("Add notebooks/ directory for experiments or analysis.")

    if not scan_result["has_app_dir"]:
        recommendations.append("Add app/ directory if the project has a demo application.")

    if scan_result["python_file_count"] == 0:
        recommendations.append("Add Python source files to make the project executable and easier to review.")

    if scores["overall"] >= 85:
        recommendations.append("Repository looks strong. Consider adding screenshots, badges, or deployment links.")

    return recommendations
