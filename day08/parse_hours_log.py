import sys
import re

def parse_hours_log(log_file):
    """
    Parses a log file to extract hours, prints them with their description
    and stores them in a list with the corresponding desctiption.

    """
    with open(log_file, 'r') as file:
        content = file.read()
        lines = content.splitlines()
        print(lines)
        hours_list = []
        for i,line in enumerate(lines[:-1]):
            match = re.findall(r'(^[0-9]{2}:[0-9]{2})', lines[i])
            second_match = re.findall(r'(^[0-9]{2}:[0-9]{2})', lines[i+1])
            descroption = re.findall(r'(\s.*$)', lines[i])
            #hour = f'{match}-{second_match}'
            #print(hour)
            if match and second_match and descroption:
                hour = f'{match[0]}-{second_match[0]} {descroption[0].strip()}'
                print(hour)
                hours_list.append(hour)

            if line == '':
                print('')
                hours_list.append('none')

    return hours_list

def calculate_minutes(hours_list):
    """
    Calculates the total minutes of each activity from a list of hours.

    """
    total_minutes = 0
    for hour in hours_list:
        if hour == 'none':
            continue
        match = re.findall(r'(\d{2}):(\d{2})-(\d{2}):(\d{2})', hour)
        if match:
            start_hour, start_minute, end_hour, end_minute = map(int, match[0])
            total_minutes += (end_hour - start_hour) * 60 + (end_minute - start_minute)
    return total_minutes

def return_report_file(hours_list):
    output_file = sys.argv[1].replace('.log', '_report.txt')
    with open(output_file, 'w') as f:
        for i, (key, value) in enumerate(items):
            line = "{:<15} {}".format(key, value)
            if i < len(items) - 1:
                line += '\n'
            f.write(line)

def main():
    '''Main function to execute the sequence processing.'''
    input_file = sys.argv[1]
    hours_list = parse_hours_log(input_file)
    sorted_seq_lst = sort_sequences(seq_lst)
    print(sorted_seq_lst)

if __name__ == "__main__":
    main()