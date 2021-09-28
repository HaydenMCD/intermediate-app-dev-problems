import time

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def wipe(self):
        while (not self.items == []):
            s.pop()

s=Stack()
print('Is the stack currently empty?') #Testing if the stack is empty. True = empty. False = not empty.
print(s.is_empty())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now some data will be added to the stack. The number 4 has been added') #Adding '4' to the stack.
time.sleep(2)
s.push(4)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Is the stack currently empty?') #Testing if the stack is empty. True = empty. False = not empty.
print(s.is_empty())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now you can see that the last number added to the stack is:') #Displaying the data ontop of the stack.
print(s.peek())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('and that the size of the stack is now: ') #Displaying the size of the whole stack.
print(s.size())
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now I will add the numbers 5, 3 ,1 and 2') #Adding '5', '3', '1' and '2' to the stack.
s.push(5)
s.push(3)
s.push(1)
s.push(2)
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now the new numbers have been added the stack last number in the stack is:') #
print(s.peek())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('and the stack size is now:') #
print(s.size())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now I will delete the last number in the stack') #
s.pop()
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('Now that the last number has been deleted, the new last number is:') #
print(s.peek())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('and the stack size is now:') #
print(s.size())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('I will now delete all of the remaining numbers') #
s.wipe()
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('The stack size is now:') #
print(s.size())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')

print('and the stack is now empty:') #
print(s.is_empty())
time.sleep(2)
print('')
print('---------------------------------------------------------------------------')
print('')