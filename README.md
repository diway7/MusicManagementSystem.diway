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
```


### Architecture Diagram
```mermaid
graph LR
    %% Контрастные и строгие стили (Темный текст на светлом фоне)
    classDef uiStyle fill:#FFFFFF,stroke:#1A5276,stroke-width:2px,color:#1A5276;
    classDef logicStyle fill:#FFFFFF,stroke:#1F618D,stroke-width:2px,color:#1F618D;
    classDef storageStyle fill:#FFFFFF,stroke:#6C3483,stroke-width:2px,color:#6C3483;
    classDef testStyle fill:#FFFFFF,stroke:#117A65,stroke-width:2px,stroke-dasharray: 5 5,color:#117A65;
    classDef dbStyle fill:#FDFEFE,stroke:#BA4A00,stroke-width:2px,color:#BA4A00;

    %% Узлы с принудительным переносом строк через ковычки
    UI["USER INTERFACE
    main.py (Console Menu)"]:::uiStyle

    Logic["BUSINESS LOGIC
    src/core.py (Data Models)"]:::logicStyle

    Storage["DATA STORAGE
    src/storage.py (JSON Layer)"]:::storageStyle

    Tests["AUTOMATED TESTS
    tests/test_core.py"]:::testStyle

    JSON[("LOCAL DATABASE
    data/data.json")]:::dbStyle

    %% Пути движения данных
    UI -->|Calls methods| Logic
    Logic -->|Saves & Loads data| Storage
    Storage -->|Reads & Writes| JSON
    Tests -.->|Validates behavior| Logic