def detect_prompt_injection(text):

    suspicious_patterns = [
        "ignore previous instructions",
        "reveal system prompt",
        "jailbreak",
        "bypass",
        "override"
    ]

    findings = []

    for pattern in suspicious_patterns:
        if pattern.lower() in text.lower():
            findings.append(pattern)

    if len(findings) == 0:
        risk = "Low"
    elif len(findings) <= 2:
        risk = "Medium"
    else:
        risk = "High"

    return risk, findings


sample = input("Enter prompt: ")

risk, findings = detect_prompt_injection(sample)

print("\nRisk Level:", risk)

if findings:
    print("Detected Patterns:")
    for item in findings:
        print("-", item)
else:
    print("No suspicious patterns found.")
