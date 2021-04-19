<!-- markdownlint-disable -->

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `opyrator.ui.streamlit_utils`
Hack to add per-session state to Streamlit. 

Based on: https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92 

**Global Variables**
---------------
- **CUSTOM_STREAMLIT_CSS**

---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_current_session`

```python
get_current_session() → ReportSession
```






---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_session_state`

```python
get_session_state(**kwargs: Any) → SessionState
```

Gets a SessionState object for the current session. 

Creates a new object if necessary. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SessionState`




<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(**kwargs: Any) → None
```

A new SessionState object. 


---

#### <kbd>property</kbd> input_data





---

#### <kbd>property</kbd> latest_operation_input





---

#### <kbd>property</kbd> output_data





---

#### <kbd>property</kbd> run_id







---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/ui/streamlit_utils.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `clear`

```python
clear() → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
