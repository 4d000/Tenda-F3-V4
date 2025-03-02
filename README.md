# Tenda F3 Router Exploit & File Downloader

This project is a tool for downloading various files from the Tenda F3 router (v3/v4) through an unauthenticated vulnerability (CVE-2020-35391). It allows you to get the configuration file, system log, and flash dump from a vulnerable router.

## Overview

The script exploits a vulnerability found in the Tenda F3 router, enabling an attacker to download sensitive files without authentication. Specifically, the following files can be downloaded (I'm working on adding the possibility to change the password):

- Configuration file `RouterCfm.cfg` (that contains everything in plain text)
- System log file `RouterSystem.log`
- Flash memory dump `RouterFlash.bin`

## Features

- **Download the configuration file**: Fetches the router's configuration file.
- **Download the system log file**: Fetches the router's system log file.
- **Download the flash dump**: Dumps the router's flash memory.

## Requirements

- Python 3.x
- `socket` and `optparse` libraries (usually included with Python)

## Usage

```
python3 tendaF3-tool.py --target <target_ip> [options]
```

### Options:
- `-t, --target` : Specify the target IP address (required).
- `-c, --config` : Download the configuration file (`RouterCfm.cfg`).
- `-l, --log` : Download the system log file (`RouterSystem.log`).
- `-f, --flash` : Download the flash dump (`RouterFlash.bin`).

Example usage:
```
python3 tendaF3-tool.py -t 192.168.0.1 --config
```

This will download the configuration file from the target router.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

**Note**: This tool is intended for educational purposes only. Please ensure you have proper authorization before testing any network or device.