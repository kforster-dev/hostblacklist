import blacklistutils, argparse

#TestString = "google.com"
#blacklistutils.blacklist(TestString)

DEFAULT_IP = "0.0.0.0"

parser = argparse.ArgumentParser(
    description="Arguments."
)

parser.add_argument('Domain',
    type=str,
    nargs=1,
    help='Input a domain to block.'
)

parser.add_argument('-ip',
    type=str,
    required=False,
    help='Input an IP to redirect to.'
)

args=parser.parse_args()
DomainString = args.Domain[0]
# Check if this domain already exists.
Exists = blacklistutils.checkExists(DomainString)
if Exists == False:
        # Custom IP from args
        if bool(args.ip) == True:
             blacklistutils.blacklist(DomainString, args.ip)
        # Default IP
        else:
             blacklistutils.blacklist(DomainString, DEFAULT_IP)
else:
    Input = input("This host already exists. Input D to Delete, M to Modify or C to Cancel: ")
    if Input == "D":
        blacklistutils.modifyHost(DomainString, False)
    elif Input == "M":
        # If an IP wasn't specified or was wrong, ask for one.
        if bool(args.ip) == True:
             blacklistutils.blacklist(DomainString, args.ip)
        else:
            newIP = input("Redirect a new IP to redirect to: ")
            blacklistutils.modifyHost(DomainString, newIP)
    elif Input == "C":
        print("Cancelled.")
    else:
        print("Invalid input, cancelled.")