# Step 1: Import the required lib
from flask import Flask

# Step 2: Initialize the flask
app = Flask(__name__)

# Step 3: Use decorators and func for routing
@app.route('/')
def demo():
    return "Hello!!! I'm Hari Prabu."

# Step 4: Run the application
if __name__ == '__main__':
    app.run(debug=True)