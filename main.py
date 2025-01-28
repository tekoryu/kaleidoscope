import requests
import json


def fetch_json_from_url(url):
    """
    Fetch JSON data from the provided URL.

    :param url: The URL to fetch the JSON data from.
    :return: Parsed JSON object if successful, None otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None


def main():
    # URL of the JSON file
    url = "https://legis.senado.leg.br/dadosabertos/agendareuniao/20190502.json"

    # Fetch JSON data
    json_data = fetch_json_from_url(url)

    if json_data:
        # Pretty print the JSON data (optional)
        print(json.dumps(json_data, indent=4, ensure_ascii=False))

        # Extract information based on the structure of the JSON
        # Example: Accessing agenda or meeting details
        try:
            meetings = json_data.get('AgendaReuniao', {}).get('Reunioes',
                                                              {}).get('Reuniao',
                                                                      [])
            for meeting in meetings:
                print(f"Título: {meeting.get('Titulo')}")
                print(f"Data: {meeting.get('Data')}")
                print(f"Hora: {meeting.get('Hora')}")
                print(f"Local: {meeting.get('Local')}")
                print("-" * 40)
        except KeyError as e:
            print(f"Error accessing specific data in JSON: {e}")


if __name__ == "__main__":
    main()
