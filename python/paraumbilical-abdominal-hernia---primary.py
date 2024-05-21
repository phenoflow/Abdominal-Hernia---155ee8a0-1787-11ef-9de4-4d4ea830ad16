# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7H1Cz00","system":"readv2"},{"code":"7H15100","system":"readv2"},{"code":"J323.00","system":"readv2"},{"code":"7H1Cy00","system":"readv2"},{"code":"7H1C000","system":"readv2"},{"code":"7H1C200","system":"readv2"},{"code":"J32y100","system":"readv2"},{"code":"J322.00","system":"readv2"},{"code":"7H15.00","system":"readv2"},{"code":"J321z00","system":"readv2"},{"code":"7H15z00","system":"readv2"},{"code":"J321100","system":"readv2"},{"code":"7H15y00","system":"readv2"},{"code":"7H1C100","system":"readv2"},{"code":"J323z00","system":"readv2"},{"code":"J320z00","system":"readv2"},{"code":"J321.00","system":"readv2"},{"code":"J32y.00","system":"readv2"},{"code":"7H15000","system":"readv2"},{"code":"J32z.00","system":"readv2"},{"code":"J323100","system":"readv2"},{"code":"J32..12","system":"readv2"},{"code":"7H15200","system":"readv2"},{"code":"J32..00","system":"readv2"},{"code":"J322z00","system":"readv2"},{"code":"J32yz00","system":"readv2"},{"code":"J322100","system":"readv2"},{"code":"J320100","system":"readv2"},{"code":"7H1C.00","system":"readv2"},{"code":"K42","system":"readv2"},{"code":"T24.8","system":"readv2"},{"code":"T24.3","system":"readv2"},{"code":"T24","system":"readv2"},{"code":"T24.1","system":"readv2"},{"code":"T24.2","system":"readv2"},{"code":"T24.9","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["paraumbilical-abdominal-hernia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["paraumbilical-abdominal-hernia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["paraumbilical-abdominal-hernia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
