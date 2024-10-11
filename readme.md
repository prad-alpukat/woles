# WOLES - Web Observer for Lifecycle and EOL Status

WOLES is a tool designed to detect the technologies used on a website and check their End of Life (EOL) status. WOLES uses [Wappalyzer](https://www.wappalyzer.com/) to analyze website technologies and [End of Life API](https://endoflife.date/) to retrieve EOL information for the detected technologies.

## Features

- Detects technologies used on a website.
- Retrieves version information (if available) for each technology.
- Checks the End of Life (EOL) status for detected technologies.

## Requirements

Ensure you have the following dependencies installed before running the program:

```bash
pip install Wappalyzer requests argparse
```
