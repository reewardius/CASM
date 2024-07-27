import json

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

# Чтение JSON из файла
with open("semgrep.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)

# Преобразование JSON в Markdown
markdown_report = json_to_markdown(json_data)

# Сохранение Markdown-отчета в файл
with open("semgrep_report.md", "w", encoding="utf-8") as f:
    f.write(markdown_report)

print("Преобразование завершено. Отчет сохранен в файл semgrep_report.md")
