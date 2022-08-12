# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macros for iTerm on macOS
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "iTerm",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "NewWin ", [Keycode.COMMAND, "n"]),
        (adapted_pan.COLOR_1, "NewTab ", [Keycode.COMMAND, "t"]),
        (adapted_pan.COLOR_1, "Zoom   ", [Keycode.SHIFT, Keycode.COMMAND, "0"]),
        # Row 2
        (adapted_pan.COLOR_2, "Prof   ", [Keycode.COMMAND, "O"]),
        (adapted_pan.COLOR_2, "ClsWin ", [Keycode.COMMAND, "w"]),
        (adapted_pan.COLOR_2, "ClsTrm ", [Keycode.COMMAND, "W"]),
        # Row 3
        (adapted_pan.COLOR_3, "Text + ", [Keycode.COMMAND, "+"]),
        (adapted_pan.COLOR_3, "TxtRst ", [Keycode.COMMAND, "0"]),
        (adapted_pan.COLOR_3, "Text - ", [Keycode.COMMAND, "-"]),
        # Row 4
        (adapted_pan.COLOR_4, "staal  ", [Keycode.CONTROL, Keycode.COMMAND, "s"]),
        (adapted_pan.COLOR_4, "pond   ", [Keycode.CONTROL, Keycode.COMMAND, "p"]),
        (adapted_pan.COLOR_4, "TBTL MG", [Keycode.CONTROL, Keycode.COMMAND, "m"]),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, "w"]),
    ],
}
