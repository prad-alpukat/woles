from Wappalyzer import Wappalyzer, WebPage
import requests
import argparse
import warnings
import json

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
    except (requests.RequestException, Exception) as e:
        return str(e)

def main():
    parser = argparse.ArgumentParser(description="Detect technologies used on a website.")
    parser.add_argument("-u", "--url", required=True, help="URL of the website to analyze")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    args = parser.parse_args()

    # Detect technologies used on the given URL
    result = detect_technologies(args.url)

    # Display output based on the selected format
    if args.json:
        # JSON format output
        print(json.dumps(result, indent=4))
    else:
        # Regular (default) output
        print("Technologies detected:")
        if isinstance(result, dict):
            for tech, details in result.items():
                print(f"- {tech}")
                for key, value in details.items():
                    print(f"  {key.capitalize()}: {value}")
        else:
            # Print error message if result is not a dictionary
            print(result)

if __name__ == "__main__":
    main()
