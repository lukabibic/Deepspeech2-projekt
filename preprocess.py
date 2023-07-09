import os
import pandas as pd

path = os.getcwd()
os.chdir(path)

wav = list()
transcriptions_map = dict()
txt_wav_map = dict()

for t in sorted(os.listdir("txt")):
    for file in sorted(os.listdir(os.path.join(path, "txt", t))):
        with open(os.path.join(path, "txt", t, file), "r") as readFile:
            transcriptions_map[os.path.splitext(file)[0]] = " ".join(readFile.readline().strip().split())

for w in sorted(os.listdir("wav")):
    for file in sorted(os.listdir(os.path.join(path, "wav", w))):
        if file.endswith(".wav"):
            wav.append(os.path.splitext(file)[0])
        else:
            os.remove(os.path.join(path, "wav", w, file))

for txt_file_name in transcriptions_map:
    if txt_file_name in wav:
        txt_wav_map[txt_file_name] = transcriptions_map[txt_file_name]

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(txt_wav_map, orient='index', columns=['transcription'])
df.index.name = 'filename'
df.reset_index(inplace=True)

# Define the path and filename for the CSV file
output_file = 'dataset.csv'

# Write the DataFrame to a CSV file with the specified delimiter
df.to_csv(output_file, sep='|', index=False)
