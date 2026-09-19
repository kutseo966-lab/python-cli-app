#!/usr/bin/env python3
"""
Python CLI App
Simple app for GitHub Actions demo
"""

import sys
import platform
from datetime import datetime


def get_system_info():
    """Get system information"""
    return {
        "python_version": sys.version.split()[0],
        "platform": platform.system(),
        "architecture": platform.machine(),
        "timestamp": datetime.now().isoformat()
    }


def main():
    print("Python CLI App v1.0.0")
    print("=" * 50)

    info = get_system_info()

    print(f"Python: {info['python_version']}")
    print(f"Platform: {info['platform']}")
    print(f"Architecture: {info['architecture']}")
    print(f"Build time: {info['timestamp']}")
    print("=" * 50)
    print("Application is working!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
