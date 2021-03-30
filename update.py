import requests
import json
import time
import datetime
import boto3
import os
import aws
import filename

JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

problems_file_name, time_file_name = filename.get()

s3 = aws.get()

bucket = s3.Bucket('hotproblems')

current_time = int(time.time())
research_time = current_time - 24 * 60 * 60

time_dict = dict()

time_dict["start_time"] = str(datetime.datetime.fromtimestamp(research_time, JST))
time_dict["end_time"] = str(datetime.datetime.fromtimestamp(current_time, JST))

date = datetime.datetime.now(JST) - datetime.timedelta(days=1)
time_dict["date"] = str(date.year) + "年" + str(date.month) + "月" + str(date.day) + "日"

submissions_url = "https://kenkoooo.com/atcoder/atcoder-api/v3/from/"
contests_url = "https://kenkoooo.com/atcoder/resources/contests.json"
problems_url = "https://kenkoooo.com/atcoder/resources/problems.json"
ac_url = "https://kenkoooo.com/atcoder/resources/ac.json"

contests_response = requests.get(contests_url)
print("hit API...")
time.sleep(1)
problems_response = requests.get(problems_url)
print("hit API...")
time.sleep(1)
ac_response = requests.get(ac_url)
print("hit API...")
time.sleep(1)

contests_json_data = contests_response.json()
problems_json_data = problems_response.json()
ac_json_data = ac_response.json()

total_problems_count = []
problems_count = [[] for _ in range(6)]
contests_name = dict()
problems_index = dict()
user_ac_data = dict()

for data in contests_json_data:
    contests_name[data["id"]] = data["title"]

for data in ac_json_data:
    user_ac_data[data["user_id"]] = data["problem_count"]

for data in problems_json_data:
    problems_index[data["id"]] = len(problems_count[0])
    data_dict = {"count":0, 
                "contests_name":contests_name[data["contest_id"]], 
                "problems_name":data["title"], 
                "contests_id":data["contest_id"], 
                "problems_id":data["id"]}

    total_problems_count.append(data_dict.copy())

    for i in range(6):
        problems_count[i].append(data_dict.copy())

number_of_submissions = 0

for _ in range(500):
    submissions_response = requests.get(submissions_url + str(research_time))
    print("hit API...")
    time.sleep(1)
    submissions_json_data = submissions_response.json()

    for data in submissions_json_data:
        if data["epoch_second"] >= current_time:
            print(data)
            print(datetime.datetime.fromtimestamp(int(data["epoch_second"]), JST))
            research_time = current_time
            break

        if number_of_submissions == 0:
            print(data)
            print(datetime.datetime.fromtimestamp(int(data["epoch_second"]), JST))

        total_problems_count[problems_index[data["problem_id"]]]["count"] += 1

        if data["user_id"] in user_ac_data:
            idx = user_ac_data[data["user_id"]] // 200
            if idx > 5:
                idx = 5

            problems_count[idx][problems_index[data["problem_id"]]]["count"] += 1

        number_of_submissions += 1
    
    if len(submissions_json_data) == 0:
        break
    #else:
        #print(datetime.datetime.fromtimestamp(int(submissions_json_data[-1]["epoch_second"])))

    research_time = submissions_json_data[-1]["epoch_second"] + 1

    if submissions_json_data[-1]["epoch_second"] >= current_time:
        break

time_dict["number_of_submissions"] = number_of_submissions

total_problems_count = sorted(total_problems_count, key=lambda x: x["count"], reverse=True)
total_problems_count = total_problems_count[:100]

with open(problems_file_name + ".json", 'w', encoding='utf-8') as f:
    json.dump(total_problems_count, f, ensure_ascii=False, indent=4)

bucket.upload_file(problems_file_name + '.json', 'hot_problems_data/' + problems_file_name + '.json')

for i in range(6):
    problems_count[i] = sorted(problems_count[i], key=lambda x: x["count"], reverse=True)
    problems_count[i] = problems_count[i][:100]

    with open(problems_file_name + str(200 * i) + ".json", 'w', encoding='utf-8') as f:
        json.dump(problems_count[i], f, ensure_ascii=False, indent=4)

    bucket.upload_file(problems_file_name + str(200 * i) + '.json', 'hot_problems_data/' + problems_file_name + str(200 * i) + '.json')

with open(time_file_name, 'w', encoding='utf-8') as f2:
    json.dump(time_dict, f2, ensure_ascii=False)

bucket.upload_file(time_file_name, 'hot_problems_data/' + time_file_name)