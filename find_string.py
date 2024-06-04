class FindSubString:
    def __init__(self, input_string:str, target_string:str):
        assert input_string != None, f'input string not None'
        assert target_string != None, f'target string not None'

        self.input = input_string
        self.target = target_string

    def is_valid(self):
        if self.target not in self.input or len(self.input) < 1 or len(self.target) < 1:
            return False
        return True
    
    def find_substring(self, return_index=False):
        """
        if return_index is provided, return result and index of start and end
        """
        if not self.is_valid():
            return "invalid string or target not in input string"
        else:
            start_index = 0
            end_index = 0
            res = ''
            index = []
            for i in range(len(self.input) - len(self.target) + 1):
                if self.input[i:i+len(self.target)] == self.target:
                    start_index = i
                    end_index = start_index + len(self.target)
                    index.append([start_index, end_index])
                    res += self.target
                if start_index <= i < end_index:
                    pass
                else:
                    res += "*"
            
        if len(res) != len(self.input):
            res = res + (len(self.input)-len(res)) * "*"
        
        if return_index:
            return res, index
        return res

input_string = "hfhfhhKMSTechonologydsKMSTechonology"
output = "K"
res = FindSubString(input_string, output)
print(res.find_substring(return_index=True))
