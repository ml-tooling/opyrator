<!-- markdownlint-disable -->

# API Overview

## Modules

- [`opyrator.api`](./opyrator.api.md#module-opyratorapi)
- [`opyrator.api.fastapi_app`](./opyrator.api.fastapi_app.md#module-opyratorapifastapi_app)
- [`opyrator.api.fastapi_utils`](./opyrator.api.fastapi_utils.md#module-opyratorapifastapi_utils): Collection of utilities for FastAPI apps.
- [`opyrator.components`](./opyrator.components.md#module-opyratorcomponents)
- [`opyrator.components.outputs`](./opyrator.components.outputs.md#module-opyratorcomponentsoutputs)
- [`opyrator.components.types`](./opyrator.components.types.md#module-opyratorcomponentstypes)
- [`opyrator.core`](./opyrator.core.md#module-opyratorcore)
- [`opyrator.export`](./opyrator.export.md#module-opyratorexport)
- [`opyrator.tasks`](./opyrator.tasks.md#module-opyratortasks)
- [`opyrator.ui`](./opyrator.ui.md#module-opyratorui)
- [`opyrator.ui.schema_utils`](./opyrator.ui.schema_utils.md#module-opyratoruischema_utils)
- [`opyrator.ui.streamlit_ui`](./opyrator.ui.streamlit_ui.md#module-opyratoruistreamlit_ui)
- [`opyrator.ui.streamlit_utils`](./opyrator.ui.streamlit_utils.md#module-opyratoruistreamlit_utils): Hack to add per-session state to Streamlit.
- [`opyrator.utils`](./opyrator.utils.md#module-opyratorutils)

## Classes

- [`outputs.ClassificationOutput`](./opyrator.components.outputs.md#class-classificationoutput)
- [`outputs.ScoredLabel`](./opyrator.components.outputs.md#class-scoredlabel)
- [`types.FileContent`](./opyrator.components.types.md#class-filecontent)
- [`core.Opyrator`](./opyrator.core.md#class-opyrator)
- [`export.ExportFormat`](./opyrator.export.md#class-exportformat): An enumeration.
- [`streamlit_ui.InputUI`](./opyrator.ui.streamlit_ui.md#class-inputui)
- [`streamlit_ui.OutputUI`](./opyrator.ui.streamlit_ui.md#class-outputui)
- [`streamlit_utils.SessionState`](./opyrator.ui.streamlit_utils.md#class-sessionstate)

## Functions

- [`fastapi_app.create_api`](./opyrator.api.fastapi_app.md#function-create_api)
- [`fastapi_app.launch_api`](./opyrator.api.fastapi_app.md#function-launch_api)
- [`fastapi_utils.as_form`](./opyrator.api.fastapi_utils.md#function-as_form): Adds an as_form class method to decorated models.
- [`fastapi_utils.patch_fastapi`](./opyrator.api.fastapi_utils.md#function-patch_fastapi): Patch function to allow relative url resolution.
- [`core.get_callable`](./opyrator.core.md#function-get_callable): Import a callable from an string.
- [`core.get_input_type`](./opyrator.core.md#function-get_input_type): Returns the input type of a given function (callable).
- [`core.get_output_type`](./opyrator.core.md#function-get_output_type): Returns the output type of a given function (callable).
- [`core.is_compatible_type`](./opyrator.core.md#function-is_compatible_type): Returns `True` if the type is opyrator-compatible.
- [`core.name_to_title`](./opyrator.core.md#function-name_to_title): Converts a camelCase or snake_case name to title case.
- [`schema_utils.get_single_reference_item`](./opyrator.ui.schema_utils.md#function-get_single_reference_item)
- [`schema_utils.is_multi_enum_property`](./opyrator.ui.schema_utils.md#function-is_multi_enum_property)
- [`schema_utils.is_multi_file_property`](./opyrator.ui.schema_utils.md#function-is_multi_file_property)
- [`schema_utils.is_object_list_property`](./opyrator.ui.schema_utils.md#function-is_object_list_property)
- [`schema_utils.is_property_list`](./opyrator.ui.schema_utils.md#function-is_property_list)
- [`schema_utils.is_single_boolean_property`](./opyrator.ui.schema_utils.md#function-is_single_boolean_property)
- [`schema_utils.is_single_datetime_property`](./opyrator.ui.schema_utils.md#function-is_single_datetime_property)
- [`schema_utils.is_single_dict_property`](./opyrator.ui.schema_utils.md#function-is_single_dict_property)
- [`schema_utils.is_single_enum_property`](./opyrator.ui.schema_utils.md#function-is_single_enum_property)
- [`schema_utils.is_single_file_property`](./opyrator.ui.schema_utils.md#function-is_single_file_property)
- [`schema_utils.is_single_number_property`](./opyrator.ui.schema_utils.md#function-is_single_number_property)
- [`schema_utils.is_single_object`](./opyrator.ui.schema_utils.md#function-is_single_object)
- [`schema_utils.is_single_reference`](./opyrator.ui.schema_utils.md#function-is_single_reference)
- [`schema_utils.is_single_string_property`](./opyrator.ui.schema_utils.md#function-is_single_string_property)
- [`schema_utils.resolve_reference`](./opyrator.ui.schema_utils.md#function-resolve_reference)
- [`streamlit_ui.function_has_named_arg`](./opyrator.ui.streamlit_ui.md#function-function_has_named_arg)
- [`streamlit_ui.has_input_ui_renderer`](./opyrator.ui.streamlit_ui.md#function-has_input_ui_renderer)
- [`streamlit_ui.has_output_ui_renderer`](./opyrator.ui.streamlit_ui.md#function-has_output_ui_renderer)
- [`streamlit_ui.is_compatible_audio`](./opyrator.ui.streamlit_ui.md#function-is_compatible_audio)
- [`streamlit_ui.is_compatible_image`](./opyrator.ui.streamlit_ui.md#function-is_compatible_image)
- [`streamlit_ui.is_compatible_video`](./opyrator.ui.streamlit_ui.md#function-is_compatible_video)
- [`streamlit_ui.launch_ui`](./opyrator.ui.streamlit_ui.md#function-launch_ui)
- [`streamlit_ui.render_streamlit_ui`](./opyrator.ui.streamlit_ui.md#function-render_streamlit_ui)
- [`streamlit_utils.get_current_session`](./opyrator.ui.streamlit_utils.md#function-get_current_session)
- [`streamlit_utils.get_session_state`](./opyrator.ui.streamlit_utils.md#function-get_session_state): Gets a SessionState object for the current session.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
