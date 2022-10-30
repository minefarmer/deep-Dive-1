# args: example4
import sys

#  --last-name Cleese --first-name John   ## entered in the terminal

# print(sys.argv[1:])  #  --last-name Cleese --first-name John

for i in range(1, len(sys.argv), 2):
    print(sys.argv[i], sys.argv[i+1])  # --last-name Cleese
                                       # --first-name John


