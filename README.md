
# Proxy Server README

## **Project Name**

**Simple HTTP Proxy Server**

---

## **Description**

This is a **basic HTTP proxy server** implemented in Python using the `socket` module.
It acts as a **middleman** between clients and web servers, forwarding HTTP requests and returning responses.

**Key Features:**

* Forwards HTTP requests to target servers
* Returns responses to clients
* Can log client requests in the console
* Supports caching (optional, can be extended)

**Note:** This proxy does **not support HTTPS** yet.

---

## **How It Works**

1. Client connects to the proxy server.
2. Proxy reads the HTTP request and extracts the host.
3. Proxy forwards the request to the actual web server.
4. Web server sends the response back to the proxy.
5. Proxy returns the response to the client.

Because the proxy sits between the client and the server, it is often called a **middleman**.

---

## **Features / Advantages**

* **Privacy:** Hides client IP from web servers.
* **Bandwidth Saving:** Can cache responses to reduce network load.
* **Logging:** Keeps track of user requests.
* **Speed:** Cached responses can be delivered faster.

---

## **Limitations**

* Does **not encrypt traffic** (unlike VPNs).
* Cannot handle HTTPS by default.
* Can become slow under high load.
* Cached responses may become outdated.

---

## **Requirements**

* Python 3.x
* No external libraries required (pure `socket` module)

---

## **Usage**

### **Step 1:** Run the Proxy Server

```bash
python simple_proxy.py
```

Server runs on **127.0.0.1:8888** by default.

---

### **Step 2:** Test with Browser

* Set your browser proxy to **127.0.0.1** and port **8888**
* Open any HTTP website

---

### **Step 3:** Test with CURL

```bash
curl.exe -x 127.0.0.1:8888 http://example.com
```

---

### **Step 4 (Optional): Test with Python**

```python
import requests

proxies = {'http': 'http://127.0.0.1:8888'}
r = requests.get('http://example.com', proxies=proxies)
print(r.text)
```

---

## **Future Enhancements**

* Add HTTPS support
* Add multi-threading for concurrent clients
* Implement caching system
* Add configurable logging to a file
* Add authentication for secure access

---


