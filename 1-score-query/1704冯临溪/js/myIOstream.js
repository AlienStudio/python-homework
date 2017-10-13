var data=[];
var datalength;
function output_vote_Name(vote_name){
	/*
	 * waiting for edit
	 */
}

function input_vote_Name(){
	/*
	 * Now,this program doesn't have the function to read data form the database
	 * So,I just force to give it some information
	 */
	data[0]=[];
	data[0][0]="投票1";
	data[0][1]="agree";
	data[0][2]="disagree";
	datalength=1;
	var names=[];
	var i;
	for (i=0;i<datalength;i++){
		names[i]=data[i][0]; 
	}
	return names;
}

function input_vote_Options(vote_name){
	var i;
	var x;
	for (i=0;i<data.length;i++){
		if (data[i][1]==vote_name){
			x=i;
			break;
		}
	}
	var options=[];
	for (i=0;i<data[x].length-1;i++){
		options[i]=data[x][i];
	}
	return options;
}

function getAllData(){
	return data;
}
