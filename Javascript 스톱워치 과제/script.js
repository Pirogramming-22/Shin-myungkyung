let startTime = 0; 
let elapsedTime = 0; 
let timerInterval; 

const timeDisplay = document.querySelector('.time'); // 시간
const recordList = document.querySelector('.record-list'); // 기록

function formatTime(time) {
    const seconds = Math.floor(time / 1000);
    const milliseconds = Math.floor((time % 1000) / 10); 
    return `${String(seconds).padStart(2, '0')}:${String(milliseconds).padStart(2, '0')}`;
}

// 스톱워치 시작
function startTimer() {
    if (timerInterval) return; 
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
        elapsedTime = Date.now() - startTime;
        timeDisplay.textContent = formatTime(elapsedTime);
    }, 10); 
}

// 스톱워치 정지
function stopTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
    addRecord(); // 멈출 때 기록 추가
}

// 스톱워치 초기화
function resetTimer() {
    stopTimer();
    elapsedTime = 0;
    timeDisplay.textContent = "00:00";
}

// 기록 추가
function addRecord() {
    const time = formatTime(elapsedTime);
    const listItem = document.createElement('li');
    listItem.textContent = time;
    
    // 삭제 버튼 추가
    const deleteButton = document.createElement('button');
    deleteButton.textContent = '삭제';
    deleteButton.className = 'delete-button';
    deleteButton.onclick = () => listItem.remove(); // 클릭 시 항목 삭제
    
    listItem.appendChild(deleteButton);
    recordList.appendChild(listItem);
}

// 기록 전체 삭제
function clearRecords() {
    recordList.innerHTML = ''; // 기록 리스트 초기화
}

// 이벤트 리스너
document.querySelector('.button-start').addEventListener('click', startTimer);
document.querySelector('.button-stop').addEventListener('click', stopTimer);
document.querySelector('.button-reset').addEventListener('click', resetTimer);
document.querySelector('.clear-all-button').addEventListener('click', clearRecords); // 기록 전체 삭제 이벤트
