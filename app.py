from Wappalyzer import Wappalyzer, WebPage
import requests

import warnings
warnings.filterwarnings("ignore")

def detect_technologies(url):
    wappalyzer = Wappalyzer.latest()
    try:
        # Send request without custom headers
        response = requests.get(url, verify=False, timeout=15)
        response.raise_for_status()  # Raise an error for bad status codes
        webpage = WebPage.new_from_response(response)
        technologies = wappalyzer.analyze_with_versions_and_categories(webpage)
        return technologies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return {}

def check_eol(technology_name):
    response = requests.get(f"https://endoflife.date/api/{technology_name.lower()}.json")
    if response.status_code == 200:
        eol_data = response.json()
        return eol_data
    else:
        return None

def get_eol_status(tech, version):
    response = requests.get(f"https://endoflife.date/api/{tech.lower()}.json")
    if response.status_code == 200:
        eol_data = response.json()
        # length cycle info
        cycle = eol_data[0]['cycle']
        cycle_dot = cycle.split('.')
        cycle_len = len(cycle_dot)

        # get same length cycle info from version
        version_dot = version.split('.')
        cycle_version = '.'.join(version_dot[:cycle_len])

        response_eol = requests.get(f"https://endoflife.date/api/{tech.lower()}/{cycle_version}.json")
        data_eol = response_eol.json()
        return f"EOL {data_eol['eol']} | release date {data_eol['releaseDate']}"
    else: 
        return "EOL not found"



def main(url):
    technologies = detect_technologies(url)

    print("Detected Technologies:")
    for tech, info in technologies.items():
        print("------------------------------------")
        print(f"{tech} - {info['categories']}")
        if len(info["versions"]): 
            for version in info["versions"]:
                eol = get_eol_status(tech, version)
                print(f"{version} | {eol}")
        else:
            print("No version information available")

if __name__ == "__main__":
    website_url = "https://neuversity.id"  # Ganti dengan URL yang ingin Anda cek
    main(website_url)
