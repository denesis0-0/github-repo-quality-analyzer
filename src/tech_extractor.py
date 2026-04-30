import re


TECH_KEYWORDS = {
    "Python": ["python"],
    "pandas": ["pandas"],
    "NumPy": ["numpy", "np"],
    "scikit-learn": ["scikit-learn", "sklearn"],
    "XGBoost": ["xgboost"],
    "LightGBM": ["lightgbm"],
    "CatBoost": ["catboost"],
    "SHAP": ["shap"],
    "Streamlit": ["streamlit"],
    "Jupyter": ["jupyter", "notebook", "ipynb"],
    "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"],
    "SQL": ["sql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "FastAPI": ["fastapi"],
    "Flask": ["flask"],
    "Django": ["django"],
    "Docker": ["docker", "dockerfile"],
    "Git": ["git"],
    "GitHub": ["github"],
    "PyTorch": ["pytorch", "torch"],
    "TensorFlow": ["tensorflow"],
    "Transformers": ["transformers", "huggingface", "hugging face"],
    "MLflow": ["mlflow"],
    "pytest": ["pytest"],
}


def extract_technologies(text: str) -> list[str]:
    text_lower = text.lower()
    found_technologies = []

    for technology, keywords in TECH_KEYWORDS.items():
        for keyword in keywords:
            pattern = rf"(?<![a-zA-Z0-9]){re.escape(keyword)}(?![a-zA-Z0-9])"

            if re.search(pattern, text_lower):
                found_technologies.append(technology)
                break

    return sorted(found_technologies)
