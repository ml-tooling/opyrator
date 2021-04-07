<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    opyrator
</h1>

<p align="center">
    <strong>Python functions with superpowers. Instantly deploy with REST API, UI, and more.</strong>
</p>

<p align="center">
    <a href="https://github.com/ml-tooling/opyrator/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://github.com/ml-tooling/opyrator/actions?query=workflow%3Abuild-pipeline" title="Build status"><img src="https://img.shields.io/github/workflow/status/ml-tooling/opyrator/build-pipeline?style=flat"></a>
    <a href="ttps://mltooling.substack.com/subscribe" title="Subscribe to newsletter"><img src="http://bit.ly/2Md9rxM"></a>
    <a href="https://twitter.com/mltooling" title="Follow on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social&label=Follow"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features & Screenshots</a> •
  <a href="#support--feedback">Support</a> •
  <a href="https://github.com/ml-tooling/opyrator/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#contribution">Contribution</a> •
  <a href="https://github.com/ml-tooling/opyrator/releases">Changelog</a>
</p>

Opyrator enables you to instantly turn a simple Python function into a powerful web service that includes a REST API and a full-blown graphical UI. It can be saved & shared as self-contained executable file and instantly deployed & scaled for production usage. Opyrator is powered by Pydantic, FastAPI, and Streamlit and enables you to build your web apps and services within seconds.

## Highlights

- 🪄&nbsp; Turn functions into production-ready services within seconds.
- 🔌&nbsp; Auto-generated REST API based on FastAPI.
- 🌅&nbsp; Auto-generated UI based on Streamlit.
- 📦&nbsp; Save and share as self-contained executable file.
- 📈&nbsp; Instantly deploy and scale for production usage.
- Export to Docker, Pex, ...

## Getting Started

### Installation

> _Requirements: Python 3.6+._

```bash
pip install opyrator
```

### Usage

1. A simple opyrator-compatible function could look like this:

    ```python
    from pydantic import BaseModel
    import time

    def Input(BaseModel):
        text: str
        wait: int

    def Output(BaseModel):
        text: str

    def hello_world(input: Input) -> Output:
        time.sleep(input.wait)
        return Output(text=input.text)
    ```
    _Requirements: The function needs to be annotated with typing hints, and the `input` parameter and return value needs to be based on [Pydantic Models](https://pydantic-docs.helpmanual.io/)._

2. Copy this code to a file `opyrator.py`
3. Run the UI server from command-line:

    ```
    opyrator launch-ui opyrator:hello_world
    ```
    _In the output, there's a line that shows where your web app is being served, on your local machine._

    TODO: Add screenshot

4. Run the REST API server from command-line:

    ```
    opyrator launch-api opyrator:hello_world
    ```
    _In the output, there's a line that shows where your web service is being served, on your local machine._

    TODO: Add screenshot
5. Find out more usage details and features in the [Features](#features) section.

## Support & Feedback

This project is maintained by [Benjamin Räthlein](https://twitter.com/raethlein), [Lukas Masuch](https://twitter.com/LukasMasuch), and [Jan Kalkan](https://www.linkedin.com/in/jan-kalkan-b5390284/). Please understand that we won't be able to provide individual support via email. We also believe that help is much more valuable if it's shared publicly so that more people can benefit from it.

| Type                     | Channel                                              |
| ------------------------ | ------------------------------------------------------ |
| 🚨&nbsp; **Bug Reports**       | <a href="https://github.com/ml-tooling/opyrator/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3Abug+sort%3Areactions-%2B1-desc+" title="Open Bug Report"><img src="https://img.shields.io/github/issues/ml-tooling/opyrator/bug.svg?label=bug"></a>                                 |
| 🎁&nbsp; **Feature Requests**  | <a href="https://github.com/ml-tooling/opyrator/issues?q=is%3Aopen+is%3Aissue+label%3Afeature+sort%3Areactions-%2B1-desc" title="Open Feature Request"><img src="https://img.shields.io/github/issues/ml-tooling/opyrator/feature.svg?label=feature%20request"></a>                                 |
| 👩‍💻&nbsp; **Usage Questions**   |  <a href="https://github.com/ml-tooling/opyrator/issues?q=is%3Aopen+is%3Aissue+label%3Asupport+sort%3Areactions-%2B1-desc" title="Open Support Request"> <img src="https://img.shields.io/github/issues/ml-tooling/opyrator/support.svg?label=support%20request"></a> <a href="https://gitter.im/ml-tooling/community" title="Chat on Gitter"><img src="https://badges.gitter.im/ml-tooling/community.svg"></a> |
| 📢&nbsp; **Announcements** | <a href="https://gitter.im/ml-tooling/community" title="Chat on Gitter"><img src="https://badges.gitter.im/mml-tooling/community.svg"></a>  <a href="https://mltooling.substack.com/subscribe" title="Subscribe for updates"><img src="http://bit.ly/2Md9rxM"></a> <a href="https://twitter.com/mltooling" title="ML Tooling on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social&label=Follow"> |
| ❓&nbsp; **Other Requests** | <a href="mailto:team@ml-tooling.org" title="Email ML Tooling Team"><img src="https://img.shields.io/badge/email-ML Tooling-green?logo=mail.ru&logoColor=white"></a> |

## Features

_Use this section for advertising the most important features and advantages of the project. Also, add screenshots or examples to showcase important features. The main purpose of this section is marketing._

## Documentation

_Either put the documentation here or use a deployed documentation site via mkdocs and link to the documentation._

Please refer to [our documentation](#TODO) for information about deployment or usage.

## FAQ

<details>
<summary><b>This is the example description of an faq item</b> (click to expand...)</summary>
</details>

## Known Issues

<details>
<summary><b>This is the example description of a known issue</b> (click to expand...)</summary>
</details>

## Contribution

- Pull requests are encouraged and always welcome. Read our [contribution guidelines](https://github.com/ml-tooling/opyrator/tree/main/CONTRIBUTING.md) and check out [help-wanted](https://github.com/ml-tooling/opyrator/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A"help+wanted"+sort%3Areactions-%2B1-desc+) issues.
- Submit Github issues for any [feature request and enhancement](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=feature&template=02_feature-request.md&title=), [bugs](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=bug&template=01_bug-report.md&title=), or [documentation](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=documentation&template=03_documentation.md&title=) problems.
- By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/ml-tooling/opyrator/blob/main/.github/CODE_OF_CONDUCT.md).
- The [development section](#development) below contains information on how to build and test the project after you have implemented some changes.

## Development

> _**Requirements**: [Docker](https://docs.docker.com/get-docker/) and [Act](https://github.com/nektos/act#installation) are required to be installed on your machine to execute the containerized build process._

To simplify the process of building this project from scratch, we provide build-scripts - based on [universal-build](https://github.com/ml-tooling/universal-build) - that run all necessary steps (build, check, test, and release) within a containerized environment. To build and test your changes, execute the following command in the project root folder:

```bash
act -b -j build
```

Refer to our [contribution guides](https://github.com/ml-tooling/opyrator/blob/main/CONTRIBUTING.md#development-instructions) for more detailed information on our build scripts and development process.

---

Licensed **MIT**. Created and maintained with ❤️&nbsp; by developers from Berlin.
