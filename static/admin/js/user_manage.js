// JavaScript Document
function change(obj)
{
	var tex=$(obj).parent().prev().text();
	$(obj).parent().prev().html('');
	var id=$(obj).parent().prev().attr('id');
    $(obj).parent().prev().html('<form action="/app/admin/save_user" method="post" ><input type="text" value="'+tex+'" class="edit_input" name="password" id="pwd"><input type="hidden"  name="id" value="'+id+'"><input type="submit"  value="保存" onclick="return check()"> <input type="button" onclick="cancel(this,\''+tex+'\')" value="取消"></button></form>');
	$("input:first").focus();
	$(obj).hide();
	
}

function cancel(obj,str)
	{
	   $(obj).parent().parent().next().children().show();
       $(obj).parent().parent().html(str);
	}
	
function cancel_comment(obj,str)
{
	$(obj).parent().parent().next().next().children().next().show();
	$(obj).parent().parent().html(str);
}
	
function delete_cid(obj)
{
	var ajaxurl="{:U('admin/del_user')}";
	var cid=$(obj).parent().prev().attr('id');
	if(confirm("删除用户也会删除用户发表内容！！是否继续？"))
		{	
		$.post(ajaxurl,{'id':cid},function(data)
		{
			if(data="删除成功")
               {
				   
				   $(obj).parent().parent().remove();
				   alert(data);
		       }
			 else
			 {
				 alert(data);
			 }
				   
    });	                                                    //这里先后顺序可能会产生Bug
	}
}

function add_user(obj)
{                                                      //增加用法代码脚本
    
	$(".table").append('<form action="/app/admin/add_user" method="post"><span>用户名:</span><input id="user" type="text" class="add_input" name="user"><span>发文单位:</span><input type="text" class="add_input" name="comment" id="comment"><span>密码:</span><input type="text" class="add_input" id="pwd" name="password"><input type="submit" value="保存" onclick="return check()"><input type="button" onclick="return cancel_add(this)" value="取消"></form>');
	//表单提交按钮没有响应。
	$(".table input:first").focus();
}

function check()
{
if($("#user").val()=='')
	{
		alert("用户名不能为空");
		$("#user").focus();
		return false;
	}
	else if($("#pwd").val().length<8)
	{
		alert("密码不能低于8位");
		$("#pwd").focus();
		return false;
	}
	else
	if($("#comment").val()=='')
	{
		alert("发文单位不能为空");
		$("#comment").focus();
		return false;
	}		
	else
	return true;
}
function check_comment()
{
	if($("#comment_change").val()=='')
	{
		alert("发文单位不能为空");
		$("#comment_change").focus();
		return false;
	}	
}
function cancel_add(obj)
{
	$(".table form").remove();
	return false;
}


function change_comment(obj)
{
	var tex=$(obj).parent().prev().prev().text();
	$(obj).parent().prev().prev().html('');
	var id=$(obj).parent().prev().prev().attr('id');
	$(obj).parent().prev().prev().html('<form action="/app/admin/save_user" method="post" onclick="return check_comment()"><input type="text" value="'+tex+'" class="edit_input" name="comment" id="comment_change"><input type="hidden"  name="id" value="'+id+'"><input type="submit"  value="保存"> <input type="button" onclick="cancel_comment(this,\''+tex+'\')" value="取消"></button></form>');
	$("input:first").focus();
	$(obj).hide();
	//alert(tex);
	
	/*var tex=$(obj).parent().prev().text();
	$(obj).parent().prev().html('');
	var id=$(obj).parent().prev().attr('id');
    $(obj).parent().prev().html('<form action="/app/admin/save_user" method="post"><input type="text" value="'+tex+'" class="edit_input" name="password"><input type="hidden"  name="id" value="'+id+'"><input type="submit"  value="保存"> <input type="button" onclick="cancel(this,\''+tex+'\')" value="取消"></button></form>');
	$("input:first").focus();
	$(obj).hide();*/
	
}