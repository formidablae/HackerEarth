def get_dict_values_from_file(filename):
    values_file_handler = open(filename, 'r')
    values_file_handler.readline().strip()
    dict_values = {}
    while True:
        values_line = values_file_handler.readline()
        if not values_line:
            break
        values_line_info = \
            list(map(str, values_line.strip().split(',')))
        dict_values[values_line_info[0]] = values_line_info[1]
    values_file_handler.close()
    return dict_values


diction = get_dict_values_from_file("train.csv")
training_ids = []
training_values = []
testing_ids = []
testing_values = []
for elem in diction.keys():
    if len(testing_ids) < len(training_ids):
        if diction[elem] not in training_values:
            training_ids.append(elem)
            training_values.append(diction[elem])
        else:
            testing_ids.append(elem)
            testing_values.append(diction[elem])
    else:
        training_ids.append(elem)
        training_values.append(diction[elem])

output_training_full = "image_id,breed\n"
output_training_ids = ""
output_testing_full = "image_id,breed\n"
output_testing_ids = ""
for elem in training_ids:
    output_training_full = output_training_full + str(elem) + "," + diction[elem] + "\n"
for elem in training_ids:
    output_training_ids = output_training_ids + str(elem) + ".jpg\n"
for elem in testing_ids:
    output_testing_full = output_testing_full + str(elem) + "," + diction[elem] + "\n"
for elem in testing_ids:
    output_testing_ids = output_testing_ids + str(elem) + ".jpg\n"
f = open("output_training_full.txt", "w")
f.write(output_training_full)
f.close()
f = open("output_training_ids.txt", "w")
f.write(output_training_ids)
f.close()
f = open("output_testing_full.txt", "w")
f.write(output_testing_full)
f.close()
f = open("output_testing_ids.txt", "w")
f.write(output_testing_ids)
f.close()
print(len(training_values))
print(len(training_ids))
print(len(testing_values))
print(len(testing_ids))
