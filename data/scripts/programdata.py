import csv

with open('rows.csv_accessType=DOWNLOAD') as school_file, open('programs.csv', 'w') as program_file :
	reader = csv.DictReader(school_file)
	writer = csv.writer(program_file)
	writer.writerow(['Progam ID', 'Program Type', 'School ID'])
	program_id = 0
	for row in reader :
		school_id = row['SchoolID']
		for program in row['ProgramTypes'].split('||')[:-1]:
			writer.writerow((program_id, program, school_id))
			program_id += 1
