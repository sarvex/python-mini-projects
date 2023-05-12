#Simple program to fetch dns record of a given website

import dns.resolver

#User defined website
website = input("Enter the name of the website: ")

#Fetching the 'A' record of the website and storing it in the dictionary
a_record = dns.resolver.resolve(website, 'A')
dns_record = {'A_Record_IP': ipval.to_text() for ipval in a_record}
#Fetching the mx records and storing them in the dictionary
mx_record = dns.resolver.resolve(website,'MX')
mx_record_list = list(mx_record)
for i, element in enumerate(mx_record_list):
    dns_record['MX_Record', i+1] = element

#Displaying the record on the screen
for key,value in dns_record.items():
    print(f"{key} = {value}")

