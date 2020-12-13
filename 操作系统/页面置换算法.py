page = []
page_ready = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

times = 0
def dec(func):
    stack = []
    def wrapper(page, lens, page_ready, times):
        if not page_ready:
            return times
        data = page_ready.pop(0)
        if data in page:
            stack.append(stack.pop(stack.index(data)))
            return wrapper(page, lens, page_ready, times)
        else:
            if len(page) < lens:
                page.append(data)
                stack.append(data)
                return wrapper(page, lens, page_ready, times)
            else:
                index = func(page, page_ready, stack)
                stack.pop(0)
                page[index] = data
                stack.append(data)
            return wrapper(page, lens, page_ready, times+1)
    return  wrapper

@dec
def optimal(page, page_ready, stack):
    temp_ = []
    for each in page:
        try:
            temp_.append(page_ready.index(each))
        except ValueError:
            temp_.append(float('inf'))
    return temp_.index(max(temp_))

index = -1
@dec
def fifo(page, page_ready, stack):
    global index
    index = (index+1)%3
    return index

@dec
def lru(page, page_ready, stack):
    return page.index(stack[0])

print(lru(page, 3, page_ready, 0))