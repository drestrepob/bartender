import os


def get_secret(key: str) -> str:
    """Get secret from environment or file

    Args:
        key: Secret key

    Returns:
        Secret value.
    """
    if key in os.environ:  # Secret inside environment
        return os.environ.get(key)

    with open(os.environ.get(key + "_FILE")) as file:
        return file.read().strip()
