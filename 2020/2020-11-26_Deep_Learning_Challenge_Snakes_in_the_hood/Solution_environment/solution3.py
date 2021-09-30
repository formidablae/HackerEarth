import operator

TRAIN_CSV = './dataset/train.csv'
TEST_CSV = './dataset/test.csv'
good_results = {2: 3.50922,
                #4: 3.44947,
                65: 4.94926,
                13: 3.76555,
                17: 3.75373,
                20: 3.55224,
                22: 3.75495,
                #26: 3.50508,
                66: 4.94926,
                28: 3.58987,
                31: 3.83103,
                32: 4.20814,
                33: 3.74994,
                40: 3.61153,
                52: 4.02918,
                58: 3.56893,
                61: 4.37124}


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


def get_input_images_filenames(filename):
    names_file_handler = open(filename, 'r')
    names_file_handler.readline().strip()
    names_list = []
    while True:
        values_line = names_file_handler.readline()
        if not values_line:
            break
        names_list.append(values_line.strip())
    names_file_handler.close()
    return names_list


filenames = {}
for key in good_results.keys():
    filenames[key] = "results" + str(key) + ".csv"

dictionary_of_training_values = get_dict_values_from_file(TRAIN_CSV)
all_breeds = list(set(dictionary_of_training_values.values()))
test_file_ids = get_input_images_filenames(TEST_CSV)
ids_breeds_dict = {}
for key in good_results.keys():
    this_ids_breed_dict = get_dict_values_from_file(filenames[key])
    for i in range(len(test_file_ids)):
        this_is_possible_breeds_in = this_ids_breed_dict[test_file_ids[i]]
        if test_file_ids[i] in ids_breeds_dict.keys():
            this_id_possible_breeds_already = ids_breeds_dict[test_file_ids[i]]
            if this_is_possible_breeds_in in this_id_possible_breeds_already.keys():
                this_id_possible_breeds_already[this_is_possible_breeds_in] += good_results[key]
            else:
                this_id_possible_breeds_already[this_is_possible_breeds_in] = good_results[key]
        else:
            ids_breeds_dict[test_file_ids[i]] = {this_is_possible_breeds_in: good_results[key]}

final_ids_breeds = {}
for key in ids_breeds_dict.keys():
    this_dict = ids_breeds_dict[key]
    best_breed = max(this_dict.items(), key=operator.itemgetter(1))[0]
    final_ids_breeds[key] = best_breed

print(final_ids_breeds)

results = "image_id,breed\n"
for i in range(len(test_file_ids)):
    id_value = test_file_ids[i]
    breed = final_ids_breeds[id_value]
    results = results + str(id_value) + "," + str(breed) + "\n"
print(results)
f = open("results" + "67" + ".csv", "w")
f.write(results)
f.close()
