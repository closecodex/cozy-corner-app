async function fetchCat() {
  const factEl = document.getElementById("cat-fact");
  const imgEl = document.getElementById("cat-img");
  const errEl = document.getElementById("cat-error");
  const loadingEl = document.getElementById("cat-loading");

  errEl.classList.add("cc-hidden");
  loadingEl.classList.remove("cc-hidden");

  try {
    const resp = await fetch("/api/cat");
    if (!resp.ok) throw new Error("Non-OK response");
    const data = await resp.json();

    factEl.textContent = data.fact || "A cat fact has escaped. Please try again.";
    imgEl.src = data.image_url;

    if (data.error) {
      errEl.textContent = data.error;
      errEl.classList.remove("cc-hidden");
    }
  } catch (e) {
    factEl.textContent = "The cats are offline. Consider offering snacks and trying again.";
    errEl.textContent = "Could not reach the cat servers right now.";
    errEl.classList.remove("cc-hidden");
  } finally {
    loadingEl.classList.add("cc-hidden");
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("cat-btn");
  btn.addEventListener("click", fetchCat);
});

