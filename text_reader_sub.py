from bs4 import BeautifulSoup
import csv
class reading():
  def __init__(self, type='a'):
    self.type = type

  def get_text(self):
    soup_data = BeautifulSoup(open("html.txt"), "html.parser")
    with open("sorted_data.csv", "a") as fopen:
        csv_writer = csv.writer(fopen)
        csv_writer.writerow([self.type, soup_data.find_all(self.type)])
