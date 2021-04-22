<!-- markdownlint-disable MD033 MD041 -->
<h1 align="center">
    Opyrator
</h1>

<p align="center">
    <strong>Turn your Python functions into production-ready microservices with HTTP API, UI, and more.</strong>
</p>

<p align="center">
    <a href="https://pypi.org/project/opyrator/" title="PyPi Version"><img src="https://img.shields.io/pypi/v/opyrator?color=green&style=flat"></a>
    <a href="https://pypi.org/project/opyrator/" title="Python Version"><img src="https://img.shields.io/badge/Python-3.6%2B-blue&style=flat"></a>
    <a href="https://github.com/ml-tooling/opyrator/blob/main/LICENSE" title="Project License"><img src="https://img.shields.io/badge/License-MIT-green.svg"></a>
    <a href="https://github.com/ml-tooling/opyrator/actions?query=workflow%3Abuild-pipeline" title="Build status"><img src="https://img.shields.io/github/workflow/status/ml-tooling/opyrator/build-pipeline?style=flat"></a>
    <a href="ttps://mltooling.substack.com/subscribe" title="Subscribe to newsletter"><img src="http://bit.ly/2Md9rxM"></a>
    <a href="https://twitter.com/mltooling" title="Follow on Twitter"><img src="https://img.shields.io/twitter/follow/mltooling.svg?style=social&label=Follow"></a>
</p>

<p align="center">
  <a href="#getting-started">Getting Started</a> •
  <a href="#features">Features</a> •
  <a href="#examples">Examples</a> •
  <a href="#support--feedback">Support</a> •
  <a href="https://github.com/ml-tooling/opyrator/issues/new?labels=bug&template=01_bug-report.md">Report a Bug</a> •
  <a href="#contribution">Contribution</a> •
  <a href="https://github.com/ml-tooling/opyrator/releases">Changelog</a>
</p>

Instantly turn your Python functions into production-ready microservices. Deploy and access your services via HTTP API or interactive UI. Seamlessly export your services into portable, shareable, and executable files or Docker images. Opyrator builds on open standards - OpenAPI,  JSON Schema, and Python type hints - and is powered by FastAPI, Streamlit, and Pydantic. It cuts out all the pain for productizing and sharing your Python code - or anything you can wrap into a single Python function.

<sup>Alpha Version: Only suggested for experimental usage.</sup>

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-header.png"/>

---

<p align="center">
     Try out and explore various examples in our playground <a href="https://opyrator-playground.mltooling.org">here</a>.
</p>

---

## Highlights

- 🪄&nbsp; Turn functions into production-ready services within seconds.
- 🔌&nbsp; Auto-generated HTTP API based on FastAPI.
- 🌅&nbsp; Auto-generated Web UI based on Streamlit.
- 📦&nbsp; Save and share as self-contained executable file or Docker image.
- 🧩&nbsp; Reuse pre-defined components & combine with existing Opyrators.
- 📈&nbsp; Instantly deploy and scale for production usage.

## Getting Started

### Installation

> _Requirements: Python 3.6+._

```bash
pip install opyrator
```

### Usage

1. A simple Opyrator-compatible function could look like this:

    ```python
    from pydantic import BaseModel

    class Input(BaseModel):
        message: str

    class Output(BaseModel):
        message: str

    def hello_world(input: Input) -> Output:
        """Returns the `message` of the input data."""
        return Output(message=input.message)
    ```

    _💡 An Opyrator-compatible function is required to have an `input` parameter and return value based on [Pydantic models](https://pydantic-docs.helpmanual.io/). The input und output models are specified via [type hints](https://docs.python.org/3/library/typing.html)._

2. Copy this code to a file, e.g. `my_opyrator.py`
3. Run the UI server from command-line:

    ```bash
    opyrator launch-ui my_opyrator:hello_world
    ```

    _In the output, there's a line that shows where your web app is being served, on your local machine._

    <img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-hello-world-ui.png"/>

4. Run the HTTP API server from command-line:

    ```bash
    opyrator launch-api my_opyrator:hello_world
    ```
    _In the output, there's a line that shows where your web service is being served, on your local machine._

    <img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-hello-world-api.png"/>

5. Find out more usage information in the [Features](#features) section or get inspired by our [examples](#examples).

## Examples

---

<p align="center">
     👉&nbsp; Try out and explore these examples in our playground <a href="https://opyrator-playground.mltooling.org">here</a>
</p>

---

The following collection of examples demonstrate how Opyrator can support a variety of different tasks and use-cases. All these examples are bundled into a demo playground which you can also deploy on your own machine via Docker:

```bash
docker run -p 8080:8080 mltooling/opyrator-playground:latest
```

### Text Generation

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/text-generation-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/generate_text/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/generate_text_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/generate-text-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/generate_text/
pip install -r requirements.txt
opyrator launch-ui app:generate_text --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Question Answering

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/question-answering-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/question_answering/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/question_answering_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/question-answering-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/question_answering/
pip install -r requirements.txt
opyrator launch-ui app:question_answering --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Image Super Resolution

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/image-super-resolution-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/image_super_resolution/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/image_super_resolution_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/image-super-resolution-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/image_super_resolution/
pip install -r requirements.txt
opyrator launch-ui app:image_super_resolution --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Text Preprocessing

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/text-preprocessing-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/preprocess_text/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/preprocess_text_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/preprocess-text-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/preprocess_text/
pip install -r requirements.txt
opyrator launch-ui app:preprocess_text --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Language Detection

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/language-detection-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/detect_language/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/detect_language_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/detect-language-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/detect_language/
pip install -r requirements.txt
opyrator launch-ui app:detect_language --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Audio Seperation

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/audio-seperation-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/seperate_audio/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/seperate_audio_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/seperate-audio-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/seperate_audio/
pip install -r requirements.txt
opyrator launch-ui app:seperate_audio --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Word Vectors Training

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/train-word-vectors-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/train_word_vectors/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/train_word_vectors_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/train-word-vectors-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/train_word_vectors/
pip install -r requirements.txt
opyrator launch-ui app:train_word_vectors --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Named Entity Recognition

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/named-entity-recognition-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/named_entity_recognition/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/named_entity_recognition_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/named-entity-recognition-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/named_entity_recognition/
pip install -r requirements.txt
opyrator launch-ui app:named_entity_recognition --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

### Components Showcase

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/components-showcase-demo.png"/>

- 📄&nbsp; [Source Code](https://github.com/ml-tooling/opyrator/blob/main/examples/showcase_components/app.py)
- 🌅&nbsp; [UI Demo](https://play.mltooling.com/opyrator/demos/showcase_components_ui/)
- 🔌&nbsp; [OpenAPI Spec](https://editor.swagger.io/?url=https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/openapi-demo-specs/showcase-components-openapi-spec.json)

<details>
<summary>Run this demo on your machine (click to expand...)</summary>

To run the demo on your local machine just execute the following commands:

```bash
git clone https://github.com/ml-tooling/opyrator
cd ./opyrator/examples/showcase_components/
pip install -r requirements.txt
opyrator launch-ui app:showcase_components --port 8051
```

Visit http://localhost:8051 in your browser to access the UI of the demo. Use `launch-api` instead of `launch-ui` to launch the HTTP API server.

</details>

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

<p align="center">
  <a href="#http-api">HTTP API</a> •
  <a href="#graphical-ui">Graphical UI</a> •
  <a href="#command-line-interface">CLI</a> •
  <a href="#zip-export">Zip Export</a> •
  <a href="#docker-export">Docker Export</a> •
  <a href="#pre-defined-components">Pre-defined Components</a> •
  <a href="#production-deployment">Production Deployment</a>
</p>

### HTTP API

With Opyrator, you can instantly launch a local HTTP (REST) API server for any [compatible function](#compatible-functions):

```bash
opyrator launch-api my_opyrator:hello_world
```

This will launch a [FastAPI](https://fastapi.tiangolo.com/) server based on the [OpenAPI standard](https://swagger.io/specification) and with an automatic interactive documentation.

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-hello-world-api.png"/>

_💡 Make sure that all requirements of your script are installed in the active Python enviornment._

The port used by the API server can be provided via CLI arguments:

```bash
opyrator launch-api my_opyrator:hello_world --port 8080
```

The API server can also be started via the exported zip-file format (see [zip export section](#zip-export) below).

```bash
opyrator launch-api my-opyrator.zip
```

### Graphical UI

You can launch a graphical user interface - powered by  [Streamlit](https://streamlit.io/) - for your [compatible function](#compatible-functions). The UI is auto-generated from the input- and output-schema of the given function.

```bash
opyrator launch-ui my_opyrator:hello_world
```

<img style="width: 100%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-hello-world-ui.png"/>

_💡 Make sure that all requirements of your script are installed in the active Python environment._

You can influence most aspects of the UI just by changing and improving the input- and output-schema of your function. Furthermore, it is also possible to define custom UIs for the function's input and output. For more details, refer to the [input- and output-schema](#TODO) section.

The port used by the UI server can be provided via CLI arguments:

```bash
opyrator launch-ui my_opyrator:hello_world --port 8080
```

The UI server can also be started via the exported zip-file format (see [zip export section](#zip-export) below).

```bash
opyrator launch-ui my-opyrator.zip
```

In addition, the UI server can be started by using an already running Opyrator API endpoint:

```bash
opyrator launch-ui http://my-opyrator:8080 
```

Thereby, all Opyrator calls from the UI will be executed via the configured HTTP endpoint instead of the Python function running inside the UI server.

### Command-line Interface

An Opyrator can also be executed via command-line:

```bash
opyrator call my_opyrator:hello_world '{"message": "hello"}'
```

<img style="width: 80%" src="https://raw.githubusercontent.com/ml-tooling/opyrator/main/docs/images/opyrator-cli.png"/>

The CLI interface also works using the [zip export format](#zip-export):

```bash
opyrator call my-opyrator.zip '{"message": "hello"}'
```

Or, by using an already running Opyrator API endpoint:

```bash
opyrator call http://my-opyrator:8080 '{"message": "hello"}'
```

Thereby, the function call is executed by the Opyrator API server, instead of locally using the Python function.

### Zip Export

Opyrator allows you to package and export a [compatible function](#compatible-functions) into a self-contained zip-file:

```bash
opyrator export my_opyrator:hello_world my-opyrator.zip
```

This exported zip-file packages relevant source code and data artifacts into a single file which can be shared, stored, and used for launching the API or UI as shown above.

External requirements are automatically discovered from the working directory based on the following files: `Pipfile` (Pipenv environment), `environment.yml` (Conda environment), `pyproject.toml` (Poetry dependencies), `requirements.txt` (pip-requirements), `setup.py` (Python project requirements), `packages.txt` (apt-get packages), or discovered via [pipreqs](https://github.com/bndr/pipreqs) as fallback. However, external requirements are only included as instructions and are not packaged into the zip-file. If you want to export your Opyrator fully self-contained including all requirements or even the Python interpreter itself, please refer to the [Docker](#docker-export) or [pex](#pex-export) export options.

As a side note, Opyrators exported as zip-files are (mini) Python libraries that can be pip-installed, imported, and used from other Python code:

```bash
pip install my-opyrator.zip
```

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/3)_

### Docker Export

In addition to the ZIP export, Opyrator also provides the capability to export to a Docker image:

```bash
opyrator export my_opyrator:hello_world --format=docker my-opyrator-image:latest
```

_💡 The Docker export requires that Docker is installed on your machine._

After the successful export, the Docker image can be run as shown below:

```bash
docker run -p 8080:8080 my-opyrator-image:latest
```

Running your Opyrator within this Docker image has the advantage that only a single port is required to be exposed. The separation between UI and API is done via URL paths: `http://localhost:8080/api` (API); `http://localhost:8080/ui` (UI). The UI is automatically configured to use the API for all function calls.

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/4)._

### Pex Export

Opyrator also provides the capability to export to a pex-file. [Pex](https://github.com/pantsbuild/pex) is a tool to create self-contained executable Python environments that contain all relevant python dependencies.

```bash
opyrator export my_opyrator:hello_world --format=pex my-opyrator.pex
```

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/5)._

### Python Client

Every deployed Opyrator provides a Python client library via an endpoint method which can be installed with pip:

```bash
pip install http://my-opyrator:8080/client
```

And used in your code, as shown below:

```python
from my_opyrator import Client, Input
opyrator_client = Client("http://my-opyrator:8080")
result = opyrator_client.call(Input(text="hello", wait=1))
```

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/8)._

### Pre-defined Components

Opyrator provides a growing collection of pre-defined components (input- and output models) for common tasks. Some of these components also provide more advanced UIs and Visualizations. You can reuse these components to speed up your development and, thereby, keep your Opyrators compatible with other functionality improvements or other Opyrators.

You can find some of the available interfaces in the [examples](#examples) section or in this [source code package](#TODO).

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/9)._

### Production Deployment

Rolling out your Opyrators for production usage might require additional features such as SSL, authentication, API tokens, unlimited scalability, load balancing, and monitoring. Therefore, we provide capabilities to easily  deploy your Opyrators directly on scalable and secure cloud platforms without any major overhead:

```bash
opyrator deploy my_opyrator:hello_world <deployment-provider> <deployment-provider-options>
```

_WIP: This feature is not finalized yet. You can track the progress and vote for the feature [here](https://github.com/ml-tooling/opyrator/issues/6)._

## Documentation

### Compatible Functions

A function is compatible with Opyrator if it fulfills the following requirements:

- A single parameter called `input` which MUST be a subclass of the [Pydantic BaseModel](https://pydantic-docs.helpmanual.io/usage/models/).
- A single return value that MUST be a subclass of the [Pydantic BaseModel](https://pydantic-docs.helpmanual.io/usage/models/).
- The `input` parameter and return value MUST be annotated with Python typing hints.

### Input- and Output-Schema

_WIP_

### Command-line Interface

_WIP_


## Contribution

- Pull requests are encouraged and always welcome. Read our [contribution guidelines](https://github.com/ml-tooling/opyrator/tree/main/CONTRIBUTING.md) and check out [help-wanted](https://github.com/ml-tooling/opyrator/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+label%3A"help+wanted"+sort%3Areactions-%2B1-desc+) issues.
- Submit Github issues for any [feature request and enhancement](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=feature&template=02_feature-request.md&title=), [bugs](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=bug&template=01_bug-report.md&title=), or [documentation](https://github.com/ml-tooling/opyrator/issues/new?assignees=&labels=documentation&template=03_documentation.md&title=) problems.
- By participating in this project, you agree to abide by its [Code of Conduct](https://github.com/ml-tooling/opyrator/blob/main/.github/CODE_OF_CONDUCT.md).
- The [development section](#development) below contains information on how to build and test the project after you have implemented some changes.

## Development

Refer to our [contribution guides](https://github.com/ml-tooling/opyrator/blob/main/CONTRIBUTING.md#development-instructions) for information on our build scripts and development process.

---

Licensed **MIT**. Created and maintained with ❤️&nbsp; by developers from Berlin.
