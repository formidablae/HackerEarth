import random

TRAIN_CSV = './dataset/train.csv'
TEST_CSV = './dataset/test.csv'

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


dictionary_of_training_values = get_dict_values_from_file(TRAIN_CSV)
all_breeds = list(set(dictionary_of_training_values.values()))

test_file_ids = get_input_images_filenames(TEST_CSV)

for i in range(3, 100):
    results = "image_id,breed\n"
    for j in range(len(test_file_ids)):
        index = random.randrange(35)
        id_value = test_file_ids[j]
        breed = all_breeds[index]
        results = results + str(id_value) + "," + str(breed) + "\n"
    f = open("results" + str(i) + ".csv", "w")
    f.write(results)
    f.close()
