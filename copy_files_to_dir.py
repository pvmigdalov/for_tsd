import argparse
import csv
import os


def import_files(from_dir, to_dir):
    for filename in os.listdir(from_dir):
        # read file
        read_path = os.path.join(from_dir, filename)
        with open(read_path, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            data = [row for row in reader]

        # write to file
        write_path = os.path.join(to_dir, filename)
        with open(write_path, 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str)
    args = parser.parse_args()

    if args.mode == 'totsd':
        import_files('data', 'to_save')
    elif args.mode == 'fromtsd':
        import_files('to_save', 'data')