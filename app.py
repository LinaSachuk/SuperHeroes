import os
import csv
from flask import request
from flask import Flask, render_template, url_for, template_rendered

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


# from nbconvert import HTMLExporter
# import codecs
# import nbformat
# exporter = HTMLExporter()
# output_notebook = nbformat.read('ETL-Project.ipynb', as_version=4)
# output, resources = exporter.from_notebook_node(output_notebook)
# codecs.open('test.html', 'w', encoding='utf-8').write(output)


app = Flask(__name__)

csv_path = os.path.join('movie_actor_hero copy.csv')


movies_list = []
with open(csv_path, newline='') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',')
    # print(csv_data)

    csv_header = next(csv_data)
    # print(f"csv_header: {csv_header}")

    count = 0
    for row in csv_data:
        movies = {}
        # print('================================')

        # print(count)
        movies['Movie_Rank'] = row[5]
        movies['Title'] = row[0]
        movies['Plot'] = row[3]
        movies['Poster'] = row[4]
        movies['Hero_Name'] = row[7]
        movies['Hero_Images'] = row[12]
        count += 1

        movies_list.append(movies)
# print('================================')

sorted_list = sorted(movies_list, key=lambda k: int(k['Movie_Rank']))
# print(sorted_list)
# print('================================')


@app.route('/')
def index():

    # @TODO: render an index.html template and pass it the data you retrieved from the database

    return render_template("index.html", list=sorted_list)


@app.route('/ETL')
def etl():
    return app.send_static_file('ETL-Project.html')


if __name__ == "__main__":
    app.run(debug=True)
