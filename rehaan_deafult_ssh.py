#SSH Port Scanner
#Rehaan Lachporia - 101594859
import socket

target = ("ssh.0x10.cloud")
port = 22

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    print(f"\n  Target: {target}")
    print(f"  Port: {port}")
    print(f"  Scanning...")

    result = sock.connect_ex((target, port))
    if result == 0:
        print("\n  [!DANGER - VULNERABILITY DETECTED]")
        print(f"  Connection established to port: {port}")
        print("  Default SSH port (22) is OPEN")
    else:
        print("   [OK]")
        print(f"   Connection refused to port: {port}")


    sock.close()
except socket.error as e:
    print(e)