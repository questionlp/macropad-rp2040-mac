# SPDX-FileCopyrightText: 2022 Andy Piper, Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macro that allows the pad to be used like a fidget toy with all of the
keys and encoder button press do not have an assigned action and all
LEDs are set to off.
"""

from colors import basic

app = {
    "name": "Fidget",
    "macros": [
        # Color | Label | Key sequence
        # Row 1
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        # Row 2
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        # Row 3
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        # Row 4
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        # Encoder button
        (basic.OFF, "", []),
    ],
}
