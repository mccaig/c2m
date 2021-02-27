import csv
import chevron
import sys

csv_file = sys.argv[1]
template_file = sys.argv[2]
file_name_field = sys.argv[3]
file_name_extension = sys.argv[4]

with open(template_file, 'r') as t:
  with open(csv_file, 'r') as c:
    reader = csv.DictReader(c)
    for row in reader:
      out_file_name = row[file_name_field] + "." + file_name_extension
      with open(out_file_name, "w") as out_file:
        t.seek(0) # Chevron doesnt seek to 0 on each use for some reason
        rendered = chevron.render(template=t, data=row)
        out_file.write(rendered)
