class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None or self.head.exp < exp:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.exp > exp:
                current = current.next

            if current.next and current.next.exp == exp:
                current.next.coeff += coeff
                if current.next.coeff == 0:
                    current.next = current.next.next
            else:
                new_node.next = current.next
                current.next = new_node

    def display(self):
        if self.head is None:
            print("0")
            return

        current = self.head
        result = []
        while current:
            coeff = current.coeff
            exp = current.exp
            if exp == 0:
                term = f"{coeff}"
            elif exp == 1:
                term = f"{coeff}x"
            else:
                term = f"{coeff}x^{exp}"
            result.append(term)
            current = current.next
        print(" + ".join(result))

    @staticmethod
    def add(poly1, poly2):
        p1 = poly1.head
        p2 = poly2.head
        result = Polynomial()

        while p1 and p2:
            if p1.exp > p2.exp:
                result.insert_term(p1.coeff, p1.exp)
                p1 = p1.next
            elif p1.exp < p2.exp:
                result.insert_term(p2.coeff, p2.exp)
                p2 = p2.next
            else:  
                sum_coeff = p1.coeff + p2.coeff
                if sum_coeff != 0:
                    result.insert_term(sum_coeff, p1.exp)
                p1 = p1.next
                p2 = p2.next

        while p1:
            result.insert_term(p1.coeff, p1.exp)
            p1 = p1.next

        while p2:
            result.insert_term(p2.coeff, p2.exp)
            p2 = p2.next

        return result

if __name__ == "__main__":
    poly1 = Polynomial()
    poly1.insert_term(5, 2) 
    poly1.insert_term(4, 1)  
    poly1.insert_term(2, 0)  

    poly2 = Polynomial()
    poly2.insert_term(5, 1)  
    poly2.insert_term(5, 0)  

    print("Polynomial 1:")
    poly1.display()

    print("Polynomial 2:")
    poly2.display()

    result = Polynomial.add(poly1, poly2)
    print("Sum of polynomials:")
    result.display()
