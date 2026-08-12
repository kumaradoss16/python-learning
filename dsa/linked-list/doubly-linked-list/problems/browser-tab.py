class PageNode:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None

class BrowserTab:
    def __init__(self, homepage):
        self.current = PageNode(homepage)

    def visit(self, url):
        new_page = PageNode(url)
        new_page.prev = self.current
        self.current.next = new_page
        self.current = new_page

    def go_back(self):
        if self.current.prev:
            self.current = self.current.prev
        return self.current.url

    def go_forward(self):
        if self.current.next:
            self.current = self.current.next
        return self.current.url


tab = BrowserTab("home.com")
tab.visit("google.com")
tab.visit("github.com")

print(tab.go_back())
print(tab.go_back())
print(tab.go_forward())
