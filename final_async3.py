import shutil
import speedtest
import psutil
import time
import asyncio

st = speedtest.Speedtest()
async def download():
    print("Download speed: ",round((st.download()/1000000),2)," Mbps")
async def upload():
    print("Upload speed: ",round((st.upload()/1000000),2), "Mbps")
async def ping():
    print("Ping speed: ",round(st.results.ping,2), " ms")
    print()

async def storage_results():
    total, used, free = shutil.disk_usage("/")
    print("Total storage: %d GiB" % (total // (2**30)))
    print("Used:  %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))
    print()

async def cpu_ram_results():
    print("The CPU % usage is: ", psutil.cpu_percent())
    print("RAM memory % used: ", psutil.virtual_memory()[2])
    print()

async def main():
    start = time.time()
    task1 = asyncio.create_task(download())
    task2 = asyncio.create_task(upload())
    task3 = asyncio.create_task(ping())
    task4 = asyncio.create_task(storage_results())
    task5 = asyncio.create_task(cpu_ram_results())

    await task1
    await task2
    await task3
    await task4
    await task5

    end = time.time()
    time_e = end - start
    print("Time to execute: ", round(time_e,2))

for i in range(2):
    asyncio.run(main())
