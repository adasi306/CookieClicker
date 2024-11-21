# Cookie Clicker Automation Script

This project automates the [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/) game using Selenium. The script clicks the cookie and periodically purchases upgrades to maximize cookies per second.

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Description

The script is written in Python and uses the Selenium library to:
- Automatically click the big cookie.
- Periodically check and purchase available upgrades in the store.
- Display cookies per second (CPS) after 5 minutes of gameplay.

## Installation

1. **Install Python 3.x**: Download it from python.org.
2. **Install Selenium**:
   pip install selenium
3. **Download Chrome WebDriver**:
   - Visit ChromeDriver Downloads: https://chromedriver.chromium.org/downloads
   - Download the version matching your Google Chrome browser.
   - Place the `chromedriver` executable in your system's PATH or the same directory as the script.

## Usage

1. Save the script as `cookie_clicker_bot.py`.
2. Run the script:
   python cookie_clicker_bot.py
3. Script functionality:
   - Opens the Chrome browser.
   - Navigates to the Cookie Clicker game.
   - Starts clicking the cookie and purchasing upgrades.
4. After 5 minutes:
   - Displays cookies per second (CPS).
   - Continues running until manually stopped.

## Technical Details

How the script works:
- **Clicking the cookie**: The script continuously clicks the big cookie to accumulate cookies.
- **Checking for upgrades**:
  - Every 5 seconds, the script checks which upgrades in the store are available.
  - Purchases the most expensive upgrade you can afford.
- **Gameplay duration**: By default, the gameplay lasts 5 minutes. You can change this in the script:
   play_time = time.time() + 300

## Troubleshooting

### ChromeDriver Version Mismatch
1. Ensure your ChromeDriver version matches your installed Google Chrome version.
2. Check your Chrome version by navigating to:
   chrome://settings/help

### Selenium Issues
If you encounter Selenium-related errors, update the library:
   pip install --upgrade selenium

### Script Not Working Correctly
- Ensure you have a stable internet connection.
- Make sure the game has fully loaded in the browser.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.
