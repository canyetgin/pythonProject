import os
with open('1.PNG', 'rb') as in_file:
    with open('2.PNG', 'ab') as out_file:
        total= os.path.getsize("1.PNG")
        per = 0
        chunk = 4096

        while True:
            chnk = in_file.read(chunk)
            if chnk:
                out_file.write(chnk)
                per += len(chnk)

                done = int(50 * per / total)

                print("%s :[%s%s][%s%s]" % ("file_name", "%", done, '#' * done, ' ' * (50 - done)), end="\r")
            else:
              print("[OK] ", end=55 * " " + "\n")
              break


        out_file.write(str.encode("//1//PNG"))