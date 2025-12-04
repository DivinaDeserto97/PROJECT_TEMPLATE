import importlib

DEPENDENCIES = ["dotenv", "pytest", "black", "ruff"]


def test_dependencies_are_importable():
    for name in DEPENDENCIES:
        module = importlib.import_module(name)
        assert module is not None, f"Modul {name} konnte nicht importiert werden"
