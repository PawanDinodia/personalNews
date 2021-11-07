$(document).ready(function(){
	getCat();

});

function getCat(){
	$.ajax({
		url:"/catagories",
		type:"POST",
		success:function(result){
			populateCats(result);
		}
	});
}
function populateCats(cats){
	cats=JSON.parse(cats);
	number_of_cats=Object.keys(cats).length;
	for(i=0;i<number_of_cats;i++){
		htmlStrng='<li><a href="javascript:void(0);" class="catagory_links" id="'+cats[i][0]+'">&nbsp;&nbsp;'+cats[i][1]+' ('+cats[i][2]+')</a></li>';
		$("#full_side_bar ul").append(htmlStrng);
	}
	bindEvents1();
}
function bindEvents1(){
	$(".catagory_links").click(function(){
		cat_uid=$(this).attr("id");
		$.ajax({
		url:"/getUpdate",
		type:"POST",
		data:{"id":cat_uid},
		success:function(result){
			populateUpdates(JSON.parse(result));
		}
	});
	});
}
function populateUpdates(all_selected_updates){
	create_cat=`
			<div class="update_catagory">
				<div class="cat_heading"><a class="websiteLink" href="http:\\\\`+all_selected_updates["sites"][0]+`" target="_blank">`+all_selected_updates["updateCatagoryTitle"][0]+`</a></div>
			</div>
	`;
		$(".updates_sec").html(create_cat);
		//console.log(all_selected_updates);

	for(i=0;i<all_selected_updates["subcats"].length;i++){
		subcat=all_selected_updates["subcats"][i][0];
		updateLink=all_selected_updates["subcats"][i][1];
		create_subcat=`
			<div class="updateType">
				<a href="`+updateLink+`" target="_blank">`+subcat+`</a>
				<div class="updates">
					<table class="update_table update_table_`+subcat+`">
							<tr>
								<td>Sr. no.
								</td><td class="important_head">Star
								</td><td>Description
								</td><td>Delete
								</td><td>New/Old
								</td>
							</tr>
					</table>
				</div>
			</div>`;
		$(".update_catagory").append(create_subcat);

		no_rows=all_selected_updates["dat"][subcat].length;
		// console.log(no_rows);
		for(k=0;k<no_rows;k++){
			row_dat=all_selected_updates["dat"][subcat][k];
			j=k+1;
			// console.log("generating "+j+"th row for "+subcat);
			starred_class="starred";
			unstarred_class="unstarred hidden";
			if(row_dat[10]==0){
				//unstarred
				starred_class="starred hidden";
				unstarred_class="unstarred";
			}
			markNew_class="markNew new";
			markNew_text="New";
			if(row_dat[9]==0){
				//unstarred
				markNew_class="markNew";
				markNew_text="Old";
			}
			update_rw=`<tr id="`+row_dat[0]+`" class="update_row"><td class="srno">`+j+`</td><td class="important"><img class="`+unstarred_class+`" src="/unstarred_img"><img class="`+starred_class+`" src="/starred_img">
				</td><td class="updateTitle"><a target="_blank" href="`+row_dat[8]+`">`+row_dat[4]+`</a><br>`+row_dat[6]+`
				</td><td class="delete_update"><img src="/del_img">
				</td><td class="`+markNew_class+`">`+markNew_text+`
				</td></tr>`;
			console.log(subcat+"\n"+update_rw);
		$("table.update_table_"+subcat+"").append(update_rw);
		}
	}
	bindEvents2();
}

function bindEvents2(){
	$(".important").click(function(){
		row_id=$(this).parent().attr("id");
		if($(this).find("img.unstarred").hasClass("hidden")){
			$(this).find("img.unstarred").removeClass("hidden");
			$(this).find("img.starred").addClass("hidden");
			$.ajax({
				url:"/starr_change",
				type:"POST",
				data:{"updateId":row_id, "status":0},
				success:function(result){
					console.log(result);
				}
			});
			sendSomeToast("Row with rowid: "+row_id+" has been unstarred successfully!");
		}else{
			$(this).find("img.unstarred").addClass("hidden");
			$(this).find("img.starred").removeClass("hidden");
			$.ajax({
				url:"/starr_change",
				type:"POST",
				data:{"updateId":row_id, "status":1},
				success:function(result){
					console.log(result);
				}
			});
			sendSomeToast("Row with rowid: "+row_id+" has been starred successfully!");
		}
		
	});
	$(".delete_update").click(function(){
		row_id=$(this).parent().attr("id");
		$("#"+row_id).remove();
		$.ajax({
				url:"/delFlagOn",
				type:"POST",
				data:{"updateId":row_id},
				success:function(result){
					console.log(result);
				}
			});
		sendSomeToast("Row with rowid: "+row_id+" has been deleted successfully!");
	});
	$(".markNew").click(function(){
		row_id=$(this).parent().attr("id");

		if($(this).hasClass("new")){
			$(this).removeClass("new");
			$(this).text("Old");
			$.ajax({
				url:"/updateMark",
				type:"POST",
				data:{"updateId":row_id, "status":0},
				success:function(result){
					console.log(result);
				}
			});
			sendSomeToast("Row with rowid: "+row_id+" has been to OLD update!");
		}else{
			$(this).addClass("new");
			$(this).text("New");
			$.ajax({
				url:"/updateMark",
				type:"POST",
				data:{"updateId":row_id, "status":1},
				success:function(result){
					console.log(result);
				}
			});
			sendSomeToast("Row with rowid: "+row_id+" has been to NEW update!");
		}
	});
	$(".updateTitle").click(function(){
		isNew=$(this).parent().find(".markNew");
		row_id=$(this).parent().attr("id");
		if(isNew.hasClass("new")){
			$(isNew).removeClass("new");
			$(isNew).text("Old");
			$.ajax({
				url:"/updateMark",
				type:"POST",
				data:{"updateId":row_id, "status":0},
				success:function(result){
					console.log(result);
				}
			});
		}
	});
}