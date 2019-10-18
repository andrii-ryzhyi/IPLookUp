import json
import time

NETWORK_FILE = r"C:\Dev\PycharmProjects\IPLookUp\data\grx_lookup.json"
IP_FILE = r"C:\Dev\PycharmProjects\IPLookUp\data\ips.txt"


def ip_to_binary(ip):
    octet_list_int = ip.split(".")
    octet_list_bin = [format(int(i), '08b') for i in octet_list_int]
    binary = "".join(octet_list_bin)
    return binary


def get_addr_network(address, net_size):
    # Convert ip address to 32 bit binary
    ip_bin = ip_to_binary(address)
    # Extract Network ID from 32 binary
    network = ip_bin[0:32 - (32 - net_size)]
    return network


def ip_in_prefix(ip_address, prefix):
    # CIDR based separation of address and network size
    [prefix_address, net_size] = prefix.split("/")
    # Convert string to int
    net_size = int(net_size)
    # Get the network ID of both prefix and ip based net size
    prefix_network = get_addr_network(prefix_address, net_size)
    ip_network = get_addr_network(ip_address, net_size)
    if ip_network == prefix_network:
        print(prefix_network)
        print(ip_network)
    return ip_network == prefix_network


if __name__ == "__main__":

    ips = []
    networks = []
    with open(NETWORK_FILE, 'r') as JSON:
        network_data = json.load(JSON)
        for record in network_data:
            networks.append(record)

    with open(IP_FILE, 'r') as fh:
        for ip in fh:
            ips.append(ip)

    start_time = time.time()
    for ip in ips:
        for record in networks:
            netw = record['value']
            if ip_in_prefix(ip, netw):
                print(f'IP {ip} belongs to network {netw}')
                break
    end_time = time.time()
    total_time = end_time - start_time
    print(f'Total execution time: {total_time} seconds')
