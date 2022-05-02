import pandas
import numpy
import os

df = pandas.read_csv("./ISIC-images/metadata.csv")

path = "./ISIC-images/Images"
path_mel = "./ISIC-images/Images/mel"
path_no_mel = "./ISIC-images/Images/no_mel"

mel = set()
non_mel = set()


for row in df.iterrows():

    if row[1]["dx"] == "mel":
        mel.add(row[1]["image_id"] + ".jpg")
    else:
        non_mel.add(row[1]["image_id"] + ".jpg")


files = os.listdir(path)
mel_list = list(mel)
for i in range(0,20):
    print(files[i])
    print(mel_list[i])




for file in files:
    if file.find("ISIC") == -1:
        continue
    if file in mel:
        os.rename(path + "/" + file, path_mel + "/" + file)
    else:
        os.rename(path + "/" + file, path_no_mel + "/" + file)
