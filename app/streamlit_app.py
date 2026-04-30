import sys
from pathlib import Path

import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.report import analyze_github_repository


st.set_page_config(
    page_title="GitHub Repo Quality Analyzer",
    page_icon="📊",
    layout="wide",
)


st.title("GitHub Repository Quality Analyzer")

st.markdown(
    """
    Tool for analyzing GitHub repository quality and portfolio readiness.

    Enter a public GitHub repository URL to get structure, reproducibility,
    code quality scores, and improvement recommendations.
    """
)


repo_url = st.text_input(
    "GitHub repository URL",
    value="https://github.com/denesis0-0/credit-risk-scoring.git",
)

analyze_button = st.button("Analyze repository")


def score_status(score: int) -> str:
    if score >= 85:
        return "Excellent"

    if score >= 70:
        return "Good"

    if score >= 50:
        return "Needs improvement"

    return "Weak"


if analyze_button:
    if not repo_url.strip():
        st.error("Please enter a GitHub repository URL.")
    else:
        with st.spinner("Cloning and analyzing repository..."):
            try:
                report = analyze_github_repository(repo_url.strip())
            except Exception as error:
                st.error(f"Failed to analyze repository: {error}")
                st.stop()

        scores = report["scores"]
        scan_result = report["scan_result"]
        readme_result = report["readme_result"]
        recommendations = report["recommendations"]

        st.subheader("Overall score")

        st.metric("Portfolio readiness score", f"{scores['overall']}/100")

        st.subheader("Category scores")

        score_table = pd.DataFrame(
            [
                {
                    "Category": "Documentation",
                    "Score": scores["documentation"],
                    "Status": score_status(scores["documentation"]),
                },
                {
                    "Category": "Structure",
                    "Score": scores["structure"],
                    "Status": score_status(scores["structure"]),
                },
                {
                    "Category": "Reproducibility",
                    "Score": scores["reproducibility"],
                    "Status": score_status(scores["reproducibility"]),
                },
                {
                    "Category": "Code",
                    "Score": scores["code"],
                    "Status": score_status(scores["code"]),
                },
            ]
        )

        st.dataframe(score_table, use_container_width=True)

        st.subheader("Repository checks")

        checks = {
            "README": scan_result["has_readme"],
            "requirements.txt": scan_result["has_requirements"],
            "pyproject.toml": scan_result["has_pyproject"],
            ".gitignore": scan_result["has_gitignore"],
            "src/ directory": scan_result["has_src_dir"],
            "tests/ directory": scan_result["has_tests_dir"],
            "notebooks/ directory": scan_result["has_notebooks_dir"],
            "app/ directory": scan_result["has_app_dir"],
        }

        check_table = pd.DataFrame(
            [
                {
                    "Check": check_name,
                    "Passed": "Yes" if passed else "No",
                }
                for check_name, passed in checks.items()
            ]
        )

        st.dataframe(check_table, use_container_width=True)

        st.subheader("README checks")

        readme_checks = {
            "Description": readme_result["has_readme_description"],
            "Installation": readme_result["has_readme_installation"],
            "Usage": readme_result["has_readme_usage"],
            "Technologies": readme_result["has_readme_technologies"],
            "Results / Metrics": readme_result["has_readme_results"],
            "Images / Screenshots": readme_result["has_readme_images"],
        }

        readme_table = pd.DataFrame(
            [
                {
                    "Check": check_name,
                    "Passed": "Yes" if passed else "No",
                }
                for check_name, passed in readme_checks.items()
            ]
        )

        st.dataframe(readme_table, use_container_width=True)
        st.metric("README length", readme_result["readme_length"])

        st.subheader("Repository statistics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Python files", scan_result["python_file_count"])

        with col2:
            st.metric("Notebooks", scan_result["notebook_count"])

        with col3:
            st.metric("Total files", scan_result["total_file_count"])

        st.subheader("Recommendations")

        if recommendations:
            for recommendation in recommendations:
                st.write(f"- {recommendation}")
        else:
            st.success("No recommendations. Repository looks strong.")
