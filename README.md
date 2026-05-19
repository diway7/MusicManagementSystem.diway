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
├── src/
│   ├── __init__.py
│   ├── core.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   └── test_core.py
│
├── main.py
├── README.md
└── requirements.txt
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
graph TD
    %% Strict High-Contrast Styles (Black text on crisp white backgrounds)
    classDef uiStyle fill:#FFFFFF,stroke:#1A5276,stroke-width:2px,color:#000000;
    classDef logicStyle fill:#FFFFFF,stroke:#2471A3,stroke-width:2px,color:#000000;
    classDef storageStyle fill:#FFFFFF,stroke:#6C3483,stroke-width:2px,color:#000000;
    classDef testStyle fill:#FFFFFF,stroke:#117A65,stroke-width:2px,stroke-dasharray: 5 5,color:#000000;
    classDef dbStyle fill:#FFFFFF,stroke:#BA4A00,stroke-width:2px,color:#000000;

    %% Root Level Portals
    UI["USER INTERFACE
    main.py (App Entry Point)"]:::uiStyle

    %% Isolated System Packages (src/ and tests/)
    Logic["BUSINESS LOGIC
    src/core.py (Data Models)"]:::logicStyle

    Storage["DATA STORAGE LAYER
    src/storage.py (JSON Framework)"]:::storageStyle

    Tests["AUTOMATED TESTS
    tests/test_core.py (Unittest)"]:::testStyle

    %% Database Directory (data/)
    JSON[("INDEPENDENT DATABASE
    data/data.json")]:::dbStyle

    %% Explicit Execution Flow & Architecture Constraints
    UI -->|1. Invokes Logic| Logic
    Logic -->|2. Requests Persistence| Storage
    Storage -->|3. Writes to Root Directory| JSON
    Tests -.->|Validates Integrity| Logic
```


### Flowchart
```mermaid
graph TD
    %% High-contrast and simple styles (Black text on white background)
    classDef startStyle fill:#FFFFFF,stroke:#000000,stroke-width:2px,color:#000000;
    classDef processStyle fill:#FFFFFF,stroke:#1A5276,stroke-width:1px,color:#000000;
    classDef conditionStyle fill:#FFFFFF,stroke:#B7950B,stroke-width:2px,color:#000000;

    %% Application flow block definitions
    START([START]):::startStyle
    
    Load["Load System Data
    (StorageManager.load_data)"]:::processStyle
    
    Check{"Is User
    Logged In?"}:::conditionStyle
    
    MenuGuest["SHOW GUEST MENU
    - Register
    - Login
    - Exit"]:::processStyle
    
    MenuUser["SHOW USER DASHBOARD
    - Search Content
    - Create Playlist
    - Stream Playlists
    - Logout"]:::processStyle

    %% Logical paths and routing execution
    START --> Load
    Load --> Check
    
    Check -->|NO| MenuGuest
    Check -->|YES| MenuUser
    
    %% Infinite loop mechanics (return to session state check)
    MenuGuest -.->|Loop| Check
    MenuUser -.->|Loop| Check