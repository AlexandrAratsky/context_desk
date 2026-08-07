# Context Desk

> Локальный менеджер AI-контекста для разработчиков и AI coding agents.

Context Desk — настольное веб-приложение для централизованного хранения, редактирования и экспорта AI-контекста: Skills, Rules и Prompts.

Проект задуман как единый локальный источник истины для контекста, который используется в разных IDE и AI-плагинах.

## Зачем нужен проект

Разные IDE и AI-плагины хранят инструкции, правила и навыки в разных форматах. Из-за этого один и тот же контекст приходится дублировать, вручную синхронизировать и поддерживать в нескольких местах.

Context Desk решает эту задачу через локальный Context Repository:

- контекст хранится в одном месте;
- файлы остаются человекочитаемыми;
- экспорт в IDE выполняется явно;
- Prompts доступны как библиотека и через MCP;
- приложение не требует облака, регистрации или базы данных.

## Возможности и границы MVP

MVP включает:

- хранение Skills, Rules и Prompts в Markdown-файлах с YAML Frontmatter;
- просмотр и редактирование контекстных объектов через Web UI;
- экспорт Skills и Rules в поддерживаемые IDE;
- dry-run, статус экспорта и удаление ранее экспортированных файлов;
- Prompt Gallery с копированием Prompt'ов;
- встроенный MCP Server для публикации Prompt'ов;
- конфигурацию через `settings.yaml`.

В MVP не входят:

- облачная синхронизация;
- авторизация и совместная работа;
- база данных;
- Git-интеграция;
- история изменений и версионирование;
- двусторонний импорт изменений из IDE;
- полнотекстовый поиск;
- поддержка бинарных файлов;
- MCP Tools и MCP Resources.

## Контекстные объекты и репозиторий

Context Desk работает с тремя типами объектов.

### Skill

Большая специализированная инструкция: процесс разработки, архитектура, доменная экспертиза или рабочий метод.

Skills хранятся в каталоге `skills/` и экспортируются в IDE через Connector'ы.

### Rule

Правило поведения или ограничение для AI-агента.

Rules хранятся в каталоге `rules/` и экспортируются в IDE через Connector'ы.

### Prompt

Шаблон пользовательского запроса.

Prompts хранятся в каталоге `prompts/`, доступны в Prompt Gallery и могут публиковаться через MCP. В файловую структуру IDE они не экспортируются.

Пример структуры Context Repository:

```text
context-repository/
  skills/
    code-review/
      SKILL.md
  rules/
    terse-output.md
  prompts/
    explain-error.md
```

Все файлы должны быть UTF-8 Markdown с YAML Frontmatter.

## Архитектура и экспорт

Приложение построено вокруг локального Context Repository.

```text
Context Repository
        ↓
Web UI / App State
        ↓
File Manager ─ Export Engine ─ Connectors
        ↓              ↓
      Files        IDE targets
```

Основные подсистемы:

- **File Manager** читает, записывает и валидирует Markdown/YAML-файлы;
- **Export Engine** координирует экспорт и ведёт manifest экспортированных файлов;
- **Connectors** преобразуют Skills и Rules в формат конкретной IDE;
- **Prompt Manager** обслуживает Prompt Gallery и MCP-публикацию;
- **MCP Server** публикует валидные Prompt'ы через Model Context Protocol.

В MVP планируются Connector'ы для:

- Zed;
- Kilo Code;
- Explyt.

Экспорт всегда односторонний. IDE считается получателем, но не источником данных.

## MCP и Prompts

Встроенный MCP Server используется только для Prompt'ов.

MVP-поведение:

- публикуются только валидные и включённые Prompt'ы;
- доступны операции списка Prompt'ов и получения конкретного Prompt;
- Skills и Rules через MCP не публикуются;
- MCP не заменяет файловый экспорт для IDE.

## Технологический стек

Планируемый стек MVP:

- Python 3.11+;
- Reflex для Web UI;
- PyYAML для YAML Frontmatter;
- Jinja2 для шаблонов экспорта;
- FastMCP или совместимая MCP-реализация;
- Uvicorn;
- uv;
- just;
- ruff.

## Быстрый старт

Установка зависимостей:

```bash
just install
```

Запуск в режиме разработки:

```bash
just dev
```

Запуск в production-режиме:

```bash
just run
```

Проверка и форматирование:

```bash
just check
just format
just lint
```

## Конфигурация

Основной файл конфигурации — `settings.yaml`.

Он задаёт:

- путь к Context Repository (`source_dir`);
- настройки приложения;
- настройки MCP Server;
- список Connector'ов;
- target-каталоги для экспорта;
- режимы overwrite и форматы экспорта.

Примерная структура:

```yaml
version: 1
source_dir: "~/context-desk"

application:
  language: "ru"
  theme: "system"
  open_browser: true

mcp:
  enabled: true
  transport: "streamable_http"
  host: "127.0.0.1"
  port: 8765
  path: "/mcp"

connectors:
  zed:
    enabled: true
    projects:
      personal:
        target_dir: "~/.config/zed"
  kilo_code:
    enabled: true
  explyt:
    enabled: true
```

## Статус проекта

Проект находится на стадии MVP draft.

Приоритет MVP — простая локальная работа с AI-контекстом без базы данных, облака и сложной синхронизации.
