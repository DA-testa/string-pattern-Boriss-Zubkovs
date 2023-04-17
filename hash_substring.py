
def read_input():
    # this function needs to aquire input both from keyboard and file

    input_type = input()

    if "I" in input_type:
        pattern = input()
        text = input()

    elif "F" in input_type:
      filePath = "06"
      fp = "./tests/" + filePath
      with open(fp, mode ="r") as f:
            pattern = f.readline()
            text = f.readline()
    
    return (pattern.rstrip(), text.rstrip())

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
            d = (e * (d - ord(text[i]) * r) + ord(text[i + U])) % pr
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
        