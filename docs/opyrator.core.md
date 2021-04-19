<!-- markdownlint-disable -->

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `opyrator.core`





---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `name_to_title`

```python
name_to_title(name: str) → str
```

Converts a camelCase or snake_case name to title case. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_compatible_type`

```python
is_compatible_type(type: Type) → bool
```

Returns `True` if the type is opyrator-compatible. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L37"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_input_type`

```python
get_input_type(func: Callable) → Type
```

Returns the input type of a given function (callable). 



**Args:**
 
 - <b>`func`</b>:  The function for which to get the input type. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the function does not have a valid input type annotation. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L66"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_output_type`

```python
get_output_type(func: Callable) → Type
```

Returns the output type of a given function (callable). 



**Args:**
 
 - <b>`func`</b>:  The function for which to get the output type. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the function does not have a valid output type annotation. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L92"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_callable`

```python
get_callable(import_string: str) → Callable
```

Import a callable from an string. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L107"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Opyrator`




<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/core.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(func: Union[Callable, str]) → None
```






---

#### <kbd>property</kbd> description





---

#### <kbd>property</kbd> input_type





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> output_type










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
