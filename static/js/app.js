/**
 * Government Service Query Classifier - Frontend Logic
 * =====================================================
 * Handles chat interface, API calls, and DFA visualization
 */

// Current language
let currentLanguage = 'en';

// Translations
const translations = {
    en: {
        mainTitle: 'Government Service Classifier',
        subtitle: 'Automaton-based Query Classification System',
        langLabel: 'Language:',
        dfaTitle: 'DFA State Diagram',
        stateLabel: 'Current State:',
        formalTitle: 'Formal Definition',
        chatTitle: 'Chat with Classifier',
        statusText: 'Online',
        quickLabel: 'Quick queries:',
        welcomeMsg: "Welcome! I'm the Government Service Query Classifier. I use a DFA (Deterministic Finite Automaton) to classify your queries about Sri Lankan government services.",
        instructionMsg: "Try asking about: NIC, Passport, Birth Certificate, Driving License, Vehicle Registration, Tax, Pension, Samurdhi, Education, or Health services.",
        inputPlaceholder: 'Type your query here...',
        hintText: 'Press Enter to send | Supports English, සිංහල, தமிழ்',
        accept: 'ACCEPT',
        reject: 'REJECT',
        stateTransition: 'State Transition:',
        serviceName: 'Service:',
        description: 'Description:',
        office: 'Office:',
        documents: 'Required Documents:',
        website: 'Website:'
    },
    si: {
        mainTitle: 'රජයේ සේවා වර්ගීකරණය',
        subtitle: 'ස්වයංක්‍රීය විමසුම් වර්ගීකරණ පද්ධතිය',
        langLabel: 'භාෂාව:',
        dfaTitle: 'DFA තත්ත්ව රූප සටහන',
        stateLabel: 'වත්මන් තත්ත්වය:',
        formalTitle: 'විධිමත් අර්ථ දැක්වීම',
        chatTitle: 'වර්ගීකාරකය සමඟ කතා කරන්න',
        statusText: 'සබැඳි',
        quickLabel: 'ඉක්මන් විමසුම්:',
        welcomeMsg: "ආයුබෝවන්! මම රජයේ සේවා විමසුම් වර්ගීකාරකයයි. මම ශ්‍රී ලංකාවේ රජයේ සේවා පිළිබඳ ඔබේ විමසුම් වර්ගීකරණය කිරීමට DFA භාවිතා කරමි.",
        instructionMsg: "මේවා ගැන විමසන්න: හැඳුනුම්පත, ගමන් බලපත්‍රය, උප්පැන්න සහතිකය, රියදුරු බලපත්‍රය, වාහන ලියාපදිංචිය, බදු, විශ්‍රාම වැටුප්, සමෘද්ධි, අධ්‍යාපනය, හෝ සෞඛ්‍ය සේවා.",
        inputPlaceholder: 'ඔබේ විමසුම මෙහි ටයිප් කරන්න...',
        hintText: 'යැවීමට Enter ඔබන්න | English, සිංහල, தமிழ் සහාය',
        accept: 'පිළිගනු',
        reject: 'ප්‍රතික්ෂේප',
        stateTransition: 'තත්ත්ව මාරුව:',
        serviceName: 'සේවාව:',
        description: 'විස්තරය:',
        office: 'කාර්යාලය:',
        documents: 'අවශ්‍ය ලේඛන:',
        website: 'වෙබ් අඩවිය:'
    },
    ta: {
        mainTitle: 'அரசு சேவை வகைப்படுத்தி',
        subtitle: 'தானியங்கி வினவல் வகைப்பாடு அமைப்பு',
        langLabel: 'மொழி:',
        dfaTitle: 'DFA நிலை வரைபடம்',
        stateLabel: 'தற்போதைய நிலை:',
        formalTitle: 'முறையான வரையறை',
        chatTitle: 'வகைப்படுத்தியுடன் உரையாடல்',
        statusText: 'இணைப்பில்',
        quickLabel: 'விரைவு வினவல்கள்:',
        welcomeMsg: "வணக்கம்! நான் அரசு சேவை வினவல் வகைப்படுத்தி. இலங்கை அரசு சேவைகள் பற்றிய உங்கள் வினவல்களை வகைப்படுத்த DFA ஐ பயன்படுத்துகிறேன்.",
        instructionMsg: "இவை பற்றி கேளுங்கள்: அடையாள அட்டை, கடவுச்சீட்டு, பிறப்புச் சான்றிதழ், ஓட்டுநர் உரிமம், வாகன பதிவு, வரி, ஓய்வூதியம், சமுர்தி, கல்வி, அல்லது சுகாதார சேவைகள்.",
        inputPlaceholder: 'உங்கள் வினவலை இங்கே தட்டச்சு செய்யுங்கள்...',
        hintText: 'அனுப்ப Enter அழுத்தவும் | English, සිංහල, தமிழ் ஆதரவு',
        accept: 'ஏற்கப்பட்டது',
        reject: 'நிராகரிக்கப்பட்டது',
        stateTransition: 'நிலை மாற்றம்:',
        serviceName: 'சேவை:',
        description: 'விளக்கம்:',
        office: 'அலுவலகம்:',
        documents: 'தேவையான ஆவணங்கள்:',
        website: 'இணையதளம்:'
    }
};

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const languageSelect = document.getElementById('language-select');
const quickBtns = document.querySelectorAll('.quick-btn');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    // Language change handler
    languageSelect.addEventListener('change', handleLanguageChange);

    // Send message handlers
    sendBtn.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    // Quick button handlers
    quickBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const query = currentLanguage === 'en' ? btn.dataset.query :
                          currentLanguage === 'si' ? btn.dataset.si :
                          btn.dataset.ta;
            userInput.value = query;
            sendMessage();
        });
    });

    // Focus input
    userInput.focus();
});

/**
 * Handle language change
 */
function handleLanguageChange() {
    currentLanguage = languageSelect.value;
    updateUILanguage();
}

/**
 * Update UI text based on selected language
 */
function updateUILanguage() {
    const t = translations[currentLanguage];

    document.getElementById('main-title').textContent = t.mainTitle;
    document.getElementById('subtitle').textContent = t.subtitle;
    document.getElementById('lang-label').textContent = t.langLabel;
    document.getElementById('dfa-title').textContent = t.dfaTitle;
    document.getElementById('state-label').textContent = t.stateLabel;
    document.getElementById('formal-title').textContent = t.formalTitle;
    document.getElementById('chat-title').textContent = t.chatTitle;
    document.getElementById('status-text').textContent = t.statusText;
    document.getElementById('quick-label').textContent = t.quickLabel;
    document.getElementById('welcome-msg').textContent = t.welcomeMsg;
    document.getElementById('instruction-msg').textContent = t.instructionMsg;
    document.getElementById('user-input').placeholder = t.inputPlaceholder;
    document.getElementById('hint-text').textContent = t.hintText;
}

/**
 * Send message to server
 */
async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    // Add user message to chat
    addMessage(query, 'user');
    userInput.value = '';

    // Show typing indicator
    const typingId = showTypingIndicator();

    try {
        // First check if it's a greeting
        const greetResponse = await fetch('/api/greet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, language: currentLanguage })
        });
        const greetData = await greetResponse.json();

        if (greetData.is_greeting) {
            removeTypingIndicator(typingId);
            addMessage(greetData.response, 'bot');
            return;
        }

        // Classify the query
        const response = await fetch('/api/classify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query, language: currentLanguage })
        });
        const result = await response.json();

        removeTypingIndicator(typingId);

        // Update DFA visualization
        updateDFAVisualization(result);

        // Add bot response
        addResultMessage(result);

    } catch (error) {
        removeTypingIndicator(typingId);
        addMessage('Error processing your query. Please try again.', 'bot');
        console.error('Error:', error);
    }
}

/**
 * Add a message to the chat
 */
function addMessage(content, type) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}-message`;

    const avatar = type === 'user' ? '&#128100;' : '&#129302;';
    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    messageDiv.innerHTML = `
        <div class="message-avatar">
            <span>${avatar}</span>
        </div>
        <div class="message-content">
            <div class="message-bubble">
                <p>${content}</p>
            </div>
            <span class="message-time">${time}</span>
        </div>
    `;

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Add a result message with classification details
 */
function addResultMessage(result) {
    const t = translations[currentLanguage];
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message bot-message';

    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const statusClass = result.is_accepted ? 'accept' : 'reject';
    const statusText = result.is_accepted ? t.accept : t.reject;

    let serviceHTML = '';
    if (result.is_accepted && result.service) {
        const s = result.service;
        serviceHTML = `
            <div class="service-info">
                <h4>${t.serviceName} ${s.name}</h4>
                <p><strong>${t.description}</strong> ${s.description}</p>
                <p class="office"><strong>${t.office}</strong> ${s.office}</p>
                <p><strong>${t.website}</strong> <a href="https://${s.website}" target="_blank" class="website">${s.website}</a></p>
                <p><strong>${t.documents}</strong></p>
                <div class="documents">
                    ${s.documents.map(doc => `<span class="doc-tag">${doc}</span>`).join('')}
                </div>
            </div>
        `;
    } else if (result.message) {
        serviceHTML = `<p>${result.message}</p>`;
    }

    messageDiv.innerHTML = `
        <div class="message-avatar">
            <span>&#129302;</span>
        </div>
        <div class="message-content">
            <div class="message-bubble">
                <div class="result-card ${statusClass}">
                    <span class="result-status ${statusClass}">${statusText}</span>
                    <p><strong>${t.stateTransition}</strong></p>
                    <div class="result-transition">${result.transition}</div>
                    ${serviceHTML}
                </div>
            </div>
            <span class="message-time">${time}</span>
        </div>
    `;

    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

/**
 * Update DFA visualization
 */
function updateDFAVisualization(result) {
    // Update current state display
    const stateBadge = document.getElementById('current-state');
    const stateName = document.getElementById('state-name');
    const transitionText = document.getElementById('transition-text');

    stateBadge.textContent = result.state;
    stateName.textContent = result.state_name;
    transitionText.textContent = result.transition;

    // Update badge color
    stateBadge.classList.remove('accept', 'reject');
    if (result.is_accepted) {
        stateBadge.classList.add('accept');
    } else {
        stateBadge.classList.add('reject');
    }

    // Highlight active state node
    document.querySelectorAll('.state-node').forEach(node => {
        node.classList.remove('active', 'animating');
    });

    const activeNode = document.querySelector(`[data-state="${result.state}"]`);
    if (activeNode) {
        activeNode.classList.add('active', 'animating');
    }
}

/**
 * Show typing indicator
 */
function showTypingIndicator() {
    const id = 'typing-' + Date.now();
    const typingDiv = document.createElement('div');
    typingDiv.id = id;
    typingDiv.className = 'message bot-message';
    typingDiv.innerHTML = `
        <div class="message-avatar">
            <span>&#129302;</span>
        </div>
        <div class="message-content">
            <div class="message-bubble">
                <div class="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    `;
    chatMessages.appendChild(typingDiv);
    scrollToBottom();
    return id;
}

/**
 * Remove typing indicator
 */
function removeTypingIndicator(id) {
    const element = document.getElementById(id);
    if (element) {
        element.remove();
    }
}

/**
 * Scroll chat to bottom
 */
function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
