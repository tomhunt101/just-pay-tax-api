from flask import Flask, jsonify
import time

app = Flask(__name__)

# Start time for tax evasion counter
START_TIME = time.time()
TAX_EVASION_PER_SECOND = 523.45  # Adjust this number as needed

@app.route('/tax-counter')
def tax_counter():
    elapsed_time = time.time() - START_TIME
    total_evasion = elapsed_time * TAX_EVASION_PER_SECOND
    return jsonify({"total_tax_evasion": round(total_evasion, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
