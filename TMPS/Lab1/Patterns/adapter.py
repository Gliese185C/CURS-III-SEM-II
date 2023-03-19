
class Server:

    def getHost(self):
        return ("host/static/78-213-113-153.moldtelecom.md")



class Web:

    def showIp(self,host):
        if len(host) > 16:
            return "Error"
        return host


class Adapter:

    def hostToIp(self,host):
        ip = host
        new = [str(item) for item in range(1,10)]
        for item in host:
            if item not in new and item != "-":
                ip = ip.replace(item, "")
        ip = ip.replace("-",".")

        return ip




if __name__ == "__main__":
    backside = Server()
    frontside = Web()
    adapter = Adapter()

    print(frontside.showIp(adapter.hostToIp(backside.getHost())))
