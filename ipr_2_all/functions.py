import gzip
import io
import re
import matplotlib.pyplot as plt
from datetime import datetime
import os


def good_date(obj):
    result = datetime.strptime(str(obj[1]), "%d/%b/%Y:%H:%M")
    return str(result)

def unzip(file):
    if not os.path.isdir("results_files"):
        os.mkdir("results_files")
    with gzip.open(file, 'rb') as archiv:
        with io.TextIOWrapper(archiv, encoding='utf-8') as decoder:
            with open(f"results_files\\{file}.csv", "w") as csv_file:
                # Let's read the content using read()
                content = decoder.read()
                if file == "u05smevosb02_srv01_access.log.gz_csv.gz":
                    content = re.sub(r'(\d\d/\w+/\d{4}:\d\d:\d\d):\d\d\s\+\d{4}', good_date, content)
                csv_file.write(content)
    #return "results_files\\" + file + ".csv"
    return f"results_files\\{file}.csv"

def plotter(plt_label, df):
    fig = plt.figure()
    plt.plot('request', data=df, label='Интенсивность')
    plt.title(plt_label)
    plt.xlabel("Продолжительность чч:мм")
    plt.ylabel("Запросов в минуту")
    plt.ylim(0)

    #границы графика
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)

    plt.legend(loc=1)
    plt.grid(axis='y', alpha=.3)

    xtick_location = df.index.tolist()[::10]
    xtick_labels = [x[-9:-3] for x in df.index.tolist()[::10]]
    plt.xticks(ticks=xtick_location, rotation=90, labels=xtick_labels)

    #plt.show()
    if not os.path.isdir("grafics"):
        os.mkdir("grafics")
    fig.savefig("grafics\\" + plt_label + ".png")
