import ipaddress

def process_ip(input_ip):
    try:
        # Parse the input IP with subnet
        network = ipaddress.IPv4Network(input_ip, strict=False)

        # Extract subnet mask, network ID, and gateway
        subnet_mask = str(network.netmask)
        network_id = str(network.network_address)
        gateway = str(network.network_address + 1)  # Assuming the first host is the gateway

        # Display the results
        print(f"Input IP with Subnet: {input_ip}")
        print(f"Subnet Mask: {subnet_mask}")
        print(f"Network ID: {network_id}")
        print(f"Gateway: {gateway}")

    except ipaddress.AddressValueError as e:
        print(f"Error: {e}")
    except ipaddress.NetmaskValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Get user input
    user_input = input("Enter IP with Subnet (e.g., 192.168.1.0/24): ")

    # Process the input
    process_ip(user_input)

