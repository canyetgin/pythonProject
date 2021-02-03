with open('1.PNG', 'rb') as in_file:
    with open('2.PNG', 'ab') as out_file:
        chunk = 4096

        while True:
            chnk = in_file.read(chunk)
            if chnk:
                out_file.write(chnk)
            else:
                break