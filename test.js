var c=0
var t

function timedCount()
 {
      document.getElementById('txt').value=c
      c=c+1
      t=setTimeout("timedCount()",1000)
    
      if(t%5==0){
        alert(t)
      }
}

function stopCount()
 {
 clearTimeout(t)
 }