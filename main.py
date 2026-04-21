import os
import sys
import subprocess

AUDIO_EXTENSIONS = {
    "mp3", "wav", "flac", "aac", "ogg", "wma", "m4a",
    "alac", "aiff", "ape", "amr",
    "MP3", "WAV", "FLAC", "AAC", "OGG", "WMA", "M4A",
    "ALAC", "AIFF", "APE", "AMR"
}

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

    for dirpath, _, files in os.walk(filepath):
        for file in files:
            full_filepath = dirpath + '/' + file
            dest_filepath = 'output/' + full_filepath
            dot_i = dest_filepath.rfind('.')
            opus_filepath = dest_filepath[:dot_i] + '.opus'
            slash_i = opus_filepath.rfind('/')
            os.makedirs(opus_filepath[:slash_i], exist_ok=True)

            extension = dest_filepath[dot_i + 1:]
            command = []
            match extension:
                case _ if extension in AUDIO_EXTENSIONS:
                    command = ['ffmpeg', '-i', full_filepath, opus_filepath]
                case _:
                    command = ['cp', full_filepath, dest_filepath]

            print(command)
            subprocess.run(command, check=False)

def main():
    filepath = check_input()
    convert_songs(filepath)

if __name__ == '__main__':
    main()
