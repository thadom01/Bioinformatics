import argparse

# creates and stores the arguments created for argparse and opens the file
def main():
    parser = argparse.ArgumentParser(description="Calculate nucleotide frequency")
    parser.add_argument('-k', dest='k', default=1, type=int, help='length of sequence')
    parser.add_argument('-f', dest='file', required=True, help='sequence file name' )
    args = parser.parse_args()

    f = open(args.file, 'r')
    seq = f.read().replace('\n', '')
    k = args.k
    kmerCount(seq, k)

# allows for user to input a file/string and a k for the length of sequence you want
def kmerCount(geneFile, k):
    kFreq = {}
    total = 0
    nuc = ''
    frequency = {}

# for loop that goes through each element of the file
# if/else statement checks for each element in the file
# if each element is in the file it adds to the count of that element
# if not already recorded it records it along with its count
    for nuc in range(0, len(geneFile)-(k-1)):
        nuc = geneFile[nuc: nuc + k]
        if nuc in kFreq:
            frequency = kFreq.get(nuc)
            kFreq[nuc] += 1
            total += 1
        else:
            kFreq[nuc] = 1
            total += 1
    print(kFreq)

    outFile = open("ps1_Results.txt", "w")
    for x in kFreq:
        outFile.write(x + "  "+ str(kFreq[x]))
        outFile.write('\n')

# allows the program to run by calling the main function
if __name__ == '__main__':
    main()

