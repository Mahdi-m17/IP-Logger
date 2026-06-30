# IP Logger

Fetches your public IP address and logs it to `my_ips.txt` with a timestamp.

Example output:

```
Your IP address: 203.0.113.42
IP address successfully saved to my_ips.txt.
```

Each run appends a line to `my_ips.txt`:

```
Date: 2026-06-30 14:32:10 | IP Address: 203.0.113.42
```

## Note

If the IP fetch fails (e.g. no internet connection), the script prints an error and skips saving to the log file.
