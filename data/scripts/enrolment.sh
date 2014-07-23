in2csv ../raw_data/enrollment/cps_2013-14\ high\ school\ tarantula_2lwg.xlsx | \
tail -n +3 | \
sed 's/=//g' | \
sed 's/#DIV\/0!//g' > \
../processed_data/2013-2014_enrollment_high_school.csv
