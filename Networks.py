class Network:
    networks_binary = []

    def __init__(self, data):
        self._data = data

    def _ip_to_binary(self, ip):
        octet_list_int = ip.split(".")
        octet_list_bin = [format(int(i), '08b') for i in octet_list_int]
        binary = "".join(octet_list_bin)
        return binary

    def _network_to_binary(self, address, net_size):
        ip_bin = self._ip_to_binary(address)
        # Extract Network ID from 32 binary
        network = ip_bin[0:32 - (32 - net_size)]
        return network

    def init_network_binary(self):
        for record in self._data:
            raw_network = record['value']
            [prefix_address, net_size] = raw_network.split("/")
            net_size = int(net_size)
            inner = (self._network_to_binary(prefix_address, net_size), net_size, raw_network)
            self.networks_binary.append(inner)
        print(self.networks_binary)
        self._sort_data()

    def init_binary_data(self):
        self.net_bin, self.net_size, self.net_raw = zip(*self.networks_binary)

    def _sort_data(self):
        self.networks_binary.sort()

    def ip_in_network(self, ip):
        for net_bin, net_size, netw in self.networks_binary:
            ip_bin = self._network_to_binary(ip, net_size)
            if ip_bin == net_bin:
                return ip, netw
        return ip, "Not found"

    def binary_search(self, ip):
        first = 0
        last = len(self.net_bin)-1
        found = False
        idx = None

        while first <= last and not found:
            midpoint = (first + last) // 2
            net_size = self.net_size[midpoint]
            ip_bin = self._network_to_binary(ip, net_size)
            if self.net_bin[midpoint] == ip_bin:
                found = True
                idx = midpoint
            else:
                if ip_bin < self.net_bin[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
        if found:
            return f'IP {ip} belongs to network: {self.net_raw[idx]}'
        return f'IP {ip} NOT FOUND'



