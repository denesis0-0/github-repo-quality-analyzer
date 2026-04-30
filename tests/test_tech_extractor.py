from src.tech_extractor import extract_technologies


def test_extract_technologies_detects_known_tools():
    text = """
    This project uses Python, pandas, scikit-learn, XGBoost,
    SHAP and Streamlit.
    """

    technologies = extract_technologies(text)

    assert "Python" in technologies
    assert "pandas" in technologies
    assert "scikit-learn" in technologies
    assert "XGBoost" in technologies
    assert "SHAP" in technologies
    assert "Streamlit" in technologies


def test_extract_technologies_returns_empty_list_for_unknown_text():
    text = "This is a simple project description without known tools."

    technologies = extract_technologies(text)

    assert technologies == []
