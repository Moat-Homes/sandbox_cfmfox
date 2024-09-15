

import psutil

def get_disk_usage():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"Drive: {partition.device}")
            print(f"  Total Size: {usage.total / (1024 ** 3):.2f} GB")
            print(f"  Used: {usage.used / (1024 ** 3):.2f} GB")
            print(f"  Free: {usage.free / (1024 ** 3):.2f} GB")
            print(f"  Percentage: {usage.percent}%\n")
        except PermissionError:
            continue

if __name__ == "__main__":
    get_disk_usage()
