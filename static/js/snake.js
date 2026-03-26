// snake.js
document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("snake-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  
  const startBtn = document.getElementById("snake-start-btn");
  const initialBtn = document.getElementById("snake-initial-btn");
  const gameOverScreen = document.getElementById("snake-gameover");
  const startScreen = document.getElementById("snake-start-screen");
  const scoreEl = document.getElementById("snake-score");
  
  const gridSize = 20;
  const tileCount = canvas.width / gridSize;
  
  let snake = [];
  let fruit = {x: 0, y: 0};
  let dx = 0;
  let dy = 0;
  let score = 0;
  let loop;
  let isPlaying = false;
  
  function initGame() {
    snake = [{x: 10, y: 10}];
    dx = 1; dy = 0;
    score = 0;
    scoreEl.innerText = score;
    placeFruit();
    gameOverScreen.classList.add("hidden");
    startScreen.classList.add("hidden");
    isPlaying = true;
    
    if (loop) clearInterval(loop);
    loop = setInterval(gameStep, 100);
  }
  
  function placeFruit() {
    fruit.x = Math.floor(Math.random() * tileCount);
    fruit.y = Math.floor(Math.random() * tileCount);
    // ensure fruit not on snake
    for (let s of snake) {
      if (s.x === fruit.x && s.y === fruit.y) {
        placeFruit();
        break;
      }
    }
  }
  
  function gameStep() {
    // move
    let head = {x: snake[0].x + dx, y: snake[0].y + dy};
    
    // wall collision
    if (head.x < 0 || head.x >= tileCount || head.y < 0 || head.y >= tileCount) {
      return gameOver();
    }
    
    // self collision
    for (let i = 0; i < snake.length; i++) {
      if (snake[i].x === head.x && snake[i].y === head.y) {
        return gameOver();
      }
    }
    
    snake.unshift(head);
    
    // eating fruit
    if (head.x === fruit.x && head.y === fruit.y) {
      score += 10;
      scoreEl.innerText = score;
      placeFruit();
    } else {
      snake.pop();
    }
    
    draw();
  }
  
  function draw() {
    ctx.fillStyle = "#111"; // match border
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    
    ctx.fillStyle = "#00e5ff"; // snake color cyan
    for (let s of snake) {
      ctx.fillRect(s.x * gridSize + 1, s.y * gridSize + 1, gridSize - 2, gridSize - 2);
    }
    
    ctx.fillStyle = "#ff0055"; // fruit color pink
    ctx.fillRect(fruit.x * gridSize + 1, fruit.y * gridSize + 1, gridSize - 2, gridSize - 2);
  }
  
  function gameOver() {
    clearInterval(loop);
    isPlaying = false;
    gameOverScreen.classList.remove("hidden");
  }
  
  // Controls
  window.addEventListener("keydown", (e) => {
    if (!isPlaying) return;
    switch (e.key) {
      case "ArrowUp": if (dy !== 1) { dx = 0; dy = -1; } break;
      case "ArrowDown": if (dy !== -1) { dx = 0; dy = 1; } break;
      case "ArrowLeft": if (dx !== 1) { dx = -1; dy = 0; } break;
      case "ArrowRight": if (dx !== -1) { dx = 1; dy = 0; } break;
    }
    // prevent default scrolling
    if(["Space","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {
      e.preventDefault();
    }
  });
  
  startBtn.addEventListener("click", initGame);
  initialBtn.addEventListener("click", initGame);

  // Initial render (blank grid)
  draw();
});
