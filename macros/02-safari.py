# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macros for Apple Safari browser
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "Safari",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "< Back ", [Keycode.COMMAND, "["]),
        (adapted_pan.COLOR_1, "Fwd >  ", [Keycode.COMMAND, "]"]),
        (adapted_pan.COLOR_1, "Up     ", [Keycode.SHIFT, Keycode.SPACEBAR]),
        # Row 2
        (adapted_pan.COLOR_2, "< Tab  ", [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (adapted_pan.COLOR_2, "Tab >  ", [Keycode.CONTROL, Keycode.TAB]),
        (adapted_pan.COLOR_2, "Down   ", Keycode.SPACEBAR),
        # Row 3
        (adapted_pan.COLOR_3, "Reload ", [Keycode.COMMAND, "r"]),
        (adapted_pan.COLOR_3, "Home   ", [Keycode.COMMAND, "H"]),
        (adapted_pan.COLOR_3, "Private", [Keycode.COMMAND, "N"]),
        # Row 4
        (adapted_pan.COLOR_4, "Rspnsv ", [Keycode.CONTROL, Keycode.COMMAND, "R"]),
        (adapted_pan.COLOR_4, "Cache  ", [Keycode.ALT, Keycode.COMMAND, "e"]),
        (adapted_pan.COLOR_4, "Inspect", [Keycode.ALT, Keycode.COMMAND, "i"]),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, "w"]),
    ],
}
