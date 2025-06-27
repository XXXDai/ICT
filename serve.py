from flask import Flask, send_from_directory
import os

app = Flask(__name__)

project_root = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def serve_index():
    return send_from_directory(project_root, 'index.html')

@app.route('/<path:filename>')
def serve_files(filename):
    return send_from_directory(project_root, filename)

if __name__ == '__main__':
    # 监听 0.0.0.0 地址以允许外部访问
    # 您可以根据需要更改端口，确保它不与服务器上其他服务冲突
    PORT = 8081
    print(f"Flask 服务器已启动，正在监听 http://0.0.0.0:{PORT}")
    print(f"http://43.162.125.199:{PORT}")
    
    app.run(host="0.0.0.0", port=PORT) 