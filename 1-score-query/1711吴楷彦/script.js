window.onload=function(){
  var div=document.getElementById('div');
  if (confirm('开始新投票？')==true){
    div.innerHTML+="<p>投票名称：</p><input type='text' id='title'></br><button text='新建问题' onclick='newQuestion()'>";
  }else if (confirm('投票？')==true){
    div.innerHTML+="title</br>";
    showQuestion();
  }else if (confirm('查看投票结果？')==true){
    showResult();
  };
  function questionType(){
    maxNum=0;
    string[10];
  }
  var question=new questionType[10];
  var i=0;
  function newQuestion(){
    div.innerHTML+="<input type='int' id=Num"+i+">";
  }
}