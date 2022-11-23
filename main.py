from res import test

# the class Test performs tests about research and insertion speed both with red-black trees and the binary ones

# we can choose to execute the tests with random values or with sequential values with this initialization:
#                                                                   test_type, research_type, start, max value and step

# NOTE:  more than 900 max value with normal mode won't work, because it can't execute more than 900 recursions in the
#        binary tree

# test = test.Test("random", "not success", 1000, 10000, 200, "rand_not_sux_res test")

test1 = test.Test("random", "success", 0, 5001, 100, "rand_sux_res_tot test")
test1.create_plot()
test1.create_docs()
del test1

test2 = test.Test("random", "success", 0, 201, 10, "rand_sux_res_low test")
test2.create_plot()
test2.create_docs()
del test2

test3 = test.Test("random", "success", 2200, 2401, 10, "rand_sux_res_mid test")
test3.create_plot()
test3.create_docs()
del test3
#
test4 = test.Test("random", "success", 4800, 5001, 10, "rand_sux_res_high test")
test4.create_plot()
test4.create_docs()
del test4

test5 = test.Test("normal", "success", 1, 800, 10, "sequential_values test")
test5.create_plot()
test5.create_docs()
del test5



