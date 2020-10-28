import os
path=r"C:\Users\mbobbili\Desktop\0302"
pdfs=[i for i in os.listdir(path) if i.find(".pdf")>=0]
class TrieNode:
    def __init__(self,data):
        self.data=data
        self.children={}
        self.isCompleted=False
    def __str__(self):
        return self.data
def display(node,str):
    if node.isCompleted:
        print(str)
    else:
        for child in node.children:
            child_node=node.children[child]
            display(child_node,str+child)
def suggestions(root,character):
    if root.isCompleted:
        return False
    else:
        for i in character:
            if i in root.children:
                node=root.children[i]
                suggestions(node,)

def add(root,character):
    node=root
    for i in character:
        found_in_child=False
        if i in node.children:
            found_in_child=True
            node=node.children[i]
        if not found_in_child:
            new_node=TrieNode(i)
            node.children[i]=new_node
            node=new_node
    node.isCompleted=True
def search(root,character):
    node=root

root=TrieNode("*")
print(root.children)
for i in pdfs:
    print(i)
    add(root,i)
print_trie(root)
