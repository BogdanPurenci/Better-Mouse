from flask import Flask, request, jsonify, render_template_string
import pyautogui
import qrcode
import socket
import io
from PIL import Image

app = Flask(__name__)

def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
        return ip
    except Exception as e:
        print("Error detecting local IP:", e)
        return socket.gethostbyname(socket.gethostname())


def display_qr_code():
    ip = get_local_ip()
    url = f"http://{ip}:5000"
    qr = qrcode.make(url)
    
    print("Scan this QR code to open the trackpad interface:")
    qr.print_ascii()

    qr.show()

@app.route('/')
def index():
    html_page = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Wireless Mouse</title>
        <style>
            body { margin: 0; overflow: hidden; }
            #trackpad { width: 100vw; height: 100vh; background: #f0f0f0; }
        </style>
    </head>
    <body>
        <div id="trackpad"></div>
        <script>
            let startX, startY;

            function sendMovement(dx, dy) {
                fetch('/control', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ action: 'move', dx: dx, dy: dy })
                });
            }

            document.getElementById('trackpad').addEventListener('touchstart', function(e) {
                startX = e.touches[0].clientX;
                startY = e.touches[0].clientY;
            });

            document.getElementById('trackpad').addEventListener('touchmove', function(e) {
                let dx = e.touches[0].clientX - startX;
                let dy = e.touches[0].clientY - startY;
                sendMovement(dx, dy);
                startX = e.touches[0].clientX;
                startY = e.touches[0].clientY;
            });

            document.getElementById('trackpad').addEventListener('click', function() {
                fetch('/control', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ action: 'click' })
                });
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_page)

@app.route('/control', methods=['POST'])
def control():
    data = request.json
    action = data.get('action')
    if action == 'move':
        dx, dy = data.get('dx', 0), data.get('dy', 0)
        pyautogui.moveRel(dx, dy)
    elif action == 'click':
        pyautogui.click()
    return jsonify(success=True)

if __name__ == '__main__':
    display_qr_code()
    app.run(host='0.0.0.0', port=5000)
