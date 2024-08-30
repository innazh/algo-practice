def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    bracket_dict = {"(":")", "[":"]", "{":"}"}
    stack = []
    for ch in s:
        if ch == "(" or ch == "[" or ch == "{":
            stack.append(ch)
        else:
            if len(stack)<1:
                return False
            last_bracket=stack.pop()
            print(last_bracket)
            if bracket_dict[last_bracket]!=ch:
                return False

    return len(stack)==0


    # ({)})