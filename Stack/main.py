def push(self, item):
    if len(self.items) < self.max:
        self.items.append(item)
    else:
        print('abort pusb in orer to preven stack overflow')

def pop(self):
    if len(self.items) > 0:
        self.items.pop()
    else:
        print('stack is empth, abort pop to prevent stack underflow')