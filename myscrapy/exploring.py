from scrapy.selector import Selector
from scrapy.http import HtmlResponse

body = '''
<!DOCTYPE html>
<html>
<head>
<meta name="keywords" content="财经|股票|基金|期货|理财|行情|金融|债券|股指期货|外汇|保险|银行|黄金|博客|股吧">
<meta name="description" content="和讯网-中国财经网络领袖和中产阶级网络家园，创立于1996年，为您全方位提供财经资讯及全球金融市场行情，覆盖股票、基金、期货、股指期货、外汇、债券、保险、银行、黄金、理财、股吧、博客等财经综合信息">
<meta property="qc:admins" content="74223736776050566375" />

<meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.hexun.com/index.html"> 
<meta http-equiv="mobile-agent" content="format=html5; url=http://m.hexun.com/index.html">
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>和讯网</title>
<link href="http://img.hexun.com/zl/hx/index/style/index.css" rel="stylesheet" type="text/css" />
<script src="http://img.hexun.com/zl/tool/jquery-1.4.2.min.js"></script>
<script src="http://img.hexun.com/zl/hx/index/js/index.js"></script>
<script src="http://utrack.hexun.com/dp/hexun_dplus_ver1.0.1.js"></script>
<link href="http://login.tool.hexun.com/OtherInterFace/style/newbase.css" rel="stylesheet" type="text/css">
<script src="http://login.tool.hexun.com/OtherInterFace/js/popup.js" type="text/javascript" charset="gb2312"></script>
<script charset="gb2312" type="text/javascript" language="javascript">
		var href=window.location.href;
		hexunMember_loginSetup_signOutURL=href;//登出地址
		hexunMember_loginSetup_noLoginDisplayMsg=""; //没登陆的提示
		hexunMember_loginSetup_noLoginDisplayFlag="";//登录和注册中间的分隔符号 或 用户名与登出中间的分隔符号，不需要分隔符可以为空
		hexunMember_loginSetup_islogined_isDisplay=true;//如果是登陆状态，true=显示用户名和登出按钮等信息,flase=不显示任何信息
		hexunMember_loginSetup_referrer=document.referrer;//请不要修改此项
		hexunMember_loginSetup_MastLogin=0;//如果需要不登陆就一直弹窗，在此设置一下弹窗时间间隔(秒)。如果等于0本项无效
</script>

<base target="_blank" />
<style>
#wrap{width:100%;margin:0 auto;}
/*.toolbar{width:100%;margin:0 auto;background: url('http://itv.hexun.com/lbi-html/ly/2016/ph/ny18_2.png') no-repeat center #a00;}*/
.footer{background:#fff;}
</style>

</head>

<body>

<center><div id="fullScreeMedia"></div><div id="topFullWidthBanner"></div></center>
<div id="wrap">
<!--顶部工具条-->
<center>
         <div id="fullScreeMedia"></div>
	<div id="topFullWidthBanner"></div>
</center>
<div class="toolbar" id="t-float">
	<div class="toolbarC clearfix">
		<div class="toolbarCL">
			
			<a class="a1" style="background:url('http://img.hexun.com/zl/hx/index/images/dong2.gif') no-repeat;width:82px;height:60px;" href="http://news.hexun.com/2015/znxz/?utm_campaign=web_all_top" rel="nofollow">
			<!--顶部app下载--><div class="popapp"><img alt="" src="http://img.hexun.com/zl/hx/index/images/apptop.jpg"></div><!--顶部app下载-->
			</a>
			
			<a href="http://news.hexun.com/weixin/" class="a2" rel="nofollow">公众号</a>
		</div>
		<div class="toolbarCR">
			<!--未登录--> 
			<div class="hr-login-box" id="longinBox">
				<div class="hr-login-l fl">
					<div class="txt"><strong class="fl">登录</strong><a href="https://reg.hexun.com/regname.aspx?fromhost=www.hexun.com&urlreferrerhost=http%3a%2f%2fwww.hexun.com%2f&gourl=http%3a%2f%2fwww.hexun.com%2f" class="fr red">快速注册</a><span class="fr">没有账号？</span></div>
					<input type="text" onblur="index.focusBtn(this,2)" onfocus="index.focusBtn(this,1)" value="用户名/手机/邮箱" id="name" autocomplete="off" />
					<input type="password" onblur="index.focusBtn(this,2)" onfocus="index.focusBtn(this,1)" value="******" id="pwd" autocomplete="off" />
					<input type="button" value="" onclick="index.loginGo()" class="btn" />
					<label class="j"><input type="checkbox" checked="checked" id="check" />记住我</label>
					<a target="_blank" href="http://reg.hexun.com/GetPasswordPre.aspx" class="reg">找回密码</a>
					<p class="hr-login-error" id="loginError"><span class="ico">&nbsp;</span><u>登录超时，稍后再试</u></p>
				</div>
				<div class="hr-login-r fr">
					<div class="vline"></div>
					<p>免注册 快速登录</p>
					<a href="https://reg.hexun.com/bindqq.aspx?gourl=aHR0cDovL3d3dy5oZXh1bi5jb20=&fromhost=www.hexun.com" class="qq"></a><a  href="https://reg.hexun.com/bindsina.aspx?gourl=aHR0cDovL3d3dy5oZXh1bi5jb20=&fromhost=www.hexun.com" class="wb"></a><a href="https://reg.hexun.com/bindweixin.aspx?gourl=aHR0cDovL3d3dy5oZXh1bi5jb20=&fromhost=www.hexun.com" class="wx"></a>
					<div class="close" onclick="index.hideBox('longinBox')"></div>
				</div>
			</div>
			<!--未登录 e--> 

			<a href="http://mymoney.hexun.com/istock/" class="bn" rel="nofollow">自选股</a>

			<a href="javascript:void(0);" target="_self" class="bn" onclick="javascript:popupReg();">注册</a>

			<a href="javascript:void(0);" target="_self" class="loginBn" onclick="javascript:popupLogin();"></a>

			<!--已登录--> 
			<div class="YesLogin claerfix">
				<div class="username"></div>
				<div class="round"></div>
				<div class="menu">
					<ul>
						<li class="s">
							<a href="http://i.hexun.com" class="t">个人门户</a>
							<em class="tip"></em>
							<div class="list">
								<p class="clearfix"><strong class="fl"><a href="http://message.hexun.com/">消息</a></strong><span id="userMessageCount" class="fr"></span></p>
								<p class="clearfix"><strong class="fl"><a href="http://message.hexun.com/notice">通知</a></strong><span id="userNotifyCount" class="fr"></span></p>
								<p class="clearfix h"><strong class="fl"><a href="#">公告</a></strong><span class="fr">0</span></p>
							</div>
						</li>
						<li>
							<a href="http://epay.hexun.com/">钱包</a>
						</li>
						<li class="end"><a href="http://hexun.com/newHome/set/userinfo">设置</a></li>
					</ul>
				</div>
			</div>
			<!--已登录 e--> 

		</div>
	</div>
</div>
<!--顶部工具条 e-->

<div class="layout mg top clearfix">
	<style>
		.top .logo{
			padding-left:40px;
		}
		.top .right{
			width: 50px;
		}
		.gover{
			float:left;
			padding-top: 26px;
			margin-left: 20px;
		}
		.gover a{
			display:block;
		}
		.gover a img{
			border:0;
			width:113px;
			height:37px;
		}
	</style>
 <h1 class="logo"><a href="http://www.hexun.com"><img src="http://img.hexun.com/zl/hx/index/images/logo.png" alt="和讯网" /></a></h1>
	<div class="search">
		<!--搜索-->
		<div class="searchbox">
			<div class="sm-lay clearfix">
				<form id="hexunsearch" name="hexunsearch" action="" method="post" target="_blank" onsubmit="return false;">
				<div class="s_let fl">
				<div class="sl_lay fl">
				<div class="l clearfix fl">
				<div class="sl_select" id="selectBox"><span class="s-name">股&nbsp;票</span><span class="s-jt">&nbsp;</span></div>
				<div class="selectLayer" id="selectLayer" style="display:none">
							<div><span style="border:0px; line-height:33px">股&nbsp;票</span></div>
							<div><span>基&nbsp;金</span></div>
							<div><span>微&nbsp;博</span></div>
							<div><span>新&nbsp;闻</span></div>
							<div><span>博&nbsp;客</span></div>
						</div>
				</div>
				<input type="text" class="hx_inp" id="textMessage" name="textMessage" value="输入代码/名称/拼音" autocomplete="off"/>
				</div>
					</div>
				<input type="button" class="hx_btn"  id="btnSearch"/>
				<div id="hidRadio" style="display:none;">
					<input id="stockkey" type="hidden" name="key" />
					<input id="stocktype" type="hidden" name="type" />
				</div>
				</form> 
			</div>
		</div>
<div class=searchWords 360chrome_form_autofill="2">热门：<a href="http://licaike.hexun.com/subject/sub_hotSaleFund04.html?knownChannel=lcktl1" 360chrome_form_autofill="2">“火基”风云榜</a><a href="http://licaike.hexun.com/subject/sub_hqy01.html" 360chrome_form_autofill="2">活期盈</a><a href="http://licaike.hexun.com/wallet/index.html?from_jj=hxsy" 360chrome_form_autofill="2">抢加倍收益</a><em>|</em><a href="http://simu.hexun.com/" 360chrome_form_autofill="2">私募路演</a> <a href="http://stock.hexun.com/investmentcalendar/" target=_blank 360chrome_form_autofill="2"><font color=#990000>股票内参</font></a> <a href="http://zhibo.hexun.com/?utm_campaign=web_hexun_wzsy" target=_blank 360chrome_form_autofill="2">行情直播</a></div>
				<div id="searchInfPanel"></div>
		<script type="text/javascript" src="http://img.hexun.com/search/2014/js/config.js" charset="GB2312"></script>
		<script type="text/javascript" src="http://img.hexun.com/search/2014/js/search20151231.js" charset="GB2312"></script>
		<script type="text/javascript">
		hexun.common.Search.get().init({
			url:"http://so.hexun.com/ajax.do",
			inputID:"textMessage",
			containerID:"searchInfPanel",
			config:urlConfigList,
			searchBtnID:"btnSearch",
			openNewPage:"_blank"
		});
		</script>
		<!--搜索 e-->
	</div>
<div class="gover">
		<a href="" target="_blank"><img src="" alt="" /></a>
	</div>
	<div class="right" style="display:none;"><div class="ercode"><img src="http://img.hexun.com/zl/hx/index/images/ercode.png" alt="" /></div></div>
<script>
		var urls = [{href:"http://jubao.12377.cn:13225/reportsitetitle.do",rel:"nofollow", img:"http://i0.hexun.com/2016/pc/home/1.jpg"},{href:"http://jubao.china.cn:13225/reportform.do",rel:"nofollow", img:"http://i0.hexun.com/2016/pc/home/2.jpg"},{href:"http://www.12377.cn/",rel:"nofollow", img:"http://i0.hexun.com/2016/pc/home/3.jpg"},{href:"http://www.12377.cn/node_548470.htm",rel:"nofollow", img:"http://i0.hexun.com/2016/pc/home/4.jpg"}],i=0;
		setInterval(function(){
			jQuery(".gover").find("a").attr("href", urls[i].href).find("img").attr("src", urls[i].img);
			i+=1;
			if (i>=urls.length) i=0;
		},3000)
	</script>
</div>

<!--导航-->
<div class="layout mg nav clearfix">
<div class=b1>
<ul class=clearfix>
<li><a href="http://news.hexun.com/">新闻</a></li>

<li><a  href="http://news.hexun.com/events/">时事</a></li>

<li><a  href="http://315.hexun.com/">3.15</a></li>

<li><a  href="http://opinion.hexun.com/">评论</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://stock.hexun.com/">股票</a></li>

<li><a  href="http://stock.hexun.com/usstock/">美股</a></li>

<li><a  href="http://hk.stock.hexun.com/">港股</a></li>
<li><a  href="http://stock.hexun.com/7x24h/ ">快讯</a></li>

<li style="display:none;"><a  href="http://stock.hexun.com/newstock/">新股</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://funds.hexun.com/">基金</a></li>

<li><a  href="http://funds.hexun.com/smjj/">私募</a></li>

<li><a  href="http://money.hexun.com/">理财</a></li>

<li><a  href="http://trust.hexun.com/">信托</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://p2p.hexun.com/" rel="nofollow">P2P</a></li>

<li><a  href="http://tech.hexun.com/">科技</a></li>

<li><a  href="http://bond.hexun.com/">债券</a></li>

<li><a  href="http://iof.hexun.com/">互金</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://futures.hexun.com/">期货</a></li>

<li><a  href="https://zhibo.9dcj.com/" rel="nofollow">非农</a></li>

<li><a  href="http://dazong.hexun.com/">大宗</a></li>

<li><a  href="http://futures.hexun.com/2015/qihuobao/?fromhost=from_qhkhhs">开户</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://insurance.hexun.com/">保险</a></li>

<li><a  href="http://bank.hexun.com/">银行</a></li>

<li><a  href="http://gold.hexun.com/">黄金</a></li>

<li><a  href="http://forex.hexun.com/">外汇</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://quote.hexun.com/">行情</a></li>

<li><a  href="http://data.hexun.com/">数据</a></li>

<li><a href="http://house.hexun.com/" id="nav_house" >房产</a></li> 
<script language="JavaScript">
function houseDepart(id){
	if(document.cookie.indexOf("TOWN=3205")!=-1){
	document.getElementById(id).href="http://suzhou.house.hexun.com/";
	}
	if(document.cookie.indexOf("CITY=51")!=-1){
	document.getElementById(id).href="http://sc.house.hexun.com/";
	}
	if(document.cookie.indexOf("CITY=61")!=-1){
	document.getElementById(id).href="http://xa.house.hexun.com/";
	} 
	if(document.cookie.indexOf("CITY=50")!=-1){
	document.getElementById(id).href="http://cq.house.hexun.com/";
	}
	if(document.cookie.indexOf("CITY=53")!=-1){
	document.getElementById(id).href="http://yn.house.hexun.com/";
	}
	if(document.cookie.indexOf("CITY=52")!=-1){
	document.getElementById(id).href="http://gz.house.hexun.com/";
	}
	if(document.cookie.indexOf("TOWN=3201")!=-1){
	document.getElementById(id).href="http://nj.house.hexun.com/";
	}
}
houseDepart('nav_house');
</script>

<li><a  href="http://auto.hexun.com/">汽车</a></li>
</ul>
</div>
<div class="b1 ml15">
<ul class=clearfix>
<li><a  href="http://blog.hexun.com/">博客</a></li>

<li><a href="http://xfjr.hexun.com/">消金</a></li>

<li><a href="http://bbs.hexun.com/">论坛</a></li>

<li><a href="http://caidao.hexun.com/">财道</a></li>
</ul>
</div>
<div class="b2 ml15">
<ul class=clearfix>
<li class=w5><a href="http://hexun.gq.com.cn/?utm_source=hexun.com&utm_medium=syn_OG&utm_content=navigation&utm_campaign=regular" rel="nofollow">奢侈品</a></li>

<li class=w3><a href="http://news.hexun.com/socialmedia/">名家</a></li>

<li class=w5><a href="http://game.hexun.com/">游戏</a></li>

<li class=w3><a href="http://haiwai.hexun.com/">海外</a></li>
</ul>
</div>
	 
</div>
<!--导航 e-->

<div class="layout mg imgLink pt20 pb20">
 <ul class=clearfix>
<li class=i8><a href="https://fmall.hexun.com/fmall-website/ " 360chrome_form_autofill="2"><em></em>钱包理财</a></li>

<li class=i3><a href="http://caidao.hexun.com/?utm_campaign=web_www" 360chrome_form_autofill="2"><em></em>财道社区</a></li>

<li class=i4><a href="http://licaike.hexun.com/" 360chrome_form_autofill="2"><em></em>理财客</a></li>

<li class=i1><a href="http://zhibo.hexun.com/?utm_campaign=www_hexun_mjzb" 360chrome_form_autofill="2"><em></em>名家直播</a></li>

<li class=i2><a href="http://px.hexun.com/" 360chrome_form_autofill="2"><em></em>投资学院</a></li>
<!--li class=i6><a href="http://www.baohejr.com/" 360chrome_form_autofill="2"><em></em>宝和金融</a></li-->
<li class=i7><a href="http://www.fangxinbao.com/" rel=nofollow 360chrome_form_autofill="2"><em></em>放心保</a></li>

<li class=i9><a href="http://ds.hexun.com/" 360chrome_form_autofill="2"><em></em>期货大赛</a></li>

<li class=i10><a href="http://yuqing.hexun.com/upload/hexuntong/hexuntong/index.html" 360chrome_form_autofill="2"><em></em>和讯通</a></li>
</ul>

 </div>

<!--广告1000*100-->
<div id=tonglan_1 class="layout mg pt20" style="padding-top: 15px;"><a href="http://www.hexun.com"></a></div>
<!--广告1000*100 end-->

<!--广告192*70-->
 	<div class="layout mg">
<ul class="clearfix mt20" style="margin-top:10px">
<li class=fl id="button_1"><a href="http://www.hexun.com/"><img src="http://img.hexun.com/zl/img/temp.png" width=192 height=70></a></li>

<li class="fl ml10" id="button_2"><a href="http://www.hexun.com/"><img src="http://img.hexun.com/zl/img/temp.png" width=192 height=70></a></li>

<li class="fl ml10" id="button_3"><a href="http://www.hexun.com/"><img src="http://img.hexun.com/zl/img/temp.png" width=192 height=70></a></li>

<li class="fl ml10" id="button_4"><a href="http://www.hexun.com/"><img src="http://img.hexun.com/zl/img/temp.png" width=192 height=70></a></li>

<li class="fl ml10" id="button_5"><a href="http://www.hexun.com/"><img src="http://img.hexun.com/zl/img/temp.png" width=192 height=70></a></li>
</ul>
</div>
<!--广告192*70 end-->

<!--全球指数-->
 <div class="layout mg globalData"><a href="http://stockdata.stock.hexun.com/indexhq_000001_1.shtml"><i>上证指数</i><span id=shanghai-top></span></a> <a href="http://stockdata.stock.hexun.com/indexhq_399001_2.shtml"><i class=ml38>深证</i><span id=shenzhen-top></span></a> <a href="http://hkquote.stock.hexun.com/urwh/hkstock/90001.shtml"><i class=ml38>恒生指数</i><span id=hk-top></span></a> <a href="http://stockdata.stock.hexun.com/qqgz/index.aspx?code=.DJI"><i class=ml38>道琼斯指数</i><span id=NYSE-top></span></a> <a href="http://stockdata.stock.hexun.com/qqgz/index.aspx?code=.IXIC"><i class=ml38>纳斯达克</i><span id=NASDAQ-top></span></a> </div>
<!--全球指数 end-->

<!--新闻,时事,评论,名家-->
<div class="layout mg pt30 clearfix">
	<div class="c1"> 
 <div class="newsTop">
 		 		<a href="http://news.hexun.com/" id="setA1" onmouseover="index.setTab('setA',1,2)" class="s">新闻</a><em>|</em><a href="http://news.hexun.com/events/" id="setA2" onmouseover="index.setTab('setA',2,2)">时事</a><div id="xwss_gm"></div>
 
		 </div>
 		<div id="con_setA_1">
			<div class="newsList">
			<ul sizcache="1" sizset="53">
<li><a href="http://news.hexun.com/" target="_blank" 360chrome_form_autofill="2">中美重启经贸磋商 中方本月下旬赴美</a> </li>






<li _extended="true"><a href="http://news.hexun.com/2018-08-17/193804164.html" target="_blank" 360chrome_form_autofill="2">美威胁实施更多制裁 土耳其里拉闪崩2千点</a></li>




<li><a href="http://forex.hexun.com/2018-08-17/193803679.html" target="_blank" 360chrome_form_autofill="2">央行暴打空头？人民币做空成本创最大涨幅</a></li>



<li><a href="http://opinion.hexun.com/2018-08-17/193803940.html" target="_blank" 360chrome_form_autofill="2">重大信号！中央开了一次史无前例的会议</a></li>


<li _extended="true"><a href="http://futures.hexun.com/2018-08-17/193805814.html" target="_blank" 360chrome_form_autofill="2">方星海：加快推国债期权国债期货等新产品</a></li>


<li><a href="http://tech.hexun.com/2018-08-17/193803397.html" target="_blank" 360chrome_form_autofill="2">史上最大币灾下众生相：韭菜开始丧失信心</a></li>




<li><a href="http://house.hexun.com/2018-08-17/193804131.html" target="_blank" 360chrome_form_autofill="2">多地居民称房租上涨 谁推高房租</a> <a href="http://house.hexun.com/2018-08-17/193803252.html" target="_blank">供给减少</a></li>






<li><a href="http://tech.hexun.com/2018-08-17/193803249.html" target="_blank" 360chrome_form_autofill="2">红芯浏览器陷造假风波："自主可控"遭质疑</a></li>





<li><a href="http://news.hexun.com/2018-08-17/193803198.html" target="_blank" 360chrome_form_autofill="2">起底供应链管理：金融成最赚钱环节 有秘密</a> </li>


<li><a href="http://tech.hexun.com/2018-08-17/193804222.html" target="_blank" 360chrome_form_autofill="2">怕了吗？亚马逊下一个扫荡的行业：电影院</a></li>











</ul>

			 
		</div>
		</div>
		<div id="con_setA_2" class="h">
			<div class="newsList">
			<ul>
<li><a href="http://news.hexun.com/events/" target=_blank 360chrome_form_autofill="2">习近平对首个“中国医师节”作出重要指示</a></li>

<li _extended="true"><a href="http://news.hexun.com/2018-08-16/193801326.html" target=_blank 360chrome_form_autofill="2">政治局听取长春长生疫苗问题调查报告</a></li>

<li><a href="http://news.hexun.com/2018-08-17/193805116.html" target=_blank 360chrome_form_autofill="2">新时代，习近平这样推进军队党建</a></li>

<li><a href="http://news.hexun.com/2018-08-17/193805109.html" target=_blank 360chrome_form_autofill="2">国务院常务会：没收长春长生所有违法所得 </a></li>

<li><a href="http://news.hexun.com/2018/jinxingdaodi/index.html" target=_blank 360chrome_form_autofill="2">将改革开放进行到底</a> <a href="http://news.hexun.com/2018/gaigekaifang40zhounian/index.html" target=_blank 360chrome_form_autofill="2">改革开放40周年</a></li>

<li _extended="true"><a href="http://news.hexun.com/2018-08-17/193805275.html" target=_blank 360chrome_form_autofill="2">中国对外资吸引力稳增</a> <a href="http://news.hexun.com/2018-08-17/193805261.html" target=_blank 360chrome_form_autofill="2">扩开放不止步</a></li>

<li><a href="http://news.hexun.com/2018-08-17/193805433.html" target=_blank 360chrome_form_autofill="2">中国经济，“稳”的特征更加鲜明</a> </li>

<li _extended="true"><a href="http://tech.hexun.com/2018-08-17/193805405.html" target=_blank 360chrome_form_autofill="2">他们脑洞为何如此之大？做到这些你也可以</a> </li>

<li><a href="http://news.hexun.com/2018-08-17/193805204.html" target=_blank 360chrome_form_autofill="2">厦航客机在马尼拉降落时偏出跑道 无人受伤</a></li>

<li><a href="http://news.hexun.com/2018-08-17/193805366.html" target=_blank 360chrome_form_autofill="2">原来，这就是爱情的模样！</a> <a href="http://news.hexun.com/2018-08-17/193805370.html" target=_blank 360chrome_form_autofill="2">三代人的爱情观</a> </li>
</ul>

			  
			</div>
		</div>
	</div>
<script>
                (function(){
                    var dfzCodes = {'CITY=42':{'ifr_src':'http://hubei.hexun.com/ipdx/index.html', 'tit_name':'湖北', 'tit_href':'http://hubei.hexun.com/'}
                    },  
                        currentCityCode =(document.cookie).match(/CITY=\d+/);
                        currentCity = dfzCodes[currentCityCode]; 
                        if(currentCity){ 
                            $('#con_setA_2 .newsList').children().eq(0).remove();
                            $('#con_setA_2 .newsList').prepend('<iframe src="'+currentCity.ifr_src+'" frameborder="0" scrolling="no" style="height: 306px;"></iframe>')
                            $('#setA2').text(currentCity.tit_name);
                            $('#setA2').attr('href',currentCity.tit_href);

                        }
                    })();  
                </script>
	<div class="c1 ml40">

		<div class="newsTop">
<a class=s href="http://stock.hexun.com/" 360chrome_form_autofill="2" id="setQES1" onmouseover="index.setTab('setQES',1,2)">股票</a><em>|</em><a href="http://stock.hexun.com/7x24h/" 360chrome_form_autofill="2" id="setQES2" onmouseover="index.setTab('setQES',2,2)">7×24快讯<em class="qespoint h"></em></a> 
		</div>
		 
<div id="con_setQES_1">
		<div class="newsList">
<ul sizset="72" sizcache="0">
<li><a href="http://stock.hexun.com/7x24h/" target=_blank 360chrome_form_autofill="2"><img alt="全球市场24小时 " src="http://i3.hexun.com/2017-02-13/188123497.jpg" 360chrome_form_autofill="2"></a><a href="http://stock.hexun.com/" target=_blank 360chrome_form_autofill="2">市场积重难返 控好仓位多看少动</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193804455.html" target=_blank 360chrome_form_autofill="2">国家队持仓稳健 二季度险资重仓11只A股</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803229.html" target=_blank 360chrome_form_autofill="2">券商股昨吸金1.76亿</a> <a href="http://stock.hexun.com/2018-08-17/193803246.html" target=_blank>5G基站提升板块热度</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803191.html" target=_blank 360chrome_form_autofill="2">QFII二季度持股新动向</a> <a href="http://stock.hexun.com/2018-08-17/193803245.html" target=_blank>券商现身52家公司</a></li>

<li _extended="true"><a href="http://stock.hexun.com/2018-08-17/193803232.html" target=_blank 360chrome_form_autofill="2">机构月内调研241家公司 电子等四行业受宠</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803857.html" target=_blank 360chrome_form_autofill="2">A股新动向！产业资本半年来首现净增持</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803262.html" target=_blank 360chrome_form_autofill="2">A股震荡创新低 海外资金抄底力度有望加大</a></li>

<li><a class=red href="http://stock.hexun.com/company/" target=_blank 360chrome_form_autofill="2">公司</a><em>|</em><a href="http://stock.hexun.com/2018-08-17/193803140.html" target=_blank 360chrome_form_autofill="2">上海钢联现金流吃紧 高管基金忙减持</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803142.html" target=_blank 360chrome_form_autofill="2">夺权大戏愈演愈烈远方信息无法控制孙公司</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803202.html" target=_blank 360chrome_form_autofill="2">非洲猪瘟南下流窜郑州双汇 生猪行业临大敌</a></li>
</ul>

 
		</div>
</div>
                <div id="con_setQES_2" class="h newsflash">
                	<div class="newsList">
                		<div class="qes" id="qesid"></div>
                	</div>
                </div>
                <script src="http://img.hexun.com/2016/7X24/js/liveNews.js"></script>
                <script>
                        var ln = new live.news(".qes", {
                                size: 5
                            }),
                            watch = new live.watch({
                                queuetime: 200,
                                fetchtime: 30000
                            });
                        $.extend(ln, {
                            itemHtml: '<div class="tl"><em class="tlp"></em><dl class="newsDl clearfix" id="{{timestamp}}" nid="{{id}}"><dt>{{issuancetime}}</dt><em>|</em><dd datatxt="{{content}}">{{content}}</dd></dl></div>',
                            itemTagHtml: '<div class="tl"><em class="tlp"></em><dl class="newsDl clearfix" id="{{timestamp}}" nid="{{id}}" style="color:red"><dt>{{issuancetime}}</dt><em>|</em><dd>{{content}}</dd></dl></div>',
                            itemListPop: '<div class="qesmask" id="qesmaskid"><i class="qesmaskclose"></i><div class="qescontent"></div></div>',
                            itemDateHtml: '<div class="timeBox"></div>'/*,
                            TimingHidden: function(selector, timer, timerid) {
                                if (!timerid) {
                                    selector.removeClass('h');
                                    timerid = setTimeout(function() {
                                        selector.addClass('h');
                                    }, timer);
                                } else {
                                    clearTimeout(timerid);
                                    selector.removeClass('h');
                                    timerid = setTimeout(function() {
                                        selector.addClass('h');
                                    }, timer);
                                }
                                return this;
                            }*/
                        });

                        ln.getNews(ln.api.getNews, {}, function() {
                                // console.log("init success");
                                //console.log("first: " + new Date(ln.firstTimeSamp))
                                //console.log("last: " + new Date(ln.lastTimeStamp))
                                watch.queue(ln).fetch(function() {
                                    ln.getNews(ln.api.getMoreNews, {
                                            timestamp: ln.firstTimeSamp
                                        }, function(result) {
                                            // watch.isNoAdd = true;
                                            if (result.list.length > 0) {
                                                //ln.firstDate = result.list[result.list.length - 1].date;
                                                ln.firstTimeSamp = result.list[result.list.length - 1].timestamp;
                                                //console.log("update_first: " + new Date(ln.firstTimeSamp))
                                                //console.log("update_last: " + new Date(ln.lastTimeStamp))
                                                /*var pointhiddentimer;
                                                if ($("#con_setQES_2").css("display") !== "block") {
                                                    ln.TimingHidden($(".qespoint"), 10000, pointhiddentimer);
                                                } else {
                                                    ln.TimingHidden($(".qespoint"), 10000, pointhiddentimer);
                                                };*/
                                                $(".qespoint").removeClass('h');
                                                timerid = setTimeout(function() {
                                                    $(".qespoint").addClass('h');
                                                }, 10000);
                                            };
                                            if ($("#qesid dl").length > 5) {
                                                $("#qesid dl:gt(5)").remove();
                                            };
                                            for (var i = 0; i < result.list.length; i++) {
                                                watch.list.push(result.list[i])
                                            };
                                            // watch.isNoAdd = false;
                                            // watch.isNoAdd = false;
                                        },
                                        function(error) {
                                            // console.log(error);
                                        }, 2);
                                });
                            },
                            function() {
                                // console.log("init error:" + error);
                            }, 0);
                        var lnP = new live.news(".qespopup"),
                            watchP = new live.watch({
                                //queuetime: 200,
                                fetchtime: 15000
                            });
                        $.extend(lnP, {
                            itemWinPopWrap: '<div class="qespopup" id="qespopupid"><i class="qespopupclose"></i><div class="qespopupcontent"></div><i class="qeshxlogo"></i></div>',
                            itemWinPopContent: '<dl class="newsDl clearfix" id="{{timestamp}}" nid="{{id}}"><a href="http://stock.hexun.com/7x24h/"><dt>{{issuancetime}}</dt><dd>{{content}}</dd></a></dl>',
                            api: { getPopNews: "http://nwapi.hexun.com/liveNews/getHintedLiveNews?timestamp={{timestamp}}" }
                        });

                        watchP.queue(lnP).fetch(function() {
                            lnP.getNews(lnP.api.getPopNews, {
                                    timestamp: lnP.firstTimeSamp
                                }, function(result) {
                                        if (result.data !== "") {
                                            lnP.firstTimeSamp = result.timestamp;
                                            //console.log("update_first: " + new Date(ln.firstTimeSamp))
                                            //console.log("update_last: " + new Date(ln.lastTimeStamp))
                                            $("body").append(lnP.itemWinPopWrap);
                                            var winpopdowntimer,
                                                winpopcontent = lnP.tmpl(lnP.itemWinPopContent, result);
                                            if (!winpopdowntimer) {
                                                $(".qespopupcontent").html(winpopcontent);
                                                winpopdowntimer = setTimeout(function() {
                                                    $(".qespopup").remove();
                                                }, 30000);
                                            } else {
                                                clearTimeout(winpopdowntimer);
                                                $(".qespopupcontent").html("");
                                                $(".qespopupcontent").html(winpopcontent);
                                                // $(".qespopupcontent dl").replaceWith(winpopcontent);
                                                winpopdowntimer = setTimeout(function() {
                                                    $(".qespopup").remove();
                                                }, 30000);
                                            };
                                        };
                                    $(".qespopupclose").click(function(event) { $(".qespopup").remove(); });
                                    $(".qespopupclose").click(function(e) {
                                        // console.log("关闭7×24h快讯弹窗")
                                        typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                                            "FUNCTION": "关闭7×24h快讯弹窗",
                                            "LEVEL": "和首弹窗页-7×24h快讯",
                                            "TYPE": "列表页",
                                            "PLATFORM": "WEB"
                                        });
                                    });
                                    $(".qespopup a").click(function(e) {
                                        // console.log("点击7×24h快讯弹窗内容")
                                        typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                                            "FUNCTION": "点击7×24h快讯弹窗内容",
                                            "LEVEL": "和首弹窗页-7×24h快讯",
                                            "TYPE": "列表页",
                                            "PLATFORM": "WEB"
                                        });
                                    });
                                    // watch.isNoAdd = false;
                                },
                                function(error) {
                                    // console.log(error);
                                }, 2);
                        });
                        $(".qes").click(function(event) {
                            var tag = event.target;
                             if ($(tag).parent().is('dl')) {
                                $(".qes").after(ln.itemListPop);
                                $(".qesmask .qescontent").append($(tag).parent().clone());
                                $(".qesmask").click(function() {
                                    $(this).remove();
                                });
                             }else if ($(tag).is('dl')) {
                                $(".qes").after(ln.itemListPop);
                                $(".qesmask .qescontent").append($(tag).clone());
                                $(".qesmask").click(function() {
                                    $(this).remove();
                                });
                            };
                        });
                        $("#setQES2").click(function(e) {
                            // console.log("点击7×24h快讯")
                            typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                                "FUNCTION": "点击7×24h快讯",
                                "LEVEL": "和讯网首页",
                                "TYPE": "列表页",
                                "PLATFORM": "WEB"
                            });
                        });
                        $("#setQES2").mouseover(function(e) {
                            // console.log("滑动至7×24h快讯")
                            typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                                "FUNCTION": "滑动至7×24h快讯",
                                "LEVEL": "和讯网首页",
                                "TYPE": "列表页",
                                "PLATFORM": "WEB"
                            });
                        });
                        $(".qes").click(function(e) {
                            // console.log("点击7×24h快讯单条内容")
                            typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                                "FUNCTION": "点击7×24h快讯单条内容",
                                "LEVEL": "和首标签页-7×24h快讯",
                                "TYPE": "列表页",
                                "PLATFORM": "WEB"
                            });
                        });
                        // $(".qespopupclose").click(function(e) {
                        //     console.log("关闭7×24h快讯弹窗")
                        //     typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                        //         "FUNCTION": "关闭7×24h快讯弹窗",
                        //         "LEVEL": "和首标签页-7×24h快讯",
                        //         "TYPE": "列表页",
                        //         "PLATFORM": "WEB"
                        //     });
                        // });
                        // $(".qespopup a").click(function(e) {
                        //     console.log("点击7×24h快讯弹窗内容")
                        //     typeof dplus_Click != "undefined" && dplus_Click("点击事件", {
                        //         "FUNCTION": "点击7×24h快讯弹窗内容",
                        //         "LEVEL": "和首标签页-7×24h快讯",
                        //         "TYPE": "列表页",
                        //         "PLATFORM": "WEB"
                        //     });
                        // });
                        $("#setQES2").mouseover(function(e) {
                            if($("#con_setQES_2").css("display") !== "block"){
                                clearTimeout(timerid);
                                $(".qespoint").addClass('h');
                            };
                        });
                </script>
	</div>
	
	<div class="c0 ml40">
<div style="display:none;">
<div class="gsjj" 360chrome_form_autofill="2" sizcache="0" sizset="82">
<div class="hd" 360chrome_form_autofill="2">
<div style="background: rgb(251, 94, 103); padding: 2px 0px 0px 17px; width: 80px; height: 28px; color: white; font-family: 微软雅黑; font-size: 18px;" 360chrome_form_autofill="2"><a style="color: white;" href="http://caidao.hexun.com/lesson/?utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2">财道聚焦</a></div></div>
<div class="bd" 360chrome_form_autofill="2"><a href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=816709&utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2"><img width="300" height="170" alt="" src="http://i8.hexun.com/2018-07-09/193406363.jpg" 360chrome_form_autofill="2"></a> 
<h2 style="text-align: center;"><a href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=816709&utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2"><strong>王者：关注无退市风险被错杀的个股</strong></a></h2></div>
<ul class="ft" sizcache="0" sizset="82">
<li><a href="http://lesson.hexun.com/web/play.html?classId=1001162&utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2">徐小明：关注超跌个股机会</a></li>
<li><a href="http://lesson.hexun.com/web/play.html?classId=1001163&utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2">冯矿伟：KDJ和MACD特点及运用</a></li>
<li><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=816769&utm_campaign=web_www_gsjj" target="_blank" 360chrome_form_autofill="2">王赫：挖掘机行业或将迎来井喷行情</a></li>
</ul></div>
</div>

<div class="gsjj" 360chrome_form_autofill="2" sizcache="0" sizset="82">
<div class="hd" 360chrome_form_autofill="2">
<div style="background: rgb(251, 94, 103); padding: 2px 0px 0px 17px; width: 80px; height: 28px; color: white; font-family: 微软雅黑; font-size: 18px;" 360chrome_form_autofill="2"><a style="color: white;" href="http://news.hexun.com/socialmedia/" target="_blank" 360chrome_form_autofill="2">名家聚焦</a></div></div>
<div class="bd" 360chrome_form_autofill="2"><a href="http://opinion.hexun.com/" target="_blank" 360chrome_form_autofill="2"><img alt="" src="http://i5.hexun.com/2018-08-17/193804866.jpg" width="300" height="170" 360chrome_form_autofill="2"></a> 
<h2 style="text-align: center;"><a href="http://opinion.hexun.com/2018-08-17/193804762.html" target="_blank" 360chrome_form_autofill="2">最严问责，是惩戒更是警示 </a></h2></div>
<ul class="ft" sizcache="0" sizset="82">


<li _extended="true"><a href="http://news.hexun.com/2018-08-17/193804047.html" target="_blank" 360chrome_form_autofill="2">土耳其阿根廷接连中招 下一个或是乌克兰</a></li>














<li><a href="http://news.hexun.com/2018-08-17/193803871.html" target="_blank" 360chrome_form_autofill="2">美联储很快要实行第4轮QE？逻辑很简单</a></li>













<li><a href="http://funds.hexun.com/2018-08-17/193804614.html" target="_blank" 360chrome_form_autofill="2">要让大家缴纳"二胎基金"的人究竟是谁？</a></li>

















</ul>

















</div>

		 
	</div>
</div>
<!--新闻,时事,评论,名家 e-->

<!--股票,行情,数据,投顾,研报,策略-->
<div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class=s href="http://caidao.hexun.com/?utm_campaign=www_hexun_hxmj">和讯名家</a> 
		</div>
		<div class="newsList">			 
<ul sizset="86" sizcache="0" _extended="true">
<li _extended="true"><a href="http://caidao.hexun.com/?utm_campaign=www_hexun_hxmj1" target="_blank" 360chrome_form_autofill="2">大盘调整已比较充分 多头大军随时卷土重来</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/29826631/article109810.html?utm_campaign=www_hexun_hxmj2" target="_blank" 360chrome_form_autofill="2">周五盘前导航：架构已露瑕疵 把握反抽调节</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/1037523/article109820.html?utm_campaign=www_hexun_hxmj3" target="_blank" 360chrome_form_autofill="2">PTA价格大幅上涨 行业龙头股有望充分受益</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/29586764/article109833.html?utm_campaign=www_hexun_hxmj6" target="_blank" 360chrome_form_autofill="2">荣华论股：市场氛围不佳 指数破底量缩待变</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/25405058/article109822.html?utm_campaign=www_hexun_hxmj5" target="_blank" 360chrome_form_autofill="2">A股真正底部只有这一个 短线切勿盲目抄底</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/27394773/article109830.html?utm_campaign=www_hexun_hxmj4" target="_blank">大盘强势反弹即将到来 罕见底部机会应珍惜</a></li>






<li _extended="true"><a href="http://caidao.hexun.com/1037523/article109745.html?utm_campaign=www_hexun_hxmj7" target="_blank" 360chrome_form_autofill="2">消费电子旺季进行时 PCB行业龙头快速成长</a></li>





</ul>



<ul sizset="96" sizcache="1">
<li><a href="http://caidao.hexun.com/29586764/article109748.html?utm_campaign=www_hexun_hxmj8" target=_blank 360chrome_form_autofill="2">指数震荡回弱谨慎情绪升温 等待新热点出现</a></li>

<li _extended="true"><a href="http://caidao.hexun.com/29852286/article109734.html?utm_campaign=www_hexun_hxmj9" target=_blank 360chrome_form_autofill="2">短期有扭转颓势迹象</a> <a href="http://caidao.hexun.com/27394773/article109753.html?utm_campaign=www_hexun_hxmj9" target=_blank>A股行情能否涅槃重生</a></li>

<li _extended="true"><a href="http://caidao.hexun.com/29663383/article109726.html?utm_campaign=www_hexun_hxmj0" target=_blank 360chrome_form_autofill="2">不要因为下跌而乱了方寸 机会总是悄悄来临</a></li>
</ul>

 
</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class="s" href="http://zhibo.hexun.com/?utm_campaign=www_hexun_hqzz" 360chrome_form_autofill="2">名家直播</a>
</div>
<div class="newsList">
<ul sizset="96" sizcache="0">
<li><a href="http://zhibo.hexun.com/?utm_campaign=www_hexun_hqzz1" target="_blank" 360chrome_form_autofill="2"><strong>提防下周国际股市冲击</strong></a> <a href="http://zhibo.hexun.com/11018/default.html?utm_campaign=www_hexun_hqzz2" target="_blank"><strong>视频解读今日机会</strong></a></li>






















































<li><a href="http://zhibo.hexun.com/1725/default.html?utm_campaign=www_hexun_hqzz2" target="_blank" 360chrome_form_autofill="2">勿慌！现在就是大底</a> <a href="http://zhibo.hexun.com/10331/default.html?utm_campaign=www_hexun_hqzz2" target="_blank">被套的散户如何自救</a></li>





















































</ul>


<ul sizset="96" sizcache="0">
<li><a href="http://zhibo.hexun.com/10615/default.html?utm_campaign=www_hexun_hqzz3" target="_blank" 360chrome_form_autofill="2">中美谈判重启能否激活A股</a> <a href="http://zhibo.hexun.com/682/default.html?utm_campaign=www_hexun_hqzz5" target="_blank">三次探底完成</a></li>







































































































































<li><a href="http://zhibo.hexun.com/10752/default.html?utm_campaign=www_hexun_hqzz4" target="_blank"><font color="#990000">高开是诱多还是独立行情？</font></a> <a href="http://zhibo.hexun.com/10975/default.html?utm_campaign=www_hexun_hqzz4" target="_blank"><font color="#990000">此时盲目抄底</font></a></li>







































































































































<li><a href="http://zhibo.hexun.com/162/?utm_campaign=www_hexun_hqzz5" target="_blank" 360chrome_form_autofill="2">大级别低点抄底后等反弹</a> <a href="http://zhibo.hexun.com/659/default.html?utm_campaign=www_hexun_hqzz5" target="_blank">七夕能否翻身仗</a></li>







































































































































<li><a href="http://zhibo.hexun.com/10409/?utm_campaign=www_hexun_hqzz6" target="_blank">创业板最快明年末反转</a> <a href="http://zhibo.hexun.com/10142/default.html?utm_campaign=www_hexun_hqzz6" target="_blank">真正底部只有一个</a></li>






































































































































</ul>


<ul>
<li><a href="http://zhibo.hexun.com/1296/default.html?utm_campaign=www_hexun_hqzz7" target="_blank">牛散大学堂早报</a> <a href="http://zhibo.hexun.com/445/default.html?utm_campaign=www_hexun_hqzz7" target="_blank">大盘技术性反抽会有多高</a></li>















































</ul>


 
<!--上证 / 深证  -->
<div class="stockData clearfix">
	<div id="shanghai-box" class="left"></div>
	<div id="shenzhen-box" class="right"></div>
</div>
		</div>
	</div>
	<div class="c0 ml40">
<style>
body,ul,li,dl,dt,dd,p,h1,h2,h3,h4,form,table,th,td,img,div{padding:0;margin:0}
a{text-decoration:none;color:#000;}
a:hover{text-decoration:underline;color:#a00;}
/*20170503*/
.gsjj .hd{background: url(http://img.hexun.com/zl/hx/index/images/ifr_title.jpg) 0 -531px;width: 100%;height: 32px;position: relative; margin-bottom: 20px;}
.gsjj .bd h2{ height: 40px; line-height: 40px; background: #f6f6f6; width: 100%}
.gsjj .bd h2 a{padding-left:10px; font-size: 16px; }
.gsjj .ft a{font-size: 16px;}
.gsjj .ft li{height: 37px; line-height: 37px;}
.mjjd .hd{background: url(http://img.hexun.com/zl/hx/index/images/ifr_title.jpg) 0 -564px;width: 100%;height: 32px;position: relative;}
.mjjd .hd a{display: inline-block;width: 100%; height: 32px;}
/*.mjjd .bd{background: url(http://img.hexun.com/zl/hx/index/images/icon_mjjd.jpg) no-repeat; padding: 16px 0 10px 46px; }
.mjjd .bd div{font-size: 16px;margin-bottom: 18px;position: relative;line-height: 24px; height: 48px; margin-bottom: 18px; }
/*.mjjd .bd .c999{ color: #999; font-size:12px; }*/
/*.mjjd .bd .pr_rt{position: absolute;right: 0; top: 0}
.mjjd .bd .pr_rb{position: absolute;right: 0; bottom: 0}
.mjjd .bd .pr_lb{position: absolute;left: 0; bottom: 0}*/*/

.mjjd{ margin-top: 50px;}
.mjjd .hd{width: 100%;height: 32px;position: relative;}
.mjjd .hd a{display: inline-block;width: 100%; height: 32px;}
.mjjd .bd{ padding: 16px 0 0px 0px; }
.mjjd .bd div{font-size: 16px;margin-bottom:8px;position: relative;line-height: 24px; height: 48px;  padding: 0px 0 10px 0px; }
.mjjd .bd .div1 a{font-size: 16px;}
.mjjd .bd .c999{ color: #999; font-size:12px; }
.mjjd .bd .pr_rt{position: absolute;right: 0; top: 0}
.mjjd .bd .pr_rb{
	position: absolute;
	right: 6px;
	bottom: 8px
}
.mjjd .bd .pr_lb{
	position: absolute;
	left: 44px;
	bottom: 1px
}
.mjjd .imgBox{width: 44px; float: left;}
.mjjd h2{padding-top:5px;font-size: 16px;font-weight:normal}
.mjjd{font-family: "microsoft yahei";}
</style>
<base target="_blank">
<div class="mjjd">
				<div class="hd">
					
<div style="background: #44B3C4;width: 80px;height: 28px;font-size: 18px;color: white;font-family: \5fae\8f6f\96c5\9ed1;padding: 2px 0px 0px 17px;">
    <a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy" target="_blank" style="color: white;">投资学院</a>
</div>
				</div>
				<div class="bd">
	<div class="div2">
<span class="imgBox"><a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy"><img src="http://i7.hexun.com/2018-06-21/193242849.png" alt=""></a></span>
<h2><a href="http://lesson.hexun.com/web/play.html?classId=1001162&utm_campaign=www_hexun_tzxy1">关注超跌股 分仓降低踩雷风险</a></h2>
<span class="c999 pr_lb">讲师：徐小明</span>
<span class="c999 pr_rb">热度：97%</span>
				  </div>
<div class="div3">
<span class="imgBox"><a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy"><img src="http://i7.hexun.com/2018-06-21/193242849.png"  alt=""></a></span>
<h2><a href="http://lesson.hexun.com/web/play.html?classId=1001163&utm_campaign=www_hexun_tzxy2">KDJ和MACD的特点以及结合运用</a></h2>
<span class="c999 pr_lb">讲师：冯矿伟</span>					
<span class="c999 pr_rb">热度：92%</span>				  </div>
<div class="div5">
<span class="imgBox"><a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy"><img src="http://i7.hexun.com/2018-06-21/193242849.png" alt=""></a></span>
<h2><a href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=817248&utm_campaign=www_hexun_tzxy3">分化相对乐观 降低交易频率</a></h2>
<span class="c999 pr_lb">讲师：冯矿伟</span>
<span class="c999 pr_rb">热度：95%</span>
				  </div>
<div class="div4">
<span class="imgBox"><a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy"><img src="http://i6.hexun.com/2018-06-21/193242869.png" alt=""></a></span>
<h2><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=816769&utm_campaign=www_hexun_tzxy4">挖掘机行业或将迎来井喷行情</a> <span class="c999 pr_lb"></span>  </h2>
<span class="c999 pr_lb">讲师：王赫</span>
<span class="c999 pr_rb">好评：90%</span>
				  </div>
<div class="div1">
<span class="imgBox"><a href="http://caidao.hexun.com/lesson/?utm_campaign=www_hexun_tzxy"><img src="http://i6.hexun.com/2018-06-21/193242869.png" alt=""></a></span>
<h2><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=816767&utm_campaign=www_hexun_tzxy5">股市大起大落 反弹能延续吗</a></h2>
<span class="c999 pr_lb">讲师：财富大魔方</span>
<span class="c999 pr_rb">人气：28789</span>
				  </div>
		  </div>
</div>
   </div>
	
</div>
<!--股票,行情,数据,投顾,研报,策略 e-->

<!--信托,私募,基金,理财,P2P-->
<div class="layout mg pt44 pb20 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class=s href="http://funds.hexun.com/">基金</a><i></i><a href="http://funds.hexun.com/smjj">私募</a><i></i><a href="http://trust.hexun.com/">信托</a>
		</div>

		<div class="newsList">
<ul sizset="105" sizcache="0">
<li><a href="http://funds.hexun.com/2018-08-17/193803572.html" 360chrome_form_autofill="2">双汇跌停 抱团取暖的基金经理心已不齐</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803723.html" target=_blank 360chrome_form_autofill="2">发行失败频现　基金发行“寒冬”已至</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803726.html" 360chrome_form_autofill="2">市场需求巨大　养老资管人才成“香饽饽”</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803727.html" target=_blank 360chrome_form_autofill="2">基金经理普遍一拖多　基金业求贤若渴</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803194.html" 360chrome_form_autofill="2">双GP备案收紧 “借通道”模式难以为继</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803331.html" 360chrome_form_autofill="2">养老目标基金需便民金融科技平台助力</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803307.html" target=_blank 360chrome_form_autofill="2">对冲基金开启避险投资模式 涌入美元、日元</a></li>

<li><a class=red href="http://funds.hexun.com/smjj" 360chrome_form_autofill="2">私募</a><em>|</em> <a href="http://funds.hexun.com/2018-08-16/193792130.html" 360chrome_form_autofill="2">私募卖壳生意要凉？中基协出新要求</a></li>

<li><a href="http://funds.hexun.com/2018-08-17/193803449.html" 360chrome_form_autofill="2">5家私募被证监局责令整改 网红基金在列</a></li>

<li><a class=red href="http://trust.hexun.com/" 360chrome_form_autofill="2">信托</a><em>|</em><a href="http://trust.hexun.com/2018-08-17/193803309.html" 360chrome_form_autofill="2">家族信托存量规模合计超500亿</a></li>
</ul>

		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class=s href="http://iof.hexun.com/">互金</a><i></i><a href="http://money.hexun.com/">理财</a><i></i><a href="http://bond.hexun.com/">债券</a>
</div>
<div class="newsList">
<ul>
<li><a class=red href="http://p2p.hexun.com/" 360chrome_form_autofill="2">P2P</a><em>|</em><a href="http://p2p.hexun.com/2018-08-17/193803156.html" target=_blank 360chrome_form_autofill="2">P2P平台钱包金融现兑付危机</a></li>

<li><a href="http://p2p.hexun.com/2018-08-14/193769243.html" target=_blank 360chrome_form_autofill="2">网贷行业十举措堵风险行业面临大洗牌</a></li>

<li><a href="http://p2p.hexun.com/2018-08-13/193766857.html" target=_blank 360chrome_form_autofill="2">今年底前P2P平台完成自查自纠</a></li>
</ul>


<ul>
<li><a class=red href="http://money.hexun.com/" 360chrome_form_autofill="2">理财</a><em>|</em> <a href="http://money.hexun.com/2018-08-17/193803897.html" target=_blank 360chrome_form_autofill="2">突然间，流行降薪了</a></li>

<li><a href="http://money.hexun.com/2018-08-17/193803892.html" target=_blank 360chrome_form_autofill="2">如何成为传说中的期权策略投资大神？</a></li>

<li><a href="http://money.hexun.com/2018-08-17/193803943.html" target=_blank 360chrome_form_autofill="2">理财市场发生重要变化 财商培养要与时俱进</a></li>

<li><a href="http://money.hexun.com/2018-08-17/193803985.html" target=_blank 360chrome_form_autofill="2">头发做手链 周生生是ayawawa关门弟子？</a></li>

<li><a href="http://money.hexun.com/2018-08-16/193792556.html" target=_blank 360chrome_form_autofill="2">“理财不慎”挣9个亿 黄晓明账户委托理财</a></li>
</ul>

<ul>
<li><a class=red href="http://bond.hexun.com/" 360chrome_form_autofill="2">债券</a><em>|</em><a href="http://bond.hexun.com/2018-08-17/193803541.html" target=_blank 360chrome_form_autofill="2">地产债发行好转 市场谨慎配置</a></li>

<li><a href="http://bond.hexun.com/2018-08-17/193803775.html" target=_blank 360chrome_form_autofill="2">信用风险事件不断 城投平台转型急切</a></li>
</ul>


		</div>
	</div>
	
	<div class="c0 ml40">
<style>
.lck{overflow:visible}
.lck .details span em.f30{
    line-height: 36px;
height:36px;
}
</style>
<div class=lck >
				<div class=hd >
					<a href="http://licaike.hexun.com/" ></a>
				</div>
				<div class=bd>	
					<dl class="lckBox">
						<dt><img src="http://img.hexun.com/www/20170929/lck_icon_1.jpg" alt=""></dt>
						<dd>
							<div class="txtBox">
								<h2><a href="http://funds.hexun.com/2017-04-25/188952271.html">个基私诊，为您解忧！</a></h2>
								<p>投资疑难，逐一解答！</p>
							</div>
							<a href="http://funds.hexun.com/2017-04-25/188952271.html" class="lckBtn1">我要诊断</a>
						</dd>
					</dl>
					<dl class="lckBox">
						<dt><img src="http://img.hexun.com/www/20170929/lck_icon_2.jpg" alt=""></dt>
						<dd>
							<div class="txtBox">
								<h2><a href="http://licaike.hexun.com/subject/sub_hqy01.html">收益最高超活期10-20倍</a></h2>
								<p>买卖0费用 T+0快速取现</p>
							</div>
							<a href="http://licaike.hexun.com/subject/sub_hqy01.html" class="lckBtn2">产品推荐</a>
						</dd>
					</dl>
					<dl class="lckBox br_no">
						<dt><img src="http://img.hexun.com/www/20170929/lck_icon_3.jpg" alt=""></dt>
						<dd>
							<div class="txtBox">
								<h2><a href="https://fmall.hexun.com/fmall-website/?utm_campaign=web_www">开启互金理财新篇章</a></h2>
								<p>最高20倍活期收益说送就送</p>
							</div>
							<a href="https://fmall.hexun.com/fmall-website/?utm_campaign=web_www" class="lckBtn3">立即抢购</a>
						</dd>
					</dl>
				</div>
				<div class="ft">
					<a href="https://emall.licaike.com/fund/login/Init.action?knownchannel=hslck-gm"><img src="http://img.hexun.com/www/20170929/lck_btn_1.jpg" alt=""></a>
					<a href="https://emall.licaike.com/fund/register/Rit1Init.action?knownchannel=hslck-kh" class="flr"><img src="http://img.hexun.com/www/20170929/lck_btn_2.jpg" alt=""></a>
				</div>
		</div>
	</div>
	
</div>
<!--信托,私募,基金,理财,P2P e-->

<div class="layout mg pt40 pb40" id="tonglan_2" style="margin-top:40px"></div>


<!--和讯热门金融产品-->
<div class="layout mg pt40 pb40 fProduct"   style="display:none;">
	<div class="sclasstitle">
		<h4>和讯直播</h4>
	</div>
	<div class="sclasstitle moreclass">
		<a href="http://caidao.hexun.com/lesson/index.html"><span>更多&gt;&gt;</span></a>
	</div>
	<div class="hxlive clearfix">
	    
	<div class="hxlivebox livebox lboxl">
		<div class="videopic">
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=510385"><img src="http://cnstatic01.e.vhall.com/upload/webinars/img_url/24/ad/24ad961357c850f678b828fe5edeed3d.jpg" ></a>
			<div class="lvcover" onclick="location=''">
				<a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=510385"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>
			</div>
		</div>
		<div class="videotitle">
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=510385"><span>史月波午盘加油站</span></a>
		</div>
		<div class="videodetails">
			<a class="detail anchor" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=510385"><span>史月波高控盘</span></a>
			<span class="detail viewer"><span>431</span></span>
			<span class="detail">人看过</span>
		</div>
	</div>
	<div class="livebox lboxr">
        	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=518208"><img src="http://cnstatic01.e.vhall.com/upload/webinars/img_url/24/ad/24ad961357c850f678b828fe5edeed3d.jpg"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=518208"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=518208"><span>午盘解读</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=518208"><span>史月波高控盘</span></a>	
			<span class="detail viewer"><span>654</span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
       	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=0"><img src="http://cnstatic01.e.vhall.com/upload/webinars/img_url/d7/11/d711756096bf7390dbf6da3e7da40907.jpg"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=0"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=0"><span>史月波直播室</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=0"><span>史月波高控盘</span></a>	
			<span class="detail viewer"><span>34633</span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
       	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://lesson.hexun.com/web/play.html?classId=206104"><img src="http://i4.hexun.com/2017-09-30/191084998.png"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://lesson.hexun.com/web/play.html?classId=206104"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://lesson.hexun.com/web/play.html?classId=206104"><span>双轮驱动选股法</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://lesson.hexun.com/web/play.html?classId=206104"><span>史月波高控盘</span></a>	
			<span class="detail viewer"><span></span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
       	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=514803"><img src="http://cnstatic01.e.vhall.com/upload/webinars/img_url/24/ad/24ad961357c850f678b828fe5edeed3d.jpg"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=514803"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=514803"><span>2017.11.15【午盘解析】</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=514803"><span>史月波高控盘</span></a>	
			<span class="detail viewer"><span>333</span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
       	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=509106"><img src="http://cnstatic01.e.vhall.com/upload/webinars/img_url/24/ad/24ad961357c850f678b828fe5edeed3d.jpg"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=509106"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=509106"><span>2017.11.9【午盘解析】</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=509106"><span>史月波高控盘</span></a>	
			<span class="detail viewer"><span>546</span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
       	<div class="hxlivebox">	
		<div class="videopic">	
			<a class="livelink" href="http://lesson.hexun.com/web/play.html?classId=204768"><img src="http://px.hexun.com/ClassImages/20170607-144111-546.jpg"></a>	
			<div class="lvcover" onclick="location=''">	
				<a href="http://lesson.hexun.com/web/play.html?classId=204768"><img src="http://i9.hexun.com/2016/pc/index_ver171115/img/playericon.png"> </a>	
			</div>	
		</div>	
		<div class="videotitle">	
			<a class="livelink" href="http://lesson.hexun.com/web/play.html?classId=204768"><span>易问道公开课</span></a>	
		</div>	
		<div class="videodetails">	
			<a class="detail anchor" href="http://lesson.hexun.com/web/play.html?classId=204768"><span>易问道</span></a>	
			<span class="detail viewer"><span></span></span>	
			<span class="detail">人看过</span>	
		</div>	
	</div>
    	</div>
 <!--{2018-06-29 14:54:53}-->
	</div>
</div>

<div class="layout mg pt40 pb40 fProduct"  style="display:none;">

<h4>和讯热门证券产品</h4>
	 
	<div class="con clearfix">
		<div class="col bor">
			<div class="i1"></div>
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/040008.shtml" target=_blank 360chrome_form_autofill="2">信达澳银新能源股票</a></strong> <em>基金类型：股票型</em> 
<div class=txt1 360chrome_form_autofill="2">近3个月收益：<span><i>19.68</i>%</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>申购费率: 1.50% </span><a class=bn href="http://jingzhi.funds.hexun.com/040008.shtml" target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://px.hexun.com/t3764690/default.html" target=_blank 360chrome_form_autofill="2">王者视频高级语音课</a></strong> <em>跑赢大盘的王者</em> 
<div class=txt1 360chrome_form_autofill="2">超值价格：<span><i>1000</i>元/月</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>赠指标使用权限</span> <a class=bn href="http://px.hexun.com/t3764690/default.html?utm_medium=dkz " target=_blank 360chrome_form_autofill="2">立即抢购</a> </div></div>
		</div>
		<div class="col bor">
			<div class="i2"></div>
<div class="box bob" 360chrome_form_autofill="2"><strong><a class=bn href="http://caidao.hexun.com/13798641/index.html?utm_medium=dkz" 360chrome_form_autofill="2" targ et="_blank">史月波操盘手培训课套餐</a></strong><em>和讯讲师：史月波</em> 
<div class=txt1 360chrome_form_autofill="2">超值价格：<span><i>1000</i>元/月</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>买一送一</span> <a class=bn href="http://caidao.hexun.com/13798641/index.html?utm_medium=dkz" target=_blank 360chrome_form_autofill="2">立即抢购 </a></div></div>
			 
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://px.hexun.com/t19444494/default.html?utm_campaign=web_www_zqcp" target=_blank 360chrome_form_autofill="2">金色池塘实战牛股套餐</a></strong> <em>财智人生</em> 
<div class=txt1 360chrome_form_autofill="2">超值特惠：<span><i> 11600</i>元/年</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>原价：18000元/年</span> <a class=bn href="http://px.hexun.com/t19444494/default.html?utm_campaign=web_www_zqcp" target=_blank 360chrome_form_autofill="2">立即抢购</a> </div></div>
			 
		</div>
		<div class="col">
			<div class="i3"></div>
<div class="box bob" 360chrome_form_autofill="2"><strong><a class=bn href="http://px.hexun.com/t10780870/default.html" target=_blank 360chrome_form_autofill="2">冯矿伟高级网络实战课程</a></strong> <em>和讯讲师：冯矿伟</em> 
<div class=txt1 360chrome_form_autofill="2">特惠价格：<span><i>7000</i>元/年</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>原价15800/年</span> <a class=bn href="http://px.hexun.com/t10780870/default.html" target=_blank 360chrome_form_autofill="2">立即抢购</a> </div></div>
			 
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://caidao.hexun.com/1037523/index.html?utm_medium=dkz" target=_blank 360chrome_form_autofill="2">夏立军掘金涨停VIP套餐</a></strong> <em> 投资名家：夏立军</em> 
<div class=txt1 360chrome_form_autofill="2">特惠价格：<span><i>3800元/月</i></span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>买到就是赚到</span><a class=bn href="http://caidao.hexun.com/1037523/index.html?utm_medium=dkz" target=_blank 360chrome_form_autofill="2">立即抢购</a> </div></div>
			 
		</div>
	</div>
</div>
<!--和讯热门金融产品 e-->

<!--原油,大宗商品,期货,期指,现货-->
<div class="layout mg pt10 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class=s href="http://crudeoil.hexun.com/index.html">原油</a><i style="background: none;"></i><a href="javascript:void(0)"></a> 
<div id=yydz_gm></div>
		 
		</div>
		 
		<div class="stockData clearfix">
			<div class="left" id="NYMEXCLcv1"></div>
			<div class="right" id="ICELCOcv1"></div>
		</div>
		<div class="newsList">
			
<ul sizset="122" sizcache="0">


<li><a href="http://futures.hexun.com/2018-08-17/193804516.html" 360chrome_form_autofill="2">SC原油受累下跌 下游表现不一</a></li>



<li><a href="http://crudeoil.hexun.com/2018-08-17/193803671.html" 360chrome_form_autofill="2">多重利空因素共振 原油短期弱势难改 </a></li>


<li><a href="http://crudeoil.hexun.com/2018-08-17/193804343.html" 360chrome_form_autofill="2">中美贸易紧张局势有望缓解 油价反弹</a></li>


<li><a href="http://futures.hexun.com/2018-08-17/193803774.html" 360chrome_form_autofill="2">油价已系统性上台阶 对能化行业影响深远  </a></li>


<li><a href="http://crudeoil.hexun.com/2018-08-17/193804356.html" 360chrome_form_autofill="2">美国务院成立“伊朗行动组”监督对伊制裁 </a></li>





<li><a href="http://futures.hexun.com/2018-08-17/193803338.html" 360chrome_form_autofill="2">引入做市商制度 原油期货有望率先受益  </a></li>


<li><a href="http://futures.hexun.com/2018-08-17/193803317.html" 360chrome_form_autofill="2">下半年成品油调价料首次搁浅 油价上涨承压
</a></li>



</ul>
				 
		
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class=s href="http://futures.hexun.com/">期货</a><i></i><a href="http://qizhi.hexun.com/">期指</a><i></i><a href="http://xianhuo.hexun.com/">现货</a><div id="qhqz_gm"></div>
		 
		</div>
		<div class="newsList">
<ul sizset="132" sizcache="0">
<li><a href="http://futures.hexun.com/2018-08-17/193809898.html" 360chrome_form_autofill="2">苹果涨停焦炭暴涨近7% 螺纹成交量超四百万</a></li>







<li><a href="http://futures.hexun.com/2018-08-17/193803159.html" 360chrome_form_autofill="2">突破2500！是“谁”推动焦炭节节攀升？</a></li>










<li><a href="http://futures.hexun.com/2018-08-17/193803218.html" 360chrome_form_autofill="2">一鸣惊人 起飞21天的PTA还能翱翔吗</a></li>









<li><a href="http://futures.hexun.com/2018-08-17/193803939.html" 360chrome_form_autofill="2">外围市场普跌 沪胶期价加速探底</a></li>








<li><a href="http://futures.hexun.com/2018-08-17/193803365.html" 360chrome_form_autofill="2">有色金属集体沦陷后 噩梦还会不会再来？ </a>





</li>
<li><a href="http://futures.hexun.com/2018-08-17/193803732.html" 360chrome_form_autofill="2">考虑远月卷螺差套利、动煤中线做多机会</a></li>








<li><a href="http://futures.hexun.com/2018-08-17/193803365.html" 360chrome_form_autofill="2">解析：钢铁行业频繁限产究竟为哪般？</a></li>









<li><a href="http://futures.hexun.com/2018-08-17/193803197.html" 360chrome_form_autofill="2">有色金属价格承压 铜锌期货创逾一年新低 </ </a></li>









<li><a class="red" href="http://qizhi.hexun.com/" 360chrome_form_autofill="2">期指</a><em>|</em><a href="http://qizhi.hexun.com/2018-08-17/193808398.html" 360chrome_form_autofill="2">期指早盘延续跌势 期债盘中跳水</a></li>









<li><a class="red" href="http://xianhuo.hexun.com/" 360chrome_form_autofill="2">现货</a><em>|</em><a href="http://xianhuo.hexun.com/2018-08-17/193804559.html" 360chrome_form_autofill="2">清理整顿引导交易场所走出“至暗时刻” 

</a></li>










</ul>
		</div>
	</div>
	
	<div class="c0 ml40">
	<iframe src="http://open.tool.hexun.com/MongodbNewsService/hexunIndex/zgqhds.jsp" width="300" height="370" frameborder="0"  marginwidth="0" marginheight="0" scrolling="no" frameborder="No" border="0" id=""></iframe>		</div>
</div>
<!--原油,大宗商品,期货,期指,现货 e-->

<!--银行,互联网金融-->
<div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class=s href="http://bank.hexun.com/">银行</a><i></i><a href="http://xfjr.hexun.com/">消费金融</a>
		 
		</div>
		 
		<div class="bankData">
			<strong>一年期利率</strong>
			<p><a href="http://data.bank.hexun.com/ll/ckll.aspx">存款<i id="deposit"></i>%</a>，<a href="http://data.bank.hexun.com/ll/dkll.aspx">贷款<i id="loan"></i>%</a></p>
		</div>
		<script>stockData.deposit();</script>
		<div class="newsList">
		
<ul>
<li><a href="http://bank.hexun.com/2018-08-17/193803793.html" target=_blank 360chrome_form_autofill="2">时隔多日央行重启逆回购天净投放400亿元</a></li>

<li><a href="http://bank.hexun.com/2018-08-17/193803333.html" target=_blank 360chrome_form_autofill="2">违法违规！8家银行遭外汇局罚款超2700万</a></li>

<li><a href="http://stock.hexun.com/2018-08-17/193803152.html" target=_blank 360chrome_form_autofill="2">酒鬼酒存款失踪案判决农行赔付5933.67万</a></li>

<li><a href="http://bank.hexun.com/2018-08-17/193804945.html" target=_blank 360chrome_form_autofill="2">银行不良上升不一定代表资产质量恶化 </a></li>

<li><a href="http://bank.hexun.com/2018-08-15/193781616.html" target=_blank 360chrome_form_autofill="2">1～7月消费金融ABS发行量缩水70％</a></li>

<li><a class=red href="http://pe.hexun.com/" 360chrome_form_autofill="2">创投</a><em>|</em><a href="http://pe.hexun.com/2018-08-16/193792242.html" 360chrome_form_autofill="2">陆奇的下一站：中国创投圈</a></li>
</ul>


<ul>
<li><a class=red href="http://xfjr.hexun.com/" 360chrome_form_autofill="2">消金</a><em>|</em><a href="http://news.hexun.com/2018-08-17/193803461.html" 360chrome_form_autofill="2">女性消费经济催生消费金融黄金时代</a></li>
</ul>
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class=s href="http://insurance.hexun.com/">保险</a><i></i><a href="http://pension.hexun.com/">养老金</a>
	 
		</div>
		<div class="newsList">
			<ul sizset="149" sizcache="0">

<li><a href="http://insurance.hexun.com/2018-08-17/193803220.html" target=_blank 360chrome_form_autofill="2">银保监会重罚两家保险中介61万元</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193803446.html" target=_blank 360chrome_form_autofill="2">银保监会拟规定责任险不得保网贷</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193803210.html" target=_blank 360chrome_form_autofill="2">多家寿险公司新增保费不足 现金流为负</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193803214.html" target=_blank 360chrome_form_autofill="2">三上市险企前7月保费同比增12%至9180亿元</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193803219.html" target=_blank 360chrome_form_autofill="2">寿险渠道数据透视：银邮渠道转型压力更大</a></li>

<li><a href="http://insurance.hexun.com/2018-08-16/193796607.html" target=_blank 360chrome_form_autofill="2">人保再迎高层人事变动 部门整合透视新战略</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193805646.html" target=_blank 360chrome_form_autofill="2">广东企业500强揭晓 富德生命列保险业第2</a></li>

<li><a href="http://insurance.hexun.com/2018-08-17/193807200.html" target=_blank 360chrome_form_autofill="2">阳光首个区块链健康数据授权查看证上线</a></li>




</ul>
<ul>

<li><a href="http://insurance.hexun.com/2018-08-16/193792137.html" target=_blank 360chrome_form_autofill="2">安达百慕大保险拟受让华泰保险5000万股权</a></li>

<li><a href="http://money.hexun.com/2018-08-16/193792266.html" target=_blank 360chrome_form_autofill="2">蒋光祥:以房养老既需要也有望实现两厢情愿</a></li>




</ul>
			
		</div>
	</div>
	
	<div class="c0 ml40">
	<iframe src="http://insurance.hexun.com/hxsyfxbtjw/" width="300" height="370" frameborder="0"  marginwidth="0" marginheight="0" scrolling="no" frameborder="No" border="0" id=""></iframe>

	</div>
</div>
<!--银行,互联网金融 e-->

		<div class="layout mg pt40"  id="tonglan_3"></div>


<!--私财-->
<div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class="s" href="https://sicai.hexun.com/" 360chrome_form_autofill="2">和讯私财</a><i></i><a href="https://sicai.hexun.com/login.do?gourl=https://cp.hexun.com/" 360chrome_form_autofill="2">财富管理</a>
		 
		</div>
		<div class="newsPic">
		
<a href="https://sicai.hexun.com/news/detail.do?id=384" target=_blank 360chrome_form_autofill="2"><img alt="" src="https://p2.ssl.cdn.btime.com/t01dbc5bc7eb1ca1385.jpg?size=492x287" 360chrome_form_autofill="2"></a> <a class=t href="https://sicai.hexun.com/news/detail.do?id=384" 360chrome_form_autofill="2">中国"早晚是下一个土耳其"?</a><a class=m href="https://sicai.hexun.com/news/detail.do?id=384" 360chrome_form_autofill="2">详情&gt;&gt;</a>
			 
		</div>
		<div class="newsList">
			
<ul>
<li><a href="https://sicai.hexun.com/news/detail.do?id=386" 360chrome_form_autofill="2">阿里巴巴与上海战略合作，打造新零售之都</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=387" 360chrome_form_autofill="2">骗局，农民怀揣致富梦想却成去产能背锅侠！</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=388" 360chrome_form_autofill="2">国企改革提速明显 投资主线都在这里了！</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=396" 360chrome_form_autofill="2">明星片酬只是小意思，玩炒股投资才赚大钱</a></li>

<li><a class=red href="https://sicai.hexun.com/news/list.do?t=5" 360chrome_form_autofill="2">海外投资</a><em>|</em><a href="https://sicai.hexun.com/news/detail.do?id=389" 360chrome_form_autofill="2">天然气价格：世界版图与中国</a></li>

<li><a class=red href="https://sicai.hexun.com/news/list.do?t=6" 360chrome_form_autofill="2">一带一路</a><em>|</em><a href="https://sicai.hexun.com/news/detail.do?id=385" 360chrome_form_autofill="2">环球时报:美国谁抹黑"一带一路"</a></li>
</ul>

		
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
		<a class="s" href="https://sicai.hexun.com/login.do?gourl=https://cp.hexun.com/" 360chrome_form_autofill="2">理财规划</a><i></i><a href="https://sicai.hexun.com/login.do" 360chrome_form_autofill="2">产品诊断</a>
	 
		</div>
		<div class="newsPic">
		<a href="https://sicai.hexun.com/news/detail.do?id=391" target=_blank 360chrome_form_autofill="2"><img alt="" src="https://file.caifashe.com/f80c53112bcc4490bb7ad3b5583d4ca7.jpg" 360chrome_form_autofill="2"></a> <a class=t href="https://sicai.hexun.com/news/detail.do?id=391" 360chrome_form_autofill="2">不吹不黑！中国科技到底skr什么水平？</a><a class=m href="https://sicai.hexun.com/news/detail.do?id=391" 360chrome_form_autofill="2">详情&gt;&gt;</a>
		</div>
		<div class="newsList">
			
		<ul>
<li><a href="https://sicai.hexun.com/news/detail.do?id=390" 360chrome_form_autofill="2">急于套现的社会没有前途</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=392" 360chrome_form_autofill="2">结婚率减30%，网越发达“单身狗”越多？</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=393" 360chrome_form_autofill="2">土耳其不浪漫了，这事儿还挺严重的</a></li>

<li><a href="https://sicai.hexun.com/news/detail.do?id=395" 360chrome_form_autofill="2">最新，中国千禧一代将面临养老金短缺问题</a></li>

<li><a class=red href="https://sicai.hexun.com/news/list.do?t=3" 360chrome_form_autofill="2">金融法律</a><em>|</em><a href="https://sicai.hexun.com/news/detail.do?id=394" 360chrome_form_autofill="2">今年Q1上市公司应收账规模分析</a></li>

<li><a class=red href="https://sicai.hexun.com/news/list.do?t=7" 360chrome_form_autofill="2">活动</a><em>|</em><a href="https://sicai.hexun.com/news/detail.do?id=379" 360chrome_form_autofill="2">企业家创新国际峰会2018济南开幕</a></li>
</ul>

			
		</div>
	</div>
	<div class="c0 ml40">
		<div class="c0 ml40" style="margin-left:0px;">
<style>
.lck{overflow:visible}
.lck .details span em.f30{
    line-height: 36px;
height:36px;
}
</style>
<div class="lck">
<div class="hd" style="background:url(https://file.caifashe.com/facc8ff140d04b7882c015707a808c64.jpg) 0 -115px">
					<a href="http://sicai.hexun.com/"></a>
				</div>
				<div class="bd">	
					<dl class="lckBox">
						<dt><img src="https://file.caifashe.com/41d0c74cc73f482583f21461ef07a0e3.jpg" alt=""></dt>
						<dd>
							<div class="txtBox">
								<h2><a href="https://sicai.hexun.com/login.do?gourl=https://cp.hexun.com/">智能测评 专业规划</a></h2>
								<p>君子爱财，升值有道！</p>
							</div>
							<a href="https://sicai.hexun.com/login.do?gourl=https://cp.hexun.com/" class="lckBtn3">我要检测</a>
						</dd>
					</dl>
					<dl class="lckBox br_no">
						<dt><img src="https://file.caifashe.com/916a2953b69b4cb3a3ff1c2587a18faf.jpg" alt=""></dt>
						<dd>
							<div class="txtBox">
								<h2><a href="https://sicai.hexun.com/login.do">剖析理财产品真面目</a></h2>
								<p>理财我很放心</p>
							</div>
							<a href="https://sicai.hexun.com/login.do" class="lckBtn2">产品诊断</a>
						</dd>
					</dl>
					
				</div>
				<div class="ft">
					
<a href="https://sicai.hexun.com/news/detail.do?id=194">
<img src="https://file.caifashe.com/d7ba7d8d7cc242a19d977f2406efb507.jpg" alt="">
</a>
					
				</div>
		</div>
	</div>
		 
	 </div>
</div>
<!--私财 e-->


<!--黄金,白银,外汇,汇率-->
<div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class="s" href="http://gold.hexun.com/">黄金</a> <i></i> <a href="http://gold.hexun.com/silver/">白银</a><i></i> <a href="http://gold.hexun.com/2018/hjsskx/" target="_blank">快讯</a>
		 
		</div>
 		<div class="goldData">
			<div id="goldData"></div>
		</div>
		<div class="newsList">
			
<ul sizset="179" sizcache="0">
<li><font style="color: rgb(221, 221, 221);"></font><a href="http://gold.hexun.com/2018-08-17/193804323.html" target="_blank" 360chrome_form_autofill="2">黄金涨势昙花一现 市场仍面临抛售压力</a></li>
































<li><a href="http://gold.hexun.com/2018-08-17/193804493.html" target="_blank" 360chrome_form_autofill="2">美元闪跌 黄金重返1170人气依旧负面</a> </li>
































<li><a href="http://gold.hexun.com/2018-08-17/193804483.html" target="_blank" 360chrome_form_autofill="2">中美贸易释放重大信号黄金颓势不改</a></li>

































<li><a href="http://gold.hexun.com/2018-08-17/193804620.html" target="_blank" 360chrome_form_autofill="2">惨淡的夏季后 黄金旺季多头能否力挽狂澜？ </a></li>


































<li><a href="http://gold.hexun.com/2018-08-17/193804658.html" target="_blank" 360chrome_form_autofill="2">美元大涨致黄金暴跌 为何美元这么强势？ </a></li>







































</ul>

<ul>
<li><a href="http://gold.hexun.com/silver/" target="_blank" 360chrome_form_autofill="2"><font style="color: rgb(170, 0, 0);">白银</font></a><font style="color: rgb(221, 221, 221);">|</font><a href="http://gold.hexun.com/2018-08-17/193804707.html" target="_blank" 360chrome_form_autofill="2">贵金属及商品市场交易策略</a></li>

































<li><a href="http://gold.hexun.com/bullion/" target="_blank" 360chrome_form_autofill="2"><font style="color: rgb(170, 0, 0);">实物金</font></a><font style="color: rgb(221, 221, 221);">|</font><a href="http://gold.hexun.com/2018-08-17/193804363.html" target="_blank" 360chrome_form_autofill="2">最新全球各国央行黄金储备数据公布</a></li>


















































































</ul>

		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class=s href="http://forex.hexun.com/">外汇</a><i></i><a href="http://forex.hexun.com/rmb/">汇率</a>
		</div> 
		<div class="stockData clearfix">
			<div id="onshoreForex" class="left"></div>
			<div id="offshoreForex" class="right"></div>
		</div>
		<div class="newsList">
		
<ul>
<li><a href="http://forex.hexun.com/2018-08-17/193804836.html" 360chrome_form_autofill="2">土耳其、阿根廷接连中招 下一个国家是？</a></li>

<li><a href="http://forex.hexun.com/2018-08-17/193803443.html" 360chrome_form_autofill="2">21起外汇违规案曝光 内保外贷成重灾区</a></li>

<li><a href="http://forex.hexun.com/2018-08-17/193804532.html" 360chrome_form_autofill="2">中美重启贸易谈判澳元获喘息 后市仍不乐观</a></li>

<li><a href="http://forex.hexun.com/2018-08-17/193807133.html" 360chrome_form_autofill="2">土耳其危机成欧元大跌导火索 苦日子在后面</a></li>

<li><a class=red href="http://forex.hexun.com/rmb/" 360chrome_form_autofill="2">人民币</a><em>|</em><a href="http://forex.hexun.com/2018-08-17/193803445.html" 360chrome_form_autofill="2">人民币汇率上演“保7”拉锯战</a></li>

<li><a class=red href="http://fc.hexun.com/forexsalon" 360chrome_form_autofill="2">线下沙龙</a><em>|</em><a href="http://fc.hexun.com/forexsalon/489" 360chrome_form_autofill="2">CMC Markets八月投资分享讲堂</a></li>
</ul>

<ul>
<li><a class=red href="http://fc.hexun.com/" 360chrome_form_autofill="2">社区</a><em>|</em><a href="http://forex.hexun.com/2018-08-17/193804766.html" target=_blank 360chrome_form_autofill="2">工商银行：8月17日金融市场日报</a></li>
</ul>

			
		</div>
	</div>
	
	<div class="c0 ml40">
<div class="wh">
<div class=hd><a class=a1 href="http://forex.hexun.com/forexsalon/"></a><a class=a2 href="http://salon.hexun.com/gold/index.aspx"></a></div>
	<div class="bd">
<div class="msgBoard w">
<div class=clock><img alt="" src="http://img.hexun.com/zl/hx/index/images/icon_time1.jpg"></div>
<div class=top>正在进行外汇沙龙，今日 <br>15：00-18：00</div>
<dl class="userBox clearfix">
<dt><a href="http://zhibo.hexun.com/10061/default.html"><img alt=邵悦华 src="http://i1.hexun.com/2017-03-31/188702419.jpg" width=100 height=100></a> </dt>
<dd>
<h2 class=f14><a href="http://zhibo.hexun.com/10061/default.html">邵悦华</a></h2>
<p>和讯签约分析师</p><a class=aBtn href="http://zhibo.hexun.com/10061/default.html">我要提问</a> </dd></dl></div>
<div class="msgBoard h" 360chrome_form_autofill="2">
<div class=clock 360chrome_form_autofill="2"><img alt="" src="http://img.hexun.com/zl/hx/index/images/icon_time2.jpg" 360chrome_form_autofill="2"></div>
<div class=top 360chrome_form_autofill="2">正在进行黄金、白银沙龙，今日 <br>9：00-11：30</div>
<dl class="userBox clearfix">
<dt><a href="http://gold.hexun.com/2013/goldsl/" 360chrome_form_autofill="2"><img alt=李旭峰 src="http://i2.hexun.com/2017-07-31/190254748.jpg " 360chrome_form_autofill="2"></a> </dt>
<dd>
<h2 class=f14><a href="http://gold.hexun.com/2013/goldsl/" 360chrome_form_autofill="2">李旭峰</a></h2>
<p>资深投资人、分析师</p><a class=aBtn href="http://gold.hexun.com/2013/goldsl/" 360chrome_form_autofill="2">我要提问</a> </dd></dl></div>
</div>
</div>
	</div>
	
</div>
<!--黄金,白银,外汇,汇率 e-->


<!--和讯热门证券产品-->
<div class="layout mg pt40 pb40 sProduct"   style="display:none;">

	<h4>和讯热门金融产品</h4>
	 
	<div class="con clearfix">
<div class="box bob bor" 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/100060.shtml" target=_blank 360chrome_form_autofill="2">富国高新技术产业混合</a></strong> <em>逆市上涨 </em>
<div class=txt1 360chrome_form_autofill="2">近三个月收益：<span><i>11.457</i>%</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>类型：混合型</span> <a class=bn href="https://emall.licaike.com/fund/purchase/FirstLoad.action?fundCode=100060&amp;knownChannel=hexun_jjxq&amp;token=5066aa815b89ce0cf75e1edf7c982726 " target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
	 
<div class="box bor bob" 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/001705.shtml" target=_blank 360chrome_form_autofill="2">泓德战略转型股票基金</a></strong> <em>金牛基金</em> 
<div class=txt1 360chrome_form_autofill="2">近3月收益：<span><i>10.297</i>%</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>类型：股票型</span> <a class=bn href="https://emall.licaike.com/fund/purchase/FirstLoad.action?fundCode=001705&amp;knownChannel=hexun_jjxq " target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
	 
<div class="box bob" 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/001331.shtml" target=_blank 360chrome_form_autofill="2">鹏华弘信混合A</a></strong> <em>收益遥遥领先</em> 
<div class=txt1 360chrome_form_autofill="2">最新净值：<span><i>1.1625</i>元</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>类型：混合型</span> <a class=bn href="https://emall.licaike.com/fund/purchase/FirstLoad.action?fundCode=001331&amp;knownChannel=hexun_jjxq" target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
	 
<div class="box bor" 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/002443.shtml" target=_blank 360chrome_form_autofill="2">前海开源沪港深龙头</a></strong> <em>价值投资</em> 
<div class=txt1 360chrome_form_autofill="2">最新净值：<span><i>1.04</i>元</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>类型：混合型</span> <a class=bn href="https://emall.licaike.com/fund/purchase/FirstLoad.action?fundCode=002443&amp;knownChannel=hexun_jjxq" target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
	 
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/165520.shtml" target=_blank 360chrome_form_autofill="2">信诚中证800有色指数</a></strong> <em>指数型，行情火</em> 
<div class=txt1 360chrome_form_autofill="2">最新净值：<span><i>1.3104</i>元</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>申购费率：1.20%</span><a class=bn href="http://jingzhi.funds.hexun.com/165520.shtml" target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
	 
<div class=box 360chrome_form_autofill="2"><strong><a class=bn href="http://jingzhi.funds.hexun.com/040008.shtml" target=_blank 360chrome_form_autofill="2">华安策略优选</a></strong> <em>基金类型：混合型</em> 
<div class=txt1 360chrome_form_autofill="2">最新净值：<span><i>1.4214</i>元</span></div>
<div class="bottom clearfix" 360chrome_form_autofill="2"><span>申购费率: 1.50% </span><a class=bn href="http://jingzhi.funds.hexun.com/040008.shtml" target=_blank 360chrome_form_autofill="2">立即购买</a> </div></div>
		 
	</div>
</div>
<!--和讯热门证券产品 e-->

 

<!--论坛,股吧-->
<div class="layout mg pt44 clearfix" style="display:none;">
	<div class="c1">
		<div class="newsTop">
<a class=s href="javascript:void(0)" 360chrome_form_autofill="2">股吧</a><i></i><a href="javascript:void(0)/" 360chrome_form_autofill="2">论坛</a>
		 
		</div>
		<div class="newsList">
			
<ul sizcache="0" sizset="173">
<li><a href="http://caidao.hexun.com/29673582/article57279.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">什么最值得投资？也许我该回乡下种菜养鸡</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57262.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">我们应该如何拯救月光族？不妨从记账开始</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57264.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">为什么你每天辛苦的工作 还是没有升职加薪</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57263.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">虽然你的人生很长 可关键的决定就那么几个</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57268.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">你知道吗？有钱有闲才属于真正的财务自由</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57269.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">我十分好奇 金钱决定品味还是品味决定金钱</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57270.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">干货：你都不知道自己是谁还谈什么做自己</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57272.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">赚100万不是梦 教你一个最简单的方法实现</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57275.html?utm_campaign=web_www_gblink" 360chrome_form_autofill="2">思想解放！每周工作四小时你准备好了么？</a></li>

<li><a href="http://caidao.hexun.com/29667185/article57265.html?utm_campaign=web_www_gblink" target=_blank 360chrome_form_autofill="2">学习理财投资 帮你扫除财务自由路上的障碍</a></li>
</ul>

		
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
<a class=s href="http://blog.hexun.com/">博客</a><i></i><a href="http://f.blog.hexun.com/">财经博客</a>
		 
		</div>
		<div class="newsList">
			
<ul sizcache="0" sizset="184">
<li><a href="http://caidao.hexun.com/14187514/article57376.html%20?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">一个人是否靠谱，这一点瞬间说明真相！</a></li>

<li><a href="http://caidao.hexun.com/14066353/article57251.html?utm_campaign=web_www_bloglink" target=_blank 360chrome_form_autofill="2">有钱人烦恼多？说说中产阶级为何如此焦虑</a></li>

<li><a href="http://caidao.hexun.com/14187514/article57379.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">弄不懂这个赚钱逻辑，你永远都是最底层</a></li>

<li><a href="http://caidao.hexun.com/15052256/article57398.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">明白这些理财知识，2018年让你多赚10万</a></li>

<li><a href="http://caidao.hexun.com/15054257/article57391.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">必看！银行打死都不会告诉你的存钱秘诀</a></li>

<li><a href="http://caidao.hexun.com/6117109/article57247.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">达人黄斌汉：“共有产权”或引楼市大涨</a></li>

<li><a href="http://caidao.hexun.com/15052256/article57401.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">2018年新的一轮房价已经开始，来看波分析</a></li>

<li><a href="http://caidao.hexun.com/15054257/article57392.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">“投资杠杆” 通过杠杆来实现资产的增值</a></li>

<li><a href="http://caidao.hexun.com/15054257/article57390.html?utm_campaign=web_www_bloglink" 360chrome_form_autofill="2">富人越富，穷人越穷，你知道根源在哪吗？</a></li>

<li><a href="http://caidao.hexun.com/14187514/article57382.html?utm_campaign=web_www_bloglink" target=_blank 360chrome_form_autofill="2">所有成功的投资和婚姻，因做对了这两件事</a></li>
</ul>

			
		</div>
	</div>
	<div class="c0 ml40">
<iframe src="http://open.tool.hexun.com/MongodbNewsService/hexunIndex/cjmb.jsp" width="300" height="370" frameborder="0"  marginwidth="0" marginheight="0" scrolling="no" frameborder="No" border="0" id="mBoIfr"></iframe>
	</div>
</div>
<!--论坛,股吧 e-->

<!--科技,数码-->
<div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
<a class=s href="http://tech.hexun.com/">科技</a><i></i><a href="http://data.digi.hexun.com/products/index.php">数码</a>
		 
		</div>
		<div class="newsPic">
		
<a href="http://tech.hexun.com/2018-08-16/193792780.html" target=_blank 360chrome_form_autofill="2"><img alt="" src="http://i2.hexun.com/2018-08-16/193792779.jpg" 360chrome_form_autofill="2"></a> <a class=t href="http://tech.hexun.com/2018-08-16/193792780.html" 360chrome_form_autofill="2">今日头条们：一边道歉一边做大</a><a class=m href="http://tech.hexun.com/2018-08-16/193792780.html" 360chrome_form_autofill="2">详情&gt;&gt;</a>
			 
		</div>
		<div class="newsList">
			
<ul>
<li _extended="true"><a href="http://tech.hexun.com/2018-08-17/193806007.html" target=_blank 360chrome_form_autofill="2">红芯浏览器致歉：不应特别强调国产自主</a></li>

<li><a href="http://tech.hexun.com/2018-08-17/193805953.html" target=_blank 360chrome_form_autofill="2">创造101尴尬 游戏凉凉 腾讯能否拥有梦想?</a></li>

<li><a href="http://tech.hexun.com/2018-08-17/193804222.html" target=_blank 360chrome_form_autofill="2">怕了吗？亚马逊下一个扫荡的行业: 电影院</a></li>

<li><a href="http://tech.hexun.com/2018-08-17/193805497.html" target=_blank 360chrome_form_autofill="2">中国的互联网创业 也许进入了最无聊时期</a></li>

<li><a href="http://tech.hexun.com/2018-08-17/193805833.html" target=_blank 360chrome_form_autofill="2">陆奇与YC：两个中年人的患难与共</a></li>

<li><a href="http://tech.hexun.com/2018-08-17/193803806.html" target=_blank 360chrome_form_autofill="2">聊一聊电信和联通合并的可能性有多大？</a></li>
</ul>

		
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
		<a class=s href="http://auto.hexun.com/">汽车</a><i></i><a href="http://che.hexun.com/sign/">车型</a>
	 
		</div>
		<div class="newsPic">
		<a href="http://auto.hexun.com/2018-08-17/193803754.html" target=_blank 360chrome_form_autofill="2"><img alt="" src="http://i4.hexun.com/2018-08-17/193803743.jpg" 360chrome_form_autofill="2"></a> <a class=t href="http://auto.hexun.com/2018-08-17/193803754.html" 360chrome_form_autofill="2">蔚来不是特斯拉，李斌也不是马斯克</a><a class=m href="http://auto.hexun.com/2018-08-17/193803754.html" 360chrome_form_autofill="2">详情&gt;</a>
		</div>
		<div class="newsList">
			
		<ul>
<li><a href="http://auto.hexun.com/2018-08-17/193803734.html" target=_blank 360chrome_form_autofill="2">吉利首次回应负债三年几乎翻番</a></li>

<li><a href="http://auto.hexun.com/2018-08-17/193803583.html" target=_blank 360chrome_form_autofill="2">6万就能拥有双离合 长安悦翔全系购车手册</a></li>

<li><a href="http://auto.hexun.com/2018-08-17/193804389.html" target=_blank 360chrome_form_autofill="2">驾趣升级，“疾风者”混动新雅阁极速破风</a></li>

<li><a href="http://auto.hexun.com/2018-08-17/193803314.html" target=_blank 360chrome_form_autofill="2">国内导入NCM811电池 是否操之过急？</a></li>

<li><a href="http://auto.hexun.com/2018-08-17/193803868.html" target=_blank 360chrome_form_autofill="2">7万元买啥车？消费降级下这几款车必看！</a></li>

<li><a href="http://auto.hexun.com/2018-08-17/193803258.html" target=_blank 360chrome_form_autofill="2">日本对美出口连续两月下滑 汽车下跌12.1%</a></li>
</ul>

			
		</div>
	</div>
	<div class="c0 ml40">
		<style>
.hcd{height: 370px;overflow: hidden; }
.hcd .tac{text-align: center}
.hcd .f30{font-size: 30px;}
.hcd .mainColor { color: #fb5e67;}
.hcd .hd{background: url(http://i9.hexun.com/2017-08-07/190346649.jpg) ;width: 100%;height: 32px;position:relative;}
.hcd .hd a{position:absolute;top:0;left:0;height:32px;width:300px;}
.hcd .bd{ padding-top: 20px;}
.hcd .bd h2{font-size: 18px; padding:13px 0 8px 0}
.hcd .bd .aBtn{width: 190px; margin-top: 20px;}
.hcd .bd .aBtn {    border: 1px solid #f9d1d4;    border-radius: 3px;    color: #fb5e67;    display: inline-block;    font-size: 18px;    height: 34px;    line-height: 34px;    text-align: center;}
</style>
<div class=hcd>
<div class=hd></div>
<div class="bd tac"><a href="http://auto.hexun.com/qcbgt/index.html"><img alt=汽车曝光台 src="http://i8.hexun.com/2018-02-05/192401906.jpg" width=300 height=245></a> 
<a class=aBtn href="http://auto.hexun.com/qcbgt/index.html">《汽车曝光台》上线</a></div></div>
		 
	 </div>
</div>
<!--科技,数码 e-->

		<div class="layout mg pt40" id="tonglan_4"></div>


<!--海外,移民-->
<div class="layout mg pt40 clearfix">
	<div class="c1">
		<div class="newsTop">
		<a class=s href="http://haiwai.hexun.com/">海外</a><i></i><a href="http://haiwai.hexun.com/">移民</a>
		</div>
		
		<div class="newsPic">
			<a href="http://house.hexun.com/2018-08-17/193804873_1.html" target=_blank 360chrome_form_autofill="2"><img src="http://i3.hexun.com/2018-08-17/193804903.jpg" 360chrome_form_autofill="2"></a><a class=t href="http://house.hexun.com/2018-08-17/193804873_1.html" 360chrome_form_autofill="2">伊万卡参观模拟空间站 现场“秀肌肉”</a><a class=m href="http://house.hexun.com/2018-08-17/193804873_1.html" 360chrome_form_autofill="2">详情&gt;</a>
		</div>
		<div class="newsList">
		
		<ul>
<li><a href="http://house.hexun.com/2018-08-17/193804032.html" target=_blank 360chrome_form_autofill="2">新西兰立法限制外国人买房，只待总督点头</a></li>

<li><a href="http://haiwai.hexun.com/2018-08-17/193804557.html" target=_blank 360chrome_form_autofill="2">土耳其将对美国货关税翻倍 报复美制裁行动</a></li>

<li><a href="http://haiwai.hexun.com/2018-08-17/193804591.html" target=_blank 360chrome_form_autofill="2">大批英国人趁里拉贬值赴土耳其“捡便宜”</a></li>

<li><a href="http://haiwai.hexun.com/2018-08-17/193804599.html" target=_blank 360chrome_form_autofill="2">台媒：85度C被大陆多家外卖平台下架</a></li>

<li><a href="http://haiwai.hexun.com/2018-08-17/193804612.html" target=_blank 360chrome_form_autofill="2">亚洲人更在意颜值？日本整形头面部占90% </a></li>

<li><a href="javascript:void(0)" 360chrome_form_autofill="2"><font color=#990000>海外趣闻</font> </a><a href="http://haiwai.hexun.com/2018-08-17/193804795.html" target=_blank 360chrome_form_autofill="2">芬兰人这样应对“最热夏天”</a></li>
</ul>

		
		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
		<a class=s href="http://house.hexun.com/" id="content_name" >房产</a><i></i><a href="http://data.house.hexun.com/lp/product.aspx">新楼盘</a>

<script language="JavaScript">
houseDepart("content_name");
</script>
		</div>
	
		<div class="newsPic">
				<a href="http://house.hexun.com/2018-08-17/193804942.html" target=_blank 360chrome_form_autofill="2"><img alt="" src="http://i4.hexun.com/2018-08-17/193804958.jpg" 360chrome_form_autofill="2"> </a><a class=t href="http://house.hexun.com/2018-08-17/193804942.html" target=_blank 360chrome_form_autofill="2">豪宅解读者邱德光：在情怀与商业中寻找平衡</a><a class=m href="http://house.hexun.com/2018-08-17/193804942.html" target=_blank 360chrome_form_autofill="2">详情&gt;</a>
		</div>
		<div class="newsList">
		
		<ul sizset="211" sizcache="0">
<li><a href="http://house.hexun.com/2018-08-16/193799355.html" target=_blank 360chrome_form_autofill="2">盛煦王谦：存量市场未来三年形成行业格局</a> </li>

<li><a href="http://house.hexun.com/2018-08-17/193803256.html" target=_blank 360chrome_form_autofill="2">应将房租纳入调控 </a><a href="http://house.hexun.com/2018-08-17/193803252.html" target=_blank 360chrome_form_autofill="2">部分城市房租上涨探因</a></li>

<li><a href="http://house.hexun.com/2018-08-17/193803250.html" target=_blank 360chrome_form_autofill="2">房租急涨谁之过： 抢占房源机构短兵相接</a> </li>

<li><a href="http://house.hexun.com/2018-08-17/193803538.html" target=_blank 360chrome_form_autofill="2">房租暴涨还逼着二胎？北漂或被迫撤离</a> </li>

<li><a href="http://house.hexun.com/2018-08-17/193803759.html" target=_blank 360chrome_form_autofill="2">石家庄楼市乱象仍存 </a><a href="http://house.hexun.com/2018-08-17/193803740.html" target=_blank 360chrome_form_autofill="2">房地产监管风潮燃起 </a></li>

<li><a href="http://house.hexun.com/2018-08-17/193804056.html" target=_blank 360chrome_form_autofill="2">全国首例 这家租房黑中介被判黑社会性质</a> </li>
</ul>

			
		</div>
	</div>
		
	<div class="c0 ml40">
	<style>
a {
    text-decoration: none;
    color: #000;
}
a:hover {
    text-decoration: underline;
    color: #a00;
}
.hfd {
    height: 370px;
    overflow: hidden;
}

.hfd .hd {
    background: url(http://i8.hexun.com/2018-06-08/193170649.png) 0 -371px;
    width: 100%;
    height: 32px;
}

.hfd .bd {
    padding-top: 20px;
}

.hfd .bd h2 {
    font-size:22px;
    padding: 15px 0 0 0;
    margin:0;
}

.hfd .bd .aBtn {
    border: 1px solid #f9d1d4;
    border-radius: 3px;
    color: #fb5e67;
    display: inline-block;
    font-size: 16px;
    height: 34px;
    line-height: 34px;
    text-align: center;
    width: 190px;
    margin-top:12px;

}

.hfd p {
    margin:0;
    color: #999;
}
.hfd .redspan{
	color: #fb5e67;
}
.hfd span {
    color: #999
}

.hfd .hd a {
    display: inline-block;
    width: 100%;
    height: 100%;
}

.hfd .tac {
    text-align: center;
}

.hfdImg {
    display: inline-block;
    position: relative;
}

.hfdImg img {
    width: 220px;
    height: 165px;
}

.hfdImg .ing,
.hfdImg .ed {
    position: absolute;
    top: 0;
    right: 5px;
    background: url(http://img.hexun.com/lux/indexSide/images/icon_st.png);
    width: 60px;
    height: 42px;
}

.hfdImg .ed {
    background-position: -60px 0;
}
.hfd .fs12{
	font-size: 12px;
}
.hfd .fs14{
	font-size: 14px;
}

.hfd .fs24{
    font-size: 24px;
         font-style: normal;
}

</style>

<div class=hfd>
<div class=hd><a href="http://house.hexun.com/" target=_blank></a></div>
<div class="bd tac"><a class=hfdImg href="http://house.hexun.com/2018/2018lcxc/" target=_blank><img alt="" src="http://i3.hexun.com/2018-08-02/193657323.jpg"> </a>
<h2><a href="http://house.hexun.com/2018/2018lcxc/" target=_blank>
均价：14000元/平方米</a> </h2>
<a class=aBtn href="http://house.hexun.com/2018/2018lcxc/" target=_blank>点击了解</a> </div></div>
	 
	</div>
</div>
<!--海外,移民 e-->

<!--商学院,收藏-->
<!-- div class="layout mg pt44 clearfix">
	<div class="c1">
		<div class="newsTop">
		<a class=s href="http://bschool.hexun.com/">商学院</a><i></i><a href="http://shoucang.hexun.com/">收藏</a>
		</div>
		
		<div class="newsPic">
			<a href="http://bschool.hexun.com/2016-12-27/187510993.html" target=_blank 360chrome_form_autofill="2"><img alt=揭秘中国民营企业的大败局 src="http://i5.hexun.com/2016-12-27/187511194.jpg" 360chrome_form_autofill="2"> </a><a class=t href="http://bschool.hexun.com/2016-12-27/187510993.html" target=_blank 360chrome_form_autofill="2">揭秘民营企业的大败局：健力宝和华晨之殇</a><a class=m href="http://bschool.hexun.com/2016-12-27/187510993.html" target=_blank 360chrome_form_autofill="2">详情&gt;</a>
		</div>
		<div class="newsList">
				
			<ul>
<li><a href="http://bschool.hexun.com/2016-12-27/187510948.html" target=_blank 360chrome_form_autofill="2">俞敏洪：缺这8种能力 创业失败可能性很大</a></li>

<li><a href="http://bschool.hexun.com/2016-12-27/187511151.html" target=_blank 360chrome_form_autofill="2">星巴克咖啡卖不动了 出了部动画片想搞事情</a></li>

<li><a href="http://bschool.hexun.com/2016-12-27/187510897.html" target=_blank 360chrome_form_autofill="2">经济独立的成年人 是什么限制了你的优雅？</a></li>

<li><a href="http://bschool.hexun.com/2016-12-27/187511065.html" target=_blank 360chrome_form_autofill="2">赚钱本身就是最大的修行 选择比努力更重要</a></li>
</ul>

<ul>
<li><a href="http://shoucang.hexun.com/2016-12-27/187511380.html" target=_blank 360chrome_form_autofill="2">村民拆老房现大量银元遭哄抢</a></li>

<li><a href="http://shoucang.hexun.com/pic/" target=_blank 360chrome_form_autofill="2"><img alt=" " src="http://www.hexun.com/images/con_news_ico_pic.jpg" 360chrome_form_autofill="2"></a><a href="http://shoucang.hexun.com/2016-12-27/187511360.html" target=_blank 360chrome_form_autofill="2">男子收藏500张地契和票证</a></li>
</ul>


		</div>
	</div>
	<div class="c1 ml40">
		<div class="newsTop">
		<a class=s href="http://book.hexun.com/" target=_blank>读书</a><i></i><a href="http://data.book.hexun.com/categorys.aspx" target=_blank>书馆</a>
		 
		</div>
		
		<div class="newsPic">
			<a href="http://book.hexun.com/2016-12-27/187511288.html" target=_blank><img src="http://i5.hexun.com/2016-12-26/187496714.jpg"></a><a class=t href="http://book.hexun.com/2016-12-27/187511288.html" target=_blank>从天才盛产地探索天才与环境的关系</a><a class=m href="http://book.hexun.com/2016-12-27/187511288.html" target=_blank>详情&gt;</a>
		</div>
		<div class="newsList">
			
		<ul>
<li><a href="http://book.hexun.com/2016-12-27/187511174.html" target=_blank 360chrome_form_autofill="2">比房地产投资还赚钱的项目：“域名投资”</a></li>

<li><a href="http://book.hexun.com/2016-12-27/187502965.html" target=_blank 360chrome_form_autofill="2">企业如何找钱 看贾跃亭找财的七种武器</a></li>

<li><a href="http://book.hexun.com/2016-12-27/187511231.html" target=_blank 360chrome_form_autofill="2">从《我在故宫修文物》看中国的工匠精神</a></li>

<li><a href="http://book.hexun.com/2016-12-27/187511208.html" target=_blank 360chrome_form_autofill="2">有些人作努力 为什么却得不到老板的赏识</a></li>

<li><a href="http://book.hexun.com/2016-12-27/187460664.html" target=_blank 360chrome_form_autofill="2">张之洞中探花实际是慈禧太后送的顺水人情</a></li>

<li><a class=red href="http://data.book.hexun.com/category-0.shtml" target=_blank 360chrome_form_autofill="2">新书</a><em>|</em><a href="http://book.hexun.com/2016-12-27/187511378.html" target=_blank 360chrome_form_autofill="2">一个抗联战士的口述:我从朝鲜到中国</a></li>
</ul>

			
		</div>
	</div>
	
	<div class="c0 ml40">
		<iframe src="http://open.tool.hexun.com/MongodbNewsService/hexunIndex/zcyhsk.jsp" width="300" height="370" frameborder="0"  marginwidth="0" marginheight="0" scrolling="no" frameborder="No" border="0" id="libraryIfr"></iframe>
	</div>
</div -->
<!--商学院,收藏 e-->

<!--奢侈品,视频-->
<div class="layout mg pt44 pb40 clearfix">
	<div class="c1">
		<div class="newsTop">
		<a class=s href="http://hexun.gq.com.cn/?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=navigation&amp;utm_campaign=regular" rel=nofollow 360chrome_form_autofill="2">奢侈品</a>
		</div>
		

<div class="newsPic"><a href="http://www.vogue.com.cn/invogue/vogue-style/news_15339380237a4363.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_pic" target=_blank><img src="http://img3.selfimg.com.cn/Lvogue1229/2018/08/08/1533704667_a1HFsk.jpg" /></a><a href="http://www.vogue.com.cn/invogue/vogue-style/news_15339380237a4363.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular "  id="hexun_vogue_pic"  class="t">为了美女人又爱又恨</a><a href="http://www.vogue.com.cn/invogue/vogue-style/news_15339380237a4363.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_pic"  class="m">详细</a></div><div class="newsList"><style>.newsList_lux li a {font-size: 16px;margin-right: 10px;}</style><ul class="newsList_lux"><li><a href="http://hexun.gq.com.cn/fashion/news/news_19257b07261d6d90.html?time=1526898121 " id="hexun_vogue_short_text" >穿什么才能有底气？</a><a href="http://hexun.gq.com.cn/fashion/news/news_104gc79a4db1f578.html?time=1526898084 " id="hexun_vogue_short_text" >职场也能背帆布包</a></li><li><a href="http://hexun.gq.com.cn/fashion/news/news_12g196af24533138.html?time=1526898034 " id="hexun_vogue_short_text" >个性工业拼色单肩包</a><a href="http://hexun.gq.com.cn/fashion/news/news_13226395f4bf47fb.html?time=1526897989 " id="hexun_vogue_short_text" >经典的复刻高帮板鞋</a></li><li><a href="http://hexun.gq.com.cn/fashion/news/news_10gp9gebb910577c.html?time=1526383183 " id="hexun_vogue_short_text" >趣味的犬印花T恤</a><a href="http://hexun.gq.com.cn/fashion/news/news_1151619e9de2d2b0.html?time=1526383154 " id="hexun_vogue_short_text" >摩登牛皮拼色运动鞋</a></li><li><a href="http://www.cntraveler.com.cn/guide/destinations/pic_102gf1cf8c23e530.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >冬雾让这里美成仙境</a><a href="http://www.vogue.com.cn/invogue/street-chic/pic_16339b553b137b67.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >健身背心凉快又超酷</a></li><li><a href="http://www.vogue.com.cn/invogue/industry/news_1915d66e11882688.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >丹麦配饰走向全球</a><a href="http://www.vogue.com.cn/invogue/street-chic/pic_1643398f5267e1e9.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >时尚性感两不误</a></li><li><a href="http://www.vogue.com.cn/invogue/street-chic/news_101g34ad69c0c9a9.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >老牌明星时尚风向标</a><a href="http://www.vogue.com.cn/invogue/street-chic/pic_1422fcf298c68484.html?utm_source=hexun.com&amp;utm_medium=syn_OG&amp;utm_content=home_lux&amp;utm_campaign=regular " id="hexun_vogue_short_text" >这鞋好看好穿好走</a></li></ul></div>

				 
	 </div>
	<div class="c1 ml40">
		<div class="newsTop">
		<a class=s href="http://caidao.hexun.com/lesson/" 360chrome_form_autofill="2">视频</a>
		 
		</div>
		<div class="newsPic">
			<a href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=816709&amp;utm_campaign=web_www_tvlink" target=_blank 360chrome_form_autofill="2"><img src="http://i2.hexun.com/2018-06-05/193147865.jpg" 360chrome_form_autofill="2"></a> <a class=t href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=816709&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">王者：关注无退市风险被错杀的个股<span class=movIcon></span></a><a class=m href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=816709&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">详情&gt;</a>
		
		</div>
		<div class="newsList">
			
		<ul>
<li><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=816767&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">股市大起大落 反弹能延续吗</a><span class="movIcon"></span></li>


<li><a href="http://caidao.hexun.com/13798641/caibo672154728.html?reviewid=816552&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">市场还未走出中期下跌趋势</a><span class="movIcon"></span></li>


<li><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=816769&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">挖掘机行业或将迎来井喷行情<span class="movIcon"></span></a></li>


<li><a href="http://caidao.hexun.com/25500723/caibo309990233.html?reviewid=817248&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">分化相对乐观 降低交易频率<span class="movIcon"></span></a></li>


<li><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=813465&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">中证500和创业板能否成为新风口<span class="movIcon"></span></a> </li>


<li><a href="http://caidao.hexun.com/29766392/caibo241484305.html?reviewid=813394&amp;utm_campaign=web_www_tvlink" 360chrome_form_autofill="2">大资金涌向独角兽次新 后市可追吗<span class="movIcon"></span></a> </li>

</ul>
		
		</div>
	</div>
	<div class="c0 ml40">
 
<div id="publicClassNoLogin"><div class="video"><div class="hd"><a target="_blank" href="http://tv.hexun.com/2011/course/"></a></div><div class="bd"><a  class="hx_img_mask" href="http://tv.hexun.com/2018-08-08/193716344.html" target="_blank"><img alt="AI换脸终结者问世！美国防部推首款AI侦测工具，“反换脸”精度99%！ " src="http://img.hexun.com/tv/hexunlogtv.gif"><div class="mask"></div><h2><span>文强 大明 肖琴 </span>	</h2></a><p class="txt"><a target="_blank" href="http://tv.hexun.com/kj/index.html" >科技</a></p></div><div class="ft tac">	<p><a target="_blank"  href="http://tv.hexun.com/2018-08-08/193716344.html">AI换脸终结者问世！美国防部推首款AI侦测工具，“反换脸”精度99%！ </a></p>	<p><a target="_blank"  href="https://reg.hexun.com/login.aspx?gourl=www.hexun.com" class="aBtn">登录免费看精品课</a></p></div></div></div><div id="publicClassIsLogin" class="h"><div class="video">	<div class="hd hd-logined"><a href="http://tv.hexun.com/2011/course/"></a></div><div class="bd">	<dl class="videoBox clearfix">		<dt><a  target="_blank" href="http://tv.hexun.com/2018-08-08/193716344.html"><img src="http://img.hexun.com/tv/hexunlogtv.gif" alt=""></a></dt>		<dd> 		<h2><a target="_blank"  href="http://tv.hexun.com/2018-08-08/193716344.html">AI换脸终结者问世！美国防部推首款AI侦测工具，“反换脸”精度99%！ </a></h2>		<p>文强 大明 肖琴 <a target="_blank"  href="http://tv.hexun.com/2018-08-08/193716344.html" class="vTag">新智元</a>	</dd> </dl>	<dl class="videoBox clearfix">		<dt><a  target="_blank" href="http://tv.hexun.com/2018-07-18/193495208.html"><img src="http://i2.hexun.com/2018-07-18/193495210.jpg" alt=""></a></dt>		<dd> 		<h2><a target="_blank"  href="http://tv.hexun.com/2018-07-18/193495208.html">女人除了长得美和嫁得好还有这些|她能量</a></h2><a target="_blank"  href="http://tv.hexun.com/2018-07-18/193495208.html" class="vTag">她能量</a>	</dd> </dl><ul> <li> <a target="_blank"  href="http://tv.hexun.com/2018-07-11/193424022.html">大国权力竞争因何引发技术革命？——万字长文透视全球科技变迁的政经逻辑 </a> </li>	</ul></div></div>	</div>

	</div>
	
</div>
<!--奢侈品,视频 e-->
<div class="greyLayout">

<div class="layout mg pb40" id="df_tonglan"></div>
	 

	<div class="layout mg clearfix">
		<div class="w662 fl">
		
	  <h4 class="pb10"><a href="#" class="s">合作专区</a></h4>
			<div class="foucs_cover">
				<div class="scroll" id="scrollPic">
				<div class=scroll-box 360chrome_form_autofill="2">
<ul class=clearfix>
<li><a href="http://news.hexun.com/2018/ggkf40/" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i4.hexun.com/2018-05-03/192947535.jpg" 360chrome_form_autofill="2"><em></em><span>和讯致敬改革开放四十周年</span></a></li>

<li><a href="http://news.hexun.com/2017/2017cjfyb/" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i4.hexun.com/2017-12-18/192012132.jpg" 360chrome_form_autofill="2"><em></em><span>第十五届财经风云榜</span></a></li>

<li class=end><a href="http://news.hexun.com/2018/2018speech/ " rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i1.hexun.com/2018-07-24/193551812.jpg" 360chrome_form_autofill="2"><em></em><span>“2018年和讯 她能量</span></a></li>
</ul>
</div>
<div class=scroll-box 360chrome_form_autofill="2">
<ul class=clearfix>
<li><a href="http://www.cebnet.com.cn/20180629/102503110.html" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i3.hexun.com/2018-07-16/193473524.jpg" 360chrome_form_autofill="2"><em></em><span>2018贵阳论道金融与科技</span></a></li>

<li><a href="http://www.cs.com.cn/jnj/jnhw/hwjn02/" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i6.hexun.com/2018-07-31/193624688.jpg" 360chrome_form_autofill="2"><em></em><span>第二届海外基金金牛奖</span></a></li>

<li class=end><a href="http://www.cnbizmedia.com/special-7.html" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i3.hexun.com/2018-08-13/193765921.jpg" 360chrome_form_autofill="2"><em></em><span>全球社会企业家生态论坛</span></a></li>
</ul>
</div>
<div class=scroll-box 360chrome_form_autofill="2">
<ul class=clearfix>
<li><a href="http://www.hdb.com/party/m22i2.html?hdb_pos=post_info" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i7.hexun.com/2018-08-10/193740134.jpg" 360chrome_form_autofill="2"><em></em><span>2018影响力投资峰会</span></a></li>

<li><a href="http://news.hexun.com/2018/2018speech/" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i1.hexun.com/2018-07-24/193551812.jpg" 360chrome_form_autofill="2"><em></em><span>2018年和讯 她能量</span></a></li>

<li class=end><a href="http://jingji.cctv.com/special/gdll/index.shtml" rel=nofollow 360chrome_form_autofill="2"><img alt="" src="http://i3.hexun.com/2018-06-21/193242525.jpg" 360chrome_form_autofill="2"><em></em><span>股东来了</span></a></li>
</ul>
</div>
					 
				</div>
				<div class="dot-wrap" id="dot3"></div>
				<a href="javascript:;" class="leftArr" id="leftArr3"><span>&lt;</span><em></em></a>
				<a href="javascript:;" class="rightArr" id="rightArr3"><span>&gt;</span><em></em></a>
			</div> 
			<script>
				var scrollPic = new ScrollPic();
				scrollPic.scrollContId = "scrollPic"; //内容容器ID
				scrollPic.dotListId = "dot3"; //点列表ID
				scrollPic.dotClassName = ""; //点className
				scrollPic.dotOnClassName = "current"; //当前点className
				scrollPic.listType = ""; //列表类型(number:数字，其它为空)
				scrollPic.listEvent = "onmouseover"; //切换事件
				scrollPic.frameWidth = 662; //显示框宽度
				scrollPic.pageWidth = 662; //翻页宽度
				scrollPic.upright = false; //垂直滚动
				scrollPic.speed = 3; //移动速度(单位毫秒，越小越快)
				scrollPic.space = 60; //每次移动像素(单位px，越大越快)
				scrollPic.autoPlay = true; //自动播放
				scrollPic.autoPlayTime = 5; //自动播放间隔时间(秒)
				scrollPic.circularly = true;
				scrollPic.initialize(); //初始化
				document.getElementById("leftArr3").onclick = function(){scrollPic.pre();return false};
				document.getElementById("rightArr3").onclick = function(){scrollPic.next();return false};
			</script>
			<div class="list">
				<ul class="clearfix">
				<li><a href="http://news.hexun.com/2017/2017cjfyb/">第十五届财经风云榜</a></li>

<li><a href="http://stock.hexun.com/2017/nycx/">2017农业创新发展资本论坛</a></li>

<li class=end><a href="http://news.hexun.com/2018/ggkf40/" rel=nofollow>和讯致敬改革开放四十周年</a></li>

<li><a href="http://i7.hexun.com/2017-03-10/188446137.png">中国大学生消费理财报告</a></li>

<li><a href="http://insurance.hexun.com/2017/china2nd/">2017第二届中国寿险发展论坛</a></li>

<li class=end><a href="http://news.hexun.com/2017/hxsps/">和讯“她能量”财智女性Power Speech</a></li>
					 
				</ul>
			</div>
		</div>
		<div class="w300 fr">
				<h4 class="pb10"><a href="http://news.hexun.com/2015/cjzgh/index.html" id="setCJZGH1" onmouseover="index.setTab('setCJZGH',1,2)" class="s">财经中国会</a><span class="vline">|</span><a href="http://news.hexun.com/2015/cjzgh/index.html" id="setCJZGH2" onmouseover="index.setTab('setCJZGH',2,2)">财富精英俱乐部</a></h4>
			<div id="con_setCJZGH_1"><a href="http://news.hexun.com/2015/cjzgh/index.html"><img src="http://i5.hexunimg.cn/2016-05-18/183927801.gif" width="300" height="250" alt="" /></a></div>
			<div id="con_setCJZGH_2" class="h"><a href="http://news.hexun.com/2015/cjzgh/index.html"><img src="http://i2.hexunimg.cn/2016-05-18/183927798.jpg" width="300" height="250" alt="" /></a></div>
		
			 
		</div>
	</div>
</div>
<script>index.isLogin();index.onload();</script>
</div>
			<div class="footer">
<!---->
<div class="f-top">
<div class="wmar">
<div class=hx_f_nav>
<div class=fl>和讯分公司</div>
<div id=nav_listxgdx class=nav_listxgdx><span style="PADDING-BOTTOM: 0px; PADDING-LEFT: 28px; PADDING-RIGHT: 6px; PADDING-TOP: 0px" id=navspan class=fl>|</span> 
<div class=con-bank-select>
<div id=sitbox class=slet onclick="index.selectMenuList('sitbox','sitlist')"><span class=s-name>地方站</span><span class=s-jt>&nbsp;</span> 
<ul id=sitlist>
	<li style="display:none;"><a href="http://fujian.hexun.com/index.html" target=_blank>福建</a></li>
	<li><a href="http://henan.hexun.com/index.html" target=_blank>河南</a></li>
	<li style="display:none;"><a href="http://sichuan.hexun.com/index.html" target=_blank>四川</a></li>
	<!--<li><a href="http://hunan.hexun.com/index.html" target=_blank>湖南</a></li-->
	<li><a href="http://hubei.hexun.com/index.html" target=_blank>湖北</a></li>
	<li><a style="BORDER-BOTTOM: 0px" href="http://jiangsu.hexun.com/index.html" target=_blank>江苏</a></li>
</ul>
</div></div><span style="PADDING-BOTTOM: 0px; PADDING-LEFT: 20px; PADDING-RIGHT: 28px; PADDING-TOP: 0px" id=navspan01 class=fl>|</span> </div>
<div class=fl><a href="http://corp.hexun.com/contact/index.html" target=_blank rel="nofollow">联系我们</a> - <a href="http://corp.hexun.com/default/index.html" target=_blank rel="nofollow">关于我们</a> - <a href="http://www.hotjob.cn/wt/hexun/web/index?brandCode=1" target=_blank rel="nofollow">加入和讯</a> - <a href="http://corp.hexun.com/partner/" target=_blank rel="nofollow">合作伙伴</a> - <a href="http://corp.hexun.com/adcenter/index.html" target=_blank rel="nofollow">广告服务</a> - <a href="http://news.hexun.com/2015/znxz/" target=_blank rel="nofollow">和讯财经新闻端</a> - <a href="http://news.hexun.com/sitemap/" target=_blank rel="nofollow">网站导航</a> - <a href="http://corp.hexun.com/law/index.html" target=_blank rel="nofollow">授权声明</a> - <a href="http://corp.hexun.com/sm/index.html" target=_blank rel="nofollow">郑重声明</a> - <a href="http://kf.hexun.com/?id=hexun" target=_blank rel="nofollow">客服中心</a> </div></div>
</div>
</div>
<div class="hx_f_img wmar" style="width:1020px"><a href="http://www.itrust.org.cn/yz/pjwx.asp?wm=2723558454" rel="nofollow"><img src="http://img.hexun.com/www/2010/img/hlwxh.gif" alt=""></a><a href="http://www.bj.cyberpolice.cn" rel="nofollow"><img src="http://img.hexun.com/www/2010/bj110.gif" alt=""></a>
<a href="http://www.bjjubao.org" target="_blank" rel="nofollow"><img src="http://img.hexun.com/www/2013/hlwjbzx.gif" alt="北京互联网举报中心"></a><a href="http://www.baom.com.cn" rel="nofollow"><img src="http://img.hexun.com/www/2013/hlwxh.gif" alt="首都互联网协会"></a>
<!--可信网站图片LOGO安装开始-->
<script src="http://kxlogo.knet.cn/seallogo.dll?sn=e130802110100418659cqy000000&amp;size=0"></script>
<!--可信网站图片LOGO安装结束-->
<a href="http://py.qianlong.com/" rel="nofollow"><img src="http://i8.hexun.com/2017-12-21/192044093.gif" alt="北京地区网站联合辟谣平台"></a>
<a href="http://news.hexun.com/2014/wlaq/" rel="nofollow"><img src="http://img.hexun.com/www/2014/wlaq2.jpg" alt="首都网络安全日"></a><a href="http://www.12377.cn/" rel="nofollow"><img src="http://img.hexun.com/zk/201512/hs/footer_1.jpg" alt="违法和不良信息举报中心" style="border:0"></a><a href="http://www.12377.cn/node_548446.htm" target="_blank" rel="nofollow"><img src="http://img.hexun.com/zk/201512/hs/footer_2.jpg" /></a>
</div>
<div class="hx_f_con wmar channelCopy">违法和不良信息举报电话：010-85650899 客服电话：010-85650688 传真：010-85650844 邮箱：yhts#staff.hexun.com(发送时#改为@)<br />
本站郑重声明：和讯网 北京和讯在线信息咨询服务有限公司所载文章、数据仅供参考，投资有风险，选择需谨慎。<br />
[<a href="http://img.hexun.com/2015/company/ICP100713/index.html" rel="nofollow">京ICP证100713号</a>]&nbsp;&nbsp;<a href="http://img.hexun.com/2012/company/0223/index.html" rel="nofollow">互联网新闻信息服务许可</a> <a href="http://img.hexun.com/2014/company/B220090331/index.html" rel="nofollow">增值电信业务经营许可证[B2-20090331]</a>　广告经营许可证[京海工商广字第0407号] <a href="http://img.hexun.com/2015/company/1110434/index.html" rel="nofollow">测绘资质证书[乙测资字1110434]</a><br />
<a href="http://img.hexun.com/2015/company/0604/index.html" rel="nofollow">信息网络传播视听节目许可证：0109404号</a>  <a href="http://img.hexun.com/2014/company/Broadcast707/" rel="nofollow">广播电视节目制作经营许可证（京）字第707号</a>  <a href="http://img.hexun.com/2014/company/JWW2014/index2017.html" rel="nofollow">网络文化经营许可证 京网文[2017]10290-1171号</a> <br /><a href="http://img.hexun.com/2013/company/hlwyp.jpg" rel="nofollow">互联网药品信息服务资格证书 （京）-经营性-2018-0205</a><br />
<div class="icp"><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11000002000026"  class="icpico"><img src="http://www.beian.gov.cn/file/ghs.png" /><p>京公网安备 11000002000026号</p></a></div>
Copyright&copy;和讯网 北京和讯在线信息咨询服务有限公司 All Rights Reserved 版权所有 复制必究<br /></div>
</div>
<script src="http://utrack.hexun.com/track/track_hx.js"></script>
<script src="http://news.hexun.com/js/count.js?date=200911261100"></script>
<!--script language="javascript" src="http://img.hexun.com/2016/trace/tracehexun.js"></script--> 
<div id="pageTail" ></div>
<script language="javascript" src="http://hxjs.tool.hexun.com/homeway/pageMediaControl_2016.js"></script>
<script language="javascript" src="http://img.hexun.com/hx_homeway/hx_homeway_index.js"></script>
<script language="javascript" src="http://img.hexun.com/zl/hx/index/js/appDplusIndex.js"></script>
  
<script type="text/javascript">var uweb_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cscript src='" + uweb_protocol + "utrack.hexun.com/dp/hexun_uweb.js' type='text/javascript'%3E%3C/script%3E"));</script>
</body>
</html>
'''

print(Selector(text=body).xpath('//div[@class="newsList"]/ul/li/a/text()').extract())

print(Selector(text=body).xpath('//div[@class="newsList"]/ul/li/a/@href').extract())
 
 
