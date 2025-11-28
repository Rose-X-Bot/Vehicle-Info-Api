from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_URL = "https://gtplay.in/API/vehicle_challan_info/testapi.php"

@app.route("/vehicle=<vehicle_no>", methods=["GET", "POST"])
def vehicle_info(vehicle_no):
    if not vehicle_no:
        return jsonify({
            "DEVELOPER BY 😎": "@Ros3_Zii",
            "ALL API BUY FOR DM": "@Ros3_Zii", 
            "JAI MAHAKAL 🥰": "@h4ck3rspybot",
            "status": False, 
            "error": "vehicle_no is required"
        }), 400

    try:
        headers = {
            "User-Agent": "okhttp/5.1.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"vehicle_no": vehicle_no}

        # Disable SSL verification (for certificate mismatch)
        response = requests.post(API_URL, headers=headers, data=data, verify=False)
        
        # Original response ko get karo
        api_response = response.json()
        
        # Naya response structure banayein
        final_response = {
            "DEVELOPER BY 😎": "@Ros3_Zii",
            "ALL API BUY FOR DM": "@Ros3_Zii",
            "JAI MAHAKAL 🥰": "@h4ck3rspybot",
            "data": api_response
        }
        
        return jsonify(final_response)

    except Exception as e:
        return jsonify({
            "DEVELOPER BY 😎": "@Ros3_Zii",
            "ALL API BUY FOR DM": "@Ros3_Zii",
            "JAI MAHAKAL 🥰": "@h4ck3rspybot",
            "status": False, 
            "error": str(e)
        })

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    app.run(host="0.0.0.0", port=5000, debug=True)
