from __future__ import annotations

import os
from pathlib import Path

from services.storage.base import StorageBackend
from services.storage.json_storage import JSONStorageBackend


def create_storage_backend(data_dir: Path) -> StorageBackend:
    """
    Create storage backend based on environment variable.
    
    Environment variables:
    - STORAGE_BACKEND: json (default, only supported backend in Lite)
    """
    backend_type = os.getenv("STORAGE_BACKEND", "json").lower().strip()
    
    print(f"[storage] Initializing storage backend: {backend_type}")
    
    if backend_type == "json":
        # Local JSON file storage
        file_path = data_dir / "accounts.json"
        auth_keys_path = data_dir / "auth_keys.json"
        print(f"[storage] Using JSON storage: {file_path}")
        return JSONStorageBackend(file_path, auth_keys_path)
    
    else:
        raise ValueError(
            f"Unknown storage backend: {backend_type}. "
            f"Lite version only supports: json"
        )
