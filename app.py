from flask import Flask, render_template
import json
import boto3
import os
import datetime
import aws
import filename

app = Flask(__name__)

@app.route('/')
def index():
    problems_file_name, time_file_name = filename.get()

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name, problems_file_name)
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name, encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('index.html',
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0')

#http://localhost:5000