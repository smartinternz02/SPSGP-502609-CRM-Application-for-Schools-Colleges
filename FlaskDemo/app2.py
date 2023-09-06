# Step 1: Import the required lib
from flask import Flask,render_template

# Step 2: Initialize the flask
app = Flask(__name__)

# Step 3: Use decorators and func for routing
@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/demo2')
def demo2():
    return render_template('demo2.html')
# Step 4: Run the application
if __name__ == '__main__':
    app.run(debug=True)