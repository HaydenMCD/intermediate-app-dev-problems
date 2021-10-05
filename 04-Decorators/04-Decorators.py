def decorator(fn):
    from datetime import datetime
    import functools  
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        with open('.logfile.txt','a+') as f:
            try:
                f.write(f'Function: {fn.__name__}\n')
                f.write(f'run at: {datetime.now().strftime("%Y-%m-%dT%H:%M:%S")}\n')
                f.write(f'arguments: {args} and {kwargs}\n')
                f.write(f'returned value: {fn(*args,**kwargs)}\n')
            except Exception as e: 
                f.write(f'exception: {e}\n')
            else:
                f.write('exception: None\n')
            finally:
                f.write('-'*50 + '\n')
        return fn(*args,**kwargs)
    return wrapper

@decorator
def userInput():
    num1 = input('Enter the first number: ') #Asks user for input twice before running calculation
    num2 = input('Enter the second number: ')
    return int(num1) + int(num2)

def main():
    x = userInput()
    print (f'{x}')

if __name__ == '__main__':
    main()