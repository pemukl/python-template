from {{cookiecutter.module_name}}.main import histring


def test_main():
    assert histring().startswith("Your {{cookiecutter.project_name}} journey starts here :)")
