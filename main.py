import os
import sys

def check_input():
    filepath = ''

    if len(sys.argv) != 2:
        print('provide argument')
        exit()
    else:
        filepath = sys.argv[1]
        if not os.path.exists(filepath):
            print('provide real filepath')
            exit()
        if not os.path.isdir(filepath):
            print('provide directory')
            exit()

    return filepath

def convert_songs(filepath):
    try:
        os.mkdir('output')
    except FileExistsError:
        pass

    for dirpath, dirs, files in os.walk(filepath):
        for file in files:
            full_path = dirpath + '/' + file
            dot_i = full_path.rfind('.')
            opus_filepath = 'output/' + full_path[:dot_i] + '.opus'
            slash_i = opus_filepath.rfind('/')
            os.makedirs(opus_filepath[:slash_i], exist_ok=True)
            os.system(f'ffmpeg -i "{full_path}" "{opus_filepath}"')

def main():
    filepath = check_input()
    convert_songs(filepath)

if __name__ == '__main__':
    main()
