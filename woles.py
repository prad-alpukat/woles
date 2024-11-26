from Wappalyzer import Wappalyzer, WebPage
import requests
import argparse
import warnings
import json

warnings.filterwarnings("ignore")

def detect_technologies(url):
    wappalyzer = Wappalyzer.latest()
    try:
        webpage = WebPage.new_from_url(url)
        technologies = wappalyzer.analyze_with_versions_and_categories(webpage)
        return technologies
    except (requests.RequestException, Exception) as e:
        return str(e)

def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)

def check_eol(tech, version):
    url = f"https://endoflife.date/api/{tech}.json"
    response = requests.get(url)
    data = response.json()
    if(type(data) == list):
        len_cycle = len(data[0]['cycle'])
        for item in data: 
            if(item['cycle'] == version[:len_cycle]): 
                if(type(item['eol']) == str): 
                    return f"true({item['eol']})"
                elif (type(item['eol']) == bool): 
                    return f"{item['eol']}"
    else: 
        return "Product not found"

def main():
    parser = argparse.ArgumentParser(description="Detect technologies used on a website.")
    parser.add_argument("-u", "--url", required=True, help="URL of the website to analyze")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("-o", "--output", help="File to save the output")
    args = parser.parse_args()

    result = detect_technologies(args.url)
    
    for tech, details in result.items():
        result[tech] = {}
        for key, value in details.items():
            if(key == 'versions' and len(value) == 0): 
                result[tech][key] = "N/A"
            else: 
                result[tech][key] = value

    if args.json:
        output_content = json.dumps(result, indent=4)
    else:
        output_content = f"Tech + EOL Info\nWebsite: {args.url}\n-------------------------"
        if isinstance(result, dict):
            for i, (tech, details) in enumerate(result.items()):
                output_content += f"\n{i+1}. {tech}\n"

                for key, value in details.items():
                    if key == 'versions' and value != "N/A":
                        # loop through versions
                        for i, version in enumerate(value):
                            output_content += f"   - {key.capitalize()}: {version}\n"
                            output_content += f"     EOL: {check_eol(tech, version)}\n"
                    elif key == 'versions' and value == "N/A":
                        output_content += f"   - {key.capitalize()}: {value}\n"

        else:
            output_content = result

    print(output_content)

    if args.output:
        save_to_file(output_content, args.output)
        print(f"Output saved to {args.output}")

if __name__ == "__main__":
    main()
