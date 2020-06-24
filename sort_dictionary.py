
def sort_dict_on_values(dict_to_sort, reverse=False):
  return [(key, value) for (key, value) in sorted(dict_to_sort.items(), key=lambda x: x[1], reverse=reverse)]

def sort_dict_on_keys(dict_to_sort, reverse=False):
  return [(key, value) for (key, value) in sorted(dict_to_sort.items(), key=lambda x: x[0], reverse=reverse)]


