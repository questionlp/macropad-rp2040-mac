# SPDX-FileCopyrightText: 2021-2022 Emma Humphries for Adafruit Industries, Linh Pham
#
# SPDX-License-Identifier: MIT
#
# pylint: disable=import-error, unused-import, too-few-public-methods
"""
Modified number pad that has zero, decimal point/full stop and ENTER
key in the bottom row and BACKSPACE assigned to the encoder button
"""

from adafruit_hid.keycode import Keycode
from colors import adapted_pan, basic

app = {
    "name" : "Numpad",
    "macros" : [
        # Color | Label | Key sequence
        # Row 1
        (adapted_pan.COLOR_1, "   7   ", ["7"]),
        (adapted_pan.COLOR_1, "   8   ", ["8"]),
        (adapted_pan.COLOR_1, "   9   ", ["9"]),
        # Row 2
        (adapted_pan.COLOR_2, "   4   ", ["4"]),
        (adapted_pan.COLOR_2, "   5   ", ["5"]),
        (adapted_pan.COLOR_2, "   6   ", ["6"]),
        # Row 3
        (adapted_pan.COLOR_3, "   1   ", ["1"]),
        (adapted_pan.COLOR_3, "   2   ", ["2"]),
        (adapted_pan.COLOR_3, "   3   ", ["3"]),
        # Row 4
        (adapted_pan.COLOR_4, "   0   ", ["0"]),
        (adapted_pan.COLOR_4, "   .   ", ["."]),
        (adapted_pan.COLOR_4, " ENTER ", [Keycode.KEYPAD_ENTER]),
        # Encoder button
        (basic.OFF, "", [Keycode.BACKSPACE]),
    ],
}
