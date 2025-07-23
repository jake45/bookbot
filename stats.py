def count_words(text):
  list_of_words = text.split()
  count = 0
  for word in list_of_words:
      count += 1
  return count



def get_char_freq(text):
  new_text = text.lower()
  char_dict = {}
  count_char = 0
  for char in new_text:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1
  return char_dict


# Using our character dictionary, create a list of dictionaries

def list_dict(dict):
  dict_list = []
  my_dict = {}
  for item in dict:
    my_dict = {"char":item, "num":dict[item]}
    dict_list.append(my_dict)
  return dict_list

def sort_on(items):
  return items["num"]