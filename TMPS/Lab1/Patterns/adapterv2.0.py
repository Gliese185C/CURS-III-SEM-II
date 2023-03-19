class Target:
    def request(self):
        return "Default request"

class Adaptee:
    def specific_request(self):
        return "Specific request"

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapted from {self.adaptee.specific_request()}"

def client_code(target):
    print(target.request())

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)