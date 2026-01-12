# Import module to access speedtest and time
import speedtest
import time

st = speedtest.Speedtest()

print("Testing ................................ ")

down = st.download() / 10**6
up = st.upload() / 10**6

# Print out the up and down speeds 
print(f"download speed : {down:.2f} Mbps")
print(f"upload speed: {up:.2f} Mbps")


