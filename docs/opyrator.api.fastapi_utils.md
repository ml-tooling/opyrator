<!-- markdownlint-disable -->

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/api/fastapi_utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `opyrator.api.fastapi_utils`
Collection of utilities for FastAPI apps. 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/api/fastapi_utils.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `as_form`

```python
as_form(cls: Type[BaseModel]) → Any
```

Adds an as_form class method to decorated models. 

The as_form class method can be used with FastAPI endpoints 


---

<a href="https://github.com/ml-tooling/opyrator/blob/main/src/opyrator/api/fastapi_utils.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `patch_fastapi`

```python
patch_fastapi(app: FastAPI) → None
```

Patch function to allow relative url resolution. 

This patch is required to make fastapi fully functional with a relative url path. This code snippet can be copy-pasted to any Fastapi application. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
