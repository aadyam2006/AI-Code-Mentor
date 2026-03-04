def answer_question(code, question):

    question = question.lower()

    if "what does this code do" in question:
        return "This code executes the operations defined in the program such as loops, conditions, or functions."

    if "complexity" in question:
        if "for" in code or "while" in code:
            return "The code likely has O(n) time complexity due to loops."
        return "The code likely has constant O(1) complexity."

    if "optimize" in question:
        if code.count("for") > 1:
            return "Nested loops detected. Consider using a more efficient algorithm."
        return "The code already looks reasonably efficient."

    if "bug" in question:
        return "Check syntax, indentation, and variable usage."

    return "Try asking: What does this code do? What is the complexity? How to optimize it?"