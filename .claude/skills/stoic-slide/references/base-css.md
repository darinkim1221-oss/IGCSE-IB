# Base CSS — Stoic Edu 슬라이드 표준

새 슬라이드 덱을 만들 때 이 CSS를 `<style>` 태그 안에 그대로 복사해서 시작한다.
로고 base64는 실제 파일에서 교체 필요.

```css
:root {
    --bg: #ffffff;
    --gold: #c8960a;
    --gold2: #e0a800;
    --blue: #0d2d52;
    --teal: #00897b;
    --red: #e53935;
    --white: #1a2340;
    --dim: #5a6a80;
    --card: #f5f7fa;
    --card2: #eef1f6;
    --border: rgba(200,150,10,0.25);
  }

  * { margin:0; padding:0; box-sizing:border-box; }

  body {
    background: #e8eaed;
    color: var(--white);
    font-family: 'Noto Sans KR', sans-serif;
    overflow: hidden;
    height: 100vh;
    width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* ===== FIXED SLIDE FRAME (16:9) ===== */
  #slide-frame {
    position: relative;
    width: 960px;
    height: 540px;
    background: var(--bg);
    border-radius: 12px;
    box-shadow: 0 8px 40px rgba(0,0,0,0.18);
    overflow: hidden;
    flex-shrink: 0;
  }

  /* Scale to fit viewport while maintaining 16:9 */
  @media (max-aspect-ratio: 16/9) {
    #slide-frame {
      width: 100vw;
      height: calc(100vw * 9 / 16);
      border-radius: 0;
    }
  }
  @media (min-aspect-ratio: 16/9) {
    #slide-frame {
      height: 100vh;
      width: calc(100vh * 16 / 9);
      border-radius: 0;
    }
  }

  /* ===== SLIDE ENGINE ===== */
  .slide {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 56px 44px 42px 44px;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.5s ease;
    overflow: hidden;
    box-sizing: border-box;
  }
  .slide.active {
    opacity: 1;
    pointer-events: all;
  }

  /* Background patterns */
  .slide::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 20% 50%, rgba(21,101,192,0.04) 0%, transparent 60%),
                radial-gradient(ellipse at 80% 20%, rgba(200,150,10,0.05) 0%, transparent 50%);
    pointer-events: none;
  }

  /* ===== NAV ===== */
  #nav {
    position: absolute;
    bottom: 14px;
    right: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    z-index: 100;
    background: rgba(255,255,255,0.92);
    backdrop-filter: blur(10px);
    border: 1px solid var(--border);
    border-radius: 50px;
    padding: 7px 16px;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
  }

  .nav-btn {
    background: none;
    border: none;
    color: var(--dim);
    font-size: 14px;
    cursor: pointer;
    transition: color 0.2s;
    line-height: 1;
  }
  .nav-btn:hover { color: var(--gold); }

  #slide-counter {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--dim);
    min-width: 36px;
    text-align: center;
  }

  .dot-nav {
    display: flex;
    gap: 4px;
  }
  .dot {
    width: 5px; height: 5px;
    border-radius: 50%;
    background: var(--dim);
    transition: all 0.3s;
    cursor: pointer;
  }
  .dot.active {
    background: var(--gold);
    width: 14px;
    border-radius: 3px;
  }

  /* ===== SLIDE 0: HOOK ===== */
  #s0 { text-align: center; }

  .hook-question {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(28px, 4.2vw, 52px);
    line-height: 1;
    letter-spacing: 2px;
    margin-bottom: 10px;
  }
  .hook-question span { color: var(--gold); }

  .hook-vs {
    display: flex;
    gap: 28px;
    margin: 12px 0;
    align-items: stretch;
  }

  .vs-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 16px 28px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    text-align: center;
    flex: 1;
    max-width: 280px;
    position: relative;
    overflow: hidden;
  }
  .vs-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 3px;
  }
  .vs-card.a::after { background: var(--blue); }
  .vs-card.b::after { background: var(--gold); }

  .vs-label {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--dim);
    margin-bottom: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .vs-amount {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 30px;
    margin-bottom: 4px;
  }
  .vs-card.a .vs-amount { color: var(--blue); }
  .vs-card.b .vs-amount { color: var(--gold); }

  .vs-desc {
    font-size: 12px;
    color: var(--dim);
    line-height: 1.6;
  }

  .vs-separator {
    display: flex;
    align-items: center;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px;
    color: var(--dim);
  }

  .hook-reveal {
    font-size: 16px;
    color: var(--teal);
    opacity: 0;
    animation: fadeUp 0.8s ease 1.5s forwards;
    letter-spacing: 1px;
  }

  @keyframes fadeUp {
    from { opacity:0; transform: translateY(12px); }
    to { opacity:1; transform: translateY(0); }
  }

  /* ===== SLIDE 1: HOW IT WORKS ===== */
  #s1 { flex-direction: row; gap: 48px; }

  .snowball-container {
    position: relative;
    width: 200px;
    height: 200px;
    flex-shrink: 0;
  }

  .snow-circle {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 35%, rgba(255,255,255,0.2), transparent 60%),
                radial-gradient(circle at center, var(--c1), var(--c2));
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Space Mono', monospace;
    font-weight: 700;
    color: var(--white);
    transition: all 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    box-shadow: 0 0 30px var(--glow);
  }

  .snow-base {
    --c1: #1a3a6e; --c2: #0d2040; --glow: rgba(13,45,82,0.35);
    width: 100px; height: 100px;
    bottom: 6px; left: 50%;
    transform: translateX(-50%);
    font-size: 15px;
    color: #ffffff;
    text-shadow: 0 1px 4px rgba(0,0,0,0.4);
    box-shadow: 0 0 40px rgba(26,143,255,0.35), 0 4px 20px rgba(0,0,0,0.15);
  }
  .snow-y1 { --c1: #1a4a7a; --c2: #0d2a52; --glow: rgba(13,45,82,0.4); }
  .snow-y2 { --c1: #c8a800; --c2: #7a6000; --glow: rgba(245,200,66,0.4); }
  .snow-y3 { --c1: #f5c842; --c2: #c8920a; --glow: rgba(245,200,66,0.6); }

  .year-balls { position: absolute; inset: 0; }

  .how-content {
    flex: 1;
    max-width: 520px;
  }

  .section-tag {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--gold);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 8px;
  }

  .big-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(28px, 4vw, 48px);
    line-height: 1;
    margin-bottom: 20px;
  }

  .year-steps { display: flex; flex-direction: column; gap: 0; }

  .year-step {
    display: flex;
    align-items: center;
    gap: 20px;
    padding: 7px 12px;
    border-left: 2px solid rgba(255,255,255,0.05);
    position: relative;
    cursor: pointer;
    transition: all 0.3s;
    border-radius: 0 12px 12px 0;
  }
  .year-step:hover, .year-step.highlight {
    background: rgba(245,200,66,0.05);
    border-left-color: var(--gold);
  }

  .step-year {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--dim);
    width: 48px;
    flex-shrink: 0;
  }
  .step-bar {
    height: 28px;
    background: linear-gradient(90deg, var(--gold), var(--gold2));
    border-radius: 4px;
    transition: width 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
    display: flex;
    align-items: center;
    padding-right: 10px;
    justify-content: flex-end;
  }
  .step-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 18px;
    color: var(--bg);
  }
  .step-formula {
    font-size: 13px;
    color: var(--dim);
    margin-left: 8px;
    font-family: 'Space Mono', monospace;
  }

  /* ===== SLIDE 2: CALCULATOR ===== */
  #s2 { flex-direction: column; }

  .calc-wrapper {
    display: flex;
    gap: 28px;
    align-items: flex-start;
    width: 100%;
    max-width: 1000px;
  }

  .calc-inputs {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 16px 20px;
    width: 290px;
    flex-shrink: 0;
  }

  .input-group {
    margin-bottom: 10px;
  }
  .input-label {
    font-size: 12px;
    color: var(--dim);
    margin-bottom: 6px;
    display: block;
    letter-spacing: 0.5px;
  }
  .input-label span { color: var(--gold); }

  .slider-wrap {
    position: relative;
  }
  input[type=range] {
    width: 100%;
    -webkit-appearance: none;
    height: 4px;
    background: rgba(255,255,255,0.1);
    border-radius: 2px;
    outline: none;
    margin-bottom: 6px;
  }
  input[type=range]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 20px; height: 20px;
    border-radius: 50%;
    background: var(--gold);
    cursor: pointer;
    box-shadow: 0 0 10px rgba(245,200,66,0.5);
  }

  .slider-val {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 24px;
    color: var(--gold);
  }

  .calc-result {
    flex: 1;
  }

  .result-main {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 14px 20px;
    margin-bottom: 8px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .result-main::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 100%, rgba(200,150,10,0.06), transparent 70%);
  }

  .result-label {
    font-size: 13px;
    color: var(--dim);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }
  .result-amount {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(24px, 3vw, 40px);
    color: var(--gold);
    line-height: 1;
    transition: all 0.4s;
  }
  .result-sub {
    font-size: 12px;
    color: var(--teal);
    margin-top: 6px;
  }

  .chart-bars {
    display: flex;
    align-items: flex-end;
    gap: 4px;
    height: 90px;
    padding: 0 4px;
    background: var(--card);
    border-radius: 16px;
    border: 1px solid var(--border);
    padding: 16px 20px 10px;
    position: relative;
  }
  .chart-bar {
    flex: 1;
    border-radius: 3px 3px 0 0;
    transition: height 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
    min-height: 4px;
  }

  /* ===== SLIDE 3: CALEB vs BLAIR ===== */
  #s3 { flex-direction: column; gap: 32px; }

  .story-header {
    text-align: center;
    margin-bottom: 6px;
  }

  .vs-timeline {
    display: flex;
    gap: 24px;
    width: 100%;
    max-width: 1000px;
  }

  .person-card {
    flex: 1;
    background: var(--card);
    border-radius: 14px;
    padding: 14px 16px;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(0,0,0,0.07); box-shadow: 0 2px 16px rgba(0,0,0,0.06);
    transition: border-color 0.5s;
  }
  .person-card.winner { border-color: var(--gold); }

  .person-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
  }
  .caleb-card::before { background: var(--gold); }
  .blair-card::before { background: var(--blue); }

  .person-name {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px;
    margin-bottom: 4px;
  }
  .caleb-card .person-name { color: var(--gold); }
  .blair-card .person-name { color: var(--blue); }

  .person-subtitle {
    font-size: 11px;
    color: var(--dim);
    margin-bottom: 6px;
    letter-spacing: 1px;
  }

  .timeline-bar {
    display: flex;
    height: 18px;
    border-radius: 9px;
    overflow: hidden;
    margin-bottom: 6px;
    background: rgba(255,255,255,0.05);
  }
  .timeline-segment {
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-family: 'Space Mono', monospace;
    transition: width 0.8s;
  }
  .seg-invest { background: var(--gold); color: var(--bg); }
  .seg-invest-b { background: var(--blue); color: white; }
  .seg-wait { background: rgba(255,255,255,0.08); color: var(--dim); }

  .timeline-labels {
    display: flex;
    justify-content: space-between;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    color: var(--dim);
    margin-bottom: 4px;
  }

  .person-stats {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .stat-row {
    display: flex;
    justify-content: space-between;
    font-size: 11px;
    padding: 3px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }
  .stat-key { color: var(--dim); }
  .stat-val { font-family: 'Space Mono', monospace; font-weight: 700; }
  .caleb-card .stat-val { color: var(--gold); }
  .blair-card .stat-val { color: var(--blue); }

  .final-amount {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px;
    margin-top: 12px;
    text-align: center;
  }
  .caleb-card .final-amount { color: var(--gold); }
  .blair-card .final-amount { color: var(--blue); }

  .winner-badge {
    position: absolute;
    top: 16px; right: 16px;
    background: var(--gold);
    color: var(--bg);
    font-family: 'Bebas Neue', sans-serif;
    font-size: 14px;
    padding: 4px 12px;
    border-radius: 20px;
    opacity: 0;
    transition: opacity 0.5s;
  }
  .caleb-card.winner .winner-badge { opacity: 1; }

  .lesson-box {
    background: linear-gradient(135deg, rgba(245,200,66,0.08), rgba(245,200,66,0.03));
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px 24px;
    text-align: center;
    max-width: 700px;
    font-size: 13px;
    line-height: 1.6;
    color: var(--white);
  }
  .lesson-box strong { color: var(--gold); }

  /* ===== SLIDE 4: RULE OF 72 GAME ===== */
  #s4 { flex-direction: column; gap: 32px; }

  .game-header { text-align: center; }

  .game-arena {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 24px 32px;
    max-width: 680px;
    width: 100%;
    text-align: center;
  }

  .game-question {
    font-size: 14px;
    color: var(--dim);
    margin-bottom: 8px;
    min-height: 28px;
  }
  .game-scenario {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 32px;
    color: var(--white);
    margin-bottom: 16px;
    line-height: 1.2;
    min-height: 56px;
  }
  .game-scenario span { color: var(--gold); }

  .answer-options {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 12px;
  }

  .ans-btn {
    background: rgba(0,0,0,0.03);
    border: 2px solid rgba(0,0,0,0.1);
    color: var(--white);
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    padding: 10px 24px;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.2s;
    min-width: 80px;
  }
  .ans-btn:hover {
    border-color: var(--gold);
    color: var(--gold);
    transform: translateY(-3px);
  }
  .ans-btn.correct {
    background: rgba(0,229,192,0.15);
    border-color: var(--teal);
    color: var(--teal);
    animation: pop 0.4s ease;
  }
  .ans-btn.wrong {
    background: rgba(255,71,87,0.15);
    border-color: var(--red);
    color: var(--red);
    animation: shake 0.4s ease;
  }

  @keyframes pop {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.15); }
  }
  @keyframes shake {
    0%,100% { transform: translateX(0); }
    25% { transform: translateX(-8px); }
    75% { transform: translateX(8px); }
  }

  .game-feedback {
    font-size: 15px;
    min-height: 24px;
    transition: all 0.3s;
    font-family: 'Space Mono', monospace;
  }
  .game-feedback.right { color: var(--teal); }
  .game-feedback.wrong { color: var(--red); }

  .score-display {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 16px;
  }
  .score-item { text-align: center; }
  .score-num {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 28px;
    color: var(--gold);
  }
  .score-lbl {
    font-size: 11px;
    color: var(--dim);
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  /* ===== SLIDE 5: DARK SIDE ===== */
  #s5 { flex-direction: column; gap: 32px; }

  .dark-split {
    display: flex;
    gap: 14px;
    max-width: 1000px;
    width: 100%;
  }

  .dark-card {
    flex: 1;
    background: var(--card);
    border-radius: 14px;
    padding: 14px 18px;
    border: 1px solid rgba(255,71,87,0.2);
    position: relative;
  }
  .dark-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--red);
  }
  .bright-card {
    flex: 1;
    background: var(--card);
    border-radius: 14px;
    padding: 14px 18px;
    border: 1px solid rgba(0,229,192,0.2);
    position: relative;
  }
  .bright-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--teal);
  }

  .side-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 22px;
    margin-bottom: 10px;
  }
  .dark-card .side-title { color: var(--red); }
  .bright-card .side-title { color: var(--teal); }

  .habit-item {
    display: flex;
    gap: 14px;
    margin-bottom: 7px;
    align-items: flex-start;
  }
  .habit-icon {
    font-size: 20px;
    flex-shrink: 0;
    width: 28px;
    text-align: center;
  }
  .habit-text { font-size: 12px; line-height: 1.5; color: var(--dim); }
  .habit-text strong { color: var(--white); display: block; margin-bottom: 2px; }

  /* ===== SLIDE 6: QUIZ ===== */
  #s6 { flex-direction: column; gap: 32px; }

  .quiz-progress {
    display: flex;
    gap: 6px;
    justify-content: center;
    margin-bottom: 8px;
  }
  .q-dot {
    width: 32px; height: 4px;
    border-radius: 2px;
    background: rgba(255,255,255,0.1);
    transition: background 0.3s;
  }
  .q-dot.done { background: var(--teal); }
  .q-dot.current { background: var(--gold); }

  .quiz-box {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 14px 28px;
    max-width: 700px;
    width: 100%;
    text-align: center;
  }

  .quiz-q {
    font-size: 20px;
    line-height: 1.6;
    margin-bottom: 12px;
    min-height: 28px;
  }
  .quiz-q span { color: var(--gold); }

  .quiz-options {
    display: flex;
    flex-direction: column;
    gap: 7px;
  }

  .quiz-opt {
    background: rgba(0,0,0,0.02);
    border: 1px solid rgba(0,0,0,0.1);
    color: var(--white);
    padding: 10px 18px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 13px;
    text-align: left;
    transition: all 0.2s;
    font-family: 'Noto Sans KR', sans-serif;
  }
  .quiz-opt:hover { border-color: var(--gold); color: var(--gold); }
  .quiz-opt.correct { background: rgba(0,229,192,0.1); border-color: var(--teal); color: var(--teal); }
  .quiz-opt.wrong { background: rgba(255,71,87,0.1); border-color: var(--red); color: var(--red); }

  .quiz-explain {
    margin-top: 20px;
    padding: 7px 12px;
    background: rgba(245,200,66,0.06);
    border-radius: 12px;
    font-size: 14px;
    color: var(--dim);
    line-height: 1.7;
    display: none;
  }
  .quiz-explain.show { display: block; }
  .quiz-explain strong { color: var(--gold); }

  .quiz-score-final {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 60px;
    color: var(--gold);
    text-align: center;
  }
  .quiz-score-msg {
    font-size: 18px;
    color: var(--dim);
    text-align: center;
    margin-top: 8px;
  }

  /* ===== UTILITIES ===== */
  .tag {
    display: inline-block;
    background: rgba(245,200,66,0.1);
    border: 1px solid var(--border);
    color: var(--gold);
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    padding: 3px 10px;
    border-radius: 20px;
    margin-bottom: 8px;
    text-transform: uppercase;
  }

  .btn {
    background: var(--gold);
    color: var(--bg);
    border: none;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 15px;
    letter-spacing: 1px;
    padding: 10px 28px;
    border-radius: 50px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn:hover {
    background: #fff;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(245,200,66,0.3);
  }

  /* Grid pattern overlay */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: linear-gradient(rgba(0,0,0,0.04) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(0,0,0,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
  }

  /* Animated number */
  @keyframes countUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .pulse { animation: pulse 2s infinite; }
  @keyframes pulse {
    0%,100% { opacity:1; }
    50% { opacity:0.6; }
  }

  /* ===== COVER SLIDE ===== */
  #s-cover { flex-direction: row; gap: 0; padding: 0; overflow: hidden; }

  /* Full navy left panel */
  .cover-left {
    position: relative;
    z-index: 1;
    width: 42%;
    height: 100%;
    background: #0d2d52;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }

  /* Subtle dot grid on navy */
  .cover-left::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.12) 1px, transparent 1px);
    background-size: 28px 28px;
  }

  .cover-rings {
    position: absolute;
    inset: 0;
    overflow: hidden;
  }
  .ring {
    position: absolute;
    border-radius: 50%;
    border: 1px solid rgba(255,255,255,0.07);
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
  }
  .r1 { width: 320px; height: 320px; }
  .r2 { width: 230px; height: 230px; }
  .r3 { width: 150px; height: 150px; }

  .cover-chart {
    position: relative;
    z-index: 2;
    display: flex;
    align-items: flex-end;
    gap: 9px;
    height: 150px;
  }
  .c-bar {
    width: 26px;
    background: rgba(255,255,255,0.2);
    border-radius: 4px 4px 0 0;
    animation: barRise 0.5s ease backwards;
  }
  .c-bar:nth-child(1) { animation-delay: 0.15s; }
  .c-bar:nth-child(2) { animation-delay: 0.25s; }
  .c-bar:nth-child(3) { animation-delay: 0.35s; }
  .c-bar:nth-child(4) { animation-delay: 0.45s; }
  .c-bar:nth-child(5) { animation-delay: 0.55s; }
  .c-bar:nth-child(6) { animation-delay: 0.65s; background: var(--gold) !important; }

  @keyframes barRise {
    from { transform: scaleY(0); transform-origin: bottom; opacity: 0; }
    to   { transform: scaleY(1); transform-origin: bottom; opacity: 1; }
  }

  /* Curved right edge on navy panel */
  .cover-left::after {
    content: '';
    position: absolute;
    right: -32px;
    top: 0; bottom: 0;
    width: 64px;
    background: #0d2d52;
    border-radius: 0 50% 50% 0 / 0 30% 30% 0;
    z-index: 2;
  }

  /* Full white right panel */
  .cover-right {
    position: relative;
    z-index: 1;
    flex: 1;
    height: 100%;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 44px 44px 44px 52px;
  }

  .cover-module {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 14px;
    animation: fadeUp 0.5s ease 0.3s backwards;
  }

  .cover-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: clamp(38px, 5.5vw, 66px);
    line-height: 1;
    color: #0d2d52;
    margin-bottom: 18px;
    animation: fadeUp 0.5s ease 0.45s backwards;
  }
  .cover-title span {
    color: var(--gold);
    display: block;
  }

  .cover-divider {
    width: 44px;
    height: 3px;
    background: var(--gold);
    border-radius: 2px;
    margin-bottom: 14px;
    animation: fadeUp 0.5s ease 0.55s backwards;
  }

  .cover-tagline {
    font-size: 13px;
    line-height: 1.7;
    color: var(--dim);
    margin-bottom: 22px;
    max-width: 340px;
    animation: fadeUp 0.5s ease 0.65s backwards;
  }

  .cover-meta {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    animation: fadeUp 0.5s ease 0.75s backwards;
  }
  .cover-pill {
    background: rgba(13,45,82,0.06);
    border: 1px solid rgba(13,45,82,0.14);
    color: #0d2d52;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 1px;
    padding: 5px 12px;
    border-radius: 20px;
    text-transform: uppercase;
  }
```
