# OSINT Challenges Platform Documentation

## Overview
The OSINT Challenges platform is a Jekyll-based web application designed to provide interactive Open Source Intelligence (OSINT) challenges. The platform features a modern, responsive design with a focus on user experience and clean aesthetics.

## Theme Design

### Color Scheme
- Primary Color: `#2563eb` (Blue)
- Secondary Color: `#3b82f6` (Lighter Blue)
- Accent Color: `#60a5fa` (Light Blue)
- Background: `#ffffff` (White)
- Text Color: `#1f2937` (Dark Gray)
- Border Color: `#e5e7eb` (Light Gray)
- Success Color: `#10b981` (Green)
- Error Color: `#ef4444` (Red)

### Typography
- Primary Font: 'Inter', sans-serif
- Font Sizes:
  - Large Headers: 2.5rem
  - Section Headers: 1.875rem
  - Subsection Headers: 1.5rem
  - Body Text: 1rem
  - Small Text: 0.875rem

### Components
1. Cards
   - Rounded corners (12px)
   - Soft shadows
   - Hover animations
   - White background

2. Buttons
   - Primary: Blue background with white text
   - Secondary: Transparent with blue text
   - Hover effects with scale and color changes

3. Status Indicators
   - Difficulty badges (Easy: Green, Medium: Yellow, Hard: Red)
   - Category tags (Light blue)
   - Points display

## Core Functionality

### Challenge System
1. Challenge Listing (`challenges.html`)
   - Grid layout of challenge cards
   - Filtering by difficulty and category
   - Dynamic hiding of completed challenges
   - Animated transitions

2. Challenge Page (`_layouts/challenge.html`)
   - Task progression tracking
   - Timer functionality
   - Input validation
   - Hint system
   - Completion tracking

3. Completion System (`_layouts/completion.html`)
   - Dynamic completion UI
   - Statistics display
   - Solution reveals
   - Navigation options

### JavaScript Functions

#### Core Functions
1. `initializeChallenge()`
   - Starts challenge timer
   - Sets up input handlers
   - Initializes task tracking

2. `checkAnswer(button)`
   - Validates user input
   - Provides feedback
   - Handles completion animations
   - Updates progress

3. `showCompletionUI()`
   - Displays completion screen
   - Shows statistics
   - Reveals solutions
   - Provides navigation options

4. `updateTimer()`
   - Updates challenge timer display
   - Formats time in MM:SS format

#### Helper Functions
1. `addConfettiEffect(element)`
   - Adds celebration animation
   - Temporary visual feedback

2. `toggleHint(button)`
   - Shows/hides hint content
   - Updates button text

3. `hideCompletedChallenges()`
   - Filters completed challenges
   - Updates challenge grid

### Local Storage
- Stores completed challenges
- Persists user progress
- Manages challenge state

## Best Practices
1. Challenge Creation
   - Clear task descriptions
   - Progressive difficulty
   - Helpful hints
   - Accurate answer validation

2. UI/UX Guidelines
   - Consistent spacing
   - Clear feedback
   - Responsive design
   - Accessible colors

3. Performance
   - Minimal dependencies
   - Optimized assets
   - Efficient DOM updates
   - Local storage usage
