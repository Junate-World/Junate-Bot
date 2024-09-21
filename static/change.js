const bot = document.querySelector(".changeImage_1");
const el = document.getElementById("chatButton")

el.addEventListener("click", ()=>{
  if (bot.classList.toggle("changeImage_1")){
      bot.classList.toggle("changeImage_3")
  } else if (bot.classList.toggle("changeImage_2")){
      bot.classList.toggle("changeImage_1")
  } else{
      bot.classList.toggle("changeImage_3")
  }
 
});