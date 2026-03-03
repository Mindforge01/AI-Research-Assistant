def export_report(history):
    report = ""
    for i, item in enumerate(history):
        report += f"Q{i+1}: {item['question']}\n"
        report += f"A{i+1}: {item['answer']}\n\n"
    return report
