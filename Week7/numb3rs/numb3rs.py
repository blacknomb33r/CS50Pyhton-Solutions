import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if not re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
            return False
      
        for i in ip.split("."):
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    
    except:
        return False

if __name__ == "__main__":
    main()
