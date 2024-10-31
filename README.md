
# Wireless Mouse with Flask

This project transforms your iPhone or any mobile device into a wireless trackpad to control your computer's mouse. It uses a Flask web server to host a webpage that acts as a virtual trackpad, allowing you to move and click the mouse from your device.

## Features
- Trackpad interface accessible via mobile devices
- Mouse movement and clicks from mobile device gestures
- QR code generation for easy access to the trackpad page

## Prerequisites

- Python 3.x
- Required Python packages:
  - `Flask` for hosting the web interface
  - `pyautogui` for controlling the mouse
  - `qrcode` and `Pillow` for generating the QR code

Install dependencies using:

```bash
pip install Flask pyautogui qrcode[pil] Pillow
```

## How to Run

1. **Start the Flask server**:
   Run the Python script to launch the server:

   ```bash
   python app.py
   ```

2. **Display the QR Code**:
   The server generates a QR code for your local IP address. Scan this code with your mobile device to open the trackpad interface.

3. **Use the Trackpad**:
   The interface will appear on your mobile device's browser, where you can:
   - Drag to move the mouse
   - Tap to simulate a mouse click

## Code Explanation

- `get_local_ip()`: Retrieves the local IP address of the machine.
- `display_qr_code()`: Generates and displays a QR code with the server’s URL.
- Flask endpoints:
  - `/`: Serves the HTML interface for the trackpad.
  - `/control`: Handles mouse movement and click actions.

## Security Considerations

This tool is designed for local networks only. Ensure your network is secure, as this app does not implement authentication.

## License

This project is open-source and free to use.

---

Enjoy your new wireless mouse setup!
