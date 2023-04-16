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

    pre = 10*9 + 7

    return alghoritm(pattern, text, pre)


def alg(pattern, text, pre)
    U, N, e, g, r, x, d, result = len(pattern), len(text), 256, pre, pow(256, len(pattern)-1, pre),0 ,0, []
    for i in range(U):
        x = (x*e + ord(pattern[i])) % g
        d = (d*e + ord(text[i])) % g
    for i in range(N-U+1):
        if x == d and pattern == text[i:i + U]:
            result.append(i)
        if i < N - U:
            d = (e (d-ord(text[i]) r) + ord(text[i + U])) % g 
               
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

