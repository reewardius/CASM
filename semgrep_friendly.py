import json
import argparse

def json_to_markdown(json_data):
    markdown = "# Отчет об уязвимостях\n\n"
    error_number = 1
    
    severity_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]
    sorted_results = sorted(json_data["results"], key=lambda x: severity_order.index(x["extra"]["metadata"]["confidence"]))

    for result in sorted_results:
        markdown += f"## Уязвимость №{error_number}\n"
        markdown += f"- **Сообщение:** {result['extra']['message']}\n"
        markdown += f"- **Критичность:** {result['extra']['metadata']['confidence']}\n"
        markdown += f"- **CWE:** {', '.join(result['extra']['metadata']['cwe'])}\n"
        markdown += f"- **Путь:** {result['path']}\n"
        markdown += f"- **Код:**\n```\n{result['extra']['lines']}\n```\n"
        markdown += f"- **Начало:** строка {result['start']['line']}\n"
        markdown += f"- **Конец:** строка {result['end']['line']}\n"
        markdown += "\n"
        error_number += 1

    return markdown

def main():
    parser = argparse.ArgumentParser(description="Преобразование JSON отчета Semgrep в Markdown")
    parser.add_argument("-f", "--file", required=True, help="Путь к входному JSON файлу")
    parser.add_argument("-o", "--output_file", default="semgrep_report.md", help="Путь к выходному Markdown файлу")
    
    args = parser.parse_args()
    
    with open(args.file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    markdown_report = json_to_markdown(json_data)

    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)

    print(f"Преобразование завершено. Отчет сохранен в файл {args.output_file}")

if __name__ == "__main__":
    main()
