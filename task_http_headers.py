import json

def find_prtcl(f_str):
    out_dict = {}
    lst = f_str.split()
    if lst[0] == 'GET' or lst[0] == 'POST':
        out_dict['method'] = lst[0]
        out_dict['url'] = lst[1]
        out_dict['protocol'] = lst[2]
    else:
        out_dict['protocol'] = lst[0]
        lst.remove(lst[0])
        out_dict['status_code'] = lst[0]
        lst.remove(lst[0])
        if out_dict['protocol'] != 'HTTP/2':
            out_dict['status_message'] = ' '.join(lst)
    return out_dict


def parse_str(t_str):
    ind = t_str.find(':')
    key = t_str[:ind]
    value = t_str[ind+2:].strip()
    return key, value


def get_source_lst(tfile):
    with open(tfile) as f:
        lst = f.readlines()
    return lst

def save_to_file(tfile, tmp_dict):
    with open(tfile, 'w') as f:
        json.dump(tmp_dict, f)


def http_headers_to_json(source_file, output_file):
    lst = get_source_lst(source_file)

    first_line = lst[0]
    lst.remove(first_line)

    out_dict = find_prtcl(first_line)
    for i in lst:
        if i != '\n':
            tmp_key, tmp_vle = parse_str(i)
            out_dict[tmp_key] = tmp_vle
    save_to_file(output_file, out_dict)



if __name__ == '__main__':

    for i in range(1,4):
        http_headers_to_json('headers-{}.txt'.format(str(i)), 'results-{}.json'.format(str(i)))
