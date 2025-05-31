class RecentCounter:

    def __init__(self):
        self.requests = []
        

        



        
    
    def ping(self, t: int) -> int:
        count = 0
        
        self.requests.append(t)
        ranger = [t-3000, t]
        snapshot = self.requests
        while self.requests and self.requests[0] < min(ranger):
            self.requests.pop(0)

      

       
        count = len(self.requests)

        return count


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)