import bgpstuff
import ipaddress
import sys

c = bgpstuff.Client()
c.get_sourced_prefixes(44477)

if c.sourced:
    output = ""
    for prefix in c.sourced:
        if ipaddress.ip_network(prefix).version == 4:
            output += str(prefix) + "\n"
    sys.stdout.write(output)