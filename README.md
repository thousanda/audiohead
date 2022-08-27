# Audio Head

音声ファイルの頭の何秒間かだけを切り出した音声を作成してファイルに書き出す。
入力はwav, mp3に対応しています。出力はwavです。

## How to Use

`main.py`のHEADで頭の何秒を切り出すか指定する
```python
HEAD: int = 15
```

必要に応じて仮想環境を作る
```shell
# audioheadvenvという名前作成する場合
$ python -m venv audioheadvenv
# アクティベート
$ source audioheadvenv/bin/activate
```

依存ライブラリをインストール
```shell
pip install -r requirements.txt
```

実行する
```shell
$ python main.py -f オーディオファイル名
```