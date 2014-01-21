import subprocess
import sys


def measure(TLP_VALUE, category_1, category_2):
    """Record the output for all the possible configurations.
        Each Analysis Output is saved in a separate file with
        10-15 entries for each configuration.
    """
    subprocess.call(["sudo", "sysctl", "-w",
                    "net.ipv4.tcp_early_retrans="+TLP_VALUE])
    f_name = "Recordings"
    link_speeds = []
    payload_lengths = []
    if TLP_VALUE == "2":
        f_name += "/NoTLP"
    elif TLP_VALUE == "3":
        f_name += "/TLP"

    if category_1 == "all":
        link_speeds = ["fast", "moderate", "slow"]
    elif category_1 == "fast":
        link_speeds.append("fast")
    elif category_1 == "moderate":
        link_speeds.append("moderate")
    elif category_1 == "slow":
        link_speeds.append("slow")

    if category_2 == "all":
        payload_lengths = ["long", "medium", "short"]
    elif category_2 == "long":
        payload_lengths.append("long")
    elif category_2 == "medium":
        payload_lengths.append("medium")
    elif category_2 == "short":
        payload_lengths.append("short")

    drop_counts = [1, 2, 4, 8]

    for link_speed in link_speeds:
        for payload_length in payload_lengths:
            for drop_count in drop_counts:
                for i in range(10):
                    out = ''
                    subprocess.call(["python2", "mininet_tlp_measurement.py",
                                    link_speed, link_speed, payload_length,
                                    "dump.pcap", str(drop_count)])
                    try:
                        out = subprocess.check_output(["python",
                                                      "tcp_analysis.py",
                                                      "dump.pcap"])
                    except:
                        print "Error"
                    f_name_current = f_name + link_speed + "_"
                    f_name_current += payload_length + "_"
                    f_name_current += str(drop_count)
                    f_write = open(f_name_current, "a")
                    print(f_name_current)
                    print(out)
                    f_write.write(out)
                    f_write.close()


if __name__ == "__main__":
    TLP = sys.argv[1]
    category_1 = sys.argv[2]
    category_2 = sys.argv[3]
    measure(TLP, category_1, category_2)
