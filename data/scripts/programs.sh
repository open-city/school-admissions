wget https://docs.google.com/spreadsheets/d/1Zi4Ot-yLGOOWw5wfj5iIelLoIIaTaHbHjM1A6D3hUbU/export?format=csv -O programs.csv
csvgrep -c 1 -r 'JROTC|Advancement Via|Fine and Performing|Early College|Small|General Education' -i programs.csv > ../processed_data/hs_programs.csv
rm programs.csv
