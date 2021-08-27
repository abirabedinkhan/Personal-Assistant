import json

question = str(input("Question: "))
answer = str(input("Answer: "))


# function to add to JSON
def write_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


with open('data.json') as json_file:
    data = json.load(json_file)

    temp = data['code']

    id = temp[-1]['id']

    # python object to be appended
    y = {
        "id": id+1,
        "question": question,
        "answer": answer
    }

    # appending data to code
    temp.append(y)

write_json(data)
