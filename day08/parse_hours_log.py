import sys
import re
from datetime import datetime

def parse_log_lines(lines):
    parsed = []
    last_was_empty = False
    
    for i in range(len(lines) - 1):
        if not lines[i] or not lines[i + 1]:
            if not last_was_empty:
                parsed.append(None)
                last_was_empty = True
            continue
        last_was_empty = False

        current = lines[i]
        next_line = lines[i + 1]

        current_match = re.match(r'^(\d{2}:\d{2})\s+(.*)$', current)
        next_match = re.match(r'^(\d{2}:\d{2})\s+(.*)$', next_line)

        if current_match and next_match:
            start = current_match.group(1)
            end = next_match.group(1)
            description = current_match.group(2).strip()

            if description.lower() == 'end':
                continue

            parsed.append((start, end, description))

    return parsed


def pair_entries_with_durations(entries):
    report_lines = []
    activity_durations = {}

    for item in entries:
        if item is None:
            report_lines.append('')
            continue

        start_time, end_time, activity = item

        start_dt = datetime.strptime(start_time, "%H:%M")
        end_dt = datetime.strptime(end_time, "%H:%M")
        duration = int((end_dt - start_dt).total_seconds() / 60)

        if duration <= 0:
            continue

        report_lines.append(f"{start_time}-{end_time} {activity}")
        activity_durations[activity] = activity_durations.get(activity, 0) + duration

    return report_lines, activity_durations


def generate_summary(activity_durations):
    """
    Generates a summary of total minutes spent on each activity and their percentage of total time.
    Returns a list of formatted strings for the summary.
    """
    total_minutes = sum(activity_durations.values())
    summary = []

    for activity, minutes in sorted(activity_durations.items(), key=lambda x: -x[1]):
        percent = (minutes / total_minutes) * 100
        summary.append(f"{activity:<25} {minutes:>3} minutes   {percent:>3.0f}%")

    return summary


def write_report(report_lines, summary_lines, input_file):
    """
    Writes the report and summary to a new file based on the input file name.
    The output file will have the same name as the input file but with '_report'.
    """
    output_file = input_file.replace('.log', '_report.txt')
    with open(output_file, 'w') as f:
        for line in report_lines:
            f.write(line + '\n')

        f.write('\n') 

        for line in summary_lines:
            f.write(line + '\n')



def main():
    """
    Main function to parse command line arguments, read the log file,
    process the entries, and write the report.
    """
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.log'):
        print("Usage: python parse_hours_log.py <file>.log")
        sys.exit(1)

    input_file = sys.argv[1]

    # Read the file and get lines
    with open(input_file, 'r') as f:
        lines = lines = [line.strip() for line in f]

    # Pass lines to the parser
    entries = parse_log_lines(lines)

    # Generate full report
    report_lines, activity_durations = pair_entries_with_durations(entries)
    summary_lines = generate_summary(activity_durations)
    write_report(report_lines, summary_lines, input_file)


if __name__ == "__main__":
    main()