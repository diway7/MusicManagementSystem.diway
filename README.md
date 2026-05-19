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
    %% Layer Styles Definition (Hex Colors)
    classDef uiStyle fill:#EBF5FB,stroke:#2980B9,stroke-width:2px;
    classDef logicStyle fill:#EAF2F8,stroke:#2471A3,stroke-width:2px;
    classDef storageStyle fill:#F4ECF7,stroke:#7D3C98,stroke-width:2px;
    classDef testStyle fill:#E8F8F5,stroke:#117A65,stroke-width:2px,stroke-dasharray: 5 5;
    classDef dbStyle fill:#FEF9E7,stroke:#D35400,stroke-width:2px;

    %% Architectural Layer Nodes
    UI[" <b>USER INTERFACE</b><br>main.py (Console Menu)"]:::uiStyle
    Logic[" <b>BUSINESS LOGIC</b><br>src/core.py (Data Models)"]:::logicStyle
    Storage[" <b>DATA STORAGE</b><br>src/storage.py (JSON Layer)"]:::storageStyle
    Tests[" <b>AUTOMATED TESTS</b><br>tests/test_core.py"]:::testStyle
    JSON[("<b>LOCAL DATABASE</b><br>data/data.json")]:::dbStyle

    %% Relationships and Data Flow
    UI -->|Calls methods| Logic
    Logic -->|Saves & Loads data| Storage
    Storage -->|Reads & Writes| JSON
    Tests -.->|Validates behavior| Logic
