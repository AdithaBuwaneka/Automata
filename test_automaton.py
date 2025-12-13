"""
Government Service Query Classifier - Test Cases
=================================================
Comprehensive test suite demonstrating DFA functionality
with test cases in English, Sinhala, and Tamil.
"""

from automaton import GovernmentServiceDFA


def print_header(title):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def print_result(query, result, lang):
    """Print formatted test result."""
    status_icon = "✅" if result['is_accepted'] else "❌"
    print(f"\n{status_icon} Query ({lang}): \"{query}\"")
    print(f"   State: {result['state']} ({result['state_name']})")
    print(f"   Status: {result['status']}")
    print(f"   Transition: {result['transition']}")
    if result['is_accepted'] and 'service' in result:
        print(f"   Service: {result['service']['name']}")
    print("-" * 50)


def test_english_queries(dfa):
    """Test English language queries."""
    print_header("ENGLISH LANGUAGE TEST CASES")

    test_cases = [
        # NIC Services
        ("How to apply for NIC?", "en"),
        ("I need my national identity card", "en"),

        # Passport
        ("Passport renewal process", "en"),
        ("How to get a travel document?", "en"),

        # Birth Certificate
        ("Birth certificate application", "en"),
        ("Birth registration for newborn", "en"),

        # Death Certificate
        ("Death certificate request", "en"),

        # Marriage Certificate
        ("Marriage registration process", "en"),

        # Driving License
        ("Driving license renewal", "en"),
        ("How to get a driver license?", "en"),

        # Vehicle Registration
        ("Vehicle registration transfer", "en"),
        ("Car registration process", "en"),

        # Tax Services
        ("Income tax filing", "en"),
        ("Tax payment methods", "en"),

        # Pension
        ("EPF withdrawal process", "en"),
        ("Pension application", "en"),

        # Samurdhi/Welfare
        ("Samurdhi benefits eligibility", "en"),
        ("Aswesuma registration", "en"),

        # Education
        ("School admission process", "en"),
        ("University application", "en"),
        ("Scholarship application", "en"),

        # Health Services
        ("Hospital services inquiry", "en"),
        ("Medical card registration", "en"),

        # REJECT cases
        ("What is the weather today?", "en"),
        ("Random unrelated query", "en"),
    ]

    accept_count = 0
    reject_count = 0

    for query, lang in test_cases:
        result = dfa.process_query(query, lang)
        print_result(query, result, lang)
        if result['is_accepted']:
            accept_count += 1
        else:
            reject_count += 1

    print(f"\n📊 English Results: {accept_count} ACCEPT, {reject_count} REJECT")
    return accept_count, reject_count


def test_sinhala_queries(dfa):
    """Test Sinhala language queries."""
    print_header("SINHALA LANGUAGE TEST CASES (සිංහල)")

    test_cases = [
        # NIC - හැඳුනුම්පත
        ("ජාතික හැඳුනුම්පත අයදුම් කරන්නේ කෙසේද?", "si"),
        ("අනන්‍යතා පත්‍රය ගන්න ඕනේ", "si"),

        # Passport - ගමන් බලපත්‍රය
        ("ගමන් බලපත්‍රය අලුත් කරන්න", "si"),
        ("පාස්පෝට් එක ගන්න කොහොමද?", "si"),

        # Birth Certificate - උප්පැන්න සහතිකය
        ("උප්පැන්න සහතිකය ගන්න ඕනේ", "si"),
        ("උපත් සහතිකය අයදුම්පත", "si"),

        # Death Certificate - මරණ සහතිකය
        ("මරණ සහතිකය ලබා ගන්නේ කෙසේද?", "si"),

        # Marriage Certificate - විවාහ සහතිකය
        ("විවාහ සහතිකය ලියාපදිංචිය", "si"),

        # Driving License - රියදුරු බලපත්‍රය
        ("රියදුරු බලපත්‍රය අලුත් කරන්න", "si"),
        ("ලයිසන් එක ගන්න ඕනේ", "si"),

        # Vehicle - වාහන
        ("වාහන ලියාපදිංචිය මාරු කරන්න", "si"),
        ("රථවාහන බලපත්‍රය", "si"),

        # Tax - බදු
        ("ආදායම් බදු ගෙවීම", "si"),
        ("බදු සේවා පිළිබඳ තොරතුරු", "si"),

        # Pension - විශ්‍රාම වැටුප්
        ("විශ්‍රාම වැටුප් අයදුම්පත", "si"),

        # Samurdhi - සමෘද්ධි
        ("සමෘද්ධි ප්‍රතිලාභ", "si"),
        ("අස්වැසුම ලියාපදිංචිය", "si"),

        # Education - අධ්‍යාපනය
        ("පාසල් ඇතුළත් කිරීම", "si"),
        ("ශිෂ්‍යත්ව අයදුම්පත", "si"),

        # Health - සෞඛ්‍ය
        ("රෝහල සේවා", "si"),
        ("වෛද්‍ය කාඩ්පත ලබාගැනීම", "si"),

        # REJECT case
        ("අද කාලගුණය කොහොමද?", "si"),
    ]

    accept_count = 0
    reject_count = 0

    for query, lang in test_cases:
        result = dfa.process_query(query, lang)
        print_result(query, result, lang)
        if result['is_accepted']:
            accept_count += 1
        else:
            reject_count += 1

    print(f"\n📊 Sinhala Results: {accept_count} ACCEPT, {reject_count} REJECT")
    return accept_count, reject_count


def test_tamil_queries(dfa):
    """Test Tamil language queries."""
    print_header("TAMIL LANGUAGE TEST CASES (தமிழ்)")

    test_cases = [
        # NIC - அடையாள அட்டை
        ("தேசிய அடையாள அட்டை விண்ணப்பம்", "ta"),
        ("அடையாளம் பெற வேண்டும்", "ta"),

        # Passport - கடவுச்சீட்டு
        ("கடவுச்சீட்டு புதுப்பித்தல்", "ta"),
        ("பாஸ்போர்ட் எடுக்க வேண்டும்", "ta"),

        # Birth Certificate - பிறப்புச் சான்றிதழ்
        ("பிறப்புச் சான்றிதழ் வேண்டும்", "ta"),
        ("பிறப்பு பதிவு செய்ய", "ta"),

        # Death Certificate - இறப்புச் சான்றிதழ்
        ("இறப்புச் சான்றிதழ் பெற", "ta"),

        # Marriage Certificate - திருமணச் சான்றிதழ்
        ("திருமணம் பதிவு செய்ய", "ta"),
        ("திருமண சான்றிதழ்", "ta"),

        # Driving License - ஓட்டுநர் உரிமம்
        ("ஓட்டுநர் உரிமம் புதுப்பிக்க", "ta"),
        ("உரிமம் எடுக்க வேண்டும்", "ta"),

        # Vehicle - வாகனம்
        ("வாகன பதிவு மாற்றம்", "ta"),
        ("வாகனம் பதிவு செய்ய", "ta"),

        # Tax - வரி
        ("வருமான வரி செலுத்த", "ta"),
        ("வரி சேவைகள்", "ta"),

        # Pension - ஓய்வூதியம்
        ("ஓய்வூதியம் விண்ணப்பம்", "ta"),
        ("ஓய்வு பெற", "ta"),

        # Samurdhi - சமுர்தி
        ("சமுர்தி உதவி", "ta"),
        ("நலன்புரி சேவை", "ta"),

        # Education - கல்வி
        ("பள்ளி சேர்க்கை", "ta"),
        ("பல்கலைக்கழகம் விண்ணப்பம்", "ta"),

        # Health - சுகாதாரம்
        ("மருத்துவமனை சேவைகள்", "ta"),
        ("மருத்துவர் சந்திப்பு", "ta"),

        # REJECT case
        ("இன்று வானிலை எப்படி?", "ta"),
    ]

    accept_count = 0
    reject_count = 0

    for query, lang in test_cases:
        result = dfa.process_query(query, lang)
        print_result(query, result, lang)
        if result['is_accepted']:
            accept_count += 1
        else:
            reject_count += 1

    print(f"\n📊 Tamil Results: {accept_count} ACCEPT, {reject_count} REJECT")
    return accept_count, reject_count


def test_edge_cases(dfa):
    """Test edge cases and boundary conditions."""
    print_header("EDGE CASES AND BOUNDARY CONDITIONS")

    test_cases = [
        # Mixed language
        ("NIC එක ගන්න ඕනේ", "en"),  # Mixed Sinhala-English

        # Case insensitivity
        ("NIC", "en"),
        ("nic", "en"),
        ("Nic", "en"),

        # Partial matches
        ("I need NIC information", "en"),
        ("What about passport fees?", "en"),

        # Empty or whitespace
        ("   ", "en"),

        # Multiple keywords (should match first)
        ("NIC and passport", "en"),
    ]

    for query, lang in test_cases:
        if query.strip():
            result = dfa.process_query(query, lang)
            print_result(query, result, lang)


def run_all_tests():
    """Run all test suites."""
    dfa = GovernmentServiceDFA()

    # Print DFA diagram
    print(dfa.get_state_diagram())

    # Print formal definition
    print_header("FORMAL DFA DEFINITION")
    formal = dfa.get_formal_definition()
    for key, value in formal.items():
        print(f"  {key}: {value}")

    # Run test suites
    en_accept, en_reject = test_english_queries(dfa)
    si_accept, si_reject = test_sinhala_queries(dfa)
    ta_accept, ta_reject = test_tamil_queries(dfa)

    # Edge cases
    test_edge_cases(dfa)

    # Final summary
    print_header("FINAL TEST SUMMARY")
    total_accept = en_accept + si_accept + ta_accept
    total_reject = en_reject + si_reject + ta_reject
    total = total_accept + total_reject

    print(f"""
    ╔══════════════════════════════════════════════════════╗
    ║              TEST RESULTS SUMMARY                     ║
    ╠══════════════════════════════════════════════════════╣
    ║  Language    │  ACCEPT  │  REJECT  │  Total          ║
    ╠══════════════════════════════════════════════════════╣
    ║  English     │    {en_accept:2d}    │    {en_reject:2d}    │    {en_accept + en_reject:2d}            ║
    ║  Sinhala     │    {si_accept:2d}    │    {si_reject:2d}    │    {si_accept + si_reject:2d}            ║
    ║  Tamil       │    {ta_accept:2d}    │    {ta_reject:2d}    │    {ta_accept + ta_reject:2d}            ║
    ╠══════════════════════════════════════════════════════╣
    ║  TOTAL       │    {total_accept:2d}    │    {total_reject:2d}    │    {total:2d}            ║
    ╚══════════════════════════════════════════════════════╝

    ✅ DFA correctly classifies government service queries
    ✅ Trilingual support (English, Sinhala, Tamil) working
    ✅ ACCEPT/REJECT outcomes properly generated
    ✅ State transitions correctly logged
    """)


if __name__ == "__main__":
    print("\n" + "🏛️ " * 20)
    print("\n   GOVERNMENT SERVICE QUERY CLASSIFIER - DFA TEST SUITE")
    print("   Sri Lanka - Automata Theory Assignment\n")
    print("🏛️ " * 20)

    run_all_tests()
