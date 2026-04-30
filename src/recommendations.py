def generate_recommendations(
    scan_result: dict,
    readme_result: dict,
    scores: dict,
) -> list[str]:
    recommendations = []

    if not scan_result["has_readme"]:
        recommendations.append("Add a README.md with project description and usage instructions.")
    else:
        if readme_result["readme_length"] < 500:
            recommendations.append("Expand README.md with more details about the project.")

        if not readme_result["has_readme_description"]:
            recommendations.append("Add a clear project description to README.md.")

        if not readme_result["has_readme_installation"]:
            recommendations.append("Add installation or setup instructions to README.md.")

        if not readme_result["has_readme_usage"]:
            recommendations.append("Add usage examples or launch commands to README.md.")

        if not readme_result["has_readme_technologies"]:
            recommendations.append("Add a technologies or tech stack section to README.md.")

        if not readme_result["has_readme_results"]:
            recommendations.append("Add project results, metrics, or output examples to README.md.")

        if not readme_result["has_readme_images"]:
            recommendations.append("Add screenshots, plots, or demo images to README.md.")

    if not scan_result["has_requirements"] and not scan_result["has_pyproject"]:
        recommendations.append("Add requirements.txt or pyproject.toml to make the project reproducible.")

    if not scan_result["has_gitignore"]:
        recommendations.append("Add .gitignore to avoid committing virtual environments, cache files, and local artifacts.")

    if not scan_result["has_src_dir"]:
        recommendations.append("Move reusable code into a src/ directory.")

    if not scan_result["has_tests_dir"]:
        recommendations.append("Add tests/ directory with basic unit tests.")

    if scan_result["python_file_count"] == 0:
        recommendations.append("Add Python source files to make the project executable and easier to review.")

    if scores["overall"] >= 85:
        recommendations.append("Repository looks strong. Consider adding badges, deployment links, or CI checks.")

    return recommendations
