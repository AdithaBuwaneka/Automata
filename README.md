# Government Service Query Classifier

An automaton-based chatbot that classifies Sri Lankan government service queries using a Deterministic Finite Automaton (DFA). Supports English, Sinhala, and Tamil languages.

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/AdithaBuwaneka/Automata.git
cd Automata
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

### 4. Open in Browser
```
http://127.0.0.1:5000
```

---

## Automata Theory Assignment

This project demonstrates the practical application of automata theory to solve a nationally relevant problem in Sri Lanka - classifying citizen queries about government services.

---

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

---

## Project Structure

```
Automata/
├── app.py                    # Flask backend server
├── automaton.py              # DFA implementation (pure Python)
├── test_automaton.py         # Test cases for all languages
├── requirements.txt          # Python dependencies
├── README.md                 # Documentation
├── .gitignore                # Git ignore rules
├── templates/
│   └── index.html            # Chat interface
└── static/
    ├── css/
    │   └── style.css         # Sri Lankan theme styling
    └── js/
        └── app.js            # Frontend logic
```

---

## How to Use

### Web Interface

1. Open http://127.0.0.1:5000 in your browser
2. Select your language (English / Sinhala / Tamil)
3. Type your query or click quick action buttons
4. View the DFA state transition and classification result

### Example Queries

**English:**
```
How to apply for NIC?
Passport renewal process
Birth certificate application
Driving license renewal
```

**Sinhala (සිංහල):**
```
හැඳුනුම්පත ගන්න ඕනේ
ගමන් බලපත්‍රය අලුත් කරන්න
උප්පැන්න සහතිකය
රියදුරු බලපත්‍රය
```

**Tamil (தமிழ்):**
```
அடையாள அட்டை வேண்டும்
கடவுச்சீட்டு புதுப்பித்தல்
பிறப்புச் சான்றிதழ்
ஓட்டுநர் உரிமம்
```

---

## Running Tests

Run the test suite to verify DFA functionality:

```bash
python test_automaton.py
```

**Expected Output:**
- 71 test cases across English, Sinhala, and Tamil
- 67 ACCEPT outcomes (correctly classified)
- 4 REJECT outcomes (unrelated queries)

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chat interface |
| `/api/classify` | POST | Classify a query |
| `/api/services` | GET | List all services |
| `/api/diagram` | GET | Get DFA diagram |
| `/api/greet` | POST | Handle greetings |

### Example API Call

**Request:**
```bash
curl -X POST http://127.0.0.1:5000/api/classify \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"NIC application\", \"language\": \"en\"}"
```

**Response:**
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
    "office": "Department of Registration of Persons",
    "website": "www.drp.gov.lk"
  }
}
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Backend logic |
| Flask | Web framework |
| HTML5/CSS3 | Frontend interface |
| JavaScript | Client-side logic |
| Pure Python DFA | Automaton implementation |

---

## Features

- **Pure Python DFA** - No external automaton libraries
- **Trilingual Support** - English, Sinhala, Tamil
- **Real-time Visualization** - Live DFA state updates
- **ACCEPT/REJECT Display** - Clear classification status
- **Service Information** - Office details, required documents, websites
- **Responsive Design** - Works on desktop and mobile

---

## Assignment Checklist

- [x] Problem Definition with national relevance
- [x] Automata Design (DFA with 14 states)
- [x] State Diagram with transitions
- [x] Python Implementation (Pure Python + Flask)
- [x] ACCEPT/REJECT outcomes
- [x] Trilingual support (EN/SI/TA)
- [x] Test cases (71 tests)
- [x] Web interface demonstration

---

## License

This project is created for educational purposes as part of an Automata Theory assignment.
