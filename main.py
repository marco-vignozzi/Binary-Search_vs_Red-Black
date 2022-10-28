from res import test

# the class Test performs tests about research and insertion speed both with red-black trees and the binary ones

# we can choose to execute the tests with random values or with sequential values with this initialization:
#                                                                   test_type, research_type, start, max value and step

# NOTE:  more than 900 max value with normal mode won't work, because it can't execute more than 900 recursions in the
#        binary tree

test1 = test.Test("normal", "success", 1, 800, 10, "sequential_values test")
test2 = test.Test("random", "not success", 1000, 10000, 200, "rand_not_sux_res test")

test1.create_plot()
test1.create_docs()

test2.create_plot()
test2.create_docs()

