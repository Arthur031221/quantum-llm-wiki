// 簡報播放：← → 空白鍵換頁、點按鈕換頁、網址 #3 直接跳到第 3 張，舞台依視窗大小縮放。
(function () {
  const slides = Array.from(document.querySelectorAll(".slide"));
  const deck = document.getElementById("deck");
  const counter = document.getElementById("counter");
  const bar = document.querySelector("#progress div");
  let cur = 0;

  function fit() {
    const s = Math.min(window.innerWidth / 1280, (window.innerHeight - 60) / 720);
    deck.style.transform = `translate(-50%, -50%) translate(0, -20px) scale(${s})`;
  }

  function show(i) {
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach((el, k) => el.classList.toggle("active", k === cur));
    counter.textContent = `${cur + 1} / ${slides.length}`;
    bar.style.width = `${((cur + 1) / slides.length) * 100}%`;
    history.replaceState(null, "", `#${cur + 1}`);
  }

  document.getElementById("prev").addEventListener("click", () => show(cur - 1));
  document.getElementById("next").addEventListener("click", () => show(cur + 1));
  document.addEventListener("keydown", (e) => {
    if (["ArrowRight", "PageDown", " "].includes(e.key)) { e.preventDefault(); show(cur + 1); }
    if (["ArrowLeft", "PageUp"].includes(e.key)) { e.preventDefault(); show(cur - 1); }
    if (e.key === "Home") show(0);
    if (e.key === "End") show(slides.length - 1);
  });
  let x0 = null;
  document.addEventListener("touchstart", (e) => { x0 = e.touches[0].clientX; });
  document.addEventListener("touchend", (e) => {
    if (x0 === null) return;
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 40) show(cur + (dx < 0 ? 1 : -1));
    x0 = null;
  });

  window.addEventListener("resize", fit);
  fit();
  show((parseInt(location.hash.slice(1), 10) || 1) - 1);
})();
