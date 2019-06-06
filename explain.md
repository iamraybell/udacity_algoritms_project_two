# Problem 1:
    For this Problem, we need to have have quick access to the least recently used Item so we can remove it when over capacity. We also needed to get access to each item.
    There are data structures that are great for one of these problems, but not both. So, to solve this, we can mix data structures. Using a doubely linked list could help use access the last and first elements quickly. It also gives us quicker removal when comparing it to the time complexity of an Array.

    The set function is O(1). The reason is that it only needs to update the same amount of 
        pointers and put itself in the cache everything
    get is also O(1).  we can get the item from the cache easily, but we need to 
    update pointers. this still we be O(1) since we dont need to treverse the full list.

    Space complexity for this is O(n). It is a little more (because we are using two data structures to store information)

# Problem 2: 
    I could to use a recursive style solution for a couple of reasons. For one, it helps with readability.  We could have used a queue and pushed the levels in an array, but that also would increase the space complexity of this problem.

    To Traverse a file system, the time complexity is  O(n + m), where n is the number of nodes, 
    and m is the number of edges. (children)

    I think the space complexity is also O(n + m), because of the recursive nature of this alogorithm. 
# Problem 3:
    There are many things needed to solve this problem. We need to have an array of sort nodes (least to greatest), we need to build a tree  showing the frequencies, and then we need to encode and decode.

    One thing I use in this code is a cache. This saves us from have to consistanly treverse the tree to get nodes. I use a minHeap algorithm to get the smallest item out when we need them. We could have used others sorts here (like quicksort). 

    As stated before, there is a lot of code that happens in this problem. I wanted to follow Clean code practices as much as possible and keep fuctions readable and small.

    Time complexity on the huffman encoding O(n log n). we 
    have to build the heap using a heapsort algorithm, which has a time complexity of O( Log n). There are smaller orders that take place like building the cache and the actual building of the tree, but this is the higher order.
   Decoding would be O(n + m) (where n is each node and m is each edge) we need to walk the tree and get the codes from
    each path. we do walk the string, but the bigger order is building the cache.

    Soace complexity would be O(n + m), where n is each node and m is each edge.

# Problem 4:
    Since this  called for checkig a group at each level to see if a user is in it, I wanted to use a queue here. We can add each group to the array in the order we see them, and fast fail if the user is in that group. We could do something similar with a recursive algorithm, but I feel like it adds a bit of complexity. I also think using a queue makes it a little more readable.

    This problem has a time complexity of O (n + m). At worst, we might have to check all groups.
    O(n) is the space complexity, where n is the amount of groups.

# Problem 5:
    Adding to the list in the blockchain is O(1). We cache the previous hash so we dont have to rewalk the list to get it. (which could make this problem O(nsqaured)) so the only complexity is to build the node.
    Space complexity for this is O(n) where n is the amount of Nodes.


# Problem 6:
    I love using caches when possible, and this problem leads it self to using one. A solution for this problem could be to walk one list, and then walk the other list and compare it against each on in that list. This would be a solution of O(nsquared) and not very good. We can save time by using a set and "saving" the results of each list. That way, we only have to walk the list once.

    I think for both the union and intersection the time complexity is O(n)
    we will need to walk both list, but we use a set to cache our results so we dont have to
    re walk the lists.
    Space complexity of this problem would be O(n). We need to create a set in both problems of both lists. (or a subset of them)
