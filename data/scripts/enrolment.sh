in2csv ../raw_data/cps_2013-14\ high\ school\ tarantula_2lwg.xlsx | \
csvcut -c 1-6 | \
tail -n +3 > \
../processed_data/2013-2014_enrollment_high_school.csv
