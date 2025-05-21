window.onload = function () {
    const buttons = document.querySelectorAll("#up, #left, #right, #down, #stop, #start, #a, #b");

    let currentButtonId = null;

    function sendControleData(data) {
        fetch('/controle', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).catch(console.error);
    }

    buttons.forEach(button => {
        button.addEventListener("mousedown", () => {
            currentButtonId = button.id;
            sendControleData({ id: button.id });
        });

        button.addEventListener("mouseup", () => {
            currentButtonId = null;
            sendControleData({});
        });

        button.addEventListener("touchstart", () => {
            currentButtonId = button.id;
            sendControleData({ id: button.id });
        });

        button.addEventListener("touchend", () => {
            currentButtonId = null;
            sendControleData({});
        });
    });

    window.addEventListener("mouseup", () => {
        if (currentButtonId !== null) {
            currentButtonId = null;
            sendControleData({});
        }
    });

    window.addEventListener("touchend", () => {
        if (currentButtonId !== null) {
            currentButtonId = null;
            sendControleData({});
        }
    });
};