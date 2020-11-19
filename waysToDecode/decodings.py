import itertools
import re
import string

# creates a dictionary mapping each letter of the alphabet to its corresponding number 1-26
alpha_map = {key: value for key, value in zip(list(string.ascii_lowercase), [i for i in range(27)[1:]])}

# gets an encoded message from the user and splits each digit into a list
message = input("Enter an encoded message:\n> ")
split_msg = list(message)

# appends a 0 to the list so the program can detect single-digit encodings in the message
# (an encoding is defined as any number 1-26)
split_msg.append("0")

# creates a set to hold all encodings found in the message
encs_found = set()

# finds all encodings in the message
for i in itertools.permutations(split_msg, r=2):
    # for every length two permutation of split_msg, this for loop:
    # joins the permutation tuple and strips any leading zeros from the resulting string
    joined_i = "".join(i).lstrip("0")
    try:
        # the permutation is considered to be an encoding if its found in the message and is a number 1-26
        if joined_i in message and int(joined_i) in alpha_map.values():
            encs_found.add(int(joined_i))
    # sometimes the joined permutation tuples end up being empty strings, which will cause a ValueError in this loop
    except ValueError:
        continue

# creates a list of all possible combinations of the values in encs_found that, when joined together as a string,
# contain all of the encoded message
possible_combinations = [list(i) for i in itertools.product(encs_found, repeat=len(message))
                         if message in "".join([str(x) for x in i])]

# creates a set to hold the numerical equivalents of each possible decoding of the message
numerical_decodings = set()

# creates a regular expression object to strip extra characters from each combination in possible_combinations
rgx_msg = re.compile(",?\s?".join(split_msg[:-1]))
for combination in possible_combinations:
    numerical_decodings.add(re.search(rgx_msg, str(combination)).group(0))

# alphabetizes each decoding in numerical_decodings
alpha_decodings = []
for decoding in numerical_decodings:
    alphabetic = []
    for i in list(decoding.split(", ")):
        alphabetic.append(list(alpha_map.keys())[int(i) - 1])
    alpha_decodings.append("".join(alphabetic))

# prints the number of ways to decode the encoded message as well a list of all possible decodings
print(f"Ways to decode: {len(alpha_decodings)}\n"
      f"Possible decodings: {', '.join(alpha_decodings)}")
