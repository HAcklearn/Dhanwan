from flask import Flask, request, jsonify
import whois

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_domain():
    domain = request.json.get('domain')
    try:
        w = whois.whois(domain)
        return jsonify({"domain": domain, "available": w.domain_name is None})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)