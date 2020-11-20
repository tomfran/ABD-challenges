from code import *

if __name__ == "__main__":

    # generate the initial input, with 10 tuples
    print("\nLOG CDC TEST\nNote: the program will sleep 3 second before committing to the datalake\n")
    generate(n = 10, max_value = 1000, start = 0, mode = 'w', path = 'data/input.txt')
    
    # initialize filesource and dirdatalake
    print("\nTEST: initialize objects and generating dataset\n")
    source = File_source('data/input.txt')
    datalake = DirDatalake('data/datalake_log')
    cdc = LogCDC(source, datalake, 'data/datalake_log/sync.json', 'threshold', 'ts')
    
    # get the fresh rows
    cdc.get_fresh_rows()
    print("\nTEST: adding 3 new lines and rerun cdc\n")
    # add 3 lines and then get the fresh rows
    generate(n = 3, start = 10, mode = 'a', path = 'data/input.txt')
    cdc.get_fresh_rows()

    print("\nTEST: adding a fake tmp file to check the rollback\n")
    with open('data/datalake_log/test.tmp', 'w') as f:
        f.write('TMP TEST\n')
    cdc.get_fresh_rows()

    # generate the initial input, with 10 tuples
    print("\n\n\nREGISTRY CDC TEST\nNote: the program will sleep 3 second before committing to the datalake\n")
    generate(n = 10, max_value = 1000, start = 0, mode = 'w', path = 'data/input.txt')
    
    # initialize filesource and dirdatalake
    print("\nTEST: initialize objects and generating dataset\n")
    source = File_source('data/input.txt')
    datalake = DirDatalake('data/datalake_reg')
    cdc_reg = RegistryCDC(source, datalake, 'data/datalake_reg/sync.json', 'key')
    
    # get the fresh rows
    cdc_reg.get_fresh_rows()
    print("\nTEST: adding 3 new lines and rerun cdc\n")
    # add 3 lines and then get the fresh rows
    generate(n = 3, start = 10, mode = 'a', path = 'data/input.txt')
    cdc_reg.get_fresh_rows()

    print("\nTEST: adding a fake tmp file to check the rollback\n")
    with open('data/datalake_reg/test.tmp', 'w') as f:
        f.write('TMP TEST\n')
    
    cdc_reg.get_fresh_rows()
    lines = []
    print("\nTEST: changing one old tuples\n")
    with open('data/input.txt', 'r') as f:
        lines = f.readlines()
        dd = eval(lines[0])
        dd['a'] = -1
        lines[0] = str(dd) + '\n'
    with open('data/input.txt', 'w') as f:
        for el in lines:
            f.write(el)    
    cdc_reg.get_fresh_rows()

    