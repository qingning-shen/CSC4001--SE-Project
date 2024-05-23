import os
with open("res.out", "w") as fout:
    if os.system("diff -w 1.out 2.out > /dev/null"):
        print(1, file=fout)
    else:
        print(0, file=fout)