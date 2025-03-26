# site_status_checker

# 📄 Brief Description: <br/>
A simple Python script that automatically checks the uptime of multiple websites at regular intervals. It uses the requests library to send HTTP GET requests and logs whether each site is up or down, handling connection errors and timeouts gracefully.

# 📌 Features: <br/>

* Monitors multiple websites for uptime.

* Runs checks every 5 seconds using the schedule module.

* Handles timeouts, connection errors, and other exceptions.

* Provides real-time logs for each website’s status.

* Supports graceful shutdown with a clean exit.
  

# 📌 How to Download and Run the Website Status Checker </br>
1. Clone the repository or download the zip file.
2. Ensure Python is installed on your system (python 3.12 recommended)
3. Install the required packages
   ` pip install -r requirements.txt `
4. Run the script ` python site_checker.py `
