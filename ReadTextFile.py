def parse_text_file(filename):
    # databse file with username and hashed-password.
    infile = "hlogins.dadt"
    # open the file to read
    try:
        fd = open(infile, "r")
    except Exception as e:
        print("File read error!: ", str(e))
        exit()

    # read the infile line by line to retrive a matching row with first
    user_pswdrows = fd.readlines()
    for eachline in user_pswdrows:
        print("Type eachline", type(eachline))
        print("eachline", eachline)
        print("")
        data_values = eachline.split(",")
        print("Type of data_values", type(data_values))
        print("tokens", data_values)
        print("=============")

        # @TODO
        # Task-6: print username field and hash field in each of the line.

        # @TODO
        # Task-7: create a search variable named as sarch_username=naresh.adhikari@sru.edu outside the loop, and perform a search to find if the search value 'naresh.adhikari@sru.edu' exists in the data file. Compare the search field with every user email field value in each row of the input file.


#Run it.
filename = "hlogins.dat"
parse_text_file(filename)