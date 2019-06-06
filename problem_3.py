import sys

class LeafNode ():
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

class freqNode ():
    def __init__(self,freq):
        self.freq = freq
        self.left = None
        self.right = None

def MinHeap (inputList):
    outputList = [None]
    for key, value in inputList.items():
        outputList.append(value) 
        upHeap(outputList, len(outputList)-1)
    return  outputList

def upHeap(outputList, childIdx):
    if childIdx <= 1:
        return
    parentIdx = int(getParentIndex(childIdx))
    if outputList[childIdx].freq < outputList[parentIdx].freq:
        swap(outputList, parentIdx, childIdx)
        upHeap(outputList, parentIdx)

def swap(outputList, parentIdx, childIdx):
    temp = outputList[parentIdx]
    outputList[parentIdx] = outputList[childIdx]
    outputList[childIdx] = temp

def getParentIndex(childIdx):
    return (childIdx - (childIdx % 2))/2

def createNodeCache(string):
    cache  = {}
    for char in string:
        if char not in cache:
            curNode = LeafNode(char, 1)
            cache[char] = curNode
        else:
            cache[char].freq +=1
    return cache
def getMinChildIdx(minHeap, parentIdx):
    child1Idx  = parentIdx * 2
    child2Idx  = (parentIdx * 2) + 1
    if child1Idx >= len(minHeap) and child2Idx >= len(minHeap):
        return None
    if child2Idx >= len(minHeap) and child1Idx < len(minHeap):
        return child1Idx
    if child1Idx >= len(minHeap) and child2Idx < len(minHeap):
        return child2Idx
    if minHeap[child1Idx].freq <= minHeap[child2Idx].freq:
        return child1Idx
    return child2Idx

def downHeap(minHeap, parentIdx):
    minChildIdx = getMinChildIdx(minHeap, parentIdx)
    if minChildIdx == None:
        return
    
    if minHeap[parentIdx].freq > minHeap[minChildIdx].freq:
        swap(minHeap, parentIdx, minChildIdx)
        downHeap(minHeap, minChildIdx)

def removeMin(minHeap):
    curMin = minHeap[1]
    swap(minHeap, 1, len(minHeap)-1)
    minHeap.pop()
    downHeap(minHeap, 1)
    return curMin

def createHoffmanTree(minHeap):
    if len(minHeap) == 1:
         raise Exception('Please Build an actual string!')
    while len(minHeap) > 2: # includes none at front
        node1 = removeMin(minHeap)
        node2 = removeMin(minHeap)
        sum = node1.freq + node2.freq
        parentNode = freqNode(sum)
        parentNode.left = node1
        parentNode.right = node2
        minHeap.insert(1,parentNode)
    if not isinstance(minHeap[1], freqNode ):
        parentNode = freqNode(minHeap[1].freq)
        parentNode.left = minHeap[1]
        minHeap[1] = parentNode
    return minHeap[1] 

def encodeCache(node, curCode, cache):
    if node == None:
        return
    if isinstance(node, LeafNode):
        cache[node.char]  = curCode
    else:
        encodeCache(node.left, curCode + '0', cache)
        encodeCache(node.right, curCode + '1', cache)
    return cache

def encodeStr(inputstr, inputCache):
    newStr =  ''
    for char in inputstr:
        newStr += str(inputCache[char])
    return newStr

def huffman_encoding(data):
    cache =  createNodeCache(data)
    minHeapNodes = MinHeap(cache)
    tree = createHoffmanTree(minHeapNodes)
    encodedCache = encodeCache(tree,'', {})
    encodedStr = encodeStr(data, encodedCache)
    return [encodedStr, tree]

def huffman_decoding(data,tree):
    originalStr = ''
    data = str(data)
    cache = encodeCache(tree, '', {})
    flipedCache = dict((v,k) for k,v in cache.items())
    
    curCode = ''
    for char in data:
        curCode += char
        if curCode in flipedCache:
            originalStr += flipedCache[curCode]
            curCode = ''

    return originalStr

testString1 = 'jb is cool'
print ("The size of the data is: {}\n".format(sys.getsizeof(testString1)))
print ("The content of the data is: {}\n".format(testString1))
encodedStr1, tree1 =  huffman_encoding(testString1)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedStr1, base=2))))
print ("The content of the encoded data is: {}\n".format(encodedStr1))
print(huffman_decoding(encodedStr1, tree1))

print('________________________')

testString2 = 'abcdefg'
print ("The size of the data is: {}\n".format(sys.getsizeof(testString2)))
print ("The content of the data is: {}\n".format(testString2))
encodedStr2, tree2 =  huffman_encoding(testString2)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedStr2, base=2))))
print ("The content of the data is: {}\n".format(encodedStr2))
print(huffman_decoding(encodedStr2, tree2))

print('________________________')

testString3 = 'zzzzzzzz' # tests same char
print ("The size of the data is: {}\n".format(sys.getsizeof(testString3)))
print ("The content of the data is: {}\n".format(testString3))
encodedStr3, tree3 =  huffman_encoding(testString3)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedStr3, base=2))))
print ("The content of the data is: {}\n".format(encodedStr3))
print(huffman_decoding(encodedStr3, tree3))


print('________________________')
testString4 = 'bbbbb eeeeee in the sink with bob'
print ("The size of the data is: {}\n".format(sys.getsizeof(testString4)))
print ("The content of the data is: {}\n".format(testString4))
encodedStr4, tree4 =  huffman_encoding(testString4)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encodedStr4, base=2))))
print ("The content of the data is: {}\n".format(encodedStr4))
print(huffman_decoding(encodedStr4, tree4))


print('________________________')
testString5 = ''
encodedStr5, tree5 =  huffman_encoding(testString5)
print(huffman_decoding(encodedStr5, tree5)) # this one should throw an error!

