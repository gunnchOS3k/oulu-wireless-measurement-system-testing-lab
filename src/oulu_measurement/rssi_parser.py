def parse_rssi(line):
    return float(line.split('=')[-1]) if '=' in line else -999
