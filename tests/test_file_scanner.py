from pathlib import Path

from src.file_scanner import scan_repository


def test_scan_repository_detects_project_files(tmp_path: Path):
    (tmp_path / "README.md").write_text("# Test project")
    (tmp_path / "requirements.txt").write_text("pandas")
    (tmp_path / ".gitignore").write_text(".venv/")
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "main.py").write_text("print('hello')")
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_main.py").write_text("def test_example(): assert True")
    (tmp_path / "notebooks").mkdir()
    (tmp_path / "notebooks" / "eda.ipynb").write_text("{}")
    (tmp_path / "app").mkdir()
    (tmp_path / "app" / "streamlit_app.py").write_text("print('app')")

    result = scan_repository(tmp_path)

    assert result["has_readme"] is True
    assert result["has_requirements"] is True
    assert result["has_gitignore"] is True
    assert result["has_src_dir"] is True
    assert result["has_tests_dir"] is True
    assert result["has_notebooks_dir"] is True
    assert result["has_app_dir"] is True
    assert result["python_file_count"] == 3
    assert result["notebook_count"] == 1
