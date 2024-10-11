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

WOLES requires Python 3.x to run.

## How to Use

You can run WOLES from the command line by specifying the website URL using the `-u` or `--url` argument.

### Example Usage:

```bash
python woles.py -u https://example.id
```

In the example above, WOLES will analyze the website `https://example.id`, detect the technologies used, and check for any End of Life (EOL) statuses for the detected versions.

### Sample Output:

```bash
Detected Technologies for https://example.id:
------------------------------------
MySQL - ['Databases']
No version information available
------------------------------------
Yoast SEO - ['SEO']
23.6 | EOL not found
------------------------------------
jQuery - ['JavaScript libraries']
3.7.1 | EOL False | release date 2016-06-09
3.4.1 | EOL False | release date 2016-06-09
1.2.1 | EOL True | release date 2006-08-31
1.13.3 | EOL True | release date 2006-08-31
3.23.3 | EOL False | release date 2016-06-09
------------------------------------
jQuery Migrate - ['JavaScript libraries']
3.4.1 | EOL not found
------------------------------------
Cloudflare - ['CDN']
No version information available
------------------------------------
WordPress - ['CMS', 'Blogs']
No version information available
------------------------------------
Google Font API - ['Font scripts']
No version information available
------------------------------------
Elementor - ['Page builders']
1.8.0 | EOL not found
6.6.2 | EOL not found
3.24.6 | EOL not found
------------------------------------
PHP - ['Programming languages']
7.4.33 | EOL 2022-11-28 | release date 2019-11-28
```

In this sample, the program detects several technologies used on the website `https://example.id`, including MySQL, jQuery, Cloudflare, WordPress, and more. The output shows the version number and End of Life (EOL) status for each technology when available. For some technologies, no version information is available, and for others, EOL data could not be found.

## Command Line Options

- `-u`, `--url`: The URL of the website you want to analyze.

## Error Handling

WOLES includes error handling mechanisms for the following scenarios:

1. **Request Timeout or Connection Error**: If the provided URL cannot be accessed within 15 seconds, the program will output a connection error message.
2. **No Technology Detected**: If Wappalyzer fails to detect any technologies for the given URL, the program will print an appropriate message.

### Common Issues:

- **No Version Information Found**: If WOLES detects a technology but no version is available, it means the version information is either not retrievable or not available.
- **EOL Not Found**: If the detected version is not available in the EOL database, the program will output a message stating that the EOL information is not found.
