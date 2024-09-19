class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.pages = []
        self.pages.append(homepage)
        self.curr = 0

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.curr+1<len(self.pages):
            self.curr = self.curr+1
            self.pages[self.curr]=url
            self.pages = self.pages[:self.curr+1]
        else:
            self.pages.append(url)
            self.curr = self.curr+1 
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps <= self.curr:
            self.curr=self.curr-steps
        else:
            self.curr = 0
        return self.pages[self.curr]
        
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if (steps + self.curr) >= len(self.pages):
            self.curr = len(self.pages)-1
        else:
            self.curr = self.curr + steps
        return self.pages[self.curr]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)