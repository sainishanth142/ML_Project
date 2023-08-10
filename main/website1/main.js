var title=document.getElementById('title');

// firebase
//       .database()
//       .ref("Registration/" + Date.now())
//       .set({
//         name: name,
//         user: username,
//         gender: gender,
//       });


const messageForm = document.getElementById("message-form");
const messageInput = document.getElementById("message-input");
const messages = document.getElementById("messages");

firebase
    .database()
    .ref("output/")
    .on("value", function (snapshot) {
      // title.innerHTML=snapshot.val();
      messages.innerHTML+=("<div class='message-container-s'><div class='message-s'><p class='message-content-s'>"+snapshot.val()+"</p></div></div>");
      
    });
    firebase
    .database()
    .ref("speech/input/")
    .on("value", function (snapshot) {
      // title.innerHTML=snapshot.val();
      messages.innerHTML+=("<div class='message-container'><div class='message'><p class='message-content'>"+snapshot.val()+"</p></div></div>");

    });
messageForm.addEventListener("submit", e => {
    e.preventDefault();
    if (messageInput.value) {
    messages.innerHTML+=("<div class='message-container'><div class='message'><p class='message-content'>"+messageInput.value+"</p></div></div>");
    // socket.emit("chat message", messageInput.value);
    firebase
    .database()
    .ref("question/value")
    .set(messageInput.value);
    firebase
    .database()
    .ref("question/done")
    .set(0);
    messageInput.value = "";
    
    }
});

// socket.on("chat message", message => {
//     const li = document.createElement("li");
//     li.textContent = message;
//     messages.appendChild(li);
// });
