function get_id(id){
    return document.getElementById(id);     //获取id
}
function addLoadEvent(func){
    var oldonload = window.onload;
    if (typeof window.onload != 'function'){
        window.onload = func;
    }
    else{
window.onload = function(){
    oldonload();
    func();
}
}
}
function addBtn(){
    if(!get_id('ibanner')||!get_id('ibanner_pic')) return;
    var picList = get_id('ibanner_pic').getElementsByTagName('a');     //获取a标签放进数组里
    if(picList.length==0) return;                           
    var btnBox = document.createElement('div');                      //增加一个按钮div
    btnBox.setAttribute('id','ibanner_btn');                            //设置id。
    var SpanBox ='';
    for(var i=1; i<=picList.length; i++ ){
        var spanList = '<span class="normal">'+i+'</span>';
        SpanBox += spanList;
    }
    btnBox.innerHTML = SpanBox;
    get_id('ibanner').appendChild(btnBox);
    get_id('ibanner_btn').getElementsByTagName('span')[0].className = 'current';               //设置样式
    for (var m=0; m<picList.length; m++){
        var attributeValue = 'picLi_'+m                                 //为每个按钮增加ID
        picList[m].setAttribute('id',attributeValue);
    }
}

function moveElement(elementID,final_x,final_y,interval){                 //运动框架函数
    if (!document.getElementById) return false;
    if (!document.getElementById(elementID)) return false; 
    var elem = document.getElementById(elementID);
    if (elem.movement){
        clearTimeout(elem.movement);
    }
    if (!elem.style.left){
        elem.style.left = "0px";
    }
    if (!elem.style.top){
        elem.style.top = "0px";           
    }
    var xpos = parseInt(elem.style.left);
    var ypos = parseInt(elem.style.top);
    if (xpos == final_x && ypos == final_y){
        moveing = false;
        return true;
    }
    if (xpos < final_x){
        var dist = Math.ceil((final_x - xpos)/10);                   //向上取整（缓慢运动）
        xpos = xpos + dist;
    }
    if (xpos > final_x){
        var dist = Math.ceil((xpos - final_x)/10);
        xpos = xpos - dist;
    }
    if (ypos < final_y){
        var dist = Math.ceil((final_y - ypos)/10);
        ypos = ypos + dist;
    }
    if (ypos > final_y){
        var dist = Math.ceil((ypos - final_y)/10);
        ypos = ypos - dist;
    }
    elem.style.left = xpos + "px";
    elem.style.top = ypos + "px";                       //最终位置
    var repeat = "moveElement('"+elementID+"',"+final_x+","+final_y+","+interval+")";    
    elem.movement = setTimeout(repeat,interval);                        
}
function classNormal(){
    var btnList = get_id('ibanner_btn').getElementsByTagName('span');
    for (var i=0; i<btnList.length; i++){
        btnList[i].className='normal';                                          //按钮样式设置为普通
    }
}

function picZ(){
    var picList = get_id('ibanner_pic').getElementsByTagName('a');
    for (var i=0; i<picList.length; i++){
        picList[i].style.zIndex='1';                                            //图片层级设置为最低
    }
}
var autoKey = false;
function iBanner(){
    if(!get_id('ibanner')||!get_id('ibanner_pic')||!get_id('ibanner_btn')) return;
get_id('ibanner').onmouseover = function(){
    autoKey = true
};
get_id('ibanner').onmouseout = function(){
    autoKey = false
};
var btnList = get_id('ibanner_btn').getElementsByTagName('span');
var picList = get_id('ibanner_pic').getElementsByTagName('a');
if (picList.length==1) return;                                           //只有一个则不用动
picList[0].style.zIndex='2';                                              //层级设为2
for (var m=0; m<btnList.length; m++){
btnList[m].onmouseover = function(){                                      //函数为鼠标停在按钮上显示显示对应的图片
    for(var n=0; n<btnList.length; n++){
        if (btnList[n].className == 'current'){
            var currentNum = n;
        }
    }
    classNormal();
    picZ();
    this.className='current';                              //先将其他样式清除，再将本按钮高亮样式
    picList[currentNum].style.zIndex='2';                  //先将其他样式清除，再将本按钮高亮样式
    var z = this.innerText-1;
    picList[z].style.zIndex='3';                                
    if (currentNum!=z){
        picList[z].style.left='650px';
        moveElement('picLi_'+z,0,0,10);           //从一个按钮转移到另一个按钮的代码
    }
}
}
}
setInterval('autoBanner()', 3000);
function autoBanner(){
    if(!get_id('ibanner')||!get_id('ibanner_pic')||!get_id('ibanner_btn')||autoKey) return;
    var btnList = get_id('ibanner_btn').getElementsByTagName('span');
    var picList = get_id('ibanner_pic').getElementsByTagName('a');
    if (picList.length==1) return;
    for(var i=0; i<btnList.length; i++){
        if (btnList[i].className == 'current'){
            var currentNum = i;
        }
    }
    if (currentNum==(picList.length-1) ){                              //当时最后一幅时。跳到第一副
        classNormal();
        picZ();
        btnList[0].className='current';
        picList[currentNum].style.zIndex='2';
        picList[0].style.zIndex='3';
        picList[0].style.left='650px';
        moveElement('picLi_0',0,0,10);
    }
    else{
        classNormal();
        picZ();
        var nextNum = currentNum+1;
        btnList[nextNum].className='current';
        picList[currentNum].style.zIndex='2';
        picList[nextNum].style.zIndex='3';
        picList[nextNum].style.left='650px';
        moveElement('picLi_'+nextNum,0,0,10);
    }
}
addLoadEvent(addBtn);
addLoadEvent(iBanner);