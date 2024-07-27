import json
import argparse

def json_to_markdown(json_data):
    markdown = "# Отчет об ошибках\n\n"
    error_number = 1
    
    for result in json_data["results"]:
        markdown += f"## Ошибка {error_number}\n"
        markdown += f"- **Сообщение:** {result['extra']['message']}\n"
        markdown += f"- **Категория:** {result['extra']['metadata']['category']}\n"
        markdown += f"- **Уверенность:** {result['extra']['metadata']['confidence']}\n"
        markdown += f"- **CWE:** {', '.join(result['extra']['metadata']['cwe'])}\n"
        markdown += f"- **Тип движка:** {result['extra']['engine_kind']}\n"
        markdown += f"- **Путь:** {result['path']}\n"
        markdown += f"- **Линии:**\n```\n{result['extra']['lines']}\n```\n"
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
    
    # Чтение JSON из файла
    with open(args.file, "r", encoding="utf-8") as f:
        json_data = json.load(f)

    # Преобразование JSON в Markdown
    markdown_report = json_to_markdown(json_data)

    # Сохранение Markdown-отчета в файл
    with open(args.output_file, "w", encoding="utf-8") as f:
        f.write(markdown_report)

    print(f"Преобразование завершено. Отчет сохранен в файл {args.output_file}")

if __name__ == "__main__":
    main()
