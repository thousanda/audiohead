import argparse
from pathlib import Path
from pydub import AudioSegment


HEAD: int = 15
SECONDS: int = 1000


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', type=str, help='audio file name you want to cut')
    return parser.parse_args()


def audio_head(filepath: Path):
    sfx = filepath.suffix
    if sfx == '.wav':
        audio = AudioSegment.from_wav(str(filepath))
    elif sfx == '.mp3':
        audio = AudioSegment.from_mp3(str(filepath))
    else:
        print(f'not supported file format, {sfx}')
        return
    print(f'original duration: {audio.duration_seconds}')

    # 頭の15秒を切り出す
    head = audio[:HEAD*SECONDS]

    # 書き出す
    head.export('./audio/exported.wav', format='wav')

    return


def main():
    args = get_args()
    filename: str = args.filename
    print(f'input file: {filename}')
    p = Path(filename)
    print(f'START: cut audio and export head {HEAD} seconds')
    audio_head(p)
    print('END: done')


if __name__ == '__main__':
    main()

