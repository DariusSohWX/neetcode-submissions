class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += '@' + s

        print(result)
        return result

    def decode(self, s: str) -> List[str]:

        result = []
        length = 0
        temp_l = ''
        temp_s = ''
        is_word = False

        for i, c in enumerate(s):

            if length > 0 and is_word:
                temp_s += c
                length -= 1
                if length == 0:
                    temp_l = ''
                    is_word = False
                    result.append(temp_s)
                    temp_s = ''
                    continue

            if c == '@' and is_word == False:
                length = int(temp_l)
                if length == 0:
                    result.append("")
                    continue
                    
                else:
                    is_word = True
                    continue

            if length == 0:
                temp_l += c
                continue

        return result
            
