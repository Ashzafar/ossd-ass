def fibonacci_sequence(limit, current=0, prev=1):
    if current > limit:
        return
    else:    
        print(current)
        fibonacci_sequence(limit, prev, current + prev)
fibonacci_sequence(100)