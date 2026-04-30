from src.scoring import calculate_scores


def test_calculate_scores_returns_expected_keys():
    scan_result = {
        "has_readme": True,
        "has_requirements": True,
        "has_pyproject": False,
        "has_gitignore": True,
        "has_src_dir": True,
        "has_tests_dir": True,
        "has_notebooks_dir": True,
        "has_app_dir": True,
        "python_file_count": 5,
        "notebook_count": 2,
        "total_file_count": 15,
    }

    readme_result = {
        "readme_length": 1000,
        "has_readme_description": True,
        "has_readme_installation": True,
        "has_readme_usage": True,
        "has_readme_technologies": True,
        "has_readme_results": True,
        "has_readme_images": False,
        "technologies": ["Python", "Streamlit"],
        "technology_count": 2,
    }

    scores = calculate_scores(scan_result, readme_result)

    assert set(scores.keys()) == {
        "overall",
        "structure",
        "reproducibility",
        "code",
        "documentation",
    }

    for score in scores.values():
        assert 0 <= score <= 100
