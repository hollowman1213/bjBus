1. 进入bjbus.com爬取通知公告；
    - 通知公告组织形式：< ..... > ，中间每个点是一个列表，每个列表下三个新闻；每个点为一个<li>；每个 > 是一个class = next-btn的<a></a>标签；
    - <div class = "news_cont">
        <div class = "item">
            <div class = "item_cont"> 
                // news block show now 
                <ul class = "list" style = "display: block">
                    // each li represent a news
                    <li>
                        <p class = "title">
                            <a href = "link of news" > title </a>
                        </p>
                        <div> display text </div> 
                    </li>
                </ul>
                // news block not show now
                <ul class = "list hide" style = "display:none">
                    // each li represent a news
                    <li>
                        <p class = "title">
                            <a hrep = "link of news" > title </a>
                        </p>
                        <div> display text </div> 
                    </li>
                </ul>
            <div class = "page_ul">
                <a href = "..." class = "prev-btn">
                ...
                <a href = "..." class = "next-btn">
            </div>
    -   $(".page_ul .next-btn").click(function(){
            sindex++;
            if(sindex>$(".pager_item li").length-1){
                sindex=0  
                $(".pager_item li").eq(sindex).click()	
            }else{
                $(".pager_item li").eq(sindex).click()	  
            } 
        })

{
    'Host':'www.bjbus.com'
    'Origin':'http://www.bjbus.com'
    'User-Agent': 'Mozilla/5.0'
    'Referer': 'http://www.bjbus.com/home/fun_news_list.php?uNewsType=1&uStyle=2&uSec=00000177&uSub=00000178'
    'Cookie': 'SERVERID=a8a28bdabe09a179b006da60d79397e0|1607595764|1607587869; Hm_lpvt_2c630339360dacc1fc1fd8110f283748=1607595171; Hm_lvt_2c630339360dacc1fc1fd8110f283748=1605873780,1606441052; acw_tc=2760828316075946761003865ea592f4ac01fb356a549a320b06a02b576df1; __utma=126505438.1761188861.1607406793.1607406793.1607587874.2; __utmc=126505438; __utmz=126505438.1607406793.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); activecity=%u5317%u4EAC%2C12956000%2C4824875%2C10; m_t_b=usertip_%251%7Cruler_%251%7Cclear_%251%7Csavemap_%251%7Ccity_%251%7Cpan_%251%7Cfzin_%251%7Cfzout_%251%7Cprint_%251%7Cfullscreen_%251%7Ccollection_%251%7Csetting_%251; SMAPUVID=1607406793035674; PHPSESSID=27b1a4ea816cd36ded80cdd9cdabcdd1'
    'X-Requested-With': 'XMLHttpRequest'
}


'txtPage': 1
'txtDisplayRows': 9
'txtType': 1
'txtCode'
'txtContainer': 'content'
'txtStyle': 2