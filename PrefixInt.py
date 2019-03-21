##############################################################################
# FCI      http://teaching.dessalles.fr/FCI            Jean-Louis Dessalles  #
# Telecom ParisTech  2019                                  www.dessalles.fr  #
# -------------------------------------------------------------------------- #
#                                              with Pierre-Alexandre Murena  #
##############################################################################

"""	This program generates a prefix code for integers
"""

import sys
import os

___Correction = 1

def Binary(N):
	" returns the binary code of N as a string "
	return bin(N)[2:]	# bin(17) == '0b10001', so bin(17)[2:] == '10001'
	
def DoublingCode(N):
	""" returns a code in wich all bits in the binary representation of N are doubled, 
		and then the last bit is reversed
	"""
	Double = ''.join([b * 2 for b in Binary(N)])	
	return Double[:-1] + str((1 - int(Double[-1])))

def DoublingLengthCode(N):
    " Returns a code in which the length of N is double-coded, followed by N in binary form "
    length = bin(len(str(N)))[2:]
    doubledlength = []
    for bit in length:
        if bit == '1':
            doubledlength.append('11')
        elif bit=='0':\
            doubledlength.append('00')

    if doubledlength[-1] == '11':
        doubledlength[-1] = '10'
    elif doubledlength[-1] == '00':
        doubledlength[-1] = '01'

    return ''.join(doubledlength)+N
                                        

def DoublingLengthDecode(BinN):
    " Interprets BinN as the double-length code of N "
    BinLength = ''	# binary reprentation of N's length
    BinN1 = iter(BinN)
    for B in BinN1:
    	BinLength += B
    	if next(BinN1) != B:	break	# consumes the next bit
    Length = int(BinLength, 2)

    return {'Number': int(BinN[-Length:],2), 'Length': Length, 'Remainder': ''}
		# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        N = int(sys.argv[1])
        PrefixCoded_N = DoublingLengthCode(N)
        print('Double-length coding for %d: %s' % (N, PrefixCoded_N))
        print('Decoding %s: %s' % (PrefixCoded_N, DoublingLengthDecode(PrefixCoded_N)))
    else:
        print("\tUsage: %s <int>" % os.path.basename(sys.argv[0]))
    print(__doc__)

	
__author__ = 'Dessalles'
