"""
## Problem 82
This problem was asked Microsoft.

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""

with open('test.txt', 'w') as f:
    f.write("Hello world")

class FileHandler(object):
    def __init__(self):
        self.buffer = []
        self.offset = 0
        self.end_reached = False
        
    def read7(self):
        with open('test.txt', 'r') as f:
            f.seek(self.offset)
            op_start_offset_value = copy.deepcopy(self.offset)
            while True:
                if self.offset % 7 == 0 and self.offset != op_start_offset_value:
                    break
                char = f.read(1)
                if not char:
                    self.end_reached = True
                    
                self.offset += 1
                self.buffer.append(char)
                      
    def readN(self, n):
        result = ""
        
        if not self.end_reached:
            self.read7()
            result = "".join(self.buffer[:n])
            self.buffer = self.buffer[n:]
        
        return result
            
    
fh = FileHandler()
print(fh.readN(7))
print(fh.readN(7))
print(fh.readN(7))
