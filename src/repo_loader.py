from pathlib import Path
from tempfile import TemporaryDirectory

from git import Repo


class TemporaryRepository:
    def __init__(self, repo_url: str):
        self.repo_url = repo_url
        self._temp_dir = None
        self.repo_path = None

    def __enter__(self) -> Path:
        self._temp_dir = TemporaryDirectory()
        self.repo_path = Path(self._temp_dir.name) / "repo"

        Repo.clone_from(self.repo_url, self.repo_path)

        return self.repo_path

    def __exit__(self, exc_type, exc_value, traceback):
        if self._temp_dir is not None:
            self._temp_dir.cleanup()
