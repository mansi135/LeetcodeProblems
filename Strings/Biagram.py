'''A bigram is a pair of consecutive words. Given a string, return the longest bigram in that string. Include the space between the words. Assume there will be no punctuation. In the case of a tie, return the earlier bigram.'''


def biagram(str):
    l = str.split(' ')
    l_new = []

    for i in range(len(l) - 2):
        if (len(l[i]) + len(l[i + 1])) > (len(l[i + 1]) + len(l[i + 2])):
            #  l_new.append(l[i])
            #  l_new.append(l[i+1])
            index1 = i
            index2 = i + 1
        else:
            index1 = i + 1
            index2 = i + 2

    l_new.append(l[index1])
    l_new.append(l[index2])

    print(" ".join(l_new))


biagram("Magic bold moveuhiuytuuu test ferogggggg")