class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
     
    def addChild(self, children):
        children.parent = self
        self.children.append(children)
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

        
            
    def print_tree(self):
        spaces = ' ' * self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children)> 0:
            for child in self.children:
                child.print_tree()
def buid_Prod_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    
    smartphone = TreeNode("Smartphone")
    smartphone.addChild(TreeNode("iphone"))
    smartphone.addChild(TreeNode("Google pixels"))
    
    Television = TreeNode("Television")
    Television.addChild(TreeNode("Samsung"))
    Television.addChild(TreeNode("LG"))
    
    root.addChild(laptop)
    root.addChild(smartphone)
    root.addChild(Television)
    
    return root
            
     
if __name__ == "__main__":
    root =buid_Prod_tree()
    root.print_tree()
            
          