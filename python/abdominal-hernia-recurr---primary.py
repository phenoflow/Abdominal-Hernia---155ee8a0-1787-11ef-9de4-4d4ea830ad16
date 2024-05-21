# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7H14.00","system":"readv2"},{"code":"7H14200","system":"readv2"},{"code":"7H1E.00","system":"readv2"},{"code":"7H1D100","system":"readv2"},{"code":"J301100","system":"readv2"},{"code":"7H12000","system":"readv2"},{"code":"7H14y00","system":"readv2"},{"code":"7H12100","system":"readv2"},{"code":"J303300","system":"readv2"},{"code":"7H1D200","system":"readv2"},{"code":"J312100","system":"readv2"},{"code":"7H1Ez00","system":"readv2"},{"code":"7H1D.00","system":"readv2"},{"code":"J313100","system":"readv2"},{"code":"J300300","system":"readv2"},{"code":"7H12y00","system":"readv2"},{"code":"7H14100","system":"readv2"},{"code":"J302100","system":"readv2"},{"code":"7H12.00","system":"readv2"},{"code":"7H1Ey00","system":"readv2"},{"code":"7H1Dz00","system":"readv2"},{"code":"7H1E100","system":"readv2"},{"code":"7H1E000","system":"readv2"},{"code":"J30y300","system":"readv2"},{"code":"7H12200","system":"readv2"},{"code":"7H14z00","system":"readv2"},{"code":"7H1E200","system":"readv2"},{"code":"J31y100","system":"readv2"},{"code":"7H1Dy00","system":"readv2"},{"code":"7H12z00","system":"readv2"},{"code":"J302300","system":"readv2"},{"code":"J30y100","system":"readv2"},{"code":"J303100","system":"readv2"},{"code":"T97.3","system":"readv2"},{"code":"T98.8","system":"readv2"},{"code":"T21.8","system":"readv2"},{"code":"T23.3","system":"readv2"},{"code":"T97.8","system":"readv2"},{"code":"T23.9","system":"readv2"},{"code":"T21.2","system":"readv2"},{"code":"T97.9","system":"readv2"},{"code":"T97.2","system":"readv2"},{"code":"T23","system":"readv2"},{"code":"T23.8","system":"readv2"},{"code":"T21.1","system":"readv2"},{"code":"T97","system":"readv2"},{"code":"T21.9","system":"readv2"},{"code":"T98.3","system":"readv2"},{"code":"T98.9","system":"readv2"},{"code":"T21","system":"readv2"},{"code":"T21.3","system":"readv2"},{"code":"T98.2","system":"readv2"},{"code":"T23.2","system":"readv2"},{"code":"T23.1","system":"readv2"},{"code":"T98","system":"readv2"},{"code":"T97.1","system":"readv2"},{"code":"T98.1","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-hernia-recurr---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-hernia-recurr---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-hernia-recurr---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
