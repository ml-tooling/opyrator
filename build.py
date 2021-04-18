import glob
import os
import shutil

from universal_build import build_utils
from universal_build.helpers import build_python

# Project specific configuration
MAIN_PACKAGE = "opyrator"
GITHUB_URL = "https://github.com/ml-tooling/opyrator"

HERE = os.path.abspath(os.path.dirname(__file__))


def main(args: dict) -> None:
    # set current path as working dir
    os.chdir(HERE)

    version = args.get(build_utils.FLAG_VERSION)

    if version:
        # Update version in _about.py
        build_python.update_version(
            os.path.join(HERE, f"src/{MAIN_PACKAGE}/_about.py"),
            build_utils._Version.get_pip_compatible_string(str(version)),
            exit_on_error=True,
        )

    if args.get(build_utils.FLAG_MAKE):
        # Install pipenv dev requirements
        build_python.install_build_env(exit_on_error=True)
        # Create API documentation via lazydocs
        build_python.generate_api_docs(
            github_url=GITHUB_URL, main_package=MAIN_PACKAGE, exit_on_error=True
        )
        # Build distribution via setuptools
        build_python.build_distribution(exit_on_error=True)

        # Copy distribution to playground
        try:
            dist_name = MAIN_PACKAGE.replace("_", "-")
            dist_file = glob.glob(f"./dist/{dist_name}-*.tar.gz")[0]
            shutil.copy(
                dist_file,
                os.path.join(HERE, "playground", "resources", dist_name + ".tar.gz"),
            )
        except Exception as ex:
            build_utils.log(
                "Failed to copy distribution to playground container " + str(ex)
            )
            build_utils.exit_process(1)

        # Copy all Demo artifacts (only py and txt files for now)
        files = []
        for ext in ("*.py", "*.txt"):
            files.extend(
                glob.glob(os.path.join(HERE, "examples", "**", ext), recursive=True)
            )

        DEMO_PATH = os.path.join(HERE, "playground", "resources", "demos")
        if os.path.exists(DEMO_PATH):
            shutil.rmtree(DEMO_PATH)

        for file in files:
            new_path = os.path.join(
                DEMO_PATH,
                os.path.relpath(file, os.path.join(HERE, "examples")),
            )
            os.makedirs(os.path.dirname(new_path), exist_ok=True)

            shutil.copy(file, new_path)

    if args.get(build_utils.FLAG_CHECK):
        build_python.code_checks(exit_on_error=True, safety=False)

    if args.get(build_utils.FLAG_TEST):
        # Remove coverage files
        build_utils.run("pipenv run coverage erase", exit_on_error=False)

        test_markers = args.get(build_utils.FLAG_TEST_MARKER)

        if (
            isinstance(test_markers, list)
            and build_utils.TEST_MARKER_SLOW in test_markers
        ):
            # Run if slow test marker is set: test in multiple environments
            # Python 3.6
            build_python.test_with_py_version(
                python_version="3.6.12", exit_on_error=True
            )

            # Python 3.7
            # build_python.test_with_py_version(
            #    python_version="3.7.9", exit_on_error=True
            # )

            # Activated Python Environment (3.8)
            build_python.install_build_env()
            # Run pytest in pipenv environment
            build_utils.run("pipenv run pytest", exit_on_error=True)

            # Update pipfile.lock when all tests are successfull (lock environment)
            build_utils.run("pipenv lock", exit_on_error=True)
        else:
            # Run fast tests
            build_utils.run('pipenv run pytest -m "not slow"', exit_on_error=True)

    if args.get(build_utils.FLAG_RELEASE):
        # Publish distribution on pypi
        build_python.publish_pypi_distribution(
            pypi_token=args.get(build_python.FLAG_PYPI_TOKEN),
            pypi_repository=args.get(build_python.FLAG_PYPI_REPOSITORY),
        )

        # TODO: Publish coverage report: if private repo set CODECOV_TOKEN="token" or use -t
        # build_utils.run("curl -s https://codecov.io/bash | bash -s", exit_on_error=False)
        pass

    # Build the opyrator playground component
    build_utils.build("playground", args)


if __name__ == "__main__":
    args = build_python.parse_arguments()
    main(args)
