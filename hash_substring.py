# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin Karp algorithm

    # Initialize variables
    P = len(pattern)
    T = len(text)
    pattern_h = sum(ord(pattern[i]) * pow(10, P - i - 1) for i in range(P))
    text_h = sum(ord(text[i]) * pow(10, P - i - 1 ) for i in range(P))
    occurrences = []

    # Loop through text
    for i in range(T - P + 1):
        # Check if hashes match
        if pattern_h == text_h:
            # Check if patterns match
            if pattern == text[i:i + P]:
                occurrences.append(i)
        # Update hash for next iteration
        if i < T - P:
            text_h = text_h - ord(text[i]) * pow(10, P - 1)
            text_h = text_h * 10 + ord(text[i + P])
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
