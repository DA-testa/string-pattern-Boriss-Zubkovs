# python3

def read_input():
    # this function needs to aquire input both from keyboard and file

    input_type = input()

    if input_type == "I":
        pattern = input()
        text = input()

    elif input_type == "F":
        with open("input.txt", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    pr = 10**9 + 7

    U = len(pattern)
    N = len(text)
    e = 256
    r = pow(256, len(pattern)-1, pr)
    x = 0
    d = 0
    result = []

    for i in range(U):
        x = (e * x + ord(pattern[i])) % pr
        d = (e * d + ord(text[i])) % pr

    for i in range(N - U + 1):
        if x == d and pattern == text[i:i + U]:
            result.append(i)

        if i < N - U:
            d = (d * (x - ord(text[i]) * r) + ord(text[i + U])) % pr
    return result

# this part launches the functions
if __name__ == '__main_':
    print_occurrences(get_occurrences(*read_input()))
        

