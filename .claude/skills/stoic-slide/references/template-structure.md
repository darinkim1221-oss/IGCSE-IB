# HTML 뼈대 구조 — Stoic Edu 슬라이드

새 덱을 만들 때 이 뼈대에서 시작한다.

> ⚠️ **절대 규칙:** (1) 모든 학생용 텍스트는 **영어**. (2) **로고 이미지 없음** — 헤더는 텍스트 워드마크 "Prepared by · STOIC EDU"만. 로고 base64/이미지/씰 embed 금지.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>[제목] | Stoic Edu</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR:wght@300;400;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  /* ← base-css.md 내용 전체 붙여넣기 */
</style>
</head>
<body>
<div id="slide-frame">

<!-- ============ COVER ============ -->
<section class="slide active" id="s-cover">
  <div class="cover-bg"></div>
  <div class="cover-left">
    <!-- 개념 시각화 (CSS 애니메이션) -->
  </div>
  <div class="cover-right">
    <div class="cover-module">Module N · Financial Literacy</div>
    <div class="cover-title">[제목]<br><span>[강조 단어]</span></div>
    <div class="cover-divider"></div>
    <div class="cover-tagline">[한 줄 설명]</div>
    <div class="cover-meta">
      <div class="cover-pill">Grade N+</div>
      <div class="cover-pill">Interactive</div>
      <div class="cover-pill">NN min</div>
    </div>
  </div>
</section>

<!-- ============ SLIDE 0: HOOK ============ -->
<section class="slide" id="s0">
  <div class="grid-bg"></div>
  <!-- hook 내용 -->
</section>

<!-- ============ SLIDE 1: 개념 설명 ============ -->
<section class="slide" id="s1">
  <div class="grid-bg"></div>
  <!-- 시각화 + 설명 -->
</section>

<!-- ============ SLIDE 2: 인터랙티브 ============ -->
<section class="slide" id="s2">
  <div class="grid-bg"></div>
  <!-- 계산기 or 시뮬레이터 -->
</section>

<!-- ============ SLIDE N: QUIZ ============ -->
<section class="slide" id="s-quiz">
  <div class="grid-bg"></div>
  <div style="text-align:center; margin-bottom:8px">
    <div class="tag">Final Quiz</div>
    <div class="big-title">How well did you get it? 🧠</div>
  </div>
  <div class="quiz-progress" id="quizProgress"></div>
  <div class="quiz-box" id="quizBox"></div>
  <button class="btn" id="quizNextBtn" style="display:none; margin-top:10px" onclick="nextQuiz()">Next Question →</button>
</section>

<!-- ============ ATTRIBUTION HEADER (텍스트 워드마크만 — 로고 이미지 없음) ============ -->
<div id="logo-header" style="
  position: absolute; top: 14px; left: 20px;
  display: flex; align-items: center; gap: 10px;
  z-index: 200; transition: transform 0.2s;
"
onmouseover="this.style.transform='translateY(-1px)'"
onmouseout="this.style.transform=''">
  <a href="https://stoic-edu.com" target="_blank" rel="noopener noreferrer"
     style="display:flex; align-items:center; gap:9px; text-decoration:none;">
    <span class="prep" style="font-family:'Noto Sans KR',sans-serif; font-size:9px; color:#5a6a80; letter-spacing:0.5px; white-space:nowrap">Prepared by</span>
    <span class="word" style="font-family:'Bebas Neue',sans-serif; font-size:16px; letter-spacing:2px; color:#0d2d52">STOIC EDU</span>
  </a>
</div>

<!-- ============ NAV ============ -->
<div id="nav">
  <button class="nav-btn" onclick="go(-1)">←</button>
  <div class="dot-nav" id="dotNav"></div>
  <span id="slide-counter">1 / N</span>
  <button class="nav-btn" onclick="go(1)">→</button>
</div>

</div><!-- /slide-frame -->

<script>
// ============ SLIDE ENGINE ============
const slides = document.querySelectorAll('.slide');
const dotNav = document.getElementById('dotNav');
const counter = document.getElementById('slide-counter');
let cur = 0;

slides.forEach((_,i) => {
  const d = document.createElement('div');
  d.className = 'dot' + (i===0?' active':'');
  d.onclick = () => goTo(i);
  dotNav.appendChild(d);
});

function go(dir) { goTo(cur + dir); }
function goTo(n) {
  n = Math.max(0, Math.min(slides.length-1, n));
  slides[cur].classList.remove('active');
  dotNav.children[cur].classList.remove('active');
  cur = n;
  slides[cur].classList.add('active');
  dotNav.children[cur].classList.add('active');
  counter.textContent = (cur+1) + ' / ' + slides.length;
  adaptLogo();
  // 슬라이드별 초기화 — 인덱스는 실제 순서에 맞게 수정
  // if(cur === GAME_IDX) initGame();
  // if(cur === QUIZ_IDX) initQuiz();
}

document.addEventListener('keydown', e => {
  if(e.key === 'ArrowRight' || e.key === ' ') go(1);
  if(e.key === 'ArrowLeft') go(-1);
});

// ============ ATTRIBUTION 워드마크 색상 자동 전환 (텍스트만) ============
function adaptLogo() {
  // 어두운 배경 슬라이드 id를 여기에 추가
  const darkSlides = ['s-cover'];
  const isDark = darkSlides.includes(slides[cur].id);
  const header = document.getElementById('logo-header');
  if (!header) return;
  const word = header.querySelector('.word');
  const prep = header.querySelector('.prep');
  if (word) word.style.color = isDark ? '#ffffff' : '#0d2d52';
  if (prep) prep.style.color = isDark ? 'rgba(255,255,255,0.7)' : '#5a6a80';
}
adaptLogo();

// ============ 슬라이드별 기능 함수 아래에 추가 ============
// initGame(), initQuiz(), updateCalc(), revealWinner() 등

</script>
</body>
</html>
```

## 로고에 대하여

**Stoic Edu 로고 파일은 없다.** 로고 이미지를 만들거나 embed하지 않는다.
헤더 attribution은 위 예시처럼 텍스트 워드마크 `Prepared by · STOIC EDU`로만 처리한다.
