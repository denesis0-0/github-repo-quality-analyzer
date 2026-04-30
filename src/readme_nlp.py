from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


IDEAL_README = """
Project overview and description.
Описание проекта.
Business problem or motivation.
Бизнес-задача.
Dataset or input data description.
Данные.
Installation instructions.
Установка.
Как запустить проект.
Usage examples.
Пример использования.
Project structure.
Структура проекта.
Technologies and tech stack.
Технологический стек.
Evaluation metrics and results.
Метрики.
Результаты.
Screenshots, plots, demo images.
Графики.
Скриншоты.
Future improvements.
Дальнейшие улучшения.
"""


README_SECTION_KEYWORDS = {
    "description": [
        "описание проекта",
        "о проекте",
        "project overview",
        "description",
    ],
    "problem": [
        "бизнес-задача",
        "ml-задача",
        "задача",
        "business problem",
        "motivation",
    ],
    "data": [
        "данные",
        "dataset",
        "data",
        "целевая переменная",
    ],
    "installation": [
        "как запустить",
        "установка",
        "install",
        "installation",
        "setup",
        "pip install",
    ],
    "usage": [
        "запустить",
        "пример использования",
        "usage",
        "how to use",
        "streamlit run",
        "python -m",
    ],
    "technologies": [
        "технологический стек",
        "технологии",
        "tech stack",
        "technologies",
        "python",
        "scikit-learn",
    ],
    "results": [
        "результаты",
        "метрики",
        "roc-auc",
        "precision",
        "recall",
        "f1",
        "results",
        "metrics",
    ],
    "structure": [
        "структура проекта",
        "project structure",
        "src/",
        "notebooks/",
        "app/",
    ],
    "improvements": [
        "дальнейшие улучшения",
        "future improvements",
        "next steps",
    ],
}


def calculate_similarity_score(readme_text: str) -> int:
    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        analyzer="word",
    )

    matrix = vectorizer.fit_transform([IDEAL_README, readme_text])
    similarity = cosine_similarity(matrix[0], matrix[1])[0][0]

    return round(similarity * 100)


def calculate_section_coverage_score(readme_text: str) -> int:
    text_lower = readme_text.lower()
    matched_sections = 0

    for keywords in README_SECTION_KEYWORDS.values():
        if any(keyword in text_lower for keyword in keywords):
            matched_sections += 1

    return round(matched_sections / len(README_SECTION_KEYWORDS) * 100)


def calculate_readme_nlp_score(readme_text: str) -> int:
    if not readme_text.strip():
        return 0

    similarity_score = calculate_similarity_score(readme_text)
    coverage_score = calculate_section_coverage_score(readme_text)

    return round(0.3 * similarity_score + 0.7 * coverage_score)