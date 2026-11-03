class Node:
    def __init__(self, url, next = None, prev = None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)

    def visit(self, url: str) -> None:
        tmp = self.history
        self.history.next = Node(url)
        self.history = self.history.next
        self.history.prev = tmp

    def back(self, steps: int) -> str:
        count = 0
        while count < steps:
            if self.history.prev:
                self.history = self.history.prev
            count += 1
        return self.history.url

    def forward(self, steps: int) -> str:
        count = 0
        while count < steps:
            if self.history.next:
                self.history = self.history.next
            count += 1
        return self.history.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)