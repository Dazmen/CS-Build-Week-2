'''
    First note, this seems like an excellent use for regex but I am currently uncomfortable with it and I will attempt to complete it with tools I am familiar so I do not look much (if anything) up
    
    Plan
    - initialize an array to hold decoded values
    - use split and turn the str into an arr
    - initialize two variables that will hold indexes to skip while iterating over the string
    - iterate over the array 
        - If the value is just a regular character, add it to the decoded array
        - if the value is a digit, we know it is going to be followed by characters in brackets (potentially including numbers and brackets inside)
            -
        
        -JUST GOING TO JUMP INTO CODING, IT WILL HELP ME WORK MY WAY THROUGH THIS
'''

class Solution:
    def decodeString(self, s: str) -> str:
        decoded_arr = []
        encoded_arr = list(s) # Had to look this up, I thought split worked like JS initially
        
        skip_start = -1
        skip_end = -1
        
        for i in range(len(encoded_arr)):
            character = encoded_arr[i]
            
            if character.isnumeric():
                # Create a helper function that takes the current index and the encoded_arr
                # The helper function will search for the matching closing bracket to the expression
                # it will take note of the index where the closing bracket is
                # Once that it found it will decode that portion of the string
                # function will return an array where the 0 index is the decoded string and the 1 index is the reference for skip_end
                decode_return, encode_stop = self.decode_helper(i, encoded_arr)
                decoded_arr.append(decode_return)
                skip_start = i
                skip_end = encode_stop
                
            elif skip_start <= i <= skip_end:
                continue
                
            else:
                decoded_arr.append(character)
                
        return ''.join(decoded_arr)
                
    # could recursivly call to deal with nested encodings?
    # If there is a number, that means there is another encoding inside of the encoding
    def decode_helper(self, index: int, arr: list) -> list:
        # Value that the string will need to be multiplied by
        multi_value = int(arr[index])
        
        # Index where the array starts
        starting_index = index + 1
        
        # Variables to keep track of ] or num indexes
        closed_bracket_location = None
        number_location = None
        

        
        # Building decoded arr
        decoded_arr = list()
        
        # skip variables
        skip_end = -1
        
        for i in range(starting_index, len(arr)):
            value = arr[i]
            
            if i <= skip_end:
                continue
            # if the value is a number, that means there is another nested encoding, here we should call the decode_helper again
            elif value.isnumeric():
                # might need to adjust logic in here to handle deeper nested encodings for recursion
                
                decoded_section, end = self.decode_helper(i, arr)
                
                decoded_arr.append(decoded_section)
                skip_end = end
                
            elif value == ']' :
                closed_bracket_location = i
                break

            elif value != '[' and value != ']':
                decoded_arr.append(value)
                
        # at this point the loop will have stopped and there will either be a value for the closing ] index
        
        # if the closed_bracket_location is truthy then we have what we need to start actually decoding!

        # Starting index + 1 will removed the opening bracket, will not have to create logic for it later
        # the slice syntax also will remove the closing bracket from the array
        # encoded_section = arr[starting_index + 1 : closed_bracket_location]
        decoded_string = ''.join(decoded_arr)
        
        return [multi_value * decoded_string, closed_bracket_location]
        

        
        
        
        