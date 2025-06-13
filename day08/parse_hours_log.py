import sys
import re
from datetime import datetime

def parse_log_lines(lines):
    parsed = []
    last_empty = False

    for i in range(len(lines) - 1):
        if not lines[i] or not lines[i + 1]:
            if not last_empty:
                parsed.append(None)
                last_empty = True
            continue
        last_empty = False

        m1 = re.match(r'^(\d{2}:\d{2})\s+(.*)$', lines[i])
        m2 = re.match(r'^(\d{2}:\d{2})\s+', lines[i + 1])
        if m1 and m2:
            start, end = m1.group(1), m2.group(1)
            desc = m1.group(2).strip()
            if desc.lower() != 'end':
                parsed.append((start, end, desc))

    return parsed


def pair_entries_with_durations(entries):
    report = []
    durations = {}

    for item in entries:
        if item is None:
            report.append('')
            continue

        start, end, desc = item
        delta = (datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")).total_seconds() / 60
        if delta <= 0:
            continue

        report.append(f"{start}-{end} {desc}")
        durations[desc] = durations.get(desc, 0) + int(delta)

    return report, durations


def generate_summary(durations):
    total = sum(durations.values())
    return [
        f"{desc:<25} {mins:>3} minutes   {mins / total:>4.0%}"
        for desc, mins in sorted(durations.items(), key=lambda x: -x[1])
    ]


def write_report(report_lines, summary_lines, input_file):
    output_file = input_file.replace('.log', '_report.txt')
    with open(output_file, 'w') as f:
        f.write('\n'.join(report_lines) + '\n\n' + '\n'.join(summary_lines) + '\n')


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.log'):
        print("Usage: python parse_hours_log.py <file>.log")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f]

    entries = parse_log_lines(lines)
    report, durations = pair_entries_with_durations(entries)
    summary = generate_summary(durations)
    write_report(report, summary, sys.argv[1])


if __name__ == "__main__":
    main()