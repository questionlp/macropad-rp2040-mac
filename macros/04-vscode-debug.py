# SPDX-FileCopyrightText: 2022 by Jessica E. Calderon
#                         2022 Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Macros for debugging applications in Microsoft Visual Studio Code for macOS
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic


app = {
    "name" : "VS Code Debug",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "TglBrk ", [Keycode.F9]),
        (adapted_pan.COLOR_1, "Start  ", [Keycode.F5]),
        (adapted_pan.COLOR_1, "Stop   ", [Keycode.SHIFT, Keycode.F5]),
        # Row 2
        (adapted_pan.COLOR_2, "StpOvr ", [Keycode.F10]),
        (adapted_pan.COLOR_2, "StpIn  ", [Keycode.F11]),
        (adapted_pan.COLOR_2, "StpOut ", [Keycode.SHIFT, Keycode.F11]),
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
