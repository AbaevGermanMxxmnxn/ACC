const views = [...document.querySelectorAll(".view")];
const navButtons = [...document.querySelectorAll("[data-view]")];

function showView(name) {
  views.forEach(v => v.classList.toggle("active", v.id === name));
  navButtons.forEach(b => b.classList.toggle("active", b.dataset.view === name));
}

navButtons.forEach(button => {
  button.addEventListener("click", () => showView(button.dataset.view));
});

document.querySelectorAll(".tile[data-view]").forEach(tile => {
  tile.addEventListener("click", () => showView(tile.dataset.view));
});

function updateClock() {
  const d = new Date();
  document.getElementById("clock").textContent =
    d.toLocaleTimeString("en-GB", {hour12:false});
}
setInterval(updateClock, 1000);
updateClock();

async function loadApplications() {
  const list = document.getElementById("applicationList");
  try {
    // The MVP does not yet expose a list endpoint, so show the demo dataset.
    // Individual records can be loaded through GET /api/v1/applications/{id}.
    const demo = [
      {id:"APP-1042", client:"Иван Иванов", amount:"500 000 ₽", score:850, status:"APPROVED"},
      {id:"APP-1041", client:"Пётр Петров", amount:"700 000 ₽", score:550, status:"REJECTED"},
      {id:"APP-1040", client:"Анна Смирнова", amount:"320 000 ₽", score:750, status:"APPROVED"},
      {id:"APP-1039", client:"Алексей Орлов", amount:"900 000 ₽", score:650, status:"SCORING"}
    ];
    list.innerHTML = demo.map(a => `
      <div class="app-row">
        <div class="app-id">${a.id}</div>
        <div class="app-name"><b>${a.client}</b><small>CONSUMER LOAN</small></div>
        <div class="app-money">${a.amount}</div>
        <div class="app-score">${a.score}</div>
        <div class="status ${a.status.toLowerCase()}">${a.status}</div>
      </div>
    `).join("");
    document.getElementById("totalCount").textContent = "31";
  } catch (e) {
    list.innerHTML = '<div class="empty">APPLICATION SERVICE UNAVAILABLE</div>';
  }
}
loadApplications();

const modal = document.getElementById("modal");
document.getElementById("newApplication").addEventListener("click", () => {
  modal.classList.remove("hidden");
});
document.getElementById("modalClose").addEventListener("click", () => {
  modal.classList.add("hidden");
});
modal.addEventListener("click", e => {
  if (e.target === modal) modal.classList.add("hidden");
});

document.getElementById("applicationForm").addEventListener("submit", async e => {
  e.preventDefault();
  const form = new FormData(e.target);
  const payload = Object.fromEntries(form.entries());
  payload.monthly_income = Number(payload.monthly_income);
  payload.requested_amount = Number(payload.requested_amount);
  payload.term_months = Number(payload.term_months);

  const result = document.getElementById("formResult");
  result.textContent = "PROCESSING...";

  try {
    const response = await fetch("/api/v1/applications", {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });
    const data = await response.json();

    if (!response.ok) {
      result.textContent = data.detail
        ? JSON.stringify(data.detail)
        : "VALIDATION ERROR";
      return;
    }

    result.innerHTML = `APPLICATION <b>#${data.id}</b> → <b>${data.status}</b>, SCORE <b>${data.score}</b>`;
    loadApplications();
  } catch {
    result.textContent = "API CONNECTION ERROR";
  }
});

document.getElementById("lock").addEventListener("click", () => {
  document.body.innerHTML = `
    <div style="height:100vh;display:grid;place-items:center;background:#373936;color:#ef6900;font-family:Inter,Arial">
      <div style="text-align:center"><div style="font-size:45px">▣</div><div style="letter-spacing:4px;font-size:12px;margin-top:12px">LEX LOCKED</div><div style="font-size:8px;color:#aaa;margin-top:8px">RELOAD PAGE TO RETURN</div></div>
    </div>`;
});

document.getElementById("searchInput").addEventListener("input", e => {
  const q = e.target.value.toLowerCase();
  document.querySelectorAll(".app-row").forEach(row => {
    row.style.display = row.textContent.toLowerCase().includes(q) ? "grid" : "none";
  });
});
