
def get_net_host(my_ip, clase):
    net_id = None
    host_id = None
    octetos = my_ip.split(".")

    if clase == "A":
        net_id = octetos[0]
        host_id = octetos[1:]
    elif clase == "B":
        net_id = octetos[:2]
        host_id = octetos[2:]
    elif clase == "C":
        net_id = octetos[:3]
        host_id = octetos[3:]
    elif clase == "D":
        print("Multicast address")
    elif clase == "E":
        print("Reserved for future use")

    return ".".join(net_id), ".".join(host_id)
