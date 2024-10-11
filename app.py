from Wappalyzer import Wappalyzer, WebPage
import requests
import datetime

import warnings
warnings.filterwarnings("ignore")

def detect_technologies(url):
    wappalyzer = Wappalyzer.latest()

    try:
        # Send request without custom headers
        response = requests.get(url, verify=False, timeout=15)
        response.raise_for_status()  # Raise an error for bad status codes
        webpage = WebPage.new_from_response(response)
        technologies = wappalyzer.analyze_with_versions(webpage)
        return technologies
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return {}

def check_eol(technology_name):
    response = requests.get(f"https://endoflife.date/api/{technology_name.lower()}.json")
    print(technology_name)
    print(response.json())
    
    if response.status_code == 200:
        eol_data = response.json()
        return eol_data
    else:
        return None

def get_eol_status(eol_data, version):
    current_date = datetime.datetime.now().date()
    if not eol_data:
        return "[no support]"

    for version_info in eol_data:
        if version_info['cycle'] == version:
            eol_date_str = version_info.get('eol', None)
            if eol_date_str:
                eol_date = datetime.datetime.strptime(eol_date_str, "%Y-%m-%d").date()
                time_diff = (current_date - eol_date).days

                if time_diff > 0:
                    return f"- EOL Date - Ended {time_diff // 30} months ago ({eol_date.strftime('%d %b %Y')})"
                elif time_diff < 0:
                    return f"- EOL Date - Ends in {-time_diff // 30} months ({eol_date.strftime('%d %b %Y')})"
                else:
                    return f"- EOL Date - Ends today ({eol_date.strftime('%d %b %Y')})"
            else:
                return "[no support]"
    return "[no support]"

def main(url):
    technologies = detect_technologies(url)

    print("List Technology with version")
    print(technologies)
    for tech, info in technologies.items():
        print("====================================") 
        print(tech)  
        # Get version information from the detected technology
        versions = info.get('versions')
        for version in versions:
            eol_data = check_eol(tech)
            eol_status = get_eol_status(eol_data, version)
            print(eol_status)
            print(f"{version} - {eol_status}")

if __name__ == "__main__":
    website_url = "https://neuversity.id"  # Ganti dengan URL yang ingin Anda cek
    main(website_url)
