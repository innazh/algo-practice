import heapq

# O(n + m log k) where n is the data size, m is the num of unique email receivers, and
# k is the output size
def top_k_email_receivers(emails, k):
    email_count = {}
    for email in emails:
        to_person = email["toPerson"]
        if to_person in email_count:
            email_count[to_person]+=1
        else:
            email_count[to_person] = 1
    
    return heapq.nlargest(k, email_count.items(), key=lambda x: x[1]) # x[1]

# Alternative to using a heap:
# items = list(email_count.items())
# items.sort(key=lambda x: x[1], reverse=True)
# top_k = items[:k]

def top_k_unique_email_receivers(emails, k):
    uniqueEmailCount = {}

    for email in emails:
        toPerson = email['toPerson']
        message = email['message']

        if toPerson not in uniqueEmailCount:
            uniqueEmailCount[toPerson] = set()
        
        uniqueEmailCount[toPerson].add(message)

    uniqueCount = {}
    for person, messages in uniqueEmailCount.items():
        uniqueCount[person] = len(messages)
    
    return heapq.nlargest(k, uniqueCount.items(), key=lambda x: x[1])

def main():
    emails = [
    {"fromPerson": "Alice", "toPerson": "Bob", "message": "Hello"},
    {"fromPerson": "Charlie", "toPerson": "Bob", "message": "Hello"},
    {"fromPerson": "Alice", "toPerson": "Bob", "message": "Hello"},  # duplicate
    {"fromPerson": "Alice", "toPerson": "David", "message": "Hey"},
    {"fromPerson": "Charlie", "toPerson": "David", "message": "Hey"},
    {"fromPerson": "Charlie", "toPerson": "David", "message": "Hey1"},
]
    e = top_k_unique_email_receivers(emails,2)
    print(e)

if __name__=="__main__":
    main()