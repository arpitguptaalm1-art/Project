# Problem Statement
People often ignore daily micro-decisions such as sleep timing, study consistency, exercise, or screen usage because they seem insignificant in the short term. However, when repeated daily, these small choices compound silently and create a butterfly effect, leading to major long-term outcomes in health, focus, career, and personal growth.
Currently, there is no simple and interactive system that helps individuals:
    Understand how their daily habits affect their future
    Visualize the compounding impact of these decisions
    Align their habits with their long-term dreams and goals

# Proposed Solution
Micro Decision Taker (MDT) is an interactive, butterfly-effect-based decision analysis system that:
    Accepts daily micro-decisions (both positive and negative habits)
    Calculates their long-term impact using frequency and time
    Detects behavioral patterns
    Evaluates alignment with the user’s dream job
    Provides honest, motivating, and corrective advice using reverse psychology
    Visualizes impact through graphs for better understanding
    The system focuses on awareness, habit correction, and future alignment, not prediction.

# Key Features
    Supports Good Habits & Bad Habits
    Butterfly Effect–based impact calculation (Impact × Frequency × Time)
    Graphical visualization of impact (Health, Focus, Career)

# System Architecture
Frontend (HTML, CSS, JavaScript, Chart.js)
        ↓ API Calls (JSON)
Backend (Flask + CORS)
        ↓
Logic Engine
  ├─ Impact Calculator
  ├─ Butterfly Intensity Engine
  ├─ Pattern Detection
  └─ Dream Job Capability Analyzer

# Tech Stack
Frontend:
    HTML5
    CSS3
    JavaScript
    Chart.js (for visualization)
Backend:
    Python
    Flask
    Flask-CORS

# How It Works
User enters their dream job
User selects a positive or negative habit
Inputs:
Frequency (in hours)
Time period (in days)
System:
Calculates micro-level impacts
Applies butterfly effect logic
Evaluates capability towards dream job
Detects behavioral pattern
Output:
Impact graph
Capability percentage
Honest, motivational advice

# Scope & Limitations
  Single-user demo system
  Rule-based logic (no machine learning predictions)
  Educational & awareness-based model
  No medical, psychological, or career guarantees
  No authentication or persistent data storage

# Future Enhancements
  Habit history tracking
  Multi-decision daily simulation
  AI-based habit analysis
PDF report generation
Gamification & streak system
Mobile app version
