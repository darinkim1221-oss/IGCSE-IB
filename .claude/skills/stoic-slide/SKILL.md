---
name: stoic-slide
description: |
  Stoic Edu 표준 HTML 인터랙티브 슬라이드를 만드는 스킬.
  금융/경제 개념을 아이들이 체험할 수 있는 수업용 슬라이드 덱으로 변환한다.
  결과물은 960×540 고정 프레임의 단일 HTML 파일로, 웹사이트 embed 및 프로젝터 수업 모두 지원한다.

  다음 상황에서 반드시 이 스킬을 사용한다:
  - "슬라이드 만들어줘", "수업 자료 만들어줘", "HTML로 만들어줘"
  - Stoic Edu 교재를 HTML로 변환하는 요청
  - 인터랙티브 수업 자료, 프레젠테이션 제작 요청
  - "이 개념을 슬라이드로", "포맷에 맞춰서 만들어줘"
  - 기존 슬라이드에 새 페이지 추가 요청
---

# Stoic Edu 슬라이드 스킬

## 🔴 절대 규칙 (ALWAYS — 예외 없음)

1. **모든 산출물은 영어로 작성한다.** 슬라이드 텍스트, 제목, 설명, 퀴즈, 게임, 피드백 메시지 등 학생이 보는 모든 콘텐츠는 **English only**. (교사와의 대화는 한국어로 해도 되지만, 파일 안의 내용물은 무조건 영어.)
2. **Stoic Edu 로고 파일은 존재하지 않는다.** 로고 이미지를 참조하거나 base64로 embed하거나, 씰/엠블럼 그래픽을 임의로 만들어내지 **않는다**. 헤더 attribution은 순수 텍스트 워드마크("Prepared by · Stoic Edu")로만 처리한다. `[LOGO_BASE64]`, `logo.png`, `logo-img`, 가짜 seal 등은 모두 사용 금지.

---

## 핵심 원칙

아이들의 뇌를 깊이 자극하는 교육 경험을 만든다.
단순한 정보 전달이 아니라 **학생이 직접 조작하고, 놀라고, 발견하는** 구조여야 한다.

---

## 기술 스펙

### 고정 프레임
- **크기**: 960 × 540px (16:9)
- **구조**: `<div id="slide-frame">` 안에 모든 슬라이드 포함
- **반응형**: 화면 비율에 따라 자동 스케일 (CSS aspect-ratio 미디어쿼리)
- **embed**: `<iframe width="960" height="540" src="...">` 로 바로 사용 가능

### 파일 구조
- 단일 HTML 파일 (CSS·JS 모두 인라인)
- **로고 없음** — 헤더 attribution은 텍스트 워드마크로만 (`Prepared by · Stoic Edu`). 로고 이미지/씰 금지 (절대 규칙 2 참조).
- 슬라이드는 `<section class="slide" id="s-cover|s0|s1...">` 로 구성
- 모든 학생용 텍스트는 영어 (절대 규칙 1 참조)

---

## 디자인 시스템

### 색상 (CSS 변수)
```css
:root {
  --bg:     #ffffff;       /* 기본 배경 */
  --gold:   #c8960a;       /* 강조 — Stoic Edu 골드 */
  --gold2:  #e0a800;
  --blue:   #0d2d52;       /* Stoic Edu 남색 (로고와 동일) */
  --teal:   #00897b;       /* 정답/긍정 피드백 */
  --red:    #e53935;       /* 오답/경고 */
  --white:  #1a2340;       /* 본문 텍스트 (어두운 네이비) */
  --dim:    #5a6a80;       /* 보조 텍스트 */
  --card:   #f5f7fa;       /* 카드 배경 */
  --border: rgba(200,150,10,0.25);
}
```

### 폰트
```html
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Noto+Sans+KR:wght@300;400;700;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
```
- **Bebas Neue** — 제목, 숫자, 임팩트 텍스트
- **Noto Sans KR** — 본문, 설명 (한/영 공용)
- **Space Mono** — 태그, 라벨, 데이터 수치

### 공통 컴포넌트 CSS
자세한 CSS는 `references/base-css.md` 참조.

---

## 슬라이드 구조

### 필수 슬라이드 순서
1. **Cover** (`id="s-cover"`) — 표지, 항상 첫 번째
2. **내용 슬라이드** (`id="s0"`, `s1"`, ...) — 개념별 구성
3. **게임/인터랙티브** — 중간에 배치해서 리듬 조절
4. **Quiz** — 마지막에서 두 번째 또는 마지막

### Cover 슬라이드 구조
```
[왼쪽 45% — 남색 배경 + 개념 시각화]  [오른쪽 55% — 흰 배경 + 텍스트]
```
- 왼쪽: 개념을 상징하는 SVG/CSS 애니메이션 (바 차트, 링, 아이콘 등)
- 오른쪽: 모듈명(Space Mono), 제목(Bebas Neue 대형, **영어**), 골드 구분선, 서브타이틀(**영어**), 메타 pill
- `cover-bg`: `linear-gradient(135deg, #0d2d52 0%, #0d2d52 45%, #ffffff 45%)`

### 고정 UI 요소 (모든 슬라이드 공통)
```html
<!-- 좌상단 attribution — 텍스트 워드마크만, 로고 이미지 없음 -->
<div id="logo-header">
  <a href="https://stoic-edu.com" target="_blank" rel="noopener noreferrer">
    <span class="prep">Prepared by</span>
    <span class="word">STOIC EDU</span>
  </a>
</div>

<!-- 우하단 네비게이터 — position: absolute, bottom:14px, right:20px -->
<div id="nav">
  <button onclick="go(-1)">←</button>
  <div class="dot-nav">...</div>
  <span id="slide-counter">1 / N</span>
  <button onclick="go(1)">→</button>
</div>
```
- attribution 워드마크는 슬라이드 배경에 따라 텍스트 **색상만** 자동 전환 (`adaptLogo()` — 어두운 배경=흰색, 밝은 배경=남색). 이미지 filter/invert 아님.
- 키보드 방향키 / 스페이스바로 슬라이드 이동

---

## 슬라이드 타입별 패턴

### 1. Hook 슬라이드 (첫 번째 내용 슬라이드)
**목적**: 예상을 깨는 질문으로 수업 시작
**구조**: 큰 질문 텍스트 + 2-way 선택지 카드 + 정답은 다음 슬라이드로
```html
<div class="hook-question"><span>A</span> vs <span>B</span><br>질문</div>
<div class="hook-vs">
  <div class="vs-card a">...</div>
  <div class="vs-separator">vs</div>
  <div class="vs-card b">...</div>
</div>
<div class="hook-reveal">👇 정답은 다음 슬라이드에...</div>
```

### 2. 개념 설명 슬라이드
**구조**: 좌측 시각화 + 우측 단계별 설명
- 시각화: CSS 애니메이션 (눈덩이, 그래프, 타임라인 등)
- 설명: `section-tag` (Space Mono 소문자) + `big-title` + 단계 리스트
- 팁박스: 골드 왼쪽 보더 + 연한 골드 배경

### 3. 인터랙티브 계산기 슬라이드
**구조**: 좌측 슬라이더 패널 + 우측 실시간 결과
```html
<div class="calc-wrapper">
  <div class="calc-inputs"> <!-- 슬라이더 3개 --> </div>
  <div class="calc-result"> <!-- 금액 + 바 차트 --> </div>
</div>
```
- 슬라이더 조작 시 `oninput` 으로 실시간 업데이트
- 결과 금액: Bebas Neue 대형 + 골드색
- 바 차트: 동적 생성 (JS)

### 4. 스토리 대결 슬라이드 (Reveal)
**구조**: 좌우 인물 카드 + "결과 공개" 버튼
- 버튼 클릭 전: 최종 금액 숨김 (`opacity:0`)
- 클릭 후: 카운트업 애니메이션 + winner 뱃지 + 교훈 박스 표시
```js
function revealWinner() {
  document.getElementById('calebFinal').style.opacity = '1';
  setTimeout(() => {
    document.getElementById('calebCard').classList.add('winner');
    document.getElementById('winnerLesson').style.display = 'block';
  }, 800);
}
```

### 5. 미니 게임 슬라이드
**구조**: 질문 표시 → 4지선다 버튼 → 정답/오답 피드백 → 자동 다음 문제
- 점수 / 연속정답(streak) / 라운드 카운터 표시
- 정답: teal 색상 + `.correct` 클래스 + pop 애니메이션
- 오답: red 색상 + `.wrong` 클래스 + shake 애니메이션
- 1.8초 후 자동으로 다음 문제

### 6. 개념 대비 슬라이드 (두 얼굴)
**구조**: 좌우 2패널
- 왼쪽: 경고/부정적 측면 (red 상단 바)
- 오른쪽: 긍정적 측면 (teal 상단 바)
- 각 패널: 아이콘 + 강조 제목 + 설명 텍스트

### 7. 최종 퀴즈 슬라이드
**구조**: 진행도 점 표시 → 문제 박스 → 클릭 후 해설 노출 → 다음 문제
- 5문제 권장
- 정답 클릭 후 `quiz-explain` 박스 자동 표시
- 마지막 문제 후 점수 화면 + "다시 풀기" 버튼

---

## 애니메이션 & 인터랙션 가이드

```css
/* 슬라이드 전환 */
.slide { transition: opacity 0.5s ease; }

/* 등장 애니메이션 */
@keyframes fadeUp {
  from { opacity:0; transform: translateY(12px); }
  to   { opacity:1; transform: translateY(0); }
}

/* 정답 */
@keyframes pop {
  0%,100% { transform: scale(1); }
  50%     { transform: scale(1.15); }
}

/* 오답 */
@keyframes shake {
  0%,100% { transform: translateX(0); }
  25%     { transform: translateX(-8px); }
  75%     { transform: translateX(8px); }
}

/* 카운트업 */
@keyframes countUp {
  from { opacity:0; transform: translateY(20px); }
  to   { opacity:1; transform: translateY(0); }
}
```

---

## 슬라이드 JS 엔진 (공통)

```js
const slides = document.querySelectorAll('.slide');
let cur = 0;

function goTo(n) {
  n = Math.max(0, Math.min(slides.length-1, n));
  slides[cur].classList.remove('active');
  dotNav.children[cur].classList.remove('active');
  cur = n;
  slides[cur].classList.add('active');
  dotNav.children[cur].classList.add('active');
  counter.textContent = (cur+1) + ' / ' + slides.length;
  adaptLogo();
  // 특정 슬라이드에서 초기화
  if(cur === GAME_SLIDE_IDX) initGame();
  if(cur === QUIZ_SLIDE_IDX) initQuiz();
}

// 로고 색상 자동 전환
function adaptLogo() {
  const darkSlides = ['s-cover']; // 어두운 배경 슬라이드 id 목록
  const isDark = darkSlides.includes(slides[cur].id);
  const img = document.getElementById('logo-img');
  if (!img) return;
  img.style.filter = isDark ? 'brightness(0) invert(1)' : 'none';
  img.previousElementSibling.style.color = isDark ? 'rgba(255,255,255,0.7)' : '#5a6a80';
}
```

---

## 제작 체크리스트

새 슬라이드 덱 만들 때 확인:

- [ ] Cover 슬라이드: 왼쪽 시각화 개념과 연결돼 있는가?
- [ ] Hook 슬라이드: 예상을 깨는 질문인가?
- [ ] 최소 1개 인터랙티브 요소 (계산기 / 게임 / reveal)
- [ ] 모든 슬라이드 내용이 960×540 안에 들어오는가?
- [ ] 퀴즈 마지막에 해설 포함되어 있는가?
- [ ] **모든 학생용 텍스트가 영어인가?** (절대 규칙 1)
- [ ] **로고 이미지/씰이 없고, 텍스트 워드마크만 쓰였는가?** (절대 규칙 2)
- [ ] attribution `adaptLogo()` — 어두운 배경 슬라이드 id 목록 업데이트했는가?
- [ ] 게임/퀴즈 슬라이드 인덱스 (`GAME_SLIDE_IDX`, `QUIZ_SLIDE_IDX`) 맞는가?

---

## 참고 파일

- `references/base-css.md` — 공통 CSS 전체 (복사해서 시작점으로 사용)
- `references/template-structure.md` — 슬라이드 HTML 뼈대 구조

새 덱을 만들 때는 `references/base-css.md`를 먼저 읽고 시작한다.
