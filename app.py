"""
Government Service Query Classifier - Flask Backend
====================================================
Flask application serving the automaton-based chatbot.
"""

from flask import Flask, render_template, request, jsonify
from automaton import GovernmentServiceDFA

app = Flask(__name__)

# Initialize the DFA
dfa = GovernmentServiceDFA()


@app.route('/')
def index():
    """Render the main chatbot interface."""
    return render_template('index.html')


@app.route('/api/classify', methods=['POST'])
def classify_query():
    """
    API endpoint to classify user queries.

    Request JSON:
        {
            "query": "user input text",
            "language": "en" | "si" | "ta"
        }

    Response JSON:
        {
            "query": "original query",
            "state": "q1",
            "state_name": "NIC_SERVICES",
            "is_accepted": true,
            "status": "ACCEPT" | "REJECT",
            "matched_keyword": "nic",
            "transition": "δ(q0, 'nic') → q1",
            "service": { ... } | "message": "..."
        }
    """
    data = request.get_json()

    if not data or 'query' not in data:
        return jsonify({
            'error': 'Missing query parameter',
            'status': 'REJECT'
        }), 400

    query = data.get('query', '').strip()
    language = data.get('language', 'en')

    if not query:
        return jsonify({
            'error': 'Empty query',
            'status': 'REJECT'
        }), 400

    # Process query through DFA
    result = dfa.process_query(query, language)

    return jsonify(result)


@app.route('/api/services', methods=['GET'])
def get_services():
    """
    Get list of all available government services.

    Query params:
        language: "en" | "si" | "ta" (default: "en")

    Response JSON:
        {
            "services": [
                {"state": "q1", "name": "NIC Services", "keywords_en": ["nic", "identity"]}
            ]
        }
    """
    language = request.args.get('language', 'en')
    services = dfa.get_all_services(language)
    return jsonify({'services': services})


@app.route('/api/diagram', methods=['GET'])
def get_diagram():
    """Get the DFA state diagram."""
    return jsonify({
        'diagram': dfa.get_state_diagram(),
        'formal_definition': dfa.get_formal_definition()
    })


@app.route('/api/states', methods=['GET'])
def get_states():
    """Get all DFA states and their descriptions."""
    return jsonify({
        'states': dfa.states,
        'accepting_states': list(dfa.accepting_states),
        'start_state': dfa.start_state
    })


# Greeting responses in all languages
GREETINGS = {
    'en': {
        'keywords': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
        'response': "Hello! Welcome to the Sri Lankan Government Service Classifier. I can help you find information about government services. Try asking about: NIC, Passport, Birth Certificate, Driving License, Tax, Pension, Education, Health, etc."
    },
    'si': {
        'keywords': ['ආයුබෝවන්', 'හලෝ', 'සුභ උදෑසනක්', 'සුභ දවසක්'],
        'response': "ආයුබෝවන්! ශ්‍රී ලංකා රජයේ සේවා වර්ගීකරණයට සාදරයෙන් පිළිගනිමු. මට ඔබට රජයේ සේවා පිළිබඳ තොරතුරු සොයා ගැනීමට උදවු කළ හැකිය. හැඳුනුම්පත, ගමන් බලපත්‍රය, උප්පැන්න සහතිකය, රියදුරු බලපත්‍රය ආදිය ගැන අසන්න."
    },
    'ta': {
        'keywords': ['வணக்கம்', 'ஹலோ', 'காலை வணக்கம்'],
        'response': "வணக்கம்! இலங்கை அரசாங்க சேவை வகைப்படுத்திக்கு வரவேற்கிறோம். அரசாங்க சேவைகள் பற்றிய தகவல்களைக் கண்டறிய நான் உங்களுக்கு உதவ முடியும். அடையாள அட்டை, கடவுச்சீட்டு, பிறப்புச் சான்றிதழ் பற்றி கேளுங்கள்."
    }
}


@app.route('/api/greet', methods=['POST'])
def handle_greeting():
    """Handle greeting messages."""
    data = request.get_json()
    query = data.get('query', '').lower().strip()
    language = data.get('language', 'en')

    # Check if it's a greeting (whole word match only)
    query_words = query.split()
    for lang, greet_data in GREETINGS.items():
        for keyword in greet_data['keywords']:
            # Check if query equals keyword or keyword is a separate word in query
            if query == keyword or keyword in query_words:
                return jsonify({
                    'is_greeting': True,
                    'response': GREETINGS[language]['response'],
                    'status': 'GREETING'
                })

    return jsonify({'is_greeting': False})


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Government Service Query Classifier - Chatbot")
    print("="*60)
    print("\nStarting Flask server...")
    print("Open http://127.0.0.1:5000 in your browser\n")

    app.run(debug=True, host='127.0.0.1', port=5000)
