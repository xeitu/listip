---
# ListIP

This Python script counts the occurrences of IP addresses in a log file.

## Usage

To run the script, follow these steps:

1. Open a terminal.
2. Navigate to the directory where the `script.py` file is located.
3. Execute the script by providing the log file you want to analyze as an argument. For example:

   ```bash
   python3 script.py access.log
   ```

   Where `access.log` is the name of the log file you want to analyze.

## Functionality

The script reads the specified log file and counts how many times each IP address appears in the file. It then displays the IP addresses along with their respective counts, ordered from highest to lowest count.

## Requirements

- Python 3.x installed on the system.

## Example Usage

Suppose you have a log file named `access.log` containing the following lines:

```
192.168.1.1 - - [01/Jan/2024:12:00:00] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [01/Jan/2024:12:00:01] "GET /images/logo.png HTTP/1.1" 404 5678
192.168.1.1 - - [01/Jan/2024:12:00:02] "POST /submit.php HTTP/1.1" 302 0
192.168.1.3 - - [01/Jan/2024:12:00:03] "GET /index.html HTTP/1.1" 200 9876
```

Running the script with the log file `access.log` would produce the following output:

```
192.168.1.1: 2 times
192.168.1.2: 1 times
192.168.1.3: 1 times
```

---


