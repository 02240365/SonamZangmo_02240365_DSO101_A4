from flask import Flask, jsonify

app = Flask(__name__)

# In-memory task list
tasks = []

@app.route('/')
def home():
    return jsonify({
        "message": "TaskFlow API is running",
        "student": "Sonam Zangmo",
        "student_id": "02240365"
    })

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    from flask import request
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Title is required"}), 400
    task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
