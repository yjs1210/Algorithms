#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []

    def Push(self, a):
        if len(self.__stack) == 0:
            self.__stack.append((a,a))
        else:
            self.__stack.append((a,max(a, self.__stack[-1][1])))

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()[0]

    def Max(self):
        assert(len(self.__stack))
        return self.__stack[-1][1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
