const typeWriter = document.getElementById("typewriter-text");
const text = "Lorem ipsum dolor sit amet.";

typeWriter.innerHTML = text;
typeWriter.style.setProperty("--characters", text.length);