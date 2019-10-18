import json
import time
from models.Networks import Network

NETWORK_FILE = r"C:\Dev\PycharmProjects\IPLookUp\data\grx_lookup.json"
IP_FILE = r"C:\Dev\PycharmProjects\IPLookUp\data\ips.txt"


if __name__ == "__main__":

    ips = []
    networks = []
    with open(NETWORK_FILE, 'r') as JSON:
        network_data = json.load(JSON)
        for record in network_data:
            networks.append(record)

    with open(IP_FILE, 'r') as fh:
        for ip in fh:
            ips.append(ip.strip())

    network_manager = Network(networks)
    network_manager.init_network_binary()
    network_manager.init_binary_data()
    print(network_manager.networks_binary)
    start_time = time.time()
    for ip in ips:
        #slow implementation
        #print(network_manager.ip_in_network(ip))
        network_manager.binary_search(ip)
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Total execution time: {total_time} seconds')
