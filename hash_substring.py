def read_input():

	choose = input()
	if "F" in choose:
		with open("tests/" + "6", 'r') as file:
			pattern = file.readline().rstrip()
			text = file.readline().rstrip()

	elif "I" in choose:
		pattern = input().rstrip()
		text = input().rstrip()


	return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    P = len(pattern)
    T = len(text)

    d = 256
    q = 1000000007
    h = pow(d, P-1) % q

    pattern_h = sum(ord(pattern[i]) * pow(d , P - i - 1, q) % q for i in range(P)) % q
    text_h = sum(ord(text[i]) * pow(d, P - i - 1, q ) % q for i in range(P)) % q
    occurrences = []

    # Loop through text
    for i in range(T - P + 1):
        if pattern_h == text_h:
            if pattern == text[i:i + P]:
                occurrences.append(i)

        if i < T - P:
            text_h = (text_h - ord(text[i]) * h % q) % q
            text_h = (text_h * d + ord(text[i + P])) % q
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
