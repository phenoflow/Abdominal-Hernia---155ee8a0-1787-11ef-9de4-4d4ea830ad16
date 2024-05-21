# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"94065","system":"readv2"},{"code":"59925","system":"readv2"},{"code":"17898","system":"readv2"},{"code":"3742","system":"readv2"},{"code":"44246","system":"readv2"},{"code":"42741","system":"readv2"},{"code":"50547","system":"readv2"},{"code":"99143","system":"readv2"},{"code":"33743","system":"readv2"},{"code":"45678","system":"readv2"},{"code":"3534","system":"readv2"},{"code":"93769","system":"readv2"},{"code":"94802","system":"readv2"},{"code":"52472","system":"readv2"},{"code":"59850","system":"readv2"},{"code":"94896","system":"readv2"},{"code":"102649","system":"readv2"},{"code":"7679","system":"readv2"},{"code":"17191","system":"readv2"},{"code":"10301","system":"readv2"},{"code":"35236","system":"readv2"},{"code":"67276","system":"readv2"},{"code":"56519","system":"readv2"},{"code":"108628","system":"readv2"},{"code":"24982","system":"readv2"},{"code":"41509","system":"readv2"},{"code":"15680","system":"readv2"},{"code":"33696","system":"readv2"},{"code":"31396","system":"readv2"},{"code":"105998","system":"readv2"},{"code":"48823","system":"readv2"},{"code":"53447","system":"readv2"},{"code":"103974","system":"readv2"},{"code":"56506","system":"readv2"},{"code":"611","system":"readv2"},{"code":"38101","system":"readv2"},{"code":"24628","system":"readv2"},{"code":"42143","system":"readv2"},{"code":"40679","system":"readv2"},{"code":"45772","system":"readv2"},{"code":"11206","system":"readv2"},{"code":"68086","system":"readv2"},{"code":"244","system":"readv2"},{"code":"48101","system":"readv2"},{"code":"15050","system":"readv2"},{"code":"60614","system":"readv2"},{"code":"268","system":"readv2"},{"code":"96844","system":"readv2"},{"code":"72057","system":"readv2"},{"code":"652","system":"readv2"},{"code":"101576","system":"readv2"},{"code":"91771","system":"readv2"},{"code":"12842","system":"readv2"},{"code":"68045","system":"readv2"},{"code":"12246","system":"readv2"},{"code":"90490","system":"readv2"},{"code":"42716","system":"readv2"},{"code":"70611","system":"readv2"},{"code":"70402","system":"readv2"},{"code":"47125","system":"readv2"},{"code":"63506","system":"readv2"},{"code":"64977","system":"readv2"},{"code":"62486","system":"readv2"},{"code":"64067","system":"readv2"},{"code":"36963","system":"readv2"},{"code":"14670","system":"readv2"},{"code":"34915","system":"readv2"},{"code":"95704","system":"readv2"},{"code":"56522","system":"readv2"},{"code":"33485","system":"readv2"},{"code":"67309","system":"readv2"},{"code":"45687","system":"readv2"},{"code":"29442","system":"readv2"},{"code":"71835","system":"readv2"},{"code":"102624","system":"readv2"},{"code":"90489","system":"readv2"},{"code":"94016","system":"readv2"},{"code":"21284","system":"readv2"},{"code":"5870","system":"readv2"},{"code":"103310","system":"readv2"},{"code":"57942","system":"readv2"},{"code":"19397","system":"readv2"},{"code":"19219","system":"readv2"},{"code":"53794","system":"readv2"},{"code":"28944","system":"readv2"},{"code":"9949","system":"readv2"},{"code":"34987","system":"readv2"},{"code":"28558","system":"readv2"},{"code":"3200","system":"readv2"},{"code":"96040","system":"readv2"},{"code":"37796","system":"readv2"},{"code":"3367","system":"readv2"},{"code":"69455","system":"readv2"},{"code":"41790","system":"readv2"},{"code":"10139","system":"readv2"},{"code":"41524","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-hernia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-hernia-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-hernia-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-hernia-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
