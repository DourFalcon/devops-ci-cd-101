from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'DevOps Learning Started! 🚀',
        'status': 'running'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200


@app.route('/api/info')
def info():
    """Info endpoint"""
    return jsonify({
        'app': 'DevOps CI/CD Demo',
        'version': '1.0',
        'environment': 'test'
    })


def add(a, b):
    """Simple math function for testing"""
    return a + b


def subtract(a, b):
    """Simple math function for testing"""
    return a - b


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
