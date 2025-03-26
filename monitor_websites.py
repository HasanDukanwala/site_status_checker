import schedule
import time
import sys
import requests


def check_websites():
    print("Running check_websites function...", flush=True)
    # Some website will not let you visit unless you have user agent provided in header
    # Remove header in request line of code below and costco will not respond.
    header = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 "
                            "Mobile Safari/537.36 Edg/134.0.0.0"}

    websites = [
        "https://www.costco.ca/",
        "https://stackoverflow.com/",
        "https://github.com"
    ]

    for site in websites:
        print(f"\nChecking {site}...", flush=True)
        try:
            # Remove header if you want to see site is down response (some site will
            # give to response even without header)
            response = requests.get(site, timeout=5, headers=header)
            # Adding a timeout of 10 seconds
            print(f"\tReceived response from {site}", flush=True)
            if response.status_code == 200:
                print(f"\t[INFO] : {site} is Up and running,", flush=True)
                print(f"\t[INFO] : Status Code: {response.status_code}", flush=True)

            else:
                print(f"[WARNING] : {site} is down and returned status code {response.status_code}", flush=True)
        except requests.ConnectionError:
            print(f"[ERROR] : {site} is down (ConnectionError)", flush=True)
        except requests.Timeout:
            print(f"[ERROR] : {site} is down (Timeout)", flush=True)
        except requests.RequestException as e:
            print(f"[ERROR] : {site} is down ({e})", flush=True)


schedule.every(5).seconds.do(check_websites)


def signal_handler(sig, frame):
    print("\nGracefully shutting down...", flush=True)
    sys.exit(0)


def run_scheduler():
    while True:
        schedule.run_pending()
        print("Scheduler running...", flush=True)
        time.sleep(5)


if __name__ == "__main__":
    print("Script has started running", flush=True)
    run_scheduler()
