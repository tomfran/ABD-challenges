from random import randint

def generate(n = 10, max_value = 1000, start = 0, mode = 'w', path = 'input.txt'):
    with open(path, mode) as f:
        l = [{"key"     : key, 
                'a'     : randint(0,max_value), 
                'b'     : randint(0,max_value), 
                'c'     : randint(0,max_value), 
                'ts'    : key} for key in range(start, start+n)]
        for el in l:
            f.write(f"{el}\n")

if __name__ == "__main__":
    generate()