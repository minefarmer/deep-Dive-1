# args: example4
import sys

#  --last-name Cleese --first-name John

print(sys.argv[1:])

for l in range(1, len(sys.argv), 2):
    print(sys.argv[l])


