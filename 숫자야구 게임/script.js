// 게임 상태 및 초기화
const game = {
    attempts: 9,
    targetNumbers: [],
    resultDisplay: document.querySelector(".result-display"),
    attemptsDOM: document.getElementById("attempts"),

    // 게임 초기화
    initialize() {
        this.attempts = 9;
        this.targetNumbers = this.generateTargetNumbers();
        this.resultDisplay.innerHTML = "";
        this.attemptsDOM.innerText = this.attempts;

        document.querySelector(".submit-button").disabled = false;
        document.getElementById("game-result-img").src = "";
        document.getElementById("number1").value = "";
        document.getElementById("number2").value = "";
        document.getElementById("number3").value = "";
    },

    // 랜덤 숫자 3개 생성 (중복 방지)
    generateTargetNumbers() {
        const digits = new Set();
        while (digits.size < 3) {
            const randomDigit = Math.floor(Math.random() * 10);
            digits.add(randomDigit);
        }
        return Array.from(digits);
    },

    // 입력된 숫자와 정답 비교
    evaluateResult(inputNumbers) {
        const result = {
            strikes: 0,
            balls: 0
        };

        for (let i = 0; i < 3; i++) {
            if (inputNumbers[i] === this.targetNumbers[i]) {
                result.strikes += 1;
            } else if (this.targetNumbers.includes(inputNumbers[i])) {
                result.balls += 1;
            }
        }

        return result;
    },

    // 결과 HTML 업데이트
    renderResult(inputNumbers, result) {
        const resultText = result.strikes === 0 && result.balls === 0
            ? `<span class="num-result out">O</span>`
            : `${result.strikes} <span class="num-result strike">S</span> ${result.balls} <span class="num-result ball">B</span>`;

        const inputSpan = document.createElement("span");
        inputSpan.className = "num-result";
        inputSpan.innerText = `${inputNumbers.join(" ")}`;

        const divider = document.createElement("span");
        divider.innerText = ":";

        const resultSpan = document.createElement("span");
        resultSpan.className = "num-result";
        resultSpan.innerHTML = resultText;

        const resultContainer = document.createElement("div");
        resultContainer.className = "check-result";
        resultContainer.appendChild(inputSpan);
        resultContainer.appendChild(divider);
        resultContainer.appendChild(resultSpan);

        this.resultDisplay.appendChild(resultContainer);
    },

    // 게임 종료 처리
    endGame(isSuccess) {
        const submitButton = document.querySelector(".submit-button");
        submitButton.disabled = true;

        const resultImage = document.getElementById("game-result-img");
        resultImage.src = isSuccess ? "success.png" : "fail.png";
    },

    // 입력값 검증 및 처리
    validateAndProcessInput() {
        const inputBoxes = [
            document.getElementById("number1"),
            document.getElementById("number2"),
            document.getElementById("number3")
        ];

        const inputValues = inputBoxes.map(input => input.value.trim());
        if (inputValues.some(value => isNaN(value) || value === "")) {
            inputBoxes.forEach(input => (input.value = ""));
            alert("숫자만 입력해주세요.");
            return;
        }

        const inputNumbers = inputValues.map(Number);
        const result = this.evaluateResult(inputNumbers);

        // 입력 박스 비우기
        inputBoxes.forEach(input => (input.value = ""));

        // 결과 업데이트
        this.renderResult(inputNumbers, result);

        // 정답 확인
        if (result.strikes === 3) {
            this.endGame(true);
            return;
        }

        // 남은 시도 횟수 감소
        this.attempts -= 1;
        this.attemptsDOM.innerText = this.attempts;

        // 게임 종료 조건 확인
        if (this.attempts === 0) {
            this.endGame(false);
        }
    }
};

document.addEventListener("DOMContentLoaded", () => {
    game.initialize();

    document.querySelector(".submit-button").addEventListener("click", () => {
        game.validateAndProcessInput();
    });
});
