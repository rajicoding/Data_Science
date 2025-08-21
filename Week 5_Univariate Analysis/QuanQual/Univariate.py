class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        # Check columns one by one using for loop
        for columnName in dataset.columns:
            if(dataset[columnName].dtype=="O"):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual