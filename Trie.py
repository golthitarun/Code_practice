class triNode(object):
    
    def __init__(self):
        self.children = {}
        self.eow = False

class tri(object):
    
    def __init__(self):
        self.root = triNode()
    
    def insert(self,Node,string,index):
        if len(string)==index:
            Node.eow = True
            return
        if string[index] in Node.children:
            self.insert(Node.children[string[index]],string,index+1)
        else:
            Node.children[string[index]] = triNode()
            self.insert(Node.children[string[index]],string,index+1)
            
    def search(self,Node,string,index):
        if len(string)==index:
            #print "here"
            if Node.eow == True:
                #print "yo"
                return 1
            else:
                return 0
        elif string[index] in Node.children:
            #print "string char",string[index],index
            return self.search(Node.children[string[index]],string,index+1)
        else:
            return 0
        
    def startswith(self,Node,string,index):
        if len(string) == index:
            return True
        elif string[index] in Node.children:
            #print Node.children[string[index]].children
            #print "string char",string[index],index
            return self.startswith(Node.children[string[index]],string,index+1)
        else:
            return False