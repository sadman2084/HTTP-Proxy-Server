# README - Simple Python Proxy with Flask & Browser UI

## Overview

This project provides a **simple HTTP/HTTPS proxy** that:

* Uses a Python Flask backend to handle HTTP/HTTPS requests
* Allows you to input a URL in the browser and view the HTML response
* Includes a socket-based proxy (`simple_proxy.py`) for terminal testing

The project consists of three main components:

1. `app.py` → Flask backend serving HTML + `/fetch` proxy route
2. `simple_proxy.py` → Low-level TCP socket proxy (for terminal testing only)
3. `index.html` → Browser UI with URL input and output display

---

## Files

| File              | Purpose                                                             |
| ----------------- | ------------------------------------------------------------------- |
| `app.py`          | Flask backend serving `index.html` and `/fetch` proxy functionality |
| `simple_proxy.py` | TCP socket-based proxy on port 8888 (terminal use only)             |
| `index.html`      | Browser UI: input box for URL, fetch button, and output display     |

---

## Setup Instructions

###  Requirements

* Python 3.x
* Required libraries: Flask, flask-cors, requests

Install dependencies:

```bash
pip install flask flask-cors requests
```

---

###  Folder Structure

```
project-folder/
│
├── app.py
├── simple_proxy.py
├── index.html
└── README.md
```

> All files should be in the same folder for Flask to serve the HTML correctly.

---

###  Running Flask + Browser UI

1. Open terminal / PowerShell and navigate to your project folder:

```powershell
cd "C:\path\to\project-folder"
```

2. Start the Flask server:

```bash
python app.py
```

* Flask runs by default on port `5000`
* Open browser and go to: `http://127.0.0.1:5000/`

3. Browser UI usage:

* Type any HTTP or HTTPS URL in the input box
* Click **Fetch**
* The response HTML/text will appear in the output div

---

> This HTML is served directly from Flask (`app.py`) root route `/`. No separate HTTP server is needed.

---

###  Running the Terminal Socket Proxy (Optional)

1. In terminal, run:

```bash
python simple_proxy.py
```

* TCP socket proxy will start on port `8888`
* It forwards HTTP requests in the terminal
* **Browser fetch is not recommended for this socket proxy**; use Flask instead

---

###  Notes / Tips

* Flask + requests library handles modern HTTP/HTTPS sites, redirects, and headers automatically
* CORS is enabled in Flask (`CORS(app)`) so browser fetch works across ports
* Socket proxy (`simple_proxy.py`) is for terminal testing/debugging only



---

If you want, I can also make a **ready-to-copy folder structure screenshot and folder layout diagram** for this project, showing exactly where `app.py`, `index.html`, and `simple_proxy.py` should go so it runs smoothly.

Do you want me to make that too?
