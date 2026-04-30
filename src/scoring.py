def calculate_structure_score(scan_result: dict) -> int:
    checks = [
        scan_result["has_readme"],
        scan_result["has_gitignore"],
        scan_result["has_src_dir"],
        scan_result["has_tests_dir"],
        scan_result["has_notebooks_dir"],
        scan_result["has_app_dir"],
    ]

    return round(sum(checks) / len(checks) * 100)


def calculate_reproducibility_score(scan_result: dict, readme_result: dict) -> int:
    checks = [
        scan_result["has_requirements"] or scan_result["has_pyproject"],
        readme_result["has_readme_installation"],
        readme_result["has_readme_usage"],
        scan_result["python_file_count"] > 0,
    ]

    return round(sum(checks) / len(checks) * 100)


def calculate_code_score(scan_result: dict) -> int:
    score = 0

    if scan_result["python_file_count"] > 0:
        score += 40

    if scan_result["has_src_dir"]:
        score += 30

    if scan_result["has_tests_dir"]:
        score += 20

    if scan_result["total_file_count"] > 5:
        score += 10

    return min(score, 100)


def calculate_documentation_score(readme_result: dict) -> int:
    checks = [
        readme_result["readme_length"] >= 500,
        readme_result["has_readme_description"],
        readme_result["has_readme_installation"],
        readme_result["has_readme_usage"],
        readme_result["has_readme_technologies"],
        readme_result["has_readme_results"],
        readme_result["has_readme_images"],
    ]

    rule_based_score = round(sum(checks) / len(checks) * 100)
    nlp_score = readme_result["nlp_readme_score"]

    return round(0.7 * rule_based_score + 0.3 * nlp_score)


def calculate_scores(scan_result: dict, readme_result: dict) -> dict:
    structure_score = calculate_structure_score(scan_result)
    reproducibility_score = calculate_reproducibility_score(scan_result, readme_result)
    code_score = calculate_code_score(scan_result)
    documentation_score = calculate_documentation_score(readme_result)

    overall_score = round(
        0.25 * structure_score
        + 0.25 * reproducibility_score
        + 0.25 * code_score
        + 0.25 * documentation_score
    )

    return {
        "overall": overall_score,
        "structure": structure_score,
        "reproducibility": reproducibility_score,
        "code": code_score,
        "documentation": documentation_score,
    }
