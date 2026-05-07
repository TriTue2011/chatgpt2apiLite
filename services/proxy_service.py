"""Simple proxy helper for Lite version - reads proxy from HTTP_PROXY env var."""

from __future__ import annotations

import os


class ProxySettingsStore:
    def build_session_kwargs(self, **session_kwargs) -> dict[str, object]:
        proxy = os.getenv("HTTP_PROXY", "") or os.getenv("HTTPS_PROXY", "")
        if proxy:
            session_kwargs["proxy"] = proxy
        return session_kwargs


proxy_settings = ProxySettingsStore()


def test_proxy(url: str, *, timeout: float = 15.0) -> dict:
    return {"ok": False, "status": 0, "latency_ms": 0, "error": "proxy test not available in Lite version"}
