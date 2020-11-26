from bstmess import BSTNode


def main():
    node = BSTNode("Memento")
    node._print_structure()
    print('> adding Melvin and Howard')
    node.add("Melvin and Howard")
    node._print_structure()
    print('> adding a second version of Melvin and Howard')
    node.add("Melvin and Howard")
    node._print_structure()
    print('> adding Mellow Mud')
    node.add("Mellow Mud")
    node._print_structure()
    print('> adding Melody')
    node.add("Melody")
    node._print_structure()
    print("Finding: ")
    print(str(node.search_node('Melvin and Howard')))



if __name__ == "__main__":
    main()
