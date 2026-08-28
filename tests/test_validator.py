import importlib.util
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("repository_validator", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class RepositoryValidatorTests(unittest.TestCase):
    def test_valid_fixture_passes_validation(self):
        with self.repository_fixture() as root:
            self.assertEqual([], MODULE.validate(root))

    def test_rejects_private_ip(self):
        with self.repository_fixture() as root:
            address = ".".join(["192", "168", "10", "20"])
            (root / "note.md").write_text(f"endpoint: {address}", encoding="utf-8")
            self.assert_has_error(root, "private_ipv4")

    def test_rejects_secret_assignment(self):
        with self.repository_fixture() as root:
            secret_name = "api" + "_key"
            payload = f'{secret_name} = "not-a-real-secret"'
            (root / "config.py").write_text(payload, encoding="utf-8")
            self.assert_has_error(root, "secret_assignment")

    def test_rejects_forbidden_file(self):
        with self.repository_fixture() as root:
            (root / "production.sqlite").write_bytes(b"synthetic")
            self.assert_has_error(root, "extensão proibida")

    def test_rejects_encoding_damage(self):
        with self.repository_fixture() as root:
            damaged_text = "valida" + "??" + "o"
            (root / "broken.md").write_text(damaged_text, encoding="utf-8")
            self.assert_has_error(root, "encoding_damage")

    @contextmanager
    def repository_fixture(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for relative in MODULE.REQUIRED:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("conteúdo sintético\n", encoding="utf-8")
            yield root

    def assert_has_error(self, root: Path, expected: str):
        errors = MODULE.validate(root)
        self.assertTrue(any(expected in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
