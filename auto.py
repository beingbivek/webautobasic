from time import sleep
import pywifi
from pywifi import const

<<<<<<< HEAD
# Initialize WiFi Interface
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
=======
# WiFi connection settings
# wifi_name = "Bivek's iPhone"
# wifi_password = "okgood12"

# Webpage login settings
url = "https://npl.bivekthapa.com.np/index.php/login/?redirect_to=https%3A%2F%2Fnpl.bivekthapa.com.np%2F"
username = "id"
password = "pass"

# Connect to WiFi
# wifi = pywifi.PyWiFi()
# interface = wifi.interfaces()[0]
# interface.connect(wifi_name, wifi_password)
>>>>>>> 7bcaa1f4026e73b997fc913ee739e00eba584e3c


# Setup WiFi profile
profile = pywifi.Profile()
profile.ssid = "STWCU_LR-12"
profile.key = ""
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_NONE)
profile.cipher = const.CIPHER_TYPE_CCMP

# Turn WiFi off
iface.disconnect()
sleep(1)
assert iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
print("WiFi turned off.")

# Turn WiFi on
iface.connect(profile)
sleep(1)
print("WiFi turned on.")

# Disconnect from Current WiFi
iface.disconnect()
sleep(1)
assert iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

# Add the profile to your WiFi interface
iface.remove_network_profile(profile)
iface.add_network_profile(profile)

# Connect to the Network
iface.connect(profile)
sleep(30)  # Increase sleep time to give more time for connection

# Verify Connection
status = iface.status()
print(f"WiFi Status: {status}")
if status == const.IFACE_CONNECTED:
    print("Connected to the network.")
else:
    print("Failed to connect.")
