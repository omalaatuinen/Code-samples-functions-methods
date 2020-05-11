
  // <textArea> should be on a page with a class='textArea'
    function myFunction() {
      var str = document.querySelector(".textArea");
      let result = 0;
      let h1 = document.querySelector(".h1");
      parsedStr = str.value.split("\n");
    
    
    for (let i of parsedStr) {
     i.trim();
     i = i.replace(",", ".");
     result += i / 100 * 7.5;
    }
     result = result.toFixed();
     h1.innerHTML = result;
    h1.style.color = "#b30000";
    }