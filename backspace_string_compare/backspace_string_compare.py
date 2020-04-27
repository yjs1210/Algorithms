class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        i = len(S) - 1
        j = len(T) - 1
        while(i >= 0 or j >= 0 ):
            pound_i = 0
            pound_j = 0
            char_i = ''
            char_j = ''

            while (i>=0):
                if(S[i] == '#'):
                    pound_i += 1
                    i -= 1
                elif(pound_i > 0):
                    i -= 1
                    pound_i -= 1
                else:
                    char_i = S[i]
                    i -= 1
                    break

            while (j>=0):
                if(T[j] == '#'):
                    pound_j += 1
                    j -= 1
                elif(pound_j > 0):
                    j -= 1
                    pound_j -= 1 
                else:
                    char_j = T[j]
                    j -= 1
                    break
            
            if char_i != char_j:
                return False

        return True
        
            