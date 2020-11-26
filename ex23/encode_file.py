import sys
script, from_file, to_file, encoding, error = sys.argv

source = open(from_file, 'r')
destination = open(to_file, 'w')

def main(from_file, to_file, encoding, errors):
    line = from_file.readline()

    if line:
        to_file.write(f'{encode_line(line, encoding, errors)}')
        return main(from_file, to_file, encoding, errors)

def encode_line(line, encoding, errors):
    return line.encode(encoding, errors = errors)

main(source, destination, encoding, error)

source.close()
destination.close()
