# python3

def read_input():
    # this function needs to aquire input both from keyboard and file

    input_type = input().strip()

    if input_type == "I":
        pattern = input().strip()
        text = input().strip()

    elif input_type == "F":
        with open("input.txt", "r") as f:
            pattern = f.readline().strip()
            text = f.rearline().strip()
    
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    pr = 10**9 + 7

    U = len(pattern)
    N = len(text)
    e = 256
    g = pr
    r = pow(256, len(pattern)-1, pr)
    x = 0
    d = 0
    result = []

    for i in range(U):
        x = (x * g + ord(pattern[i])) % e
        d = (g * d + ord(text[i])) % e

    for i in range(N - U + 1):
        if x == d and pattern == text[i:i + U]:
            result.append(i)

        if i < N - U:
            d = (e * (d - ord(text[i]) * r) + ord(text[i + U])) % g 
    return result

# this part launches the functions
if __name__ == '__main_':
    print_occurrences(get_occurrences(*read_input()))

