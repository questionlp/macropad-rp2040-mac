# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macros for Adobe Photoshop on macOS
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "Photoshop",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "Undo   ", [Keycode.COMMAND, "z"]),
        (adapted_pan.COLOR_1, "Redo   ", [Keycode.COMMAND, "Z"]),
        (adapted_pan.COLOR_1, "Brush  ", "B"),
        # Row 2
        (adapted_pan.COLOR_2, "B&W    ", "d"),
        (adapted_pan.COLOR_2, "Marquee", "M"),
        (adapted_pan.COLOR_2, "Eraser ", "E"),
        # Row 3
        (adapted_pan.COLOR_3, "Swap   ", "x"),
        (adapted_pan.COLOR_3, "Move   ", "v"),
        (adapted_pan.COLOR_3, "Fill   ", "G"),
        # Row 4
        (adapted_pan.COLOR_4, "Eyedrop", "I"),
        (adapted_pan.COLOR_4, "Wand   ", "W"),
        (adapted_pan.COLOR_4, "Heal   ", "J"),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, Keycode.OPTION, "S"]),
    ],
}
