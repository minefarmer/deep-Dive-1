i = 0  # This is an example of the while loop
while i < 5:
    print(i)
    i += 1
i = None  # 0
            # 1
            # 2
            # 3
            # 4



for i in range(5):  # This example uses the iterable object 'range'
    print(i)  # 0
                # 1
                # 2
                # 3
                # 4



for i in [1, 2, 3, 4]:
    print(i)  # 1
                # 2
                # 3
                # 4



for c in 'hello':
    print(c)  # h
                # e
                # l
                # l
                # o



for x in ('a',"b", 'c', 4):
    print(x)  # a
                # b
                # c
                # 4

for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)  # (1, 2)
            # (3, 4)
            # (5, 6)



for i in range(5):
    if i==3:
        continue
    print(i)  # 0
                # 1
                # 2
                # 4







for i in range(5):
    if i==3:
        break
    print(i)  # 0
                # 1
                # 2



for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiple of 7 found')  # 1
                                    # 2
                                    # 3
                                    # 4
                                    # no multiple of 7 found



for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiple of 7 found')  # 1
                                    # 2
                                    # 3
                                    # 4
                                    # 5
                                    # 6
                                    # 7
                                    # multiple of 7 found



for i in range(6):
    print('------------------')
    try:
        10 / i-3
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print("always run")

    print(i)  # -----------------
            # divided by 0
            # always run
            # ------------------
            # always run
            # 1
            # ------------------
            # always run
            # 2
            # ------------------
            # always run
            # 3
            # ------------------
            # always run
            # 4
            # ------------------
            # always run
            # 5



s = 'hello'
for c in s:
    print(c)  # h
                # e
                # l
                # l
                # o



s = 'hello'
i = 0
for c in s:
    print(i, c)  # 0 h
                # 1 e
                # 2 l
                # 3 l
                # 4 o
    i += 1



s = 'hello'

for i in range(len(s)):
    print(i, s[i])



s = 'hello'

for i, c in enumerate(s):
    print(i, c)  #  0 h
1 e
2 l
3 l
4 o
