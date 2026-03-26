// tictactoe.js
document.addEventListener("DOMContentLoaded", () => {
  const cells = document.querySelectorAll(".ttt-cell");
  if (!cells.length) return;
  const statusEl = document.getElementById("ttt-status");
  const resetBtn = document.getElementById("ttt-reset-btn");
  
  let board = ["", "", "", "", "", "", "", "", ""];
  let currentPlayer = "X";
  let isGameActive = true;
  let fanfarePlayed = false;
  
  const winConditions = [
    [0,1,2], [3,4,5], [6,7,8], // rows
    [0,3,6], [1,4,7], [2,5,8], // cols
    [0,4,8], [2,4,6] // diags
  ];
  
  function handleCellClick(e) {
    if (!isGameActive) return;
    
    const cell = e.target;
    // ensure cell is empty
    if (cell.innerText !== "") return;
    
    const index = parseInt(cell.getAttribute("data-index"));
    
    if (board[index] !== "") return;
    
    board[index] = currentPlayer;
    cell.innerText = currentPlayer;
    cell.classList.add(currentPlayer === "X" ? "x-mark" : "o-mark");
    
    checkResult();
  }
  
  function checkResult() {
    let roundWon = false;
    for (let i = 0; i < winConditions.length; i++) {
      const [a, b, c] = winConditions[i];
      if (board[a] && board[a] === board[b] && board[a] === board[c]) {
        roundWon = true;
        break;
      }
    }
    
    if (roundWon) {
      statusEl.innerText = `Player ${currentPlayer} Wins! 🎉`;
      statusEl.classList.add("pop-win");
      setTimeout(() => statusEl.classList.remove("pop-win"), 500);
      isGameActive = false;
      
      if (!fanfarePlayed) {
        fanfarePlayed = true;
        const fanfare = document.getElementById("ttt-fanfare");
        if (fanfare) {
          fanfare.volume = 0.5;
          fanfare.currentTime = 0;
          fanfare.play().catch(() => {});
          setTimeout(() => {
            fanfare.pause();
            fanfare.currentTime = 0;
          }, 3000);
        }
      }
      return;
    }
    
    if (!board.includes("")) {
      statusEl.innerText = "It's a Draw! 🤝";
      isGameActive = false;
      return;
    }
    
    currentPlayer = currentPlayer === "X" ? "O" : "X";
    statusEl.innerText = `Player ${currentPlayer}'s Turn`;
  }
  
  function resetGame() {
    board = ["", "", "", "", "", "", "", "", ""];
    currentPlayer = "X";
    isGameActive = true;
    fanfarePlayed = false;
    statusEl.innerText = "Player X's Turn";
    cells.forEach(cell => {
      cell.innerText = "";
      cell.classList.remove("x-mark", "o-mark");
    });
  }
  
  cells.forEach(cell => cell.addEventListener("click", handleCellClick));
  resetBtn.addEventListener("click", resetGame);
});
