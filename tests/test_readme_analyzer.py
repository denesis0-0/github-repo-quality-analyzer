from pathlib import Path

from src.readme_analyzer import analyze_readme


def test_analyze_readme_detects_sections(tmp_path: Path):
    readme_text = """
    # Test Project

    ## Описание проекта

    This project analyzes data.

    ## Как запустить проект

    pip install -r requirements.txt
    streamlit run app/streamlit_app.py

    ## Технологии

    Python, pandas, scikit-learn, Streamlit

    ## Результаты

    ROC-AUC: 0.80

    ![plot](reports/figures/plot.png)
    """

    (tmp_path / "README.md").write_text(readme_text, encoding="utf-8")

    result = analyze_readme(tmp_path)

    assert result["readme_length"] > 0
    assert result["has_readme_description"] is True
    assert result["has_readme_installation"] is True
    assert result["has_readme_usage"] is True
    assert result["has_readme_technologies"] is True
    assert result["has_readme_results"] is True
    assert result["has_readme_images"] is True
    assert "Python" in result["technologies"]
    assert "Streamlit" in result["technologies"]
