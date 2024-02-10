from scapy.all import sniff, IP, TCP
import time
from collections import defaultdict  # Import defaultdict

# Define the expected protocol types, services, and flags
expected_protocol_types = ['tcp', 'udp']
expected_services = ['http', 'ftp', 'ssh']
expected_flags = ['S', 'A', 'R']

def get_connection_key(packet):
    if IP in packet and TCP in packet:
        return f"{packet[IP].src}:{packet[TCP].sport}-{packet[IP].dst}:{packet[TCP].dport}"
    else:
        return None

def analyze_packet(packet):
    # Access the packet's attributes
    src_bytes = len(packet)
    dst_bytes = len(packet)
    
    # Print or process the src_bytes value
    # print(f"src_bytes: {src_bytes}")

    protocol_type=0
    service=0
    flag=0
    
    if IP in packet and TCP in packet:
        protocol_type = packet[IP].proto
        service = packet[TCP].dport
        flag = packet[TCP].flags.value

        # Perform behavioral analysis
        if protocol_type not in expected_protocol_types or service not in expected_services or flag not in expected_flags:
            print("Behavioral Anomaly Detected:")
            print(f"Protocol Type: {protocol_type}, Service: {service}, Flag: {flag}")
            print(f"Source IP: {packet[IP].src}, Destination IP: {packet[IP].dst}")
            print(f"Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
            print("-" * 30)
            
    current_time = time.time()
    count=0
    connection_counts = defaultdict(int)

    for packet in packet:
        connection_key = get_connection_key(packet)

        if connection_key is not None:
            # Check the timestamp of the last connection
            last_connection_time = connection_counts[connection_key]

            # Check if the connection occurred within the last two seconds
            if current_time - last_connection_time <= 2:
                # Increment the connection count for the same host
                connection_counts[connection_key] += 1
                for i,j in connection_counts[connection_key]:
                    count+=j
                print(f"Connection to the same host in the past two seconds. Count: {connection_counts[connection_key]}")
            else:
                # Reset the connection count for a new two-second window
                connection_counts[connection_key] = 1

    su_attempted=0
    if TCP in packet and IP in packet:
        payload = bytes(packet[TCP].payload)
        if payload.startswith(b'SSH'):  # Assuming SSH traffic
            if b'su root' in payload:
                su_attempted=1
                print("su root command attempted in SSH traffic.")
                print(f"Source IP: {packet[IP].src}, Destination IP: {packet[IP].dst}")
                print(f"Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
                print("-" * 30)

    host_list = ['192.168.1.1', '192.168.1.2', '192.168.1.3']

    is_host_login=0

    if TCP in packet and IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # Check if the source IP is in the host list
        is_host_login = 1 if src_ip in host_list else 0

        print(f"Login attempt detected:")
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}")
        print(f"Is Host Login: {is_host_login}")
        print("-" * 30)
    
    guest_login_detected=0
    if TCP in packet and IP in packet:
        payload = str(packet[TCP].payload)

        # Replace this string with the pattern you are looking for
        guest_login_pattern = ["guest\d+","guest|guestuser","anonymous","guest|public","Guest","Guest","public_guest"]

        # Check for the presence of the guest login pattern in the payload
        guest_login_detected=0
        for i in guest_login_pattern:
            if(i in payload):
                guest_login_detected=1
                break

        # Print information about the packet
        print("Packet analysis:")
        print(f"Source IP: {packet[IP].src}, Destination IP: {packet[IP].dst}")
        print(f"Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
        print(f"Guest login detected: {guest_login_detected}")
        print("-" * 30)

    import pandas as pd
    from sklearn.preprocessing import RobustScaler

    # Assuming 'col' is a list of column names
    val = [protocol_type,flag,service,src_bytes, dst_bytes,  count, su_attempted, is_host_login, guest_login_detected]
#     
    # print(val)
    
    import pandas as pd
    from sklearn.preprocessing import RobustScaler

    # Sample column names and values
    # col = ['src_bytes', 'dst_bytes', 'protocol_type', 'service', 'flag', 'count', 'su_attempted', 'is_host_login', 'guest_login_detected']
    # val = [100, 200, 'tcp', 'http', 'SF', 5, 0, 1, 0]
    
    col=[ 'protocol_type','flag','service','src_bytes','dst_bytes','count', 'su_attempted','is_host_login', 'guest_login_detected']
    
    # Create an empty DataFrame with the specified column names
    data = pd.DataFrame(columns=col)
    data.loc[0] = val  # Append a new row to 'data'
    # print(data)
    
    # print(data)
    from joblib import load
    # Load the saved model
    loaded_model = load('random_forest_model.joblib')
    
    # Make predictions
    prediction = loaded_model.predict(data)

    # Display the prediction result
    if prediction[0] == 0:
        print("Normal Traffic")
    else:
        print("Anomaly Detected")

# Sniff network traffic and analyze packets
sniff(prn=analyze_packet,count=200)
            