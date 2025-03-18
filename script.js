document.addEventListener("DOMContentLoaded", function () {
  let tg = window.Telegram.WebApp;
  tg.expand(); // صفحه رو فول اسکرین می‌کنه

  document.getElementById("sendMessage").addEventListener("click", function () {
    tg.sendData("این یک پیام از مینی اپ است!");
  });
});
