#!/usr/bin/env python3
"""Build a Jekyll quiz page from the Number Theory exam-class file.

The live questions use the custom 8-argument command

    \\choice{option a}{option b}{option c}{option d}{a?}{b?}{c?}{d?}

The last four arguments are the answer key: a letter in its own slot
means that option is correct. QR codes, solutions, the prerequisites
PDF, and fully commented questions are ignored.

Usage:
    python3 exam_to_quiz.py
    python3 exam_to_quiz.py "Problems and Exercise Number Theory (NET).tex" nt-quiz.md
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_SRC = HERE / "Problems and Exercise Number Theory (NET).tex"
DEFAULT_DEST = HERE / "nt-quiz.md"

LETTERS = {"a": 0, "b": 1, "c": 2, "d": 3}
MONTHS = (
    ("JANUARY", "JAN"), ("FEBRUARY", "FEB"), ("MARCH", "MAR"), ("APRIL", "APR"),
    ("JUNE", "JUN"), ("JULY", "JUL"), ("AUGUST", "AUG"), ("SEPTEMBER", "SEP"),
    ("OCTOBER", "OCT"), ("NOVEMBER", "NOV"), ("DECEMBER", "DEC"),
)
SCHEMES = {
    "A": (2, -0.5, "+2, wrong −0.5"),
    "B": (3, -0.75, "+3, wrong −0.75"),
    "C": (4.75, 0, "+4.75 if complete, otherwise 0"),
}

PAGE_HEAD = """---
layout: page
permalink: /nt/
title: Number Theory Problems
description: For Problem Solving (NET and NBHM)
nav: false
nav_order: 8
toc:
  sidebar: left
---

<style>
.transcript, .scoreboard, .mode-box, .menu, .quiz, .summary {
  background: var(--global-card-bg-color, #fff);
  color: var(--global-text-color, inherit);
  border: 1px solid var(--global-divider-color, #e5e7eb);
  border-radius: 12px;
}
.transcript {
  margin: 0 0 1.5rem;
  padding: 1rem 1.1rem;
}
.transcript p { margin: 0 0 .7rem; font-weight: 600; }
.transcript input[type="password"] {
  padding: .55rem .7rem;
  border: 1px solid var(--global-divider-color, #c5c9d1);
  border-radius: 8px;
  margin-right: .5rem;
  background: var(--global-bg-color, #fff);
  color: var(--global-text-color, inherit);
}
.transcript button, .quiz button.check, #finish-quiz, .mode label {
  padding: .5rem .9rem;
  border: 0;
  border-radius: 8px;
  background: var(--global-theme-color, #3b82c4);
  color: var(--global-hover-text-color, #fff);
  font-weight: 600;
  cursor: pointer;
}
.quiz .show-solution, #reset-quiz {
  padding: .5rem .9rem;
  border-radius: 8px;
  border: 1px solid var(--global-divider-color, #dbe3ee);
  background: transparent;
  color: var(--global-text-color, inherit);
  font-weight: 600;
  cursor: pointer;
}
.transcript .error {
  display: none;
  margin: .7rem 0 0;
  padding: .55rem .8rem;
  border-radius: 8px;
  background: #f8d7da;
  color: #8b3e46;
}
.mode-box {
  margin: 0 0 1rem;
  padding: 1rem 1.15rem 1.05rem;
  text-align: center;
}
.mode {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .7rem;
  margin: 0;
  padding: 0;
  border: 0;
}
.mode legend { padding: 0; font-weight: 600; }
.mode-choices { display: flex; justify-content: center; gap: .7rem; }
.mode label {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 7.5rem;
  margin: 0;
  border: 1px solid var(--global-divider-color, #dbe3ee);
  background: transparent;
  color: var(--global-text-color, inherit);
}
.mode input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}
.mode label:has(input:checked) {
  background: var(--global-theme-color, #3b82c4);
  color: var(--global-hover-text-color, #fff);
  border-color: transparent;
}
.mode label:focus-within { outline: 2px solid var(--global-theme-color, #3b82c4); outline-offset: 2px; }
.scheme { margin: .85rem 0 0; color: var(--global-text-color-light, #4b5563); }
.layout {
  display: grid;
  grid-template-columns: minmax(0, 220px) minmax(0, 1fr);
  gap: 1rem;
  align-items: start;
}
.menu {
  position: sticky;
  top: .5rem;
  max-height: calc(100vh - 1.5rem);
  overflow: auto;
  padding: .35rem;
}
.menu button {
  display: block;
  width: 100%;
  margin: 0;
  padding: .45rem .6rem;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: inherit;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
}
.menu button[aria-current="true"] { background: color-mix(in srgb, var(--global-theme-color, #3b82c4) 16%, transparent); }
.menu button.right { background: #d4edda; color: #155724; }
.menu button.wrong { background: #f8d7da; color: #8b3e46; }
.menu button.blank { background: #f3f4f6; }
.menu button.saved { box-shadow: inset 3px 0 0 var(--global-theme-color, #3b82c4); }
.quiz { padding: 1.1rem 1.25rem 1.25rem; margin: 0; }
.quiz .ask { margin: .35rem 0 0; color: var(--global-text-color-light, #4b5563); font-weight: 600; }
.quiz .solution {
  margin-top: .8rem;
  padding-top: .8rem;
  border-top: 1px solid var(--global-divider-color, #e5e7eb);
}
@media (max-width: 720px) {
  .layout { grid-template-columns: 1fr; }
  .menu { position: static; max-height: 240px; }
}
.quiz-top { display: flex; justify-content: space-between; gap: 1rem; align-items: baseline; }
.quiz h3 { margin: 0; }
.quiz .worth { color: var(--global-text-color-light, #6b7280); font-size: .9rem; white-space: nowrap; }
.quiz .stem { margin: .7rem 0 .75rem; }
.quiz label {
  display: flex;
  gap: .7rem;
  align-items: flex-start;
  padding: .55rem .7rem;
  border-radius: 8px;
  cursor: pointer;
}
.quiz label:hover { background: color-mix(in srgb, var(--global-theme-color, #3b82c4) 12%, transparent); }
.quiz input { margin-top: .25rem; }
.quiz.graded label { cursor: default; }
.quiz.graded label.key, .quiz.graded label.key:hover { background: #d4edda; }
.quiz.graded label.miss, .quiz.graded label.miss:hover { background: #f8d7da; }
.quiz .result { margin: .7rem 0 0; padding: .55rem .8rem; border-radius: 8px; }
.quiz .ok { background: #d4edda; color: #155724; }
.quiz .bad { background: #f8d7da; color: #8b3e46; }
.quiz .need { background: #fff4d6; color: #7a5b00; }
.scoreboard {
  position: sticky;
  top: .5rem;
  z-index: 5;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem 1rem;
  align-items: center;
  padding: .85rem 1rem;
  margin: 0 0 1rem;
}
.scoreboard strong { font-size: 1.15rem; }
.scoreboard .detail { color: var(--global-text-color-light, #4b5563); }
html[data-theme='dark'] .menu button.right,
html[data-theme='dark'] .quiz.graded label.key,
html[data-theme='dark'] .quiz.graded label.key:hover,
html[data-theme='dark'] .quiz .ok {
  background: #1c3d2a;
  color: #c8f5d4;
}
html[data-theme='dark'] .menu button.wrong,
html[data-theme='dark'] .quiz.graded label.miss,
html[data-theme='dark'] .quiz.graded label.miss:hover,
html[data-theme='dark'] .quiz .bad,
html[data-theme='dark'] .transcript .error {
  background: #4a2428;
  color: #ffd0d4;
}
html[data-theme='dark'] .menu button.blank { background: #2a2d31; color: var(--global-text-color); }
html[data-theme='dark'] .quiz .need { background: #3d3420; color: #ffe7a3; }
html[data-theme='dark'] .summary .got { color: #8fd9a8; }
html[data-theme='dark'] .summary .zero,
html[data-theme='dark'] .summary .neg { color: #f0a8a8; }
.summary { margin: 1.5rem 0 2rem; }
.summary ol { padding-left: 1.3rem; }
.summary li { margin: .25rem 0; }
.summary .got { color: #155724; }
.summary .zero { color: #8b3e46; }
.summary .neg { color: #8b3e46; }
</style>

<section class="mode-box">
  <fieldset class="mode">
    <legend>Mode</legend>
    <div class="mode-choices">
      <label><input type="radio" name="quiz-mode" value="practice" checked> Practice</label>
      <label><input type="radio" name="quiz-mode" value="exam"> Exam</label>
    </div>
  </fieldset>
  <p class="scheme">Part A: +2, wrong −0.5. Part B: +3, wrong −0.75. Part C: +4.75 only when every correct option is selected, otherwise 0. A blank answer scores 0.</p>
</section>

<form class="transcript" onsubmit="return passcheck()">
  <p>To download the Workshop (NWPSM-XIV) session transcript, enter the password.</p>
  <input type="password" id="pass1" required>
  <button type="submit">Download transcript</button>
  <p class="error"></p>
</form>

<div class="scoreboard" id="scoreboard">
  <strong id="score-now">Score: 0</strong>
  <span class="detail" id="score-detail">Check a problem to add its mark.</span>
</div>
"""

PAGE_TAIL = """
<section class="summary" id="quiz-summary" hidden>
  <h2 id="final-score"></h2>
  <p id="final-detail"></p>
  <ol id="mark-list"></ol>
</section>

<p>
  <button type="button" id="finish-quiz">Finish and show total</button>
  <button type="button" class="secondary" id="reset-quiz">Start again</button>
</p>

<script>
const cards = [...document.querySelectorAll(".quiz")];
const menuButtons = [...document.querySelectorAll(".menu button")];
let examOpen = false;

function mode() {
  return document.querySelector('input[name="quiz-mode"]:checked').value;
}

function fmt(n) {
  return (Math.round(n * 100) / 100).toFixed(2).replace(/\.00$/, "").replace(/(\.\d)0$/, "$1");
}

function signed(n) {
  const text = fmt(n);
  if (n > 0) return "+" + text;
  return text.replace("-", "−");
}

function pickedIndexes(card) {
  return [...card.querySelectorAll("input")].flatMap((el, i) => (el.checked ? [i] : []));
}

function showQuestion(index) {
  cards.forEach((card, i) => { card.hidden = i !== index; });
  menuButtons.forEach((button, i) => {
    button.setAttribute("aria-current", i === index ? "true" : "false");
  });
}

function award(card, picked, correct) {
  if (!picked.length) return 0;
  const ok = picked.length === correct.length && picked.every((i) => correct.includes(i));
  return ok ? Number(card.dataset.full) : Number(card.dataset.penalty);
}

function grade(card, fromFinish) {
  const correct = card.dataset.correct.split(",").filter(Boolean).map(Number);
  const picked = pickedIndexes(card);
  const result = card.querySelector(".result");
  const index = cards.indexOf(card);
  if (!picked.length && !fromFinish && card.dataset.graded !== "1") {
    result.hidden = false;
    result.className = "result need";
    result.textContent = "Select an answer first.";
    return;
  }
  if (card.dataset.graded !== "1") {
    card.dataset.graded = "1";
    card.dataset.blank = picked.length ? "0" : "1";
    card.dataset.scored = String(award(card, picked, correct));
    card.querySelectorAll("input").forEach((el) => { el.disabled = true; });
    card.querySelector(".check").disabled = true;
  }
  const open = mode() === "practice" || examOpen;
  const value = Number(card.dataset.scored || 0);
  const button = menuButtons[index];
  button.classList.remove("right", "wrong", "blank", "saved");
  if (!open) {
    button.classList.add("saved");
    result.hidden = false;
    result.className = "result";
    result.textContent = "Saved. Marks stay hidden until you finish.";
    return;
  }
  card.classList.add("graded");
  [...card.querySelectorAll("label")].forEach((label, i) => {
    label.classList.remove("key", "miss");
    if (correct.includes(i)) label.classList.add("key");
    else if (picked.includes(i)) label.classList.add("miss");
  });
  if (card.dataset.blank === "1") button.classList.add("blank");
  else if (value > 0) button.classList.add("right");
  else button.classList.add("wrong");
  result.hidden = false;
  result.className = "result " + (value > 0 ? "ok" : "bad");
  if (card.dataset.blank === "1") result.textContent = "Not answered · 0";
  else if (value > 0) result.textContent = "Correct · " + signed(value);
  else if (value < 0) result.textContent = "Incorrect · " + signed(value);
  else result.textContent = "Incorrect · 0";
  const solution = card.querySelector(".show-solution");
  if (solution) solution.hidden = false;
}

function totals() {
  const possible = cards.reduce((sum, card) => sum + Number(card.dataset.full), 0);
  const earned = cards.reduce((sum, card) => sum + Number(card.dataset.scored || 0), 0);
  const graded = cards.filter((card) => card.dataset.graded === "1").length;
  return {
    possible: Math.round(possible * 100) / 100,
    earned: Math.round(earned * 100) / 100,
    graded: graded
  };
}

function showRunning() {
  const { possible, earned, graded } = totals();
  if (mode() === "exam" && !examOpen) {
    document.getElementById("score-now").textContent = "Answered: " + graded + " / " + cards.length;
    document.getElementById("score-detail").textContent = "Marks stay hidden until you finish.";
    return;
  }
  document.getElementById("score-now").textContent = "Score: " + signed(earned);
  document.getElementById("score-detail").textContent = "Maximum if all correct: " + fmt(possible) + ".";
}

function showFinal() {
  examOpen = true;
  cards.forEach((card) => grade(card, true));
  const { possible, earned } = totals();
  document.getElementById("final-score").textContent = "Total: " + signed(earned);
  document.getElementById("final-detail").textContent = "Maximum if all correct: " + fmt(possible) + ".";
  document.getElementById("mark-list").innerHTML = cards.map((card) => {
    const got = Number(card.dataset.scored || 0);
    const title = card.querySelector("h3").textContent;
    const tone = got > 0 ? "got" : "zero";
    return '<li class="' + tone + '">' + title + " — " + signed(got) + "</li>";
  }).join("");
  document.getElementById("quiz-summary").hidden = false;
  showRunning();
  document.getElementById("score-detail").textContent = "Quiz finished. Maximum if all correct: " + fmt(possible) + ".";
  document.getElementById("quiz-summary").scrollIntoView({ behavior: "smooth", block: "start" });
}

function resetQuiz() {
  examOpen = false;
  cards.forEach((card) => {
    delete card.dataset.graded;
    delete card.dataset.scored;
    delete card.dataset.blank;
    card.classList.remove("graded");
    card.querySelectorAll("input").forEach((el) => { el.disabled = false; el.checked = false; });
    card.querySelector(".check").disabled = false;
    card.querySelectorAll("label").forEach((label) => label.classList.remove("key", "miss"));
    const result = card.querySelector(".result");
    result.hidden = true;
    result.textContent = "";
    result.className = "result";
    const solution = card.querySelector(".show-solution");
    const note = card.querySelector(".solution");
    if (solution) {
      solution.hidden = true;
      solution.textContent = "Show solution";
    }
    if (note) note.hidden = true;
  });
  menuButtons.forEach((button) => button.classList.remove("right", "wrong", "blank", "saved"));
  document.getElementById("quiz-summary").hidden = true;
  showQuestion(0);
  showRunning();
}

cards.forEach((card) => {
  card.querySelector(".check").addEventListener("click", () => {
    grade(card, false);
    showRunning();
  });
  const solution = card.querySelector(".show-solution");
  if (solution) {
    solution.addEventListener("click", () => {
      const note = card.querySelector(".solution");
      note.hidden = !note.hidden;
      solution.textContent = note.hidden ? "Show solution" : "Hide solution";
    });
  }
});
menuButtons.forEach((button, index) => {
  button.addEventListener("click", () => showQuestion(index));
});
document.getElementById("finish-quiz").addEventListener("click", showFinal);
document.getElementById("reset-quiz").addEventListener("click", resetQuiz);
document.querySelectorAll('input[name="quiz-mode"]').forEach((input) => {
  input.addEventListener("change", resetQuiz);
});
showQuestion(0);
showRunning();

function passcheck() {
  const error = document.querySelector(".transcript .error");
  if (document.getElementById("pass1").value !== "NT030226") {
    error.style.display = "block";
    error.textContent = "Incorrect password";
    return false;
  }
  window.open("https://www.dropbox.com/scl/fi/b5jdrqah663mbniyqr3gl/SPU_Workshop_03_Feb_2026_Transcript.pdf?rlkey=14pmnvlzeureb1kc35l7fxd93&st=49w9sy76&dl=1");
  error.style.display = "none";
  return false;
}
</script>
"""


def strip_comments(text):
    kept = []
    for line in text.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                break
            out.append(line[i])
            i += 1
        kept.append("".join(out))
    return "\n".join(kept)


def brace_groups(text, start, count):
    """Read `count` brace groups beginning at or after `start`."""
    groups = []
    i = start
    while len(groups) < count and i < len(text):
        while i < len(text) and text[i].isspace():
            i += 1
        if i >= len(text) or text[i] != "{":
            break
        depth = 0
        j = i
        while j < len(text):
            if text[j] == "\\" and j + 1 < len(text):
                j += 2
                continue
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    groups.append(text[i + 1 : j])
                    i = j + 1
                    break
            j += 1
        else:
            break
    return groups, i


def first_group(text, command):
    match = re.search(r"\\" + command + r"\b", text)
    if not match:
        return None
    groups, _ = brace_groups(text, match.end(), 1)
    return groups[0] if groups else None


def remove_command(text, command):
    pattern = re.compile(r"\\" + command + r"\*?")
    out = []
    i = 0
    while True:
        match = pattern.search(text, i)
        if not match:
            out.append(text[i:])
            break
        out.append(text[i : match.start()])
        j = match.end()
        if j < len(text) and text[j] == "[":
            depth = 1
            j += 1
            while j < len(text) and depth:
                if text[j] == "[":
                    depth += 1
                elif text[j] == "]":
                    depth -= 1
                j += 1
        if j < len(text) and text[j] == "{":
            _, j = brace_groups(text, j, 1)
        i = j
    return "".join(out)


def clean(text):
    text = text.replace(r"\&", "&")
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    text = text.replace("\\\\", "<br>")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip()


def questions(text):
    body = text.split(r"\begin{questions}", 1)
    if len(body) == 2:
        text = body[1].split(r"\end{questions}", 1)[0]
    parts = re.split(r"\\question\b", text)
    for part in parts[1:]:
        choice_at = re.search(r"\\choice\s*\{", part)
        if not choice_at:
            label = first_group(part, "label") or "unlabelled"
            print(f"skipped {label}: no \\choice{{...}}", file=sys.stderr)
            continue
        groups, end = brace_groups(part, choice_at.end() - 1, 8)
        if len(groups) != 8:
            label = first_group(part, "label") or "unlabelled"
            print(f"skipped {label}: found {len(groups)} arguments, expected 8", file=sys.stderr)
            continue
        yield part[: choice_at.start()], groups, part[end:]


def short_name(title):
    name = re.sub(r":\s*$", "", title).strip()
    for long, short in MONTHS:
        name = re.sub(rf"\b{long}\b", short, name, flags=re.I)
    return name


def card(stem_src, groups, rest, number):
    label = first_group(stem_src, "label") or f"q{number}"
    title = first_group(stem_src, "textbf") or label
    stem = remove_command(stem_src, "label")
    stem = remove_command(stem, "textbf")
    stem = remove_command(stem, "hvqrurl")
    stem = stem.replace(r"\bigskip", "")
    options = [clean(item) for item in groups[:4]]
    options = [item for item in options if item]
    correct = []
    for slot in groups[4:]:
        letter = slot.strip().lower()
        if letter in LETTERS and LETTERS[letter] < len(options):
            correct.append(LETTERS[letter])
    if not correct:
        print(f"warning {label}: no correct option marked", file=sys.stderr)
    part = ""
    match = re.search(r"\(([ABC])\)", title)
    if match:
        part = match.group(1)
    if part not in SCHEMES:
        print(f"warning {label}: no part A, B, or C in the title", file=sys.stderr)
        full, penalty, worth = 1, 0, "1 mark"
    else:
        full, penalty, worth = SCHEMES[part]
    kind = "radio" if len(correct) <= 1 else "checkbox"
    ask = "Choose one" if len(correct) <= 1 else "Choose all that apply"
    slug = re.sub(r"[^A-Za-z0-9]+", "-", label).strip("-") or f"q{number}"
    labels = "\n".join(
        f'  <label><input type="{kind}" name="{slug}"> {option}</label>'
        for option in options
    )
    solution = first_group(rest, "soln")
    solution_html = ""
    if solution and clean(solution):
        solution_html = (
            '  <button type="button" class="show-solution" hidden>Show solution</button>\n'
            f'  <div class="solution" hidden>{clean(solution)}</div>\n'
        )
    key = ",".join(str(i) for i in correct)
    hidden = "" if number == 1 else " hidden"
    name = short_name(clean(title))
    html = (
        f'<article class="quiz" id="{slug}" data-correct="{key}" data-kind="{part}" '
        f'data-full="{full}" data-penalty="{penalty}"{hidden}>\n'
        f'  <div class="quiz-top"><h3>{number}. {name}</h3>'
        f'<span class="worth">{worth}</span></div>\n'
        f'  <p class="ask">{ask}</p>\n'
        f'  <div class="stem">{clean(stem)}</div>\n'
        f"{labels}\n"
        f'  <button type="button" class="check">Check</button>\n'
        f"{solution_html}"
        f'  <p class="result" hidden></p>\n'
        f"</article>"
    )
    return {"html": html, "name": name}


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_SRC
    dest = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_DEST
    text = strip_comments(src.read_text(encoding="utf-8"))
    built = [card(stem, groups, rest, n) for n, (stem, groups, rest) in enumerate(questions(text), 1)]
    counts = {}
    for item in built:
        counts[item["name"]] = counts.get(item["name"], 0) + 1
    seen = {}
    buttons = []
    for index, item in enumerate(built):
        name = item["name"]
        if counts[name] > 1:
            seen[name] = seen.get(name, 0) + 1
            name = f"{name} · {seen[name]}"
        current = "true" if index == 0 else "false"
        buttons.append(
            f'<button type="button" aria-current="{current}">{name}</button>'
        )
    page = (
        PAGE_HEAD
        + '<div class="layout">\n<nav class="menu" aria-label="Questions">\n'
        + "\n".join(buttons)
        + '\n</nav>\n<div class="stage">\n{% raw %}\n'
        + "\n".join(item["html"] for item in built)
        + '\n{% endraw %}\n</div>\n</div>\n'
        + PAGE_TAIL
    )
    dest.write_text(page, encoding="utf-8")
    print(f"wrote {len(built)} questions to {dest}")


if __name__ == "__main__":
    main()
