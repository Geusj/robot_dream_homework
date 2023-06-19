document.addEventListener('DOMContentLoaded', function () {
  // кнопки та елементи
  const addFriendButton = document.getElementById('add-friend-button');
  const friendCountElement = document.getElementById('friend-count');
  const messageButton = document.getElementById('send-message-button');
  const jobButton = document.getElementById('offer-job-button');

  // кількість друзів
  let friendCount = Math.floor(Math.random() * 100);
  friendCountElement.textContent = friendCount.toString();
  addFriendButton.addEventListener('click', addToFriends);
  messageButton.addEventListener('click', sendMessage);
  jobButton.addEventListener('click', offerJob);

  function addToFriends() {
    // Забороняє повторне натискання кнопки
    addFriendButton.disabled = true;
    addFriendButton.textContent = 'Confirmation is pending';

    // Збільшує кількість друзів на 1
    friendCount++;
    friendCountElement.textContent = friendCount.toString();
  }

  function sendMessage() {
    console.log('Write a message');
    changeButtonColor();
  }

  function offerJob() {
    console.log('Offer a job');
    toggleFriendButtonVisibility();
  }

  function changeButtonColor() {
    const button = document.getElementById('send-message-button');
    const colors = ['red', 'blue'];
    const currentColor = button.style.backgroundColor;
    const randomColor = colors[Math.floor(Math.random() * colors.length)];

    if (currentColor !== randomColor) {
      button.style.backgroundColor = randomColor;
    } else {
      button.style.backgroundColor = '';
    }
  }

  function toggleFriendButtonVisibility() {
    if (addFriendButton.style.display === 'none') {
      addFriendButton.style.display = 'block';
      addFriendButton.textContent = 'Add to friends';
    } else {
      addFriendButton.style.display = 'none';
    }
  }

  //  додавання рядка в таблицю
  const submitHomeworkButton = document.getElementById('submit-homework-button');
  const homeworkTable = document.getElementById('homework-table');

  submitHomeworkButton.addEventListener('click', submitHomework);

  function submitHomework() {
    const taskNumber = 'Task 1'; // Замініть начення на текст завдання
    const assessment = '10'; // Замініть значення на оцінку

    const newRow = document.createElement('tr');
    const taskNumberCell = document.createElement('td');
    const assessmentCell = document.createElement('td');

    taskNumberCell.textContent = taskNumber;
    assessmentCell.textContent = assessment;

    newRow.appendChild(taskNumberCell);
    newRow.appendChild(assessmentCell);

    homeworkTable.querySelector('tbody').appendChild(newRow);
  }
});
