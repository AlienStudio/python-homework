window.onload=function(){
  var div=document.getElementById('div');
  if (confirm('��ʼ��ͶƱ��')==true){
    div.innerHTML+="<p>ͶƱ���ƣ�</p><input type='text' id='title'></br><button text='�½�����' onclick='newQuestion()'>";
  }else if (confirm('ͶƱ��')==true){
    div.innerHTML+="title</br>";
    showQuestion();
  }else if (confirm('�鿴ͶƱ�����')==true){
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