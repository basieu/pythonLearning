class Test:
    def __init__(self):
        print("Test start")
    
    def __del__(self):
        print("Test stop")


test = Test()