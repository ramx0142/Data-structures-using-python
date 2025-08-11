class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def push(self,title):
        new_node=node(title)
        new_node.next=self.top
        self.top=new_node
        print("pushed the value : ",title)
    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            print("popped:",self.top.data)
            self.top=self.top.next
    def display(self):
        if self.top is None:
            print("stack is empty")
        else:
            tmp=self.top
            while tmp:
                print(tmp.data,end="-> ")
                tmp=tmp.next
            print("Null")
if __name__ == "__main__":
    stack1=stack()
    while True:
        print("1.push")
        print("2.pop")
        print("3.display")
        print("4.exit")
        try:
            choice=int(input("Enter your choice"))
        except ValueError:
            print("Please enter a valid number : ")
            continue
        
        if choice==1:
            title=input("Enter the value to push : ")
            stack1.push(title)
        
        elif choice==2:
            stack1.pop()
        elif choice==3:
            stack1.display()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


            
            
            
                
                
        
