# Melodix: My Personal Music Vault 

---

### Welcome to Melodix!
 it's a digital home for my favorite tracks and cozy podcasts. I wanted to build something that feels as organized and pretty as a well-curated playlist.

### Key Features (System Architecture)
* **`Content` (Base Class):** The foundation for all tracks, supporting **Polymorphism**.
* **`Song` & `Podcast`:** Specialized classes inheriting from Content (**Inheritance**).
* **`Artist`:** Manages creators and their work (**Association**).
* **`Playlist`:** A collection of tracks that can be calculated and managed (**Aggregation**).
* **`User`:** Each user uniquely owns their personal playlists (**Composition**).
* **`MusicManager`:** The brain of the system, handling search and logic.

## Development Roadmap
| Week | Focus Area |
| :--- | :--- |
| **Week 1** | **Architecture:** Implementing base classes and complex relationships. |
| **Week 2** | **User Logic:** Building the User and Playlist interaction system. |
| **Week 3** | **Persistence:** Integrating JSON file handling for data storage. |
| **Week 4** | **Final Polish:** Decorators for logging and Search functionality. |

---

### Project Structure

```text
MusicManagementSystem/
│
├── data/
│   └── data.json
│
├── src/
│   ├── __init__.py
│   ├── core.py
│   └── storage.py
│
├── tests/
│   ├── __init__.py
│   └── test_core.py
│
├── main.py
├── .gitignore
└── README.md

---
```


### Entity Relationship Diagram
```mermaid
classDiagram
    class User {
        -str username
        -str password
    }
    class Playlist {
        -str name
        -list content_items
    }
    class Content {
        -str title
        -Artist artist
        -float duration
        +get_details() str
    }
    class Song {
        -str album
        -str genre
        +get_details() str
    }
    class Podcast {
        -int episode_number
        -str guest
        +get_details() str
    }
    class Artist {
        -str name
        -str bio
        -list track_list
    }

    User "1" --> "*" Playlist : owns
    Playlist "*" --> "*" Content : contains
    Content <|-- Song : Inheritance
    Content <|-- Podcast : Inheritance
    Content "*" --> "1" Artist : by
---
```

### Architecture Diagram
```mermaid
graph TD
    %% Определение стилей блоков
    classDef uiStyle fill:#f9f,stroke:#333,stroke-width:2px;
    classDef logicStyle fill:#bbf,stroke:#333,stroke-width:2px;
    classDef storageStyle fill:#fbf,stroke:#333,stroke-width:2px;
    classDef testStyle fill:#fff,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5;
    classDef dbStyle fill:#f96,stroke:#333,stroke-width:2px;

    %% Узлы архитектуры
    UI["<b>USER INTERFACE</b><br>main.py (Console Menu, Inputs & Outputs)"]:::uiStyle
    Logic["<b>BUSINESS LOGIC</b><br>src/core.py (MusicManager, User, Song, Playlist)"]:::logicStyle
    Storage["<b>DATA STORAGE</b><br>src/storage.py (JSON Framework)"]:::storageStyle
    Tests["<b>AUTOMATED TESTS</b><br>tests/test_core.py (Unittest Framework)"]:::testStyle
    JSON[("<b>LOCAL DATABASE</b><br>data/data.json")]:::dbStyle

    %% Связи между слоями
    UI -->|Calls methods| Logic
    Logic -->|Uses for save/load| Storage
    Logic -.->|Validates behavior| Tests
    Storage -->|Writes/Reads disk| JSON
---
```

### Flowchart
```mermaid
graph TD
    %% Настройка стилей для различных блоков
    classDef startEnd fill:#f9f,stroke:#333,stroke-width:2px;
    classDef process fill:#bbf,stroke:#333,stroke-width:1px;
    classDef condition fill:#ffb,stroke:#333,stroke-width:2px;
    classDef menuStyle fill:#fff,stroke:#333,stroke-width:1px;

    %% Описание узлов (блоков)
    START([START]):::startEnd
    Load["Загрузка data.json<br>(StorageManager.load_data)"]:::process
    Check{"Пользователь<br>в системе?"}:::condition
    
    MenuGuest["<b>Показать Гостевое Меню:</b><br>1. Register (Регистрация)<br>2. Login (Вход)<br>3. Exit (Выход)"]:::menuStyle
    MenuUser["<b>Показать Меню Пользователя:</b><br>1. Search content (Поиск)<br>2. Create Playlist (Создать плейлист)<br>3. View & Stream Playlists (Стриминг)<br>4. Logout (Выход из аккаунта)"]:::menuStyle

    %% Логические связи и стрелки
    START --> Load
    Load --> Check
    
    Check -->|НЕТ| MenuGuest
    Check -->|ДА| MenuUser
    
    %% Цикличность меню (возврат к проверке после действий)
    MenuGuest -.->|После выбора действия| Check
    MenuUser -.->|После выбора действия| Check