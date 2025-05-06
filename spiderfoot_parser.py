import csv

def parse_spiderfoot_csv(file_path):
    findings = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            findings.append({
                "type": row.get("Type", ""),
                "value": row.get("Value", ""),
                "description": row.get("Description", ""),
                "risk": row.get("Risk", ""),
                "confidence": row.get("Confidence", ""),
                "comments": row.get("Comments", "")
            })

    return findings

