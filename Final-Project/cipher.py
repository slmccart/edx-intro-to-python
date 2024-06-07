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
        """Encode a string using a substituion cypher, shifting each character by the value of shift"""

        encoded_string = ""
        for char in s:
            int_val = ord(char) + self.shift
            if int_val < Cipher.LOW_VAL:
                delta = Cipher.LOW_VAL - int_val
                int_val = (Cipher.HIGH_VAL + 1) - delta
            elif int_val > Cipher.HIGH_VAL:
                delta = int_val - Cipher.HIGH_VAL
                int_val = (Cipher.LOW_VAL - 1) + delta

            encoded_string += chr(int_val)

        return encoded_string
