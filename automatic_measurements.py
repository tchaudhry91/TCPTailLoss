import subprocess


def measure(TLP_VALUE):
    """Record the output for all the possible configurations.
        Each Analysis Output is saved in a separate file with
        10 entries for each configuration.
    """
    subprocess.call(["sudo", "sysctl", "-w",
                    "net.ipv4.tcp_early_retrans="+TLP_VALUE])
    f_name = "TLP"
    if TLP_VALUE == 2:
        f_name = "TLP"
    elif TLP_VALUE == 3:
        f_name = "NoTLP"
    link_speeds = ["fast", "moderate", "slow"]
    payload_lengths = ["long", "medium", "short"]
    drop_counts = [1, 2, 4, 8]
    for link_speed in link_speeds:
        for payload_length in payload_lengths:
            for drop_count in drop_counts:
                for i in range(10):
                    subprocess.call(["python", "mininet_tlp_measurement.py",
                                    link_speed, link_speed, payload_length,
                                    "dump.pcap", str(drop_count)])
                    out = subprocess.check_output(["python", "tcp_analysis.py",
                                                  "dump.pcap"])
                    f_name_current = f_name + link_speed + "_"
                    f_name_current += payload_length + "_"
                    f_name_current += str(drop_count)
                    print(out)
                    print(f_name_current)
                    subprocess.call(["echo", out, ">>", "Recordings/" +
                                    f_name_current])


if __name__ == "__main__":
    measure("2")
    measure("3")
