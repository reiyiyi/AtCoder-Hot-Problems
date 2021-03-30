from flask import Flask, render_template
import json
import boto3
import os
import aws
import filename

app = Flask(__name__)
@app.route('/')
def index():
    ignore, time_file_name = filename.get()

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(time_file_name, encoding='utf-8') as f:
        time_data = json.load(f)

    return render_template('index.html',
                        time_data=time_data)

@app.route('/ranking', methods=["GET"])
def ranking():
    problems_file_name, time_file_name = filename.get()

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="全体",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac0', methods=["GET"])
def ranking_ac0():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "0"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数0~199",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac200', methods=["GET"])
def ranking_ac200():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "200"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数200~399",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac400', methods=["GET"])
def ranking_ac400():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "400"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数400~599",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac600', methods=["GET"])
def ranking_ac600():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "600"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数600~799",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac800', methods=["GET"])
def ranking_ac800():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "800"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数800~999",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

@app.route('/ranking-ac1000', methods=["GET"])
def ranking_ac1000():
    problems_file_name, time_file_name = filename.get()
    problems_file_name = problems_file_name + "1000"

    s3 = aws.get()

    bucket = s3.Bucket('hotproblems')
    bucket.download_file('hot_problems_data/' + problems_file_name + '.json', problems_file_name + '.json')
    bucket.download_file('hot_problems_data/' + time_file_name, time_file_name)

    with open(problems_file_name + '.json', encoding='utf-8') as f:
        hot_problems_data = json.load(f)

    with open(time_file_name, encoding='utf-8') as f2:
        time_data = json.load(f2)

    return render_template('ranking.html',
                        ranking_type="AC数1000~",
                        hot_problems_data=hot_problems_data,
                        time_data=time_data)

if __name__ == "__main__":
   app.run(debug=True, host='0.0.0.0')

#http://localhost:5000