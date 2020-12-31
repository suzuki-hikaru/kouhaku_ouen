// const speech = new webkitSpeechRecognition();
// speech.lang = 'ja-JP';

// const btn = document.getElementById('btn');
// const content = document.getElementById('content');

// btn.addEventListener('click', function () {
//     // 音声認識をスタート
//     speech.start();
// });

// //---------------追記---------------//
// //音声自動文字起こし機能
// speech.onresult = function (e) {
//     speech.stop();
//     if (e.results[0].isFinal) {
//         const date1 = new Date();
//         var autotext = e.results[0][0].transcript
//         timeStamp = date1.getHours() + ":" + date1.getMinutes() + ":" + date1.getSeconds()
//         content.innerHTML += '<div>' + timeStamp + '  ' + autotext + '</div>';
//     }

// }

// speech.onend = () => {
//     speech.start()
// };
//         //--------------------------------//