class Cipher:
    """Simple Caesar cipher where characters are shifted by a specified number of characters, with wrapping"""

    # A = 65
    LOW_VAL = 65
    # Z = 90
    HIGH_VAL = 90

    def __init__(self, shift) -> None:
        self._shift = shift

    @property
    def shift(self):
        return self._shift

    def encode(self, s):
        return self.__shift_string(s, self._shift)

    def decode(self, s):
        return self.__shift_string(s, self._shift * -1)

    def __shift_string(self, s, shift):
        """Encode a string using a substitution cypher, shifting each character by the value of shift"""

        shifted_string = ""
        for char in s:
            int_val = ord(char) + shift
            if int_val < Cipher.LOW_VAL:
                delta = Cipher.LOW_VAL - int_val
                int_val = (Cipher.HIGH_VAL + 1) - delta
            elif int_val > Cipher.HIGH_VAL:
                delta = int_val - Cipher.HIGH_VAL
                int_val = (Cipher.LOW_VAL - 1) + delta

            shifted_string += chr(int_val)

        return shifted_string
