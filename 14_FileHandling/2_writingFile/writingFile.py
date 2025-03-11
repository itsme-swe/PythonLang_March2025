file1 = open("writeFile.txt", "w")

str1 = file1.write(
    """ Home Address - C-357 SiddharthNagar, Jaipur, Rajasthan 302017

Contact Num - +91 900xxxx987

Name - "Anand Ahuja" """
)

file1.close()
