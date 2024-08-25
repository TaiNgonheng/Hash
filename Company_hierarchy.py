class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []  # subordinates

    def add_subordinate(self, employee):
        self.subordinates.append(employee)

    def remove_subordinate(self, employee):
        self.subordinates = [c for c in self.subordinates if c != employee]

    def __str__(self):
        return f"{self.name}-{self.position}"

class CompanyHierarchy:
    def __init__(self, root):
        self.root = root

    def bfs_traversal(self):
        queue = [self.root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(str(current))
            queue.extend(current.subordinates)
        return ', '.join(result)

    def dfs_traversal(self):
        result = []
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(str(current))
            stack.extend(reversed(current.subordinates))  # Reverse to maintain left-to-right order
        return ', '.join(result)

    def search(self, name, position):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.name == name and current.position == position:
                return current
            queue.extend(current.subordinates)
        return None

    def delete(self, name, position):
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            for subordinate in current.subordinates:
                if subordinate.name == name and subordinate.position == position:
                    current.remove_subordinate(subordinate)
                    return True
            queue.extend(current.subordinates)
        return False

    def print_tree(self, employee=None, level=0):
        if employee is None:
            employee = self.root
        print(' ' * (level * 4) + str(employee))
        for subordinate in employee.subordinates:
            self.print_tree(subordinate, level + 1)

# company hierarchy
thuraty_ceo = Employee("Tai Ngonheng", "CEO")
dilong_manager = Employee("Dilong", "Manager(Supervisor)")
dalis_manager = Employee("Dalis", "Manager(IT Website)")
srey_staff = Employee("Srey kech", "Staff(System Admin)")
kompheak_intern = Employee("Kompheak", "Intern(IT support)")
kolab_intern = Employee("Kolab", "Intern(Roster Database)")

thuraty_ceo.add_subordinate(dilong_manager)
thuraty_ceo.add_subordinate(dalis_manager)
thuraty_ceo.add_subordinate(srey_staff)
thuraty_ceo.add_subordinate(kompheak_intern)
thuraty_ceo.add_subordinate(kolab_intern)
company = CompanyHierarchy(thuraty_ceo)

print("Company Hierarchy:")
company.print_tree()
print("\nBFS Traversal:")
print(company.bfs_traversal())
print("\nDFS Traversal:")
print(company.dfs_traversal())
employee = company.search("Kompheak", "Intern(IT support)")
search_result = "Found" if employee else "Not Found"
print(f"\nSearching for Srey kech-Staff(System Admin): {search_result}")
delete_success = company.delete("Srey kech", "Staff(System Admin)")
delete_message = "deleted" if delete_success else "not found"
print(f"\n'Srey kech-Staff(System Admin)' has been {delete_message} from the directory.")
print("\nCompany Hierarchy after Deletion:")
company.print_tree()

                                                                                               
