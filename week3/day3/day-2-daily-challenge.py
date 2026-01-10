import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # --- Navigation Methods ---

    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} is out of range")
        self.current_idx = page_num - 1
        return self  # allows chaining

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1 if self.total_pages > 0 else 0
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # --- Bonus: Custom string representation ---
    def __str__(self):
        visible = self.get_visible_items()
        return "\n".join(str(item) for item in visible)

# --- Test Cases ---
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())  
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())  
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())  
# ['y', 'z']

try:
    p.go_to_page(10)
except ValueError as e:
    print(e)  
# Page number 10 is out of range

try:
    p.go_to_page(0)
except ValueError as e:
    print(e)  
# Page number 0 is out of range

# --- Bonus: Method Chaining ---
print(p.first_page().next_page().next_page().next_page().get_visible_items())  
# ['m', 'n', 'o', 'p']

# --- Bonus: Print current page nicely ---
print(str(p))  
# m
# n
# o
# p
