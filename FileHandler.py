def WritetoFile(FileName,Data):
    with open(FileName,'w') as record:
        strr = "\n"
        content = strr.join(Data)
        record.write(content+'\n')