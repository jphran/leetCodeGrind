"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).
"""


# NOTE: I use 3 deci digits to represent up to 200 chars in the word
class Codec:
    CHARS_TO_ENCODE_LEN = 3

    def encode_str_length(self, str_to_encode: str, str_to_append_to: str) -> str:
        """
        Encodes the length of the str using 3 deci digits.
        :param str_to_encode:
        :param str_to_append_to:
        :return:
        """
        length = str(len(str_to_encode))
        while len(length) < self.CHARS_TO_ENCODE_LEN:
            length = '0' + length
        str_to_append_to += length
        return str_to_append_to

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for s in strs:
            encoded = self.encode_str_length(s, encoded)
            encoded += s

        return encoded

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strs: list[str] = []
        while len(s) > 0:
            length_of_encoded_str = s[:self.CHARS_TO_ENCODE_LEN]
            length_and_str = self.CHARS_TO_ENCODE_LEN + int(length_of_encoded_str)
            decoded_strs.append(s[self.CHARS_TO_ENCODE_LEN:length_and_str])
            s = s[length_and_str:]

        return decoded_strs



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

if __name__ == '__main__':
    codec = Codec()
    strs = ['hello', 'world']
    result = codec.decode(codec.encode(strs))
    print(result)