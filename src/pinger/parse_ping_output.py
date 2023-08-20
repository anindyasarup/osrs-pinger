def parse_ping_output(process_out: str):
    lines = process_out.strip().split('\n')
    last_line = lines[-1]
    avg_rtt = float(last_line.split('/')[-3])
    max_rtt = float(last_line.split('/')[-2])

    return avg_rtt, max_rtt
