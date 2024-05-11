""" Palindrome checker using a two point approach """

user_input = str(input("Enter input here to check: \n\t"))


def checker():
    left = 0
    right = len(user_input)-1

    while(left<right):
        if user_input[left] != user_input[right]:
            return False
        
        left = left + 1
        right = right - 1

        return True
    
print(checker())