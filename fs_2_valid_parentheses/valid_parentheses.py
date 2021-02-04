def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # offset = 0
    # for p in parens:
    #     if p == "(":
    #         offset += 1
    #     if p == ")":
    #         offset -= 1
    # return True if offset == 0 else False

    num_of_opens = 0
    for p in parens:
        if p == "(":
            num_of_opens += 1
        if p == ")":
            num_of_opens -= 1
        if num_of_opens < 0:
            return False
    return True if num_of_opens == 0 else False