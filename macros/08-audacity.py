# SPDX-FileCopyrightText: 2022 Jessica E. Calderon, Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Custom macros for use with Audacity.

Note that the macros included in this file are for use with the custom
Audacity keyboard shortcuts are customnized for my
TBTL/Marsupial Gurgle workflow and not the default Audacity keyboard
shortcuts
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "Audacity",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "Start  ", [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        (adapted_pan.COLOR_1, "SelAll ", [Keycode.COMMAND, "a"]),
        (adapted_pan.COLOR_1, "End    ", [Keycode.COMMAND, Keycode.RIGHT_ARROW]),
        # Row 2
        (adapted_pan.COLOR_2, "FadeIn ", [Keycode.SHIFT, Keycode.COMMAND, ","]),
        (adapted_pan.COLOR_2, "InsSil ", [Keycode.OPTION, "S"]),
        (adapted_pan.COLOR_2, "FadeOut", [Keycode.SHIFT, Keycode.COMMAND, "."]),
        # Row 3
        (adapted_pan.COLOR_3, "Trim   ", [Keycode.COMMAND, "l"]),
        (adapted_pan.COLOR_3, "Amplify", [Keycode.OPTION, "A"]),
        (adapted_pan.COLOR_3, "RptEft ", [Keycode.COMMAND, "r"]),
        # Row 4
        (adapted_pan.COLOR_4, "Undo   ", [Keycode.COMMAND, "z"]),
        (adapted_pan.COLOR_4, "Export ", [Keycode.COMMAND, "E"]),
        (adapted_pan.COLOR_4, "Redo   ", [Keycode.COMMAND, "Z"]),
        # Encoder button
        (basic.OFF, "", [Keycode.COMMAND, "w"]),
    ],
}
