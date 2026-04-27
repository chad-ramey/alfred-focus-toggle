#!/usr/bin/env python3
"""
Reads macOS Focus mode names from the system configuration and outputs
Alfred Script Filter JSON. Works in any OS language and automatically
includes custom modes the user has created.
"""

import json
import os
import subprocess
import sys

DEFAULT_MODES = [
    "Sleep",
    "Do Not Disturb",
    "Gaming",
    "Reduce Interruptions",
    "Work",
    "Driving",
]


def _extract_names(data):
    return [
        item["mode"]["name"].strip()
        for item in data.get("data", [])
        if item.get("mode", {}).get("name", "").strip()
    ]


def get_focus_modes():
    base = os.path.expanduser("~/Library/DoNotDisturb/DB")

    # macOS 13+ (Ventura and later) — JSON file
    json_path = os.path.join(base, "ModeConfigurations.json")
    if os.path.isfile(json_path):
        try:
            with open(json_path) as f:
                names = _extract_names(json.load(f))
            if names:
                return names
        except Exception:
            pass

    # macOS 12 (Monterey) — binary plist, convert on the fly
    plist_path = os.path.join(base, "ModeConfigurations.plist")
    if os.path.isfile(plist_path):
        try:
            result = subprocess.run(
                ["plutil", "-convert", "json", "-o", "-", plist_path],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                names = _extract_names(json.loads(result.stdout))
                if names:
                    return names
        except Exception:
            pass

    return DEFAULT_MODES


modes = get_focus_modes()

items = [
    {
        "title": m,
        "subtitle": f"Toggle {m} Focus",
        "arg": m,
        "icon": {"path": "icon.png"},
    }
    for m in modes
]

print(json.dumps({"items": items}))
