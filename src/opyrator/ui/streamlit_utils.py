"""Hack to add per-session state to Streamlit."""

try:
    import streamlit.ReportThread as ReportThread
    from streamlit.ReportSession import ReportSession
    from streamlit.server.Server import Server
except Exception:
    # Streamlit >= 0.65.0
    import streamlit.report_thread as ReportThread
    from streamlit.server.server import Server
    from streamlit.report_session import ReportSession

from typing import Any, Dict

CUSTOM_STREAMLIT_CSS = """
div[data-testid="stBlock"] button {
  width: 100% !important;
  margin-bottom: 20px !important;
  border-color: #bfbfbf !important;
}
pre code {
    white-space: pre-wrap;
}
"""


class SessionState(object):
    def __init__(self, **kwargs: Any) -> None:
        """A new SessionState object."""
        self._run_id = 0
        self._input_data: Dict = {}
        self._output_data: Any = None

        for key, val in kwargs.items():
            setattr(self, key, val)

    @property
    def run_id(self) -> int:
        return self._run_id

    @property
    def input_data(self) -> Dict:
        return self._input_data

    @property
    def output_data(self) -> Any:
        return self._output_data

    @output_data.setter
    def output_data(self, output_data: Any) -> None:
        self._output_data = output_data

    def clear(self) -> None:
        # Clear should higher the run ID to reset all widgets using this within their key
        self._run_id += 1
        self._input_data = {}
        self._output_data = None


def get_current_session() -> ReportSession:  # type: ignore
    # Hack to get the session object from Streamlit.
    ctx = ReportThread.get_report_ctx()

    this_session = None

    current_server = Server.get_current()
    if hasattr(current_server, "_session_infos"):
        # Streamlit < 0.56
        session_infos = Server.get_current()._session_infos.values()
    else:
        session_infos = Server.get_current()._session_info_by_id.values()

    for session_info in session_infos:
        s = session_info.session
        if (
            # Streamlit < 0.54.0
            (hasattr(s, "_main_dg") and s._main_dg == ctx.main_dg)
            or
            # Streamlit >= 0.54.0
            (not hasattr(s, "_main_dg") and s.enqueue == ctx.enqueue)
            or
            # Streamlit >= 0.65.2
            (
                not hasattr(s, "_main_dg")
                and s._uploaded_file_mgr == ctx.uploaded_file_mgr
            )
        ):
            this_session = s
    if this_session is None:
        raise RuntimeError(
            "Oh noes. Couldn't get your Streamlit Session object. "
            "Are you doing something fancy with threads?"
        )
    return this_session


def get_session_state(**kwargs: Any) -> SessionState:
    """Gets a SessionState object for the current session.

    Creates a new object if necessary.
    Parameters
    ----------
    **kwargs : any
        Default values you want to add to the session state, if we're creating a
        new one.
    Example
    -------
    >>> session_state = get(user_name='', favorite_color='black')
    >>> session_state.user_name
    ''
    >>> session_state.user_name = 'Mary'
    >>> session_state.favorite_color
    'black'
    Since you set user_name above, next time your script runs this will be the
    result:
    >>> session_state = get(user_name='', favorite_color='black')
    >>> session_state.user_name
    'Mary'
    """
    this_session = get_current_session()
    # Got the session object! Now let's attach some state into it.
    if not hasattr(this_session, "_custom_session_state"):
        this_session._custom_session_state = SessionState(**kwargs)

    return this_session._custom_session_state
