# Government Service Query Classifier

An automaton-based chatbot that classifies Sri Lankan government service queries using a Deterministic Finite Automaton (DFA). Supports English, Sinhala, and Tamil languages.

## Automata Theory Assignment

This project demonstrates the practical application of automata theory to solve a nationally relevant problem in Sri Lanka - classifying citizen queries about government services.

## DFA Design

### Formal Definition

| Component | Definition |
|-----------|------------|
| **Alphabet (Σ)** | Keywords in English, Sinhala, Tamil |
| **States (Q)** | {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q_reject} |
| **Start State (q₀)** | q0 |
| **Accepting States (F)** | {q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12} |
| **Transition Function (δ)** | Keyword-based state transitions |

### State Diagram

```
                              ┌─────────┐
                              │   q0    │ (START)
                              └────┬────┘
                                   │
         ┌──────────┬──────────┬───┴───┬──────────┬──────────┐
         ▼          ▼          ▼       ▼          ▼          ▼
    ┌─────────┐┌─────────┐┌─────────┐     ┌─────────┐┌─────────┐
    │   q1    ││   q2    ││   q3    │ ... │  q12    ││q_reject │
    │   NIC   ││PASSPORT ││  BIRTH  │     │ HEALTH  ││ REJECT  │
    │ ACCEPT  ││ ACCEPT  ││ ACCEPT  │     │ ACCEPT  ││ REJECT  │
    └─────────┘└─────────┘└─────────┘     └─────────┘└─────────┘
```

### Government Services (Accepting States)

| State | Service | Sinhala | Tamil |
|-------|---------|---------|-------|
| q1 | NIC Services | ජාතික හැඳුනුම්පත් | தேசிய அடையாள அட்டை |
| q2 | Passport | ගමන් බලපත්‍රය | கடவுச்சீட்டு |
| q3 | Birth Certificate | උප්පැන්න සහතිකය | பிறப்புச் சான்றிதழ் |
| q4 | Death Certificate | මරණ සහතිකය | இறப்புச் சான்றிதழ் |
| q5 | Marriage Certificate | විවාහ සහතිකය | திருமணச் சான்றிதழ் |
| q6 | Driving License | රියදුරු බලපත්‍රය | ஓட்டுநர் உரிமம் |
| q7 | Vehicle Registration | වාහන ලියාපදිංචිය | வாகன பதிவு |
| q8 | Tax Services | බදු සේවා | வரி சேவைகள் |
| q9 | Pension | විශ්‍රාම වැටුප් | ஓய்வூதியம் |
| q10 | Samurdhi/Welfare | සමෘද්ධි | சமுர்தி |
| q11 | Education | අධ්‍යාපනය | கல்வி |
| q12 | Health Services | සෞඛ්‍ය සේවා | சுகாதார சேவைகள் |

## Project Structure

```
Automata/
├── app.py                    # Flask backend server
├── automaton.py              # DFA implementation (pure Python)
├── test_automaton.py         # Test cases for all languages
├── requirements.txt          # Python dependencies
├── templates/
│   └── index.html            # Chat interface
└── static/
    ├── css/
    │   └── style.css         # Sri Lankan theme styling
    └── js/
        └── app.js            # Frontend logic
```

## Installation

1. **Clone or download the project**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   ```
   http://127.0.0.1:5000
   ```

## Usage

### Web Interface
- Type queries in English, Sinhala, or Tamil
- Use quick action buttons for common services
- View DFA state transitions in real-time
- See ACCEPT/REJECT classification results

### Example Queries

**English:**
- "How to apply for NIC?"
- "Passport renewal process"
- "Birth certificate application"

**Sinhala:**
- "හැඳුනුම්පත ගන්න ඕනේ"
- "ගමන් බලපත්‍රය අලුත් කරන්න"
- "උප්පැන්න සහතිකය"

**Tamil:**
- "அடையாள அட்டை வேண்டும்"
- "கடவுச்சீட்டு புதுப்பித்தல்"
- "பிறப்புச் சான்றிதழ்"

## Running Tests

```bash
python test_automaton.py
```

Test results show ACCEPT/REJECT outcomes for 71 test cases across all three languages.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/api/classify` | POST | Classify a query |
| `/api/services` | GET | List all services |
| `/api/diagram` | GET | Get DFA diagram |
| `/api/greet` | POST | Handle greetings |

### Classify Query Example

```bash
curl -X POST http://127.0.0.1:5000/api/classify \
  -H "Content-Type: application/json" \
  -d '{"query": "NIC application", "language": "en"}'
```

Response:
```json
{
  "query": "NIC application",
  "state": "q1",
  "state_name": "NIC_SERVICES",
  "is_accepted": true,
  "status": "ACCEPT",
  "transition": "δ(q0, 'nic') → q1",
  "service": {
    "name": "NIC Services",
    "description": "National Identity Card application...",
    "office": "Department of Registration of Persons",
    "website": "www.drp.gov.lk"
  }
}
```

## Technologies Used

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Automaton:** Pure Python DFA implementation
- **Styling:** Custom CSS with Sri Lankan government theme

## Features

- Pure Python DFA implementation (no external automaton libraries)
- Trilingual support (English, Sinhala, Tamil)
- Real-time DFA state visualization
- ACCEPT/REJECT classification display
- Government office information and required documents
- Responsive design for mobile and desktop

## License

This project is created for educational purposes as part of an Automata Theory assignment.
