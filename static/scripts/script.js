$(document).ready(function(){
var side_bar_open=false;
	$("#menu_button").click(function(){
		if(side_bar_open){
		$("#full_side_bar").css("transform","translateX(-250px)");
		side_bar_open=false;
		}else{
			$("#full_side_bar").css("transform","translateX(0px)");
			side_bar_open=true;
		}
	});

	$("#full_side_bar").hover(function(){
		$("#full_side_bar").css("transform","translateX(0px)");
			side_bar_open=true;
	},function(){
		$("#full_side_bar").css("transform","translateX(-250px)");
			side_bar_open=false;
	});

	$("#close_tst").click(function(){
		$("#tst_area").css("display","none");
	});

	$(".important").click(function(){
		row_id=$(this).parent().attr("id");
		if($(this).find("img.unstarred").hasClass("hidden")){
			$(this).find("img.unstarred").removeClass("hidden");
			$(this).find("img.starred").addClass("hidden");
			sendSomeToast("Row with rowid: "+row_id+" has been unstarred successfully!");
		}else{
			$(this).find("img.unstarred").addClass("hidden");
			$(this).find("img.starred").removeClass("hidden");
			sendSomeToast("Row with rowid: "+row_id+" has been starred successfully!");
		}
		
	});
	$(".delete_update").click(function(){
		row_id=$(this).parent().attr("id");
		$("#"+row_id).remove();
		sendSomeToast("Row with rowid: "+row_id+" has been deleted successfully!");
	});
	$(".markNew").click(function(){
		row_id=$(this).parent().attr("id");
		$(this).text("Old");

		if($(this).hasClass("new")){
			$(this).removeClass("new");
			$(this).text("Old");
			sendSomeToast("Row with rowid: "+row_id+" has been to OLD update!");
		}else{
			$(this).addClass("new");
			$(this).text("New");
			sendSomeToast("Row with rowid: "+row_id+" has been to NEW update!");
		}
	});
	$(".updateTitle").click(function(){
		isNew=$(this).parent().find(".markNew");
		if(isNew.hasClass("new")){
			$(isNew).removeClass("new");
			$(isNew).text("Old");
		}
	});
});

function sendSomeToast(msg){
	$("#tst_area").css("display","none");
	$("#tst_msg").html(msg);
	$("#tst_area").css("display","block");
}