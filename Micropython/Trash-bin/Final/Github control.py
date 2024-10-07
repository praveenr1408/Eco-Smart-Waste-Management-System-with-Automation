import network
import urequests
import time

# Wi-Fi credentials
ssid = 'Redmi'            # Replace with your SSID
password = '876543210'     # Replace with your Wi-Fi password

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    print("Connecting to Wi-Fi", end="")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConnected!")
    print(wlan.ifconfig())  # Print IP address, subnet mask, gateway, and DNS

# Call function to connect to Wi-Fi
connect_wifi()

# GitHub raw URL of your script
url = "https://raw.githubusercontent.com/praveenr1408/Eco-Smart-Waste-Management-System-with-Automation/master/Micropython/Trash-bin/Final/Final.py"

try:
    # Fetch the script from GitHub
    response = urequests.get(url)

    if response.status_code == 200:
        # Open a new file to write the content in chunks
        with open("final.py", "w") as f:
            # Stream the response content in small chunks
            while True:
                chunk = response.raw.read(512)  # Read 512 bytes at a time
                if not chunk:  # If no more content, stop
                    break
                f.write(chunk.decode('utf-8'))

        print("Script downloaded successfully!")

        # Directly execute the downloaded script
        exec(open("final.py").read())
    else:
        print(f"Failed to download script. Status code: {response.status_code}")

    response.close()

except MemoryError as e:
    print("Memory error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
