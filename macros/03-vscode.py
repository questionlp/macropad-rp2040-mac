# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macros for Microsoft Visual Studio Code for macOS
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "VS Code",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "CmdPal ", [Keycode.SHIFT, Keycode.COMMAND, "p"]),
        (adapted_pan.COLOR_1, "Open   ", [Keycode.COMMAND, "o"]),
        (adapted_pan.COLOR_1, "Settngs", [Keycode.COMMAND, ","]),
        # Row 2
        (adapted_pan.COLOR_2, "SelAll ", [Keycode.COMMAND, "a"]),
        (adapted_pan.COLOR_2, "Copy   ", [Keycode.COMMAND, "c"]),
        (adapted_pan.COLOR_2, "Cut    ", [Keycode.COMMAND, "x"]),
        # Row 3
        (adapted_pan.COLOR_3, "Paste  ", [Keycode.COMMAND, "v"]),
        (adapted_pan.COLOR_3, "Comment", [Keycode.COMMAND, "/"]),
        (adapted_pan.COLOR_3, "Format ", [Keycode.SHIFT, Keycode.ALT, "f"]),
        # Row 4
        (adapted_pan.COLOR_4, "FndAll ", [Keycode.SHIFT, Keycode.COMMAND, "f"]),
        (adapted_pan.COLOR_4, "Find   ", [Keycode.COMMAND, "f"]),
        (adapted_pan.COLOR_4, "OpnTerm", [Keycode.SHIFT, Keycode.CONTROL, "`"]),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, "w"]),
    ],
}
