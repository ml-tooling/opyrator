<!-- markdownlint-disable -->

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `opyrator.ui.streamlit_ui`




**Global Variables**
---------------
- **CUSTOM_STREAMLIT_CSS**
- **STREAMLIT_RUNNER_SNIPPET**

---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `launch_ui`

```python
launch_ui(opyrator_path: str, port: int = 8501) → None
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `function_has_named_arg`

```python
function_has_named_arg(func: Callable, parameter: str) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_output_ui_renderer`

```python
has_output_ui_renderer(data_item: BaseModel) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `has_input_ui_renderer`

```python
has_input_ui_renderer(input_class: Type[BaseModel]) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_compatible_audio`

```python
is_compatible_audio(mime_type: str) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_compatible_image`

```python
is_compatible_image(mime_type: str) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_compatible_video`

```python
is_compatible_video(mime_type: str) → bool
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L825"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_streamlit_ui`

```python
render_streamlit_ui(opyrator: Opyrator) → None
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `InputUI`




<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(session_state: SessionState, input_class: Type[BaseModel])
```








---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `render_ui`

```python
render_ui() → None
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L643"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `OutputUI`




<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L644"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(output_data: Any, input_data: Any)
```








---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_ui.py#L648"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `render_ui`

```python
render_ui() → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
