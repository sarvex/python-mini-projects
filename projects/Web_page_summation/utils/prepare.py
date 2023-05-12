import gzip

default_path = '.'

with gzip.open(f"{default_path}sumdata/train/train.article.txt.gz", "rb") as gz:
    with open(f"{default_path}sumdata/train/train.article.txt", "wb") as out:
        out.write(gz.read())

with gzip.open(f"{default_path}sumdata/train/train.title.txt.gz", "rb") as gz:
    with open(f"{default_path}sumdata/train/train.title.txt", "wb") as out:
        out.write(gz.read())
