import csv

LOOKUP = {
    'CTE_Neighborhood': 'Neighborhood',
    'Selective_Enrollment': 'Selective Enrollment',
    'IB': 'IB Diploma',
    'Magnet': 'Magnet High School',
    'Magnet_Cluster': 'Magnet Program',
    'CTE_CCA': 'CTE -  College and Career Academies',
    'Military': 'Military',
}

with open('rows.csv_accessType=DOWNLOAD') as school_file, open('programs.csv', 'w') as program_file :
  reader = csv.DictReader(school_file)
  writer = csv.writer(program_file)
  writer.writerow(['Progam ID', 'Program Type', 'School ID'])
  program_id = 0
  for row in reader :
    school_id = row['SchoolID']
    for program in row['ProgramTypes'].split('||')[:-1]:
      if row['School Category'] == 'HS' and row['Governanace'] == 'District'\
          and program == 'NA':
          writer.writerow((program_id, 'Neighborhood', school_id))
      else:
          program = LOOKUP.get(program, program)
          writer.writerow((program_id, program, school_id))

      program_id += 1
