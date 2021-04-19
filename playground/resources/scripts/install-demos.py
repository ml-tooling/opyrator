import os
import sys
from subprocess import call

RESOURCES_PATH = os.getenv("RESOURCES_PATH", "/resources")
DEMO_DIRECTORY = os.path.join(RESOURCES_PATH, "demos")
demos = [
    d
    for d in os.listdir(DEMO_DIRECTORY)
    if os.path.isdir(os.path.join(DEMO_DIRECTORY, d))
]

for demo in demos:
    # Install requirements
    call(
        f"{sys.executable} -m pip install --no-cache-dir -r "
        + os.path.join(DEMO_DIRECTORY, demo, "requirements.txt"),
        shell=True,
    )
    # Run app
    call(
        f"{sys.executable} " + os.path.join(DEMO_DIRECTORY, demo, "app.py"),
        shell=True,
    )
