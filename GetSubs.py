filename1 = 'ExternalFilesFolder/externalfile.exml'
filename2 = 'ExternalFilesFolder/externalfiletosearch.txt'
fileout = 'ExternalFilesFolder/outfile.txt'

with open(filename1) as externalfile:
    linesfile = externalfile.readlines()

with open(filename2) as externalfiletosearch:
    linestosearch = externalfiletosearch.readlines()  

with open(fileout,'w') as outfile:
    for stringsearch in linestosearch:
        for line in linesfile:
            if stringsearch.strip() in line:
                #print(line.strip())
                outfile.write(line)