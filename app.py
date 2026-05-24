import streamlit as st
from crew import analyze_startup

st.set_page_config(page_title="Stratiq", page_icon="🎯", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Geist:wght@300;400;500&display=swap');

#MainMenu, header, footer { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="stDecoration"] { display: none; }

html, body, [class*="css"] {
    font-family: 'Geist', sans-serif;
    background-color: #111110;
    color: #f0ede6;
}
.stApp { background-color: #111110; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 4rem !important;
    max-width: 720px;
}
.s-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 2rem 0;
    border-bottom: 1px solid #1e1e1c;
    margin-bottom: 6rem;
}
.s-logo {
    font-family: 'Instrument Serif', serif;
    font-size: 1.5rem;
    color: #f0ede6;
    letter-spacing: -0.5px;
}
.s-logo em { color: #d4a853; font-style: italic; }
.s-nav-tag {
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #555550;
}
.s-title {
    font-family: 'Instrument Serif', serif;
    font-size: 5.5rem;
    line-height: 1.0;
    letter-spacing: -3px;
    color: #f0ede6;
    text-align: center;
    font-weight: 400;
    margin-bottom: 1.5rem;
}
.s-title em { color: #d4a853; font-style: italic; }
.s-sub {
    font-size: 14px;
    color: #888880;
    line-height: 1.9;
    text-align: center;
    margin-bottom: 3rem;
    font-weight: 300;
    max-width: 380px;
    margin-left: auto;
    margin-right: auto;
}
.s-pills {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 1.2rem;
    margin-bottom: 4rem;
}
.s-pill {
    background: transparent;
    border: 1px solid #2a2a28;
    color: #666660;
    font-size: 11px;
    padding: 6px 16px;
    border-radius: 100px;
}
.s-divider {
    border: none;
    border-top: 1px solid #1e1e1c;
    margin: 0 0 3.5rem;
}
.s-result-eyebrow {
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #555550;
    margin-bottom: 2.5rem;
}
.s-tldr {
    border-left: 2px solid #d4a853;
    padding: 1.2rem 1.8rem;
    margin-bottom: 2.5rem;
}
.s-tldr-tag {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #d4a853;
    margin-bottom: 10px;
}
.s-tldr-text {
    font-family: 'Instrument Serif', serif;
    font-size: 1.2rem;
    line-height: 1.7;
    color: #c8c4bc;
}
.s-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    background: #1e1e1c;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 3rem;
}
.s-stat { background: #111110; padding: 1.8rem 1.5rem; text-align: center; }
.s-stat-n {
    font-family: 'Instrument Serif', serif;
    font-size: 2rem;
    color: #f0ede6;
    line-height: 1;
}
.s-stat-l {
    font-size: 10px;
    color: #555550;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-top: 6px;
}
.s-section {
    font-size: 10px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #555550;
    margin-bottom: 1.2rem;
    margin-top: 2.5rem;
}
.r-comp-grid {
    display: flex;
    flex-direction: column;
    border: 1px solid #1e1e1c;
    border-radius: 14px;
    overflow: hidden;
    margin-bottom: 1rem;
}
.r-comp-card {
    background: #0c0c0b;
    padding: 1rem 1.5rem;
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    border-bottom: 1px solid #1a1a18;
}
.r-comp-card:last-child { border-bottom: none; }
.r-comp-num {
    font-family: 'Instrument Serif', serif;
    font-size: 1.1rem;
    color: #2a2a28;
    min-width: 24px;
    line-height: 1.5;
}
.r-comp-name {
    font-size: 13px;
    color: #c8c4bc;
    font-weight: 500;
    margin-bottom: 3px;
}
.r-comp-flaw {
    font-size: 12px;
    color: #666660;
    font-weight: 300;
    line-height: 1.7;
}
.r-gaps { margin-bottom: 1rem; }
.r-gap-row {
    display: flex;
    gap: 1.5rem;
    align-items: flex-start;
    padding: 1.2rem 0;
    border-bottom: 1px solid #1a1a18;
}
.r-gap-row:last-child { border-bottom: none; }
.r-gap-num {
    font-family: 'Instrument Serif', serif;
    font-size: 1.8rem;
    color: #1e1e1c;
    min-width: 34px;
    line-height: 1;
}
.r-gap-title {
    font-size: 13px;
    color: #c8c4bc;
    font-weight: 500;
    margin-bottom: 3px;
}
.r-gap-desc {
    font-size: 12px;
    color: #666660;
    line-height: 1.8;
    font-weight: 300;
}
.r-strat {
    background: #0c0c0b;
    border: 1px solid #1e1e1c;
    border-radius: 14px;
    padding: 1.5rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
    margin-bottom: 1rem;
}
.r-strat-row {
    display: flex;
    gap: 1.2rem;
    align-items: flex-start;
}
.r-strat-dot {
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: #d4a853;
    margin-top: 9px;
    flex-shrink: 0;
}
.r-strat-title {
    font-size: 13px;
    color: #c8c4bc;
    font-weight: 500;
    margin-bottom: 2px;
}
.r-strat-desc {
    font-size: 12px;
    color: #666660;
    line-height: 1.8;
    font-weight: 300;
}
div[data-testid="stTextInput"] input {
    background: #0c0c0b !important;
    border: 1px solid #1e1e1c !important;
    border-radius: 12px !important;
    color: #f0ede6 !important;
    font-family: 'Geist', sans-serif !important;
    font-size: 14px !important;
    font-weight: 300 !important;
    padding: 18px 20px !important;
    height: auto !important;
}
div[data-testid="stTextInput"] input::placeholder { color: #444440 !important; }
div[data-testid="stTextInput"] input:focus {
    border-color: #d4a853 !important;
    box-shadow: none !important;
}
div[data-testid="stTextInput"] label { display: none !important; }
div[data-testid="stButton"] button {
    background: #d4a853 !important;
    color: #111110 !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Geist', sans-serif !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 0.75rem 0 !important;
    width: 100% !important;
    margin-top: 0.5rem !important;
}
div[data-testid="stButton"] button:hover { background: #e0b86a !important; }
div[data-testid="stDownloadButton"] button {
    background: transparent !important;
    color: #555550 !important;
    border: 1px solid #1e1e1c !important;
    border-radius: 10px !important;
    font-size: 11px !important;
    letter-spacing: 1px !important;
    width: 100% !important;
    margin-top: 1rem !important;
}
div[data-testid="stExpander"] {
    background: #0c0c0b !important;
    border: 1px solid #1e1e1c !important;
    border-radius: 12px !important;
}
div[data-testid="stExpander"] summary {
    color: #555550 !important;
    font-size: 11px !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}
</style>
""", unsafe_allow_html=True)

# ── NAV ──
st.markdown("""
<div class="s-nav">
  <div class="s-logo">strat<em>iq</em></div>
  <div class="s-nav-tag">AI Market Intelligence</div>
</div>
""", unsafe_allow_html=True)

# ── HERO ──
st.markdown("""
<div class="s-title">Your market,<br><em>decoded.</em></div>
<div class="s-sub">Type a startup idea. Get competitors, market gaps, and a winning strategy — in under 2 minutes.</div>
""", unsafe_allow_html=True)

# ── INPUT + BUTTON ──
startup_idea = st.text_input(
    "idea",
    placeholder="e.g. Online tuition app for Class 10 students in tier-2 cities",
    label_visibility="collapsed"
)
analyze = st.button("Analyze my market →")

st.markdown("""
<div class="s-pills">
  <span class="s-pill">Cloud kitchen · Delhi</span>
  <span class="s-pill">Women cab · Bangalore</span>
  <span class="s-pill">AgriTech · Punjab</span>
  <span class="s-pill">Salon booking · Mumbai</span>
</div>
<hr class="s-divider">
""", unsafe_allow_html=True)

# ── RESULTS ──
if analyze:
    if startup_idea:
        with st.spinner("Agents are working..."):
            result = analyze_startup(startup_idea)

        result_text = str(result)
        lines = [l.strip() for l in result_text.split('\n') if l.strip()]
        tldr = ' '.join(lines[:2]) if lines else result_text[:300]

        st.markdown(f"""
        <div class="s-result-eyebrow">Analysis · {startup_idea[:60]}</div>
        <div class="s-tldr">
          <div class="s-tldr-tag">TL;DR</div>
          <div class="s-tldr-text">{tldr}</div>
        </div>
        <div class="s-stats">
          <div class="s-stat"><div class="s-stat-n">3</div><div class="s-stat-l">Agents</div></div>
          <div class="s-stat"><div class="s-stat-n">Live</div><div class="s-stat-l">Web Search</div></div>
          <div class="s-stat"><div class="s-stat-n">Now</div><div class="s-stat-l">Generated</div></div>
        </div>
        """, unsafe_allow_html=True)

        # Parse sections
        sections = {}
        current = "overview"
        sections[current] = []
        keywords = {
            "competitor": "competitors", "rival": "competitors", "player": "competitors",
            "gap": "gaps", "opportunit": "gaps", "missing": "gaps", "underserv": "gaps",
            "strateg": "strategy", "position": "strategy", "recommend": "strategy",
            "target": "strategy", "value proposition": "strategy",
            "pricing": "strategy", "feature": "strategy",
        }
        for line in lines:
            low = line.lower()
            matched = False
            for kw, sec in keywords.items():
                if kw in low and len(line) < 80:
                    current = sec
                    sections.setdefault(current, [])
                    matched = True
                    break
            if not matched and line:
                sections.setdefault(current, []).append(line)

        # Competitors
        comp_lines = sections.get("competitors", [])
        if comp_lines:
            cards_html = ""
            for i, line in enumerate(comp_lines[:6]):
                if len(line) > 15:
                    parts = line.split('—') if '—' in line else line.split('-')
                    name = parts[0].strip() if len(parts) > 1 else f"Competitor {i+1}"
                    desc = parts[1].strip() if len(parts) > 1 else line
                    cards_html += f"""
                    <div class="r-comp-card">
                        <div class="r-comp-num">0{i+1}</div>
                        <div>
                            <div class="r-comp-name">{name}</div>
                            <div class="r-comp-flaw">{desc}</div>
                        </div>
                    </div>"""
            if cards_html:
                st.markdown(f"""
                <div class="s-section">Competitors found</div>
                <div class="r-comp-grid">{cards_html}</div>
                """, unsafe_allow_html=True)

        # Gaps
        gap_lines = sections.get("gaps", [])
        if gap_lines:
            gaps_html = ""
            for i, line in enumerate(gap_lines[:4]):
                if len(line) > 15:
                    parts = line.split('—') if '—' in line else line.split(':')
                    title = parts[0].strip() if len(parts) > 1 else f"Gap {i+1}"
                    desc = parts[1].strip() if len(parts) > 1 else line
                    gaps_html += f"""
                    <div class="r-gap-row">
                        <div class="r-gap-num">0{i+1}</div>
                        <div>
                            <div class="r-gap-title">{title}</div>
                            <div class="r-gap-desc">{desc}</div>
                        </div>
                    </div>"""
            if gaps_html:
                st.markdown(f"""
                <div class="s-section">Market gaps nobody is filling</div>
                <div class="r-gaps">{gaps_html}</div>
                """, unsafe_allow_html=True)

        # Strategy
        strat_lines = sections.get("strategy", [])
        if strat_lines:
            strat_html = ""
            for line in strat_lines[:5]:
                if len(line) > 15:
                    parts = line.split('—') if '—' in line else line.split(':')
                    title = parts[0].strip() if len(parts) > 1 else ""
                    desc = parts[1].strip() if len(parts) > 1 else line
                    strat_html += f"""
                    <div class="r-strat-row">
                        <div class="r-strat-dot"></div>
                        <div>
                            <div class="r-strat-title">{title}</div>
                            <div class="r-strat-desc">{desc}</div>
                        </div>
                    </div>"""
            if strat_html:
                st.markdown(f"""
                <div class="s-section">Your winning strategy</div>
                <div class="r-strat">{strat_html}</div>
                """, unsafe_allow_html=True)

        with st.expander("View full report"):
            st.markdown(
                f'<div style="color:#666660;font-size:13px;line-height:2;white-space:pre-wrap;font-weight:300">{result_text}</div>',
                unsafe_allow_html=True)

        st.download_button(
            label="Download report",
            data=result_text,
            file_name="stratiq_report.txt",
            mime="text/plain"
        )
    else:
        st.warning("Please enter a startup idea first.")