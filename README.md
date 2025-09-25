# virtual pet game

The Virtual Pet Game allows users to adopt and care for a virtual pet. Players can feed it, play with it, clean it, and monitor its happiness and health. The goal is to keep the pet alive, healthy, and happy over time.

## Features
Adopt a Pet: User can choose a pet name and type (dog, cat, etc.).

Feed Pet:Increase hunger or health stats.

Play with Pet:Increase happiness, decrease energy.

Clean Pet:Maintain hygiene stats.

Check Status:Display health, hunger, happiness, and energy.

Pet Aging & Health Decay:Stats decrease over time or after actions.

Pet can “run away” or “fall sick” if neglected.

Optional Enhancements:Save pet state to a file so it persists.

## project structure

    virtual pet game/
    |
    |---src/            # core application logic
    |    |---logic.py   #Business logic and task
    |    |__db.py       #database operations
    |
    |----api/           #Backend API
    |    |__main.py     #FASTAPI endpoints
    |
    |----frontend/      #frontend application
    |     |__app.py     #streamlit web interface
    |
    |____requirements.txt # python Dependencies
    |
    |____README.md        #project documentation
    |
    |____.env       # python variables

## Quick start

### prerequisites

- python 3.8 or higher
-A supabase account
-Git(push,cloning)

### 1. clone or Doumload the project 
# option 1: clone with Git
git clone<repository-url>

# option 2: Download and extract the zip file

### 2.Install Dependencies 

# Install all required python packages  
pip install -r requirements.txt

### 3.set up Supabase Database

1.Create the supabase project :

2.create the Tasks Table:

-Go to SQL editor in supabase dashboard

-Run this SQL command:

```
CREATE TABLE pets (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(20) NOT NULL,
    hunger INTEGER DEFAULT 50 CHECK (hunger BETWEEN 0 AND 100),
    happiness INTEGER DEFAULT 50 CHECK (happiness BETWEEN 0 AND 100),
    energy INTEGER DEFAULT 50 CHECK (energy BETWEEN 0 AND 100),
    cleanliness INTEGER DEFAULT 50 CHECK (cleanliness BETWEEN 0 AND 100),
    age INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```
3. **Get your credentials:

### 4. configure Environment variables 

1. Create a `.env` file in the project root

2. Add your supabase credentials to `.env`:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here

**EXAMPLE:**
SUPABASE_URL="https://ehplczppjftucgitgqtf.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVocGxjenBwamZ0dWNnaXRncXRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg2OTk0ODgsImV4cCI6MjA3NDI3NTQ4OH0.0iFRD78krNvm7w5bED0SqfAT702xhSj5YvNBkyuvqq0"

### 5.Run the Apllication

## streamline frontend
streamlit run frontend/app.py

The app will open in your browser at `hhtp://localhost:8501`

## FastAPI backend

cd API
python main.py
The API will be available at `http://localhost:8000`

## How to use 

## Technical Details

Project Type: Console-based / GUI Python game
Programming Paradigm: Object-Oriented Programming (OOP)
Persistence: Optional JSON / Database (Supabase / SQLite)
Logic:
Pet stats (hunger, energy, happiness, cleanliness) change over time and with actions.
Stats are bounded between 0–100.
Player interactions affect the pet’s well-being.

### Technological used

**Frontend**: Streamlit (Python web framework)
**Backend**: FastAPI (Python REST API framework)
**Database**: Supabase (PostgreSQL-based backend-as-a-service)
**Language**: Python 3.8+

### Key Components

1. **`src/db.py`**: Database operations
    -Handles all CRUD operations with Supabase

2. **`src/logic.py`**: Business logic
    -Task validation and processing

## Troubleshooting

## Common Issues

## Future Enhancement

**Multiple Pets Support**:Allow users to adopt and manage more than one pet at a time.
ach pet would have separate stats and actions.

**Persistent Storage & Cloud Sync**:Save pet data in JSON, SQLite, or Supabase.
Allow users to continue where they left off, even after closing the game.

**Graphical User Interface (GUI)**:Add a Tkinter, PyQt, or Pygame interface.
Include images, progress bars for stats, and interactive buttons.

**Pet Aging & Levels**:Implement pet growth stages (baby → adult → senior).
Add levels or experience points to unlock new actions, toys, or environments.

**Random Events & Challenges**:Randomly trigger events like sickness, gifts, or mini-games.
Encourage users to actively care for their pets.

**Notifications & Reminders**:Send reminders for feeding, playing, or cleaning.

**Social Features**:Users can visit friends’ pets or compare pet stats.

**Expanded Food & Toys System**:Add a variety of food items and toys affecting stats differently.Introduce strategies to maximize pet happiness and health.

**Mobile / Web Version**:Convert the game into a mobile app (Kivy / React Native) or web app (Flask / Django).

**AI-Based Pet Behavior**:Implement smarter pet behavior based on stats and past interactions.Pets can develop preferences, moods, or unique personalities.

## Support

If you encounter any issues or have questions please contact:
**mandalachandrakanthreddy694@gmail.com**