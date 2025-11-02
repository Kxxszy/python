v='global v'
def function_a():
    global v
    print(v)
    v="function a local"
    print(v)

def function_b():
    v_new= "function b local"
    print(v_new)
    function_a()

function_b()

