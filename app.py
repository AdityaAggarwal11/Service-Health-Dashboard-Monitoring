from flask import Flask, render_template, jsonify
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
    "timestamp": None,
    "alerts": []
}

# Thresholds
CPU_THRESHOLD = 80  # %
RAM_THRESHOLD = 80  # %
DISK_THRESHOLD = 90  # %

def collect_metrics():
    global metrics
    cpu = psutil.cpu_percent(interval=0)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()

    alerts = []

    if cpu > CPU_THRESHOLD:
        alerts.append(f"⚠️ High CPU usage: {cpu}%")
    if ram > RAM_THRESHOLD:
        alerts.append(f"⚠️ High RAM usage: {ram}%")
    if disk > DISK_THRESHOLD:
        alerts.append(f"⚠️ High Disk usage: {disk}%")

    metrics.update({
        "cpu_percent": cpu,
        "ram_percent": ram,
        "disk_percent": disk,
        "net_sent": net_io.bytes_sent,
        "net_recv": net_io.bytes_recv,
        "timestamp": datetime.now().isoformat(),
        "alerts": alerts
    })

# Start scheduler to update metrics every 5 seconds
scheduler = BackgroundScheduler()
scheduler.add_job(func=collect_metrics, trigger="interval", seconds=5)
scheduler.start()

# Run once at start
collect_metrics()

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/metrics')
def get_metrics():
    return jsonify(metrics)

@app.route('/alerts')
def get_alerts():
    return jsonify(alerts=metrics["alerts"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

