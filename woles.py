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

def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description="Detect technologies used on a website.")
    parser.add_argument("-u", "--url", required=True, help="URL of the website to analyze")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("-o", "--output", help="File to save the output")
    args = parser.parse_args()

    # Detect technologies used on the given URL
    result = detect_technologies(args.url)

    # Determine output format and content
    if args.json:
        # JSON format output
        output_content = json.dumps(result, indent=4)
    else:
        # Regular (default) output
        output_content = "Technologies detected:\n"
        if isinstance(result, dict):
            for tech, details in result.items():
                output_content += f"- {tech}\n"
                for key, value in details.items():
                    output_content += f"  {key.capitalize()}: {value}\n"
        else:
            # Include error message if result is not a dictionary
            output_content = result

    # Print the output content
    print(output_content)

    # Save to file if output file specified
    if args.output:
        save_to_file(output_content, args.output)
        print(f"Output saved to {args.output}")

if __name__ == "__main__":
    main()
