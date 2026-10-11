document.getElementById('sendBtn').addEventListener('click', async () => {
  const questionInput = document.getElementById('questionInput');
  const answerBox = document.getElementById('answerBox');
  const errorBox = document.getElementById('errorBox');

  const question = questionInput.value.trim();
  if (!question) {
    errorBox.textContent = 'Сұрақ енгізіңіз.';
    errorBox.style.display = 'block';
    answerBox.style.display = 'none';
    return;
  }

  try {
    const response = await fetch('/ask', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ question })
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || 'Ошибка');
    }

    answerBox.textContent = data.answer;
    answerBox.style.display = 'block';
    errorBox.style.display = 'none';
  } catch (error) {
    errorBox.textContent = error.message || 'Сұрақ жіберу кезінде қателік пайда болды.';
    errorBox.style.display = 'block';
    answerBox.style.display = 'none';
  }
});
