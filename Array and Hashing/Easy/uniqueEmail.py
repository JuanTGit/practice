# 929. Unique Email Addresses
# Easy

# Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, 
# the email may contain one or more '.' or '+'.

# For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
# If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to 
# the same address without dots in the local name. Note that this rule does not apply to domain names.

# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. 
# Note that this rule does not apply to domain names.

# For example, "m.y+name@email.com" will be forwarded to "my@email.com".
# It is possible to use both of these rules at the same time.

# Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

# Example 1:
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

# Example 2:
# Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
# Output: 3

def numUniqueEmails(emails):
    parsed_emails = set()
    for email in emails:
        local_name, domain_name = email.split('@')
        local_name = local_name.split('+')[0]
        local_name = local_name.replace('.', '')
        email = local_name + '@' + domain_name
        parsed_emails.add(email)
    return len(parsed_emails)

print(numUniqueEmails(emails))

def uniqueEmails(emails):
    unique = set()

    for e in emails:
        i, local = 0, ''
        while e[i] != '@' or e[i] != '+':
            if e[i] != '.':
                local += e[i]
            i += 1
        
        while e[i] != '@':
            i += 1
        domain = e[i + 1:]
        unique.add((local, domain))
    return len(unique)