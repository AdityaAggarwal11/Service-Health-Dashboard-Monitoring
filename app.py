from flask import Flask, jsonify, render_template
import psutil
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

app = Flask(__name__)

# Shared data store for metrics
metrics = {
    "cpu_percent": 0,
    "ram_percent": 0,
    "disk_percent": 0,
    "net_sent": 0,
    "net_recv": 0,
    "timestamp": None
}

def collect_metrics():
    global metrics
    metrics['cpu_percent'] = psutil.cpu_percent(interval=1)
    metrics['ram_percent'] = psutil.virtual_memory().percent
    metrics['disk_percent'] = psutil.disk_usage('/').percent

    net_io = psutil.net_io_counters()
    metrics['net_sent'] = net_io.bytes_sent
    metrics['net_recv'] = net_io.bytes_recv
    metrics['timestamp'] = datetime.now().strftime("%H:%M:%S")

# Start scheduler to update metrics every 60 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(func=collect_metrics, trigger="interval", seconds=60)
scheduler.start()

# Run once at start
collect_metrics()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/metrics')
def get_metrics():
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

