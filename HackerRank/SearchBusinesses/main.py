# Time complexity is O(n * k) where n is the input size and k is the number of words in a single string
# Space complexity is O(n + k) where n is the result array which is of input size in the worst case scenario, 
# and k is the len of indices array
def search_businesses(businesses, search_term):
    search_term = search_term.lower()
    result = []

    for b in businesses:
        b_lower = b.lower()

        if b_lower.startswith(search_term):
            result.append(b)
            continue

        indices = []
        for i in range(1,len(b_lower)):
            if b_lower[i-1]==' ':
                indices.append(i)
        
        for start in indices:
            if b_lower[start:].startswith(search_term):
                result.append(b)
                break

    return result

def main():
    businesses = ["burger king", "McDonald's", "super duper burger's", "subway", "pizza hut"]
    search_term = "duper bur"

    print(search_businesses(businesses, search_term))

if __name__=="__main__":
    main()