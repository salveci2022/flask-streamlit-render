cat <<EOT > app.py
from flask import Flask
import threading
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask rodando! Acesse /streamlit para iniciar o Streamlit"

@app.route('/streamlit')
def streamlit():
    def run():
        subprocess.run(["streamlit", "run", "app.py", "--server.port=8501"])

    thread = threading.Thread(target=run)
    thread.start()
    return "🚀 Streamlit iniciado! Acesse http://localhost:8501"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
EOT
