"""
link: https://www.lintcode.com/problem/659/

"""


from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(strs[i])}#{strs[i]}" for i in range(len(strs)))

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, string: str) -> List[str]:
        strings_list = []
        temp_string = ""
        counter = 0

        for i in range(len(string)):
            if counter:
                temp_string += string[i]
                counter -= 1
                if counter == 0:
                    strings_list.append(temp_string)
                    temp_string = ""
            elif string[i] != "#":
                temp_string += string[i]
            elif string[i] == "#":
                counter = int(temp_string)
                temp_string = ""
        return strings_list


if __name__ == "__main__":
    test = Solution()
    encoded_string = test.encode(["hello", "world", "nice", "day"])
    decoded_string = test.decode(encoded_string)
    print(encoded_string, decoded_string)

    encoded_string = test.encode(
        ["412#reallylongtexttotestmultiplenumbers:3", "51241#there##12"])
    decoded_string = test.decode(encoded_string)
    print(encoded_string, decoded_string)
