import re


def order_for_names(lst):
    for row in lst[1:]:
        name_string = row[0] + row[1] + row[2]
        if len((re.sub(r'([А-Я])', r' \1', name_string).split())) == 3:
            row[0] = re.sub(r'([А-Я])', r' \1', name_string).split()[0]
            row[1] = re.sub(r'([А-Я])', r' \1', name_string).split()[1]
            row[2] = re.sub(r'([А-Я])', r' \1', name_string).split()[2]
        elif len((re.sub(r'([А-Я])', r' \1', name_string).split())) == 2:
            row[0] = re.sub(r'([А-Я])', r' \1', name_string).split()[0]
            row[1] = re.sub(r'([А-Я])', r' \1', name_string).split()[1]
            row[2] = ''
        elif len((re.sub(r'([А-Я])', r' \1', name_string).split())) == 1:
            row[0] = re.sub(r'([А-Я])', r' \1', name_string).split()[0]
            row[1] = ''
            row[2] = ''
    return lst


def normalize_phone_numbers(lst):
    pattern = re.compile(
        r'(\+7|8)\s?[/(]?(\d{3})[/)]?\s?\D?(\d{3})[/-]?(\d{2})[/-]?(\d{2})((\s)?[/(]?(доб.)?\s?(\d+)[/)]?)?')
    for row in lst:
        row[5] = pattern.sub(r'+7(\2)\3-\4-\5\7\8\9', row[5])
    return lst


def merge_list(lst):
    merged_list = []
    merged_list.append(lst[0])
    for old_str in lst[1:]:
        for new_str in merged_list:
            if new_str[0] == old_str[0] and new_str[1] == old_str[1]:
                if len(new_str[2]) == 0:
                    new_str[2] = old_str[2]
                if len(new_str[3]) == 0:
                    new_str[3] = old_str[3]
                if len(new_str[4]) == 0:
                    new_str[4] = old_str[4]
                if len(new_str[5]) == 0:
                    new_str[5] = old_str[5]
                if len(new_str[6]) == 0:
                    new_str[6] = old_str[6]
                    break
        else:
            merged_list.append(old_str)
    return merged_list
