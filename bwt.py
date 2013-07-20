import sys

#append lexographically smallest terminal charcter to input...
in_str = sys.argv[1] + "$"

#create substrings for sorting...
sub_strs = [in_str[i:len(in_str)] + in_str[0:i] for i in range(len(in_str))]

sub_strs.sort()

bwt = "".join([sub_str[-1] for sub_str in sub_strs])

print(bwt)
