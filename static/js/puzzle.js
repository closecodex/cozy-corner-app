document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("puzzle");
  const uploadInput = document.getElementById("image-upload");
  const gridSizeSelect = document.getElementById("grid-size");
  const shuffleBtn = document.getElementById("shuffle");

  const defaultImage = container.dataset.image;
  let currentImage = defaultImage;
  let cols = 4, rows = 3; // default for 12 pieces
  let order = [];
  let solved = [];
  let selectedIndex = null;

  function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
  }

  function loadPuzzle() {
    // Determine grid size based on selection
    const pieces = parseInt(gridSizeSelect.value, 10);
    if (pieces === 12) { cols = 4; rows = 3; }
    else if (pieces === 20) { cols = 5; rows = 4; }
    else if (pieces === 30) { cols = 6; rows = 5; }

    solved = Array.from({ length: pieces }, (_, i) => i);
    order = [...solved];
    shuffleArray(order);
    
    // Load image to get true aspect ratio and render correctly
    const imgObj = new Image();
    imgObj.onload = () => {
      const aspect = imgObj.width / imgObj.height;
      container.style.aspectRatio = aspect;
      render();
    };
    imgObj.src = currentImage;
  }

  function render() {
    container.style.gridTemplateColumns = `repeat(${cols}, 1fr)`;
    container.style.gridTemplateRows = `repeat(${rows}, 1fr)`;
    container.innerHTML = "";

    order.forEach((idx) => {
      const row = Math.floor(idx / cols);
      const col = idx % cols;

      const tile = document.createElement("div");
      tile.className = "cc-tile";
      tile.dataset.idx = idx.toString();
      tile.style.backgroundImage = `url('${currentImage}')`;
      tile.style.backgroundSize = `${cols * 100}% ${rows * 100}%`;
      tile.style.backgroundPosition = cols > 1 && rows > 1 ? 
        `${(col / (cols - 1)) * 100}% ${(row / (rows - 1)) * 100}%` : '0% 0%';
      container.appendChild(tile);
    });
  }

  function clearSelection() {
    selectedIndex = null;
    container.querySelectorAll(".cc-tile.selected").forEach((el) => el.classList.remove("selected"));
  }

  function checkWin() {
    let isWin = true;
    for (let i = 0; i < order.length; i++) {
      if (order[i] !== solved[i]) {
        isWin = false;
        break;
      }
    }
    
    if (isWin) {
      triggerVictory();
    }
  }

  function triggerVictory() {
    const fanfare = document.getElementById("puzzle-fanfare");
    if (fanfare) {
      fanfare.volume = 0.5;
      fanfare.currentTime = 0;
      fanfare.play().catch(() => {});
      
      setTimeout(() => {
        fanfare.pause();
        fanfare.currentTime = 0;
      }, 3000);
    }
    
    const burst = document.createElement("div");
    burst.className = "victory-burst";
    
    const emojis = ["🎉", "✨", "👏", "🎊", "⭐", "🧩"];
    
    for (let i = 0; i < 35; i++) {
      const particle = document.createElement("div");
      particle.className = "victory-particle";
      particle.textContent = emojis[Math.floor(Math.random() * emojis.length)];
      
      const angle = Math.random() * Math.PI * 2;
      const distance = 80 + Math.random() * 150;
      const tx = Math.cos(angle) * distance;
      const ty = Math.sin(angle) * distance;
      
      particle.style.setProperty("--tx", `${tx}px`);
      particle.style.setProperty("--ty", `${ty}px`);
      particle.style.animationDelay = `${Math.random() * 0.15}s`;
      
      burst.appendChild(particle);
    }
    
    container.style.position = container.style.position === 'static' || !container.style.position ? 'relative' : container.style.position;
    container.appendChild(burst);
    
    setTimeout(() => {
      if (burst.parentNode) burst.remove();
    }, 1500);
  }

  container.addEventListener("click", (e) => {
    const tile = e.target.closest(".cc-tile");
    if (!tile) return;

    const tilePos = Array.from(container.children).indexOf(tile);

    if (selectedIndex === null) {
      selectedIndex = tilePos;
      tile.classList.add("selected");
      return;
    }

    // Swap tiles
    const a = selectedIndex;
    const b = tilePos;
    [order[a], order[b]] = [order[b], order[a]];
    render();
    clearSelection();
    
    // Check if the puzzle is completed after swap
    checkWin();
  });

  uploadInput.addEventListener("change", (e) => {
    const file = e.target.files[0];
    if (file) {
      const url = URL.createObjectURL(file);
      currentImage = url;
      loadPuzzle();
    }
  });

  gridSizeSelect.addEventListener("change", loadPuzzle);

  shuffleBtn.addEventListener("click", () => {
    order = [...solved];
    shuffleArray(order);
    render();
    clearSelection();
  });

  // initial load
  loadPuzzle();
});

