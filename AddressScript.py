inputFile = open(r'X:\Students\VKEHRI1\Sem2\GISC9317 Advanced Programming for GIS\D1\d1RawData\d1RawListOfFarms.txt', 'r')
outputFile = open(r'X:\Students\VKEHRI1\Sem2\GISC9317 Advanced Programming for GIS\D1\d1RawData\d1Result.txt', 'w')

fieldNames = 1
count = 1

for line in inputFile:
    if fieldNames == 1:
        header = 'FarmID\tAddress\tStreetNum\tStreetName\tSufType\tDir\tCity\tProvince\tPostalCode\n'
        outputFile.write(header)
    else:
        removeN = line.rstrip('\n')
        FarmIDField = removeN.split('\t')[0]
        AddressField = removeN.split('\t')[1]
        SplitAddress = AddressField.split('\t')[0]
        CityField = AddressField.split(', ')[1]
        SplitProvPost = AddressField.split(', ')[2]
        SplitAddress1 = SplitAddress.split(' ')
        StreetNumField = SplitAddress1[0]
        StreetNameField = SplitAddress1[1]
        Strip1 = SplitAddress.lstrip('')
        if count <len(StreetNumField):
            StreenName = StreetNameField[0] + ' ' + StreetNameField[1]
        else:
            StreetName = StreeNameField[0]       
        if SplitAddress1[-1] in DirList:
            StreetDirField = SplitAddress1[-1]
            strip2 = strip1.rstrip([' ' + StreetDirField])
            print strip2
        else:
            StreetDirField = ''
            StreetSufField = SplitAddress1[-1]
            strip3 = strip1.rstrip([' ' + StreetSufField])

        ProvinceField = SplitProvPost.split(' ')[0]
        PostalCodeField = SplitProvPost.strip(ProvinceField + ' ')

        FinalOutput = (FarmID + '\t' + AddressField + '\t' + StreetNumField + '\t' + StreetNameField + '\t' + StreetSufField + '\t' + StreetDirField + '\t' + CityField + '\t' + ProvinceField + '\t' + PostalCodeField +'\n')
        outputFile.write(FinalOutput)
    fieldNames = fieldNames + 1
inputFile.close()
outputFile.close()
