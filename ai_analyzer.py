import ast


def detect_language(code):

    if "def " in code or "print(" in code:
        return "Python"
    elif "#include" in code:
        return "C/C++"
    elif "System.out.println" in code:
        return "Java"
    elif "console.log" in code:
        return "JavaScript"
    elif "<-" in code:
        return "R"
    else:
        return "Unknown"


def detect_errors(code):

    try:
        compile(code, "<string>", "exec")
        return None
    except Exception as e:
        return str(e)


def auto_fix(code):

    lines = code.split("\n")
    fixed_lines = []

    for line in lines:

        stripped = line.strip()

        # Fix missing colon in loops
        if stripped.startswith("for ") and not stripped.endswith(":"):
            line = line + ":"

        if stripped.startswith("if ") and not stripped.endswith(":"):
            line = line + ":"

        if stripped.startswith("while ") and not stripped.endswith(":"):
            line = line + ":"

        fixed_lines.append(line)

    return "\n".join(fixed_lines)


def analyze_code(code):

    language = detect_language(code)

    explanation = []
    bugs = []
    complexity = "O(1)"

    error = detect_errors(code)

    corrected_code = None

    if error:

        bugs.append(error)

        corrected_code = auto_fix(code)

    if language == "Python":

        try:
            tree = ast.parse(code)

            loop_count = 0

            for node in ast.walk(tree):

                if isinstance(node, ast.For):
                    explanation.append("A for loop iterates over a sequence.")
                    loop_count += 1

                elif isinstance(node, ast.While):
                    explanation.append("A while loop repeats until a condition becomes false.")
                    loop_count += 1

                elif isinstance(node, ast.FunctionDef):
                    explanation.append(f"A function '{node.name}' is defined.")

                elif isinstance(node, ast.If):
                    explanation.append("Conditional logic is used.")

            if loop_count == 1:
                complexity = "O(n)"

            elif loop_count >= 2:
                complexity = "O(n²)"

        except:
            pass

    if not explanation:
        explanation.append(f"Basic {language} code structure detected.")

    if not bugs:
        bugs.append("No errors detected.")

    return {
        "language": language,
        "explanation": " ".join(explanation),
        "bugs": " ".join(bugs),
        "complexity": complexity,
        "fix": corrected_code
    }