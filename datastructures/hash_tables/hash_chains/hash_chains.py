# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class HeadLinkedList():
    def __init__(self, s):
        self.next = None
        self.val = s
    
    def add(self, s):
        node = HeadLinkedList(s)
        if self.next:
            node.next = self.next
            self.next = node
        else:
            self.next = node
    
    def print_nodes(self):
        if self.next is None:
            print('')
        else:
            next = self.next
            output = next.val
            while True:
                next = next.next
                if next:
                    output += ' ' + next.val
                else:
                    break
            print(output)

    def find(self, s):
        match = self.next

        while match is not None:
            if match.val == s:
                return True
            else:
                match = match.next 

        return False

    def delete(self, s):
        curr = self
        target = self.next 
        while target is not None:
            if target.val == s:
                curr.next = target.next 
                del target
                break
            else:
                curr = target
                target = target.next

    

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [HeadLinkedList(None) for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def find(self, s):
        idx = self._hash_func(s)
        if self.elems[idx].find(s):
            return idx
        else:
            raise ValueError('not in map')
    
    def add(self, s):
        idx = self._hash_func(s)
        self.elems[idx].add(s)
    
    def delete(self, s):
        idx = self._hash_func(s)
        self.elems[idx].delete(s)
    
    def check(self, ind):
        if ind != -1:
            self.elems[ind].print_nodes()
        
    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.elems[query.ind].print_nodes()
        else:
            try:
                ind = self.find(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.add(query.s)
            elif query.type == 'check':
                self.check(ind)
            else: 
                if ind != -1:
                    self.delete(query.s) 


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
