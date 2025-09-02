"""
This example demonstrates how to create a session in AGB.
"""

import os
import time
from typing import Dict, Optional

from agb import AGB
from agb.session_params import CreateSessionParams


def create_session_with_default_params() -> None:
    """Create a session with default parameters."""
    # Initialize the AGB client
    api_key = os.environ.get("AGB_API_KEY", "")
    agb = AGB(api_key=api_key)

    # Create a session with default parameters
    result = agb.create()

    if result.success and result.session:
        session = result.session
        print(f"Session created successfully with ID: {session.session_id}")
        print(f"Request ID: {result.request_id}")

        # Clean up
        delete_result = agb.delete(session)
        if delete_result.success:
            print("Session deleted successfully")
        else:
            print(f"Failed to delete session: {delete_result.error_message}")
    else:
        print(f"Failed to create session: {result.error_message}")


def create_session_with_labels() -> None:
    """Create a session with labels."""
    # Initialize the AGB client
    api_key = os.environ.get("AGB_API_KEY", "")
    agb = AGB(api_key=api_key)

    # Define labels
    labels: Dict[str, str] = {
        "environment": "development",
        "project": "example",
        "owner": "user123"
    }

    # Create session parameters with labels
    params = CreateSessionParams(labels=labels)

    # Create a session with the parameters
    result = agb.create(params)

    if result.success and result.session:
        session = result.session
        print(f"Session with labels created successfully with ID: {session.session_id}")
        print(f"Request ID: {result.request_id}")

        # Clean up
        delete_result = agb.delete(session)
        if delete_result.success:
            print("Session deleted successfully")
        else:
            print(f"Failed to delete session: {delete_result.error_message}")
    else:
        print(f"Failed to create session with labels: {result.error_message}")


def main() -> None:
    """Run all examples."""
    print("1. Creating session with default parameters...")
    create_session_with_default_params()
    print("\n2. Creating session with labels...")
    create_session_with_labels()


if __name__ == "__main__":
    main()
