class WallhavenAPIError(Exception):
    """Custom exception for handling Wallhaven API errors."""

    def __init__(self, message: str):
        super().__init__(message)
