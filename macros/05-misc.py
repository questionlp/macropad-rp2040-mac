# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Miscellaneous macros for macOS
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "Misc",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "Open   ", [Keycode.COMMAND, "o"]),
        (adapted_pan.COLOR_1, "Save   ", [Keycode.COMMAND, "s"]),
        (adapted_pan.COLOR_1, "SaveAs ", [Keycode.COMMAND, "S"]),
        # Row 2
        (adapted_pan.COLOR_2, "Copy   ", [Keycode.COMMAND, "c"]),
        (adapted_pan.COLOR_2, "Cut    ", [Keycode.COMMAND, "x"]),
        (adapted_pan.COLOR_2, "Paste  ", [Keycode.COMMAND, "p"]),
        # Row 3
        (adapted_pan.COLOR_3, "SelAll ", [Keycode.COMMAND, "a"]),
        (adapted_pan.COLOR_3, "Quit   ", [Keycode.COMMAND, "q"]),
        (adapted_pan.COLOR_3, "ForceQt", [Keycode.COMMAND, Keycode.OPTION, Keycode.ESCAPE]),
        # Row 4
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        (basic.OFF, "", []),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, "w"]),
    ],
}
