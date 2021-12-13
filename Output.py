class Output:
    def __init__(self, f_name) -> None:
        self.f = open(f"{f_name}.txt", "a")
    
    def write(self, ip) -> None:
        self.f.write(f"{ip}\n")
        self.f.flush()
    
    def close(self):
        self.f.close()