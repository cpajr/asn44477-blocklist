import bgpstuff
import ipaddress
import sys
from datetime import datetime

c = bgpstuff.Client()
c.get_sourced_prefixes(44477)

timestamp = datetime.now()
timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
output = f'# Generated {timestamp_str} \n'

if c.sourced:
    for prefix in c.sourced:
        if ipaddress.ip_network(prefix).version == 4:
            output += str(prefix) + "\n"
    sys.stdout.write(output)