import whois
sites=["facebook.com"]

companies=[whois.whois(s).org for s in sites]
creation_dtaes=[whois.whois(s).creation_date for s in sites]

print(companies)
print(creation_dtaes)

print(sites[creation_dtaes.index(min(creation_dtaes))])

emails=[whois.whois(s).emails for s in sites]
print(emails)

print(whois.whois("81.19.159.28"))