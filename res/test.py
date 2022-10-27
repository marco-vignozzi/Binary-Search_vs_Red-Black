import random
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from res.BTree.BTclass import BTree
from res.RBTree.RBTclass import RBTree
from pathlib import Path


def random_list(n):
    r_list = list(range(n))
    random.shuffle(r_list)
    return r_list


def test_insert(tree, values_list, number_of_entries, r=0):
    start = timer()
    for x in range(0, number_of_entries, r+1):
        tree.insert(values_list[x])
    end = timer()
    return tree.get_name(), "insert", number_of_entries, end - start


def test_find(tree, values_list, number_of_searches, r=0):
    start = timer()
    for x in range(1, number_of_searches, r+1):
        tree.find(values_list[x])
    end = timer()
    if r:
        return tree.get_name(), "n_find", number_of_searches//2, end - start
    else:
        return tree.get_name(), "find", number_of_searches, end - start


def choose_value(test_element, value_type):
    if value_type == "time":
        return test_element[3]
    else:
        return test_element[2]


def get_values_list(value_type, op_type, tree_type, tests_list):
    values_list = []
    for i in range(len(tests_list)):
        if tests_list[i][0] == tree_type and tests_list[i][1] == op_type:
            values_list.append(choose_value(tests_list[i], value_type))
    return values_list


def create_tests_list(op, n_list, start, end, step):  # number of times the test is executed = (end-start)/step
    t_list = list()
    b_tree = BTree()
    rb_tree = RBTree()
    if op == "insert":
        for x in range(start, end, step):
            b_tree.clear()
            rb_tree.clear()
            t_list.append(test_insert(rb_tree, n_list, x))  # add a test
            t_list.append(test_insert(b_tree, n_list, x))
    elif op == "find":
        test_insert(rb_tree, n_list, end)
        test_insert(b_tree, n_list, end)
        for x in range(start, end, step):
            t_list.append(test_find(rb_tree, n_list, x))
            t_list.append(test_find(b_tree, n_list, x))
    else:
        test_insert(rb_tree, n_list, end, 1)
        test_insert(b_tree, n_list, end, 1)
        for x in range(start, end, step):
            t_list.append(test_find(rb_tree, n_list, x, 1))
            t_list.append(test_find(b_tree, n_list, x, 1))

    return t_list


def create_txt(tree_type, op_type, tests_list):
    text = ""
    for i in range(len(tests_list)):
        if tests_list[i][0] == tree_type and tests_list[i][1] == op_type:
            text += f"number of elements = {tests_list[i][2]}" + "" \
                                    "    execution time = " + "{:10.5f}".format(tests_list[i][3]) + "\n"
    return text


class Test:

    def __init__(self, t_type="random", r_type="success", start=1, max_value=10, step=1, dir_name="test"):

        self.doc_path = Path(f"docs/{dir_name}")

        if t_type == "random":
            numbers_list = random_list(max_value)
        else:
            numbers_list = list(range(max_value))

        self.test_type = t_type
        self.r_type = r_type
        self.start = start
        self.max_value = max_value
        self.step = step
        self.numbers_list = numbers_list

        self.tests = create_tests_list("insert", numbers_list, start, max_value, step)
        self.tests += create_tests_list("find", numbers_list, start, max_value, step)

        self.rbt_time_values_i = get_values_list("time", "insert", "red-black tree", self.tests)
        self.bt_time_values_i = get_values_list("time", "insert", "binary tree", self.tests)
        self.rbt_numbers_values_i = get_values_list("number", "insert", "red-black tree", self.tests)
        self.bt_numbers_values_i = get_values_list("number", "insert", "binary tree", self.tests)

        self.rbt_time_values_r = get_values_list("time", "find", "red-black tree", self.tests)
        self.bt_time_values_r = get_values_list("time", "find", "binary tree", self.tests)
        self.rbt_numbers_values_r = get_values_list("number", "find", "red-black tree", self.tests)
        self.bt_numbers_values_r = get_values_list("number", "find", "binary tree", self.tests)

        if r_type != "success":
            self.not_sux_numbers_list = random_list(2*max_value)
            self.tests += create_tests_list("find " + r_type, self.not_sux_numbers_list, 2*start, 2*max_value, 2*step)
            self.rbt_time_values_rn = get_values_list("time", "n_find", "red-black tree", self.tests)
            self.bt_time_values_rn = get_values_list("time", "n_find", "binary tree", self.tests)
            self.rbt_numbers_values_rn = get_values_list("number", "n_find", "red-black tree", self.tests)
            self.bt_numbers_values_rn = get_values_list("number", "n_find", "binary tree", self.tests)

    def create_plot(self):
        plt.rcParams.update({'figure.figsize': (10.5, 8.5), 'figure.dpi': 100})

        if self.r_type != "success":
            rows = 3
        else:
            rows = 2

        fig, axs = plt.subplots(nrows=rows, ncols=1)
        fig.suptitle("ARN vs ABR")
        fig.tight_layout(pad=3)

        axs[0].plot(self.rbt_numbers_values_i, self.rbt_time_values_i, "r")
        axs[0].plot(self.bt_numbers_values_i, self.bt_time_values_i, "b")
        axs[0].set_xlabel("Numero elementi inseriti")
        axs[0].set_ylabel("Tempo")
        axs[0].set_title("Inserimento")
        axs[0].legend(["ARN", "ABR"])

        axs[1].plot(self.rbt_numbers_values_r, self.rbt_time_values_r, "r")
        axs[1].plot(self.bt_numbers_values_r, self.bt_time_values_r, "b")
        axs[1].set_xlabel("Numero elementi cercati")
        axs[1].set_ylabel("Tempo")
        axs[1].set_title("Ricerca con successo")
        axs[1].legend(["ARN", "ABR"])

        if self.r_type != "success":
            axs[2].plot(self.rbt_numbers_values_rn, self.rbt_time_values_rn, "r")
            axs[2].plot(self.bt_numbers_values_rn, self.bt_time_values_rn, "b")
            axs[2].set_xlabel("Numero elementi cercati")
            axs[2].set_ylabel("Tempo")
            axs[2].set_title("Ricerca senza successo")
            axs[2].legend(["ARN", "ABR"])
            plt.tight_layout()

#       plt.show()
        if not self.doc_path.exists():
            self.doc_path.mkdir()
        with open(f"{self.doc_path}/insert_and_search_comparison.png", "w") as f:
            plt.savefig(f"{self.doc_path}/insert_and_search_comparison.png")
            f.close()

        plt.close(fig)

        if self.r_type != "success":

            fig, axs = plt.subplots(nrows=2, ncols=1)
            fig.suptitle("Successo vs Insuccesso")

            axs[0].plot(self.rbt_numbers_values_r, self.rbt_time_values_r, "r")
            axs[0].plot(self.rbt_numbers_values_rn, self.rbt_time_values_rn, "b")
            axs[0].set_xlabel("Numero elementi cercati")
            axs[0].set_ylabel("Tempo")
            axs[0].set_title("Ricerca ARN")
            axs[0].legend(["Successo", "Insuccesso"])

            axs[1].plot(self.bt_numbers_values_r, self.bt_time_values_r, "r")
            axs[1].plot(self.bt_numbers_values_rn, self.bt_time_values_rn, "b")
            axs[1].set_xlabel("Numero elementi cercati")
            axs[1].set_ylabel("Tempo")
            axs[1].set_title("Ricerca ABR")
            axs[1].legend(["Successo", "Insuccesso"])

            plt.tight_layout()

            with open(f"{self.doc_path}/sux_vs_notsux_comparison.png", "w") as f:
                plt.savefig(f"{self.doc_path}/sux_vs_notsux_comparison.png")
                f.close()

    def create_docs(self):
        if not self.doc_path.exists():
            self.doc_path.mkdir()

        with open(f"{self.doc_path}/insertion_data.txt", "w") as f:
            f.write(f"Binary Tree insert() routine executed from {self.start} to {self.max_value} times with a step"
                    f" of {self.step} in {self.test_type} mode\n\n")
            paragraph = create_txt("binary tree", "insert", self.tests)
            f.write(f"{paragraph}\n\n")
            f.write(f"Red-Black Tree insert() routine executed from {self.start} to {self.max_value} times with a step"
                    f" of {self.step} in {self.test_type} mode\n\n")
            paragraph = create_txt("red-black tree", "insert", self.tests)
            f.write(f"{paragraph}\n\n")
            f.close()

        with open(f"{self.doc_path}/sux_search_data.txt", "w") as f:
            f.write(f"Binary Tree find() routine executed from {self.start} to {self.max_value} times with a step"
                    f" of {self.step} in {self.test_type} mode with successfull research\n\n")
            paragraph = create_txt("binary tree", "find", self.tests)
            f.write(f"{paragraph}\n\n")
            f.write(f"Red-Black Tree find() routine executed from {self.start} to {self.max_value} times with a step"
                    f" of {self.step} in {self.test_type} mode with successfull research\n\n")
            paragraph = create_txt("red-black tree", "find", self.tests)
            f.write(f"{paragraph}\n\n")
            f.close()

        with open(f"{self.doc_path}/values_list.txt", "w") as f:
            text_list = ""
            for x in range(len(self.numbers_list)):
                text_list += f"{self.numbers_list[x]}, "
            text_list = text_list[:-2]
            f.write("Values passed to create_tests_list() routine for both insert() and successfull find():"
                    "\n\n[ " + text_list + "]")
            f.close()

        if self.r_type != "success":
            with open(f"{self.doc_path}/not_sux_search_data.txt", "w") as f:
                f.write(f"Binary Tree find() routine executed from {self.start} to {self.max_value} times with a step"
                        f" of {self.step} in {self.test_type} mode with not successfull research\n\n")
                paragraph = create_txt("binary tree", "n_find", self.tests)
                f.write(f"{paragraph}\n\n")
                f.write(
                    f"Red-Black Tree find() routine executed from {self.start} to {self.max_value} times with a step"
                    f" of {self.step} in {self.test_type} mode with not successfull research\n\n")
                paragraph = create_txt("red-black tree", "n_find", self.tests)
                f.write(f"{paragraph}\n\n")
                f.close()

            with open(f"{self.doc_path}/not_sux_values_list.txt", "w") as f:
                text_list = ""
                for x in range(len(self.not_sux_numbers_list)):
                    text_list += f"{self.not_sux_numbers_list[x]}, "
                text_list = text_list[:-2]
                f.write("Values passed to create_tests_list() routine for not successfull find():"
                        "\n\n[ " + text_list + "]")
