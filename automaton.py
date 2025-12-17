"""
Government Service Query Classifier - DFA Implementation
========================================================
A Deterministic Finite Automaton (DFA) for classifying Sri Lankan
government service queries in English, Sinhala, and Tamil.

Formal Definition:
- Alphabet (Σ): Keywords in English, Sinhala, Tamil
- States (Q): {q0, q1, q2, ..., q12, q_reject}
- Start State (q₀): q0
- Accepting States (F): {q1, q2, ..., q12}
- Transition Function (δ): Keyword-based state transitions
"""

class GovernmentServiceDFA:
    """DFA for classifying government service queries."""

    def __init__(self):
        # Define states
        self.states = {
            'q0': 'START',
            'q1': 'NIC_SERVICES',
            'q2': 'PASSPORT',
            'q3': 'BIRTH_CERTIFICATE',
            'q4': 'DEATH_CERTIFICATE',
            'q5': 'MARRIAGE_CERTIFICATE',
            'q6': 'DRIVING_LICENSE',
            'q7': 'VEHICLE_REGISTRATION',
            'q8': 'TAX_SERVICES',
            'q9': 'PENSION',
            'q10': 'SAMURDHI_WELFARE',
            'q11': 'EDUCATION',
            'q12': 'HEALTH_SERVICES',
            'q_reject': 'REJECTED'
        }

        # Start state
        self.start_state = 'q0'

        # Current state
        self.current_state = self.start_state

        # Accepting states (all service states except reject)
        self.accepting_states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6',
                                  'q7', 'q8', 'q9', 'q10', 'q11', 'q12'}

        # Transition function: keywords mapped to states
        # Format: keyword -> (state, service_info)
        self.transitions = self._build_transitions()

        # Service information in all three languages
        self.service_info = self._build_service_info()

    def _build_transitions(self):
        """
        Build the transition function δ.
        Maps keywords (in all 3 languages) to accepting states.
        """
        return {
            # q1: NIC Services
            'nic': 'q1',
            'national identity card': 'q1',
            'identity card': 'q1',
            'id card': 'q1',
            'identity': 'q1',
            'අනන්‍යතා': 'q1',
            'අනන්‍යතා පත්‍රය': 'q1',
            'හැඳුනුම්පත': 'q1',
            'හැඳුනුම්පත්': 'q1',
            'ජාතික හැඳුනුම්පත': 'q1',
            'அடையாள அட்டை': 'q1',
            'அடையாளம்': 'q1',
            'தேசிய அடையாள அட்டை': 'q1',

            # q2: Passport
            'passport': 'q2',
            'travel document': 'q2',
            'ගමන් බලපත්‍රය': 'q2',
            'ගමන්බලපත්‍රය': 'q2',
            'පාස්පෝට්': 'q2',
            'கடவுச்சீட்டு': 'q2',
            'பாஸ்போர்ட்': 'q2',

            # q3: Birth Certificate
            'birth': 'q3',
            'birth certificate': 'q3',
            'birth registration': 'q3',
            'උප්පැන්න': 'q3',
            'උප්පැන්න සහතිකය': 'q3',
            'උපත් සහතිකය': 'q3',
            'பிறப்பு': 'q3',
            'பிறப்புச் சான்றிதழ்': 'q3',
            'பிறப்பு சான்றிதழ்': 'q3',

            # q4: Death Certificate
            'death': 'q4',
            'death certificate': 'q4',
            'death registration': 'q4',
            'මරණ': 'q4',
            'මරණ සහතිකය': 'q4',
            'இறப்பு': 'q4',
            'இறப்புச் சான்றிதழ்': 'q4',
            'இறப்பு சான்றிதழ்': 'q4',

            # q5: Marriage Certificate
            'marriage': 'q5',
            'marriage certificate': 'q5',
            'marriage registration': 'q5',
            'විවාහ': 'q5',
            'විවාහ සහතිකය': 'q5',
            'திருமணம்': 'q5',
            'திருமணச் சான்றிதழ்': 'q5',
            'திருமண சான்றிதழ்': 'q5',

            # q6: Driving License
            'driving': 'q6',
            'driving license': 'q6',
            'driver license': 'q6',
            'license': 'q6',
            'රියදුරු': 'q6',
            'රියදුරු බලපත්‍රය': 'q6',
            'ලයිසන්': 'q6',
            'ஓட்டுநர்': 'q6',
            'ஓட்டுநர் உரிமம்': 'q6',
            'உரிமம்': 'q6',

            # q7: Vehicle Registration
            'vehicle': 'q7',
            'vehicle registration': 'q7',
            'car registration': 'q7',
            'motor': 'q7',
            'වාහන': 'q7',
            'වාහන ලියාපදිංචිය': 'q7',
            'රථවාහන': 'q7',
            'வாகனம்': 'q7',
            'வாகன பதிவு': 'q7',

            # q8: Tax Services
            'tax': 'q8',
            'taxation': 'q8',
            'income tax': 'q8',
            'revenue': 'q8',
            'බදු': 'q8',
            'බදු සේවා': 'q8',
            'ආදායම් බදු': 'q8',
            'வரி': 'q8',
            'வரி சேவைகள்': 'q8',
            'வருமான வரி': 'q8',

            # q9: Pension
            'pension': 'q9',
            'retirement': 'q9',
            'epf': 'q9',
            'etf': 'q9',
            'විශ්‍රාම': 'q9',
            'විශ්‍රාම වැටුප්': 'q9',
            'පඩි': 'q9',
            'ஓய்வூதியம்': 'q9',
            'ஓய்வு': 'q9',

            # q10: Samurdhi/Welfare
            'samurdhi': 'q10',
            'welfare': 'q10',
            'social service': 'q10',
            'aswesuma': 'q10',
            'සමෘද්ධි': 'q10',
            'අස්වැසුම': 'q10',
            'සුබසාධන': 'q10',
            'சமுர்தி': 'q10',
            'நலன்புரி': 'q10',

            # q11: Education
            'education': 'q11',
            'school': 'q11',
            'university': 'q11',
            'scholarship': 'q11',
            'exam': 'q11',
            'අධ්‍යාපනය': 'q11',
            'පාසල්': 'q11',
            'විශ්ව විද්‍යාලය': 'q11',
            'ශිෂ්‍යත්ව': 'q11',
            'கல்வி': 'q11',
            'பள்ளி': 'q11',
            'பல்கலைக்கழகம்': 'q11',
            'புலமைப்பரிசில்': 'q11',

            # q12: Health Services
            'health': 'q12',
            'hospital': 'q12',
            'medical': 'q12',
            'doctor': 'q12',
            'clinic': 'q12',
            'සෞඛ්‍ය': 'q12',
            'රෝහල': 'q12',
            'වෛද්‍ය': 'q12',
            'சுகாதாரம்': 'q12',
            'மருத்துவமனை': 'q12',
            'மருத்துவர்': 'q12',
        }

    def _build_service_info(self):
        """Build detailed service information for each state."""
        return {
            'q1': {
                'name': {
                    'en': 'NIC Services',
                    'si': 'ජාතික හැඳුනුම්පත් සේවා',
                    'ta': 'தேசிய அடையாள அட்டை சேவைகள்'
                },
                'description': {
                    'en': 'National Identity Card application, renewal, and replacement services.',
                    'si': 'ජාතික හැඳුනුම්පත් අයදුම්පත්, අලුත් කිරීම සහ ප්‍රතිස්ථාපන සේවා.',
                    'ta': 'தேசிய அடையாள அட்டை விண்ணப்பம், புதுப்பித்தல் மற்றும் மாற்றீடு சேவைகள்.'
                },
                'office': {
                    'en': 'Department of Registration of Persons',
                    'si': 'පුද්ගලයින් ලියාපදිංචි කිරීමේ දෙපාර්තමේන්තුව',
                    'ta': 'நபர்கள் பதிவுத் திணைக்களம்'
                },
                'documents': ['Birth Certificate', 'Citizenship Certificate', 'Photo'],
                'website': 'www.drp.gov.lk'
            },
            'q2': {
                'name': {
                    'en': 'Passport Services',
                    'si': 'ගමන් බලපත්‍ර සේවා',
                    'ta': 'கடவுச்சீட்டு சேவைகள்'
                },
                'description': {
                    'en': 'Passport application, renewal, and emergency travel document services.',
                    'si': 'ගමන් බලපත්‍ර අයදුම්පත්, අලුත් කිරීම සහ හදිසි ගමන් ලේඛන සේවා.',
                    'ta': 'கடவுச்சீட்டு விண்ணப்பம், புதுப்பித்தல் மற்றும் அவசர பயண ஆவண சேவைகள்.'
                },
                'office': {
                    'en': 'Department of Immigration and Emigration',
                    'si': 'ආගමන විගමන දෙපාර්තමේන්තුව',
                    'ta': 'குடிவரவு மற்றும் குடியகல்வு திணைக்களம்'
                },
                'documents': ['NIC', 'Birth Certificate', 'Photos'],
                'website': 'www.immigration.gov.lk'
            },
            'q3': {
                'name': {
                    'en': 'Birth Certificate Services',
                    'si': 'උප්පැන්න සහතික සේවා',
                    'ta': 'பிறப்புச் சான்றிதழ் சேவைகள்'
                },
                'description': {
                    'en': 'Birth registration and certificate issuance services.',
                    'si': 'උපත් ලියාපදිංචිය සහ සහතික නිකුත් කිරීමේ සේවා.',
                    'ta': 'பிறப்பு பதிவு மற்றும் சான்றிதழ் வழங்கல் சேவைகள்.'
                },
                'office': {
                    'en': 'Divisional Secretariat / Registrar General',
                    'si': 'ප්‍රාදේශීය ලේකම් කාර්යාලය / රෙජිස්ට්‍රාර් ජනරාල්',
                    'ta': 'பிரதேச செயலகம் / பதிவாளர் நாயகம்'
                },
                'documents': ['Hospital Records', 'Parents NIC'],
                'website': 'www.rgd.gov.lk'
            },
            'q4': {
                'name': {
                    'en': 'Death Certificate Services',
                    'si': 'මරණ සහතික සේවා',
                    'ta': 'இறப்புச் சான்றிதழ் சேவைகள்'
                },
                'description': {
                    'en': 'Death registration and certificate issuance services.',
                    'si': 'මරණ ලියාපදිංචිය සහ සහතික නිකුත් කිරීමේ සේවා.',
                    'ta': 'இறப்பு பதிவு மற்றும் சான்றிதழ் வழங்கல் சேவைகள்.'
                },
                'office': {
                    'en': 'Divisional Secretariat / Registrar General',
                    'si': 'ප්‍රාදේශීය ලේකම් කාර්යාලය / රෙජිස්ට්‍රාර් ජනරාල්',
                    'ta': 'பிரதேச செயலகம் / பதிவாளர் நாயகம்'
                },
                'documents': ['Death Report', 'Deceased NIC'],
                'website': 'www.rgd.gov.lk'
            },
            'q5': {
                'name': {
                    'en': 'Marriage Certificate Services',
                    'si': 'විවාහ සහතික සේවා',
                    'ta': 'திருமணச் சான்றிதழ் சேவைகள்'
                },
                'description': {
                    'en': 'Marriage registration and certificate issuance services.',
                    'si': 'විවාහ ලියාපදිංචිය සහ සහතික නිකුත් කිරීමේ සේවා.',
                    'ta': 'திருமண பதிவு மற்றும் சான்றிதழ் வழங்கல் சேவைகள்.'
                },
                'office': {
                    'en': 'Divisional Secretariat / Marriage Registrar',
                    'si': 'ප්‍රාදේශීය ලේකම් කාර්යාලය / විවාහ රෙජිස්ට්‍රාර්',
                    'ta': 'பிரதேச செயலகம் / திருமண பதிவாளர்'
                },
                'documents': ['Birth Certificates', 'NIC of both parties'],
                'website': 'www.rgd.gov.lk'
            },
            'q6': {
                'name': {
                    'en': 'Driving License Services',
                    'si': 'රියදුරු බලපත්‍ර සේවා',
                    'ta': 'ஓட்டுநர் உரிம சேவைகள்'
                },
                'description': {
                    'en': 'Driving license application, renewal, and class addition services.',
                    'si': 'රියදුරු බලපත්‍ර අයදුම්පත්, අලුත් කිරීම සහ පන්ති එකතු කිරීමේ සේවා.',
                    'ta': 'ஓட்டுநர் உரிம விண்ணப்பம், புதுப்பித்தல் மற்றும் வகுப்பு சேர்த்தல் சேவைகள்.'
                },
                'office': {
                    'en': 'Department of Motor Traffic',
                    'si': 'මෝටර් රථ ප්‍රවාහන දෙපාර්තමේන්තුව',
                    'ta': 'மோட்டார் போக்குவரத்துத் திணைக்களம்'
                },
                'documents': ['NIC', 'Medical Certificate', 'Photos'],
                'website': 'www.motortraffic.gov.lk'
            },
            'q7': {
                'name': {
                    'en': 'Vehicle Registration Services',
                    'si': 'වාහන ලියාපදිංචි සේවා',
                    'ta': 'வாகன பதிவு சேவைகள்'
                },
                'description': {
                    'en': 'Vehicle registration, transfer, and revenue license services.',
                    'si': 'වාහන ලියාපදිංචිය, මාරු කිරීම සහ ආදායම් බලපත්‍ර සේවා.',
                    'ta': 'வாகன பதிவு, மாற்றம் மற்றும் வருவாய் உரிம சேவைகள்.'
                },
                'office': {
                    'en': 'Department of Motor Traffic',
                    'si': 'මෝටර් රථ ප්‍රවාහන දෙපාර්තමේන්තුව',
                    'ta': 'மோட்டார் போக்குவரத்துத் திணைக்களம்'
                },
                'documents': ['NIC', 'Vehicle Documents', 'Insurance'],
                'website': 'www.motortraffic.gov.lk'
            },
            'q8': {
                'name': {
                    'en': 'Tax Services',
                    'si': 'බදු සේවා',
                    'ta': 'வரி சேவைகள்'
                },
                'description': {
                    'en': 'Income tax, VAT, and other taxation services.',
                    'si': 'ආදායම් බදු, වැට් බදු සහ වෙනත් බදු සේවා.',
                    'ta': 'வருமான வரி, VAT மற்றும் பிற வரி சேவைகள்.'
                },
                'office': {
                    'en': 'Inland Revenue Department',
                    'si': 'දේශීය ආදායම් දෙපාර්තමේන්තුව',
                    'ta': 'உள்நாட்டு இறைவரித் திணைக்களம்'
                },
                'documents': ['NIC', 'Income Documents', 'TIN'],
                'website': 'www.ird.gov.lk'
            },
            'q9': {
                'name': {
                    'en': 'Pension Services',
                    'si': 'විශ්‍රාම වැටුප් සේවා',
                    'ta': 'ஓய்வூதிய சேவைகள்'
                },
                'description': {
                    'en': 'EPF/ETF claims, government pension, and retirement benefits.',
                    'si': 'EPF/ETF හිමිකම්, රජයේ විශ්‍රාම වැටුප් සහ විශ්‍රාම ප්‍රතිලාභ.',
                    'ta': 'EPF/ETF கோரிக்கைகள், அரசு ஓய்வூதியம் மற்றும் ஓய்வு நலன்கள்.'
                },
                'office': {
                    'en': 'Department of Pensions / EPF Department',
                    'si': 'විශ්‍රාම වැටුප් දෙපාර්තමේන්තුව',
                    'ta': 'ஓய்வூதியத் திணைக்களம்'
                },
                'documents': ['NIC', 'Service Records', 'Bank Details'],
                'website': 'www.pensions.gov.lk'
            },
            'q10': {
                'name': {
                    'en': 'Samurdhi/Welfare Services',
                    'si': 'සමෘද්ධි/සුබසාධන සේවා',
                    'ta': 'சமுர்தி/நலன்புரி சேவைகள்'
                },
                'description': {
                    'en': 'Samurdhi benefits, Aswesuma allowance, and social welfare programs.',
                    'si': 'සමෘද්ධි ප්‍රතිලාභ, අස්වැසුම දීමනාව සහ සමාජ සුබසාධන වැඩසටහන්.',
                    'ta': 'சமுர்தி நலன்கள், அஸ்வெசும உதவித்தொகை மற்றும் சமூக நலத்திட்டங்கள்.'
                },
                'office': {
                    'en': 'Divisional Secretariat / Samurdhi Authority',
                    'si': 'ප්‍රාදේශීය ලේකම් කාර්යාලය / සමෘද්ධි අධිකාරිය',
                    'ta': 'பிரதேச செயலகம் / சமுர்தி அதிகார சபை'
                },
                'documents': ['NIC', 'Income Certificate', 'Grama Niladhari Report'],
                'website': 'www.samurdhi.gov.lk'
            },
            'q11': {
                'name': {
                    'en': 'Education Services',
                    'si': 'අධ්‍යාපන සේවා',
                    'ta': 'கல்வி சேவைகள்'
                },
                'description': {
                    'en': 'School admissions, scholarships, university applications, and exam results.',
                    'si': 'පාසල් ඇතුළත් කිරීම්, ශිෂ්‍යත්ව, විශ්ව විද්‍යාල අයදුම්පත් සහ විභාග ප්‍රතිඵල.',
                    'ta': 'பள்ளி சேர்க்கை, புலமைப்பரிசில், பல்கலைக்கழக விண்ணப்பங்கள் மற்றும் தேர்வு முடிவுகள்.'
                },
                'office': {
                    'en': 'Ministry of Education / UGC',
                    'si': 'අධ්‍යාපන අමාත්‍යාංශය / UGC',
                    'ta': 'கல்வி அமைச்சு / UGC'
                },
                'documents': ['Birth Certificate', 'School Records', 'NIC'],
                'website': 'www.moe.gov.lk'
            },
            'q12': {
                'name': {
                    'en': 'Health Services',
                    'si': 'සෞඛ්‍ය සේවා',
                    'ta': 'சுகாதார சேவைகள்'
                },
                'description': {
                    'en': 'Hospital services, medical cards, and public health programs.',
                    'si': 'රෝහල් සේවා, වෛද්‍ය කාඩ්පත් සහ මහජන සෞඛ්‍ය වැඩසටහන්.',
                    'ta': 'மருத்துவமனை சேவைகள், மருத்துவ அட்டைகள் மற்றும் பொது சுகாதார திட்டங்கள்.'
                },
                'office': {
                    'en': 'Ministry of Health / District Hospital',
                    'si': 'සෞඛ්‍ය අමාත්‍යාංශය / දිස්ත්‍රික් රෝහල',
                    'ta': 'சுகாதார அமைச்சு / மாவட்ட வைத்தியசாலை'
                },
                'documents': ['NIC', 'Medical Records'],
                'website': 'www.health.gov.lk'
            }
        }

    def reset(self):
        """Reset DFA to start state."""
        self.current_state = self.start_state

    def transition(self, input_string):
        """
        Process input and transition to appropriate state.

        δ(q0, keyword) → accepting_state or q_reject

        Args:
            input_string: User query in any language

        Returns:
            tuple: (new_state, is_accepted, matched_keyword)
        """
        # Normalize input
        normalized = input_string.lower().strip()

        # Try to find matching keyword
        matched_keyword = None
        new_state = 'q_reject'

        # Check for exact matches first
        if normalized in self.transitions:
            new_state = self.transitions[normalized]
            matched_keyword = normalized
        else:
            # Check for partial matches (keyword contained in input)
            for keyword, state in self.transitions.items():
                if keyword in normalized:
                    new_state = state
                    matched_keyword = keyword
                    break

        self.current_state = new_state
        is_accepted = new_state in self.accepting_states

        return (new_state, is_accepted, matched_keyword)

    def process_query(self, query, language='en'):
        """
        Process a user query and return classification result.

        Args:
            query: User input string
            language: Response language ('en', 'si', 'ta')

        Returns:
            dict: Classification result with state, acceptance, and info
        """
        self.reset()
        state, is_accepted, matched_keyword = self.transition(query)

        result = {
            'query': query,
            'state': state,
            'state_name': self.states[state],
            'is_accepted': is_accepted,
            'status': 'ACCEPT' if is_accepted else 'REJECT',
            'matched_keyword': matched_keyword,
            'transition': f"δ(q0, '{matched_keyword or query}') → {state}"
        }

        if is_accepted and state in self.service_info:
            info = self.service_info[state]
            result['service'] = {
                'name': info['name'].get(language, info['name']['en']),
                'description': info['description'].get(language, info['description']['en']),
                'office': info['office'].get(language, info['office']['en']),
                'documents': info['documents'],
                'website': info['website']
            }
        else:
            result['message'] = {
                'en': "Sorry, I couldn't classify your query. Please try again with keywords like: NIC, passport, birth certificate, driving license, etc.",
                'si': "සමාවන්න, ඔබේ විමසුම වර්ගීකරණය කිරීමට නොහැකි විය. කරුණාකර NIC, ගමන් බලපත්‍රය, උප්පැන්න සහතිකය වැනි මූල පද සමඟ නැවත උත්සාහ කරන්න.",
                'ta': "மன்னிக்கவும், உங்கள் வினவலை வகைப்படுத்த முடியவில்லை. NIC, கடவுச்சீட்டு, பிறப்புச் சான்றிதழ் போன்ற முக்கிய சொற்களுடன் மீண்டும் முயற்சிக்கவும்."
            }.get(language, "Sorry, I couldn't classify your query.")

        return result

    def get_state_diagram(self):
        """Return a text-based DFA state diagram."""
        diagram = []
        diagram.append("\n" + "=" * 60)
        diagram.append("   DFA STATE DIAGRAM")
        diagram.append("=" * 60)
        diagram.append("\nStart State: q0 (START)")
        diagram.append("\nState Transitions (δ):")
        diagram.append("-" * 60)
        
        # Group transitions by state
        state_transitions = {}
        for keyword, state in self.transitions.items():
            if state not in state_transitions:
                state_transitions[state] = []
            state_transitions[state].append(keyword)
        
        # Display transitions for each state
        for state in sorted(state_transitions.keys()):
            state_name = self.states.get(state, 'UNKNOWN')
            diagram.append(f"\n{state} ({state_name}):")
            
            # Show sample keywords (limit to avoid clutter)
            keywords = state_transitions[state]
            sample_keywords = keywords[:5]  # Show first 5 keywords
            for kw in sample_keywords:
                diagram.append(f"  ← \"{kw}\"")
            if len(keywords) > 5:
                diagram.append(f"  ... and {len(keywords) - 5} more keywords")
        
        diagram.append("\n" + "-" * 60)
        diagram.append(f"Accepting States: {', '.join(sorted(self.accepting_states))}")
        diagram.append(f"Reject State: q_reject")
        diagram.append("=" * 60 + "\n")
        
        return "\n".join(diagram)

    def get_formal_definition(self):
        """Return formal DFA definition."""
        return {
            'alphabet': 'Σ = {keywords in English, Sinhala, Tamil}',
            'states': 'Q = {q0, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q_reject}',
            'start_state': 'q₀ = q0',
            'accepting_states': 'F = {q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12}',
            'transition_function': 'δ: Q × Σ → Q (keyword-based transitions)'
        }

    def get_all_services(self, language='en'):
        """Get list of all available services."""
        services = []
        for state_id, info in self.service_info.items():
            services.append({
                'state': state_id,
                'name': info['name'].get(language, info['name']['en']),
                'keywords_en': [k for k, v in self.transitions.items()
                               if v == state_id and k.isascii()][:3]
            })
        return services


# For testing
if __name__ == "__main__":
    dfa = GovernmentServiceDFA()

    print("Testing DFA with sample queries:")
    print("="*40)

    test_queries = [
        ("I need to get my NIC", "en"),
        ("ගමන් බලපත්‍රය ගන්න ඕනේ", "si"),
        ("பிறப்புச் சான்றிதழ் வேண்டும்", "ta"),
        ("How to apply for driving license?", "en"),
        ("random query", "en"),
    ]

    for query, lang in test_queries:
        result = dfa.process_query(query, lang)
        print(f"Query: {query}")
        print(f"State: {result['state']} ({result['state_name']})")
        print(f"Status: {result['status']}")
        print(f"Transition: {result['transition']}")
        if result['is_accepted']:
            print(f"Service: {result['service']['name']}")
        print("-" * 40)
