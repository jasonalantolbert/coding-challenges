# https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/


from anytree import Node
from anytree.walker import Walker

funnel_queue = []  # queue of words to funnel


def dig(word, parent=None, root=None):
    """
    Finds direct descendants of a word and adds them to funnel_queue.
    @param word: The word of which to find direct descendants.
    @param parent: In the funnel tree, the parent node from which the word is directly descended.
    @param root: In the funnel tree, the node from which all words are descended.
    """
    with open("enable1.txt", "r") as enable1:
        # creates a set containing all words in enable1.txt
        wordset = set(" ".join(set(enable1.readlines())).replace("\n", "").split(sep=" "))
    if root:
        # indicates that the word is the root of the funnel tree
        if word in wordset:
            node = root
        else:
            print("That's not a word.")
            exit()
    else:
        # in the funnel tree, creates for the word a node descended from the its parent word's node
        node = Node(word, parent=parent)
    for index in range(len(word)):
        # removes each character from the word and tests to see if the resulting word is in enable1.txt. if it is,
        # a dictionary containing the resulting word and its parent node are added to funnel_queue.
        split_word = list(word)
        split_word.pop(index)
        child_word = "".join(split_word)
        if child_word in wordset:
            # noinspection PyUnboundLocalVariable
            funnel_queue.append({"word": child_word, "parent_node": node})


def main():
    # requests a word from the user
    query = input("Enter a word:\n> ")
    print("Processing (this could take a few seconds)...\n")

    # sets the root node to the user's input
    root_node = Node(query)
    # finds direct descendants of root word
    dig(query, root=root_node)

    while funnel_queue:
        for index, word_dict in enumerate(funnel_queue):
            # finds direct descendants of all words in funnel queue
            funnel_queue.pop(index)
            dig(word_dict["word"], parent=word_dict["parent_node"])

    print(f"Longest funnel length: {(root_node.height + 1) if root_node.height > 0 else 0}\n"
          f"\n"
          f"Longest funnel(s):")

    longest_funnels = set()  # creates a set to hold the root word's longest funnel(s)

    # iterates through each of the deepest child nodes, adding string representations of the paths from
    # the root node to each child node to longest_funnels
    for child_node in [child for child in root_node.descendants if child.depth == root_node.height]:
        walk_path = list(Walker().walk(root_node, child_node)[2])
        walk_path.insert(0, root_node)
        funnel_string = ""
        for node in walk_path:
            funnel_string += node.name + (' -> ' if node != walk_path[-1] else "")
        longest_funnels.add(funnel_string)
    if longest_funnels:
        # prints the paths of each longest funnel
        for funnel in sorted(longest_funnels):
            print(funnel)
    else:
        print("No funnels")


main()
