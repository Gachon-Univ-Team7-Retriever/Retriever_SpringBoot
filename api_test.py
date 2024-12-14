import requests
from collections import OrderedDict
import json

test_set = [
    {
        'url': "http://127.0.0.1:5000/preprocess/extract/web_promotion",
        'data': {"html":
            '''
            <html lang="ko" class=" js cssanimations"><head><script type="text/javascript" id="www-widgetapi-script" src="https://www.youtube.com/s/player/3bb1f723/www-widgetapi.vflset/www-widgetapi.js" async=""></script>
            
                <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="theme-color" content="#00dce0">
            <meta name="msapplication-navbutton-color" content="#00dce0">
            <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
            
            <title>텔레pepegarden떨팝니다 : 생명안전연구소</title>
            <meta name="application-name" content="텔레pepegarden떨팝니다 : 생명안전연구소">
            <meta name="msapplication-tooltip" content="텔레pepegarden떨팝니다 : 생명안전연구소">
            <meta property="article:published_time" content="2024-09-06T16:51:17+09:00">
            <meta property="og:type" content="article">
            <meta property="og:title" content="텔레pepegarden떨팝니다 : 생명안전연구소">
            <meta property="og:url" content="https://xn--v42b19i81d99c.com/186/?bmode=view&amp;idx=95396760">
            <meta name="description" content="텔레pepegarden떨팝니다채널 T.me/Pepe_Garden문의 @pepegarden오픈톡t.me/+D-_3LaM0RAg5OWMy떨,떨액 두가지만 취급합니다.오픈톡과 채널 운영중이고합리적인가격으로 운영합니다.하이코리아 에서 미미월드위니드플라워 전부 겪어왔습니다.오래된 경험으로 최상급 퀄리티로 안전하게 나눔하겠니다.#떨팝니다#떨팔아요#강남떨#용산떨#홍대떨#떨인증딜러#떨삽니다#하이코리아#하이코리아네오#떨씨앗#미미월드#위니플#위니드플라워#버드팝니다#간자팝니다#떨드랍#떨선드랍#수원떨#인천떨#제주떨#부산떨#대마효능#대마합법#대마초팝니다#대마팝니다#떨팔아요#광주떨#떨액팝니다#떨액팔아요#떨액삽니다#떨액#대마액상#대마씨앗#대마재배#대마초#동작떨#광진떨#마포떨#천안떨#대구떨#대전떨#안산떨#청주떨#제주도떨#강북떨#논현떨#클럽떨#떨판매#Thc#cbd#홍대떨#한국딥웹#위니드플라워#하이코리아네오#탑코리아#건대떨#떨사요#떨인증딜러#떨팝니다#떨사는곳#쿠쉬팝니다#태국떨#북미떨#떨씨앗배송#떨씨앗국제택배#의료용대마#블루드림#레몬헤이즈#오지쿠쉬#오쥐쿠쉬#ak47쿠쉬#화이트위도우#개인장#법인장#강남오피#강남유흥#토토총판#바카라사이트#추천인코드#카지노사이트#사설카지노#토토배팅">
            <meta property="og:description" content="텔레pepegarden떨팝니다채널 T.me/Pepe_Garden문의 @pepegarden오픈톡t.me/+D-_3LaM0RAg5OWMy떨,떨액 두가지만 취급합니다.오픈톡과 채널 운영중이고합리적인가격으로 운영합니다.하이코리아 에서 미미월드위니드플라워 전부 겪어왔습니다.오래된 경험으로 최상급 퀄리티로 안전하게 나눔하겠니다.#떨팝니다#떨팔아요#강남떨#용산떨#홍대떨#떨인증딜러#떨삽니다#하이코리아#하이코리아네오#떨씨앗#미미월드#위니플#위니드플라워#버드팝니다#간자팝니다#떨드랍#떨선드랍#수원떨#인천떨#제주떨#부산떨#대마효능#대마합법#대마초팝니다#대마팝니다#떨팔아요#광주떨#떨액팝니다#떨액팔아요#떨액삽니다#떨액#대마액상#대마씨앗#대마재배#대마초#동작떨#광진떨#마포떨#천안떨#대구떨#대전떨#안산떨#청주떨#제주도떨#강북떨#논현떨#클럽떨#떨판매#Thc#cbd#홍대떨#한국딥웹#위니드플라워#하이코리아네오#탑코리아#건대떨#떨사요#떨인증딜러#떨팝니다#떨사는곳#쿠쉬팝니다#태국떨#북미떨#떨씨앗배송#떨씨앗국제택배#의료용대마#블루드림#레몬헤이즈#오지쿠쉬#오쥐쿠쉬#ak47쿠쉬#화이트위도우#개인장#법인장#강남오피#강남유흥#토토총판#바카라사이트#추천인코드#카지노사이트#사설카지노#토토배팅">
            <meta property="og:article:author" content="위커">
            <meta property="twitter:card" content="summary_large_image">
            <meta property="twitter:title" content="텔레pepegarden떨팝니다 : 생명안전연구소">
            <meta property="twitter:site" content="생명안전연구소">
            <meta property="twitter:description" content="텔레pepegarden떨팝니다채널 T.me/Pepe_Garden문의 @pepegarden오픈톡t.me/+D-_3LaM0RAg5OWMy떨,떨액 두가지만 취급합니다.오픈톡과 채널 운영중이고합리적인가격으로 운영합니다.하이코리아 에서 미미월드위니드플라워 전부 겪어왔습니다.오래된 경험으로 최상급 퀄리티로 안전하게 나눔하겠니다.#떨팝니다#떨팔아요#강남떨#용산떨#홍대떨#떨인증딜러#떨삽니다#하이코리아#하이코리아네오#떨씨앗#미미월드#위니플#위니드플라워#버드팝니다#간자팝니다#떨드랍#떨선드랍#수원떨#인천떨#제주떨#부산떨#대마효능#대마합법#대마초팝니다#대마팝니다#떨팔아요#광주떨#떨액팝니다#떨액팔아요#떨액삽니다#떨액#대마액상#대마씨앗#대마재배#대마초#동작떨#광진떨#마포떨#천안떨#대구떨#대전떨#안산떨#청주떨#제주도떨#강북떨#논현떨#클럽떨#떨판매#Thc#cbd#홍대떨#한국딥웹#위니드플라워#하이코리아네오#탑코리아#건대떨#떨사요#떨인증딜러#떨팝니다#떨사는곳#쿠쉬팝니다#태국떨#북미떨#떨씨앗배송#떨씨앗국제택배#의료용대마#블루드림#레몬헤이즈#오지쿠쉬#오쥐쿠쉬#ak47쿠쉬#화이트위도우#개인장#법인장#강남오피#강남유흥#토토총판#바카라사이트#추천인코드#카지노사이트#사설카지노#토토배팅">
            <meta property="og:image" content="https://cdn.imweb.me/thumbnail/20240906/73f4554761eca.jpg">
            <meta property="og:image:width" content="1200">
            <meta property="og:image:height" content="627">
            <meta property="twitter:image" content="https://cdn.imweb.me/thumbnail/20240906/73f4554761eca.jpg">
            <link rel="canonical" href="https://생명안전.com/186/?bmode=view&amp;idx=95396760">
            <link rel="apple-touch-icon-precomposed" sizes="57x57" href="https://cdn.imweb.me/thumbnail/20200911/a0f6542381a4f.png">
            <link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://cdn.imweb.me/thumbnail/20200911/c688d5d30f65a.png">
            <link rel="apple-touch-icon-precomposed" sizes="60x60" href="https://cdn.imweb.me/thumbnail/20200911/f4e9c2bf1a1d7.png">
            <link rel="apple-touch-icon-precomposed" sizes="76x76" href="https://cdn.imweb.me/thumbnail/20200911/c5c198779369c.png">
            <link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://cdn.imweb.me/thumbnail/20200911/2e75fdfe5d47f.png">
            <link rel="apple-touch-icon-precomposed" sizes="120x120" href="https://cdn.imweb.me/thumbnail/20200911/5782c1134c745.png">
            <link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://cdn.imweb.me/thumbnail/20200911/a6bfb896a7af4.png">
            <link rel="apple-touch-icon-precomposed" sizes="152x152" href="https://cdn.imweb.me/thumbnail/20200911/48a650432c8ec.png">
            <link rel="icon" type="image/png" href="https://cdn.imweb.me/thumbnail/20200911/9e6768dc4c15c.png" sizes="16x16">
            <link rel="icon" type="image/png" href="https://cdn.imweb.me/thumbnail/20200911/ff525d598fa9d.png" sizes="32x32">
            <link rel="icon" type="image/png" href="https://cdn.imweb.me/thumbnail/20200911/5dc31d45ff61c.png" sizes="96x96">
            <link rel="icon" type="image/png" href="https://cdn.imweb.me/thumbnail/20200911/6ad48a669e5a2.png" sizes="128x128">
            <link rel="icon" type="image/png" href="https://cdn.imweb.me/thumbnail/20200911/bcbdc765cd0b1.png" sizes="196x196">
            <meta name="msapplication-TileImage" content="https://cdn.imweb.me/thumbnail/20200911/a6bfb896a7af4.png">
            <meta name="msapplication-square70x70logo" content="https://cdn.imweb.me/thumbnail/20200911/d6b279ec13715.png">
            <meta name="msapplication-square150x150logo" content="https://cdn.imweb.me/thumbnail/20200911/d7700f47b5f09.png">
            <meta name="msapplication-square310x150logo" content="https://cdn.imweb.me/thumbnail/20200911/3274d7d9f545c.png">
            <meta name="msapplication-square310x310logo" content="https://cdn.imweb.me/thumbnail/20200911/d0e0dfcad1010.png">
            <meta property="og:type" content="website">
            <meta name="viewport" content="width=device-width,viewport-fit=cover,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no"><link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/minify_css/vendor_blue_10.css?1653367465">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/minify_css/vendor_red_10.css?1653367465">
            <!--[if lte IE 9]>
            <link rel='stylesheet' type='text/css' href='https://vendor-cdn.imweb.me/css/site/bootstrap.css?1590627710'/>
            <![endif]-->
            <!--[if lte IE 9]>
            <link rel='stylesheet' type='text/css' href='https://vendor-cdn.imweb.me/css/owl.carousel1.css?1577682282'/>
            <![endif]-->
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/im_component.css?1698001225">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/site/alarm_menu.css?1678083003">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/function.css?1666824024">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/site/site.css?1729483398">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/site/site2.css?1732260490">
            <!--[if lte IE 9]>
            <link rel='stylesheet' type='text/css' href='https://vendor-cdn.imweb.me/css/site/iefix.css?1590627710'/>
            <![endif]-->
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/site/iefix2.css?1590627710">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/animate.css?1577682282">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/chosen.css?1617331870">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/chosenImage.css?1617331762">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/fonts/im-icon/style.css?1706507651">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/ii.css?1729577226">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/fonts/pretendard/web/variable/pretendardvariable.css?1669875619">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/fonts/pretendard/web/static/pretendard.css?1669875619">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/fonts/froala-emoji-tap/style.css?1669163161">
            <link rel="stylesheet" type="text/css" href="/css/custom.cm?1732780336">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/tailwind.css?1731911256">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/emoji.css?1669163161">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/font-awesome5.min.css?1669163183">
            <link rel="stylesheet" type="text/css" href="/js/oms/style.css?1733719561">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/codemirror.css?1577682282">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/froala_editor.min.css?1669163161">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/froala_style.min.css?1669163161">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/char_counter.min.css?1607673118">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/code_view.min.css?1607673118">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/colors.min.css?1607673118">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/draggable.min.css?1607673118">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/emoticons.min.css?1669163161">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/file.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/fullscreen.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/image_manager.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/image.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/line_breaker.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/quick_insert.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/table.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/froala_311/css/plugins/video.min.css?1607673119">
            <link rel="stylesheet" type="text/css" href="https://vendor-cdn.imweb.me/css/froala/custom-theme-v3.css?1691644561">
            <style>@import url("https://vendor-cdn.imweb.me/css/suite.css"); @import url("https://vendor-cdn.imweb.me/css/montserrat.css");
                    @media (min-width: 992px){
                        .doz_sys .section_first.visual_section .full_screen_show .owl-theme .item .op,
                        .doz_sys .section_first.visual_section .full_screen_show .owl-theme .item .op .header-content {
                            height: calc(100vh - 200px) !important;
                        }
                    }
            
                #w2020100507117ad06f801 .inline_global_dropdown .unfolding_mode:first-child {
                    margin-left: 0 !important;
                }
            
                #w2020100507117ad06f801 .inline_global_dropdown .unfolding_mode:last-child {
                    margin-right: 0 !important;
                }
                #w2020100507117ad06f801 .inline_global_dropdown > div.open ~ .dropdown-menu {
                    display: block;
                }
                #w2020100507117ad06f801 .inline_global_dropdown.type_icon_wrap a {
                    vertical-align: middle;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a {
                    display : inline-block;
                    width   : 100%;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a .global_text {
                    font-size: 14px;
                    color: #212121;
                    vertical-align: middle;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a .global_text.type_text {
                    vertical-align: unset;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a .global_text.type_text ~ span i.arrow {
                    margin-top: 0;
                }
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a .global_text,
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a .icon_wrap {
                    color: #212121;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a:hover .global_text,
                #w2020100507117ad06f801 .inline_global_dropdown a:hover .icon_wrap i {
                    color: #999;
                }
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a:hover .global_text,
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a:hover .icon_wrap i {
                    color: #999;
                }
                .doz_sys .hover_section_bg #w2020100507117ad06f801 .inline_global_dropdown a:hover .icon_wrap ~ .table-cell i.arrow.fixed_transform {
                    border-top-color : #999;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a .icon_wrap {
                    color: #212121;
                    vertical-align: middle;
                    display: table-cell;
                    line-height: normal;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a .icon_wrap i {
                    font-size: 16px;
                }
                #w2020100507117ad06f801 .inline_global_dropdown span ~ .global_text {
                    padding-left: 5px;
            
                }
                #w2020100507117ad06f801 .inline_global_dropdown span ~ .global_text.type_icon_text {
                    display: table-cell;
                }
              .inline-col #w2020100507117ad06f801 .inline_global_dropdown a.nav-btn-icon i.arrow {
                    border-top-color :#212121;
                    position: static;
                    margin-top: -2px;
                    margin-left: 5px;
                    vertical-align: middle;
                }
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a.nav-btn-icon i.arrow {
                    border-top-color :#212121;
                }
                #w2020100507117ad06f801 .inline_global_dropdown a.nav-btn-icon:hover i.arrow {
                    border-top-color: #999;
                }
                .scroll-to-fixed-fixed #w2020100507117ad06f801 .inline_global_dropdown a.nav-btn-icon:hover i.arrow {
                    border-top-color: #999;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w2020100507117ad06f801 .inline_global_dropdown a .global_text,
                    .doz_sys .hover_section_bg:hover #w2020100507117ad06f801 .inline_global_dropdown a .icon_wrap {
                        color : #212121 !important;
                    }
                    .doz_sys .hover_section_bg:hover #w2020100507117ad06f801 .inline_global_dropdown a .icon_wrap ~ .table-cell i.arrow {
                        border-top-color : #212121;
                    }
                }
            
                    #w202010057a9ed5ea188ec .inline_widget i.simple {
                        vertical-align: initial;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn {
                        position: relative;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .line {
                        margin-left:3.75px;
                        margin-right:3.75px;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item {
                        margin: 0 7.5px ;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item.badge_class > a .badge_wrap {
                        padding-left: 2px;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn_text {
                        position: relative;
                        background: transparent !important;
                        color:rgba(33, 33, 33, 0.7) !important;
                        display: inline-block;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn_text i {
                        color:rgba(33, 33, 33, 0.7) !important;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover .text,
                    #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover i,
                    #w202010057a9ed5ea188ec .inline_widget a.info_name:hover {
                        color              : #212121 !important;
                        -o-transition      : .3s;
                        -ms-transition     : .3s;
                        -moz-transition    : .3s;
                        -webkit-transition : .3s;
                        transition         : .3s;
                    }
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.btn_text,
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.btn_text span,
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.btn_text i {
                        color:rgba(33, 33, 33, 0.7) !important;
                    }
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover .text,
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover i,
                    .scroll-to-fixed-fixed #w202010057a9ed5ea188ec .inline_widget a.info_name:hover {
                        color: #212121 !important;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a span.text,
                    #w202010057a9ed5ea188ec .inline_widget .use_info .info_name {
                        font-size: 12px;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a span.icon_class {
                        display: inline-block;
                        vertical-align: middle;
                        font-size: 16px;
                        line-height: 1;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .use_info .info_img ~ .info_name {
                        padding-left: 0.4em;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn.custom_class .text {
                        font-size: 12px;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a.btn .text {
                        font-size: 14px;
                    }
            
                    #w202010057a9ed5ea188ec .inline_widget a span.icon_class ~ .text {
                        padding-left: 0.4em;
                        display: inline-block;
                        vertical-align: middle;
                    }
                    #w202010057a9ed5ea188ec .inline_widget a span.icon_class ~ .text.no_text {
                        padding-left: 0;
                    }
            
                    #w202010057a9ed5ea188ec .inline_widget.button_text .inline-blocked {
                        position:relative;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.button_text .inline-blocked .tooltip {
                        z-index: 99;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.button_text .inline-blocked .use_info img {
                        border-radius: 50%;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn .inline-blocked:first-child{
                        margin-left: 0 !important;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn .inline-blocked:last-child {
                        margin-right: 0 !important;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn div.tooltip-inner {
                        min-width: auto;
                        white-space: nowrap;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn a .badge {
                        position: absolute;
                        top: 0;
                        color: #ffffff;
                        font-family: Arial;
                        right: 0;
                        letter-spacing: 0;
                        padding: 0;
                        width: 15px;
                        height: 15px;
                        text-align: center;
                        line-height: 15px;
                        font-size: 10px;
                        z-index: 10;
                        cursor: pointer;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn a .badge[disabled] {
                        visibility: hidden;
                    }
            
                    #w202010057a9ed5ea188ec .inline_widget.login_btn a.btn_text .badge {
                        left: auto;
                        margin-top: 0;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn a.info_img .badge {
                        margin-top: 0;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn .nameimg a .badge {
                        left: auto;
                        right: -10px;
                    }
                    #w202010057a9ed5ea188ec .inline_widget.login_btn .badge {
                        display: none;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                        word-wrap: break-word;
                        word-break: keep-all;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip .tooltip-inner {
                        background-color:  !important;
                        color: #fff !important;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.top .tooltip-arrow {
                        border-top-color :;
                    }
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.bottom .tooltip-arrow {
                        border-bottom-color :;
                    }
            
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow {
                        border-left-color :;
                    }
            
                    #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        border-right-color :;
                    }
                    .new_fixed_header #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow,
                    .new_fixed_header #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        top: 50% !important;
                    }
                    .new_fixed_header #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left,
                    .new_fixed_header #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right {
                        top: 0 !important;
                    }
            
                    @media (max-width: 991px) {
                        #w202010057a9ed5ea188ec .inline_widget.button_text .inline-blocked .tooltip {
                            display: none !important;
                        }
                        #w202010057a9ed5ea188ec .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                            display: block !important;
            
                        }
                    }
                    @media (min-width: 767px) {
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text span,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text i,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .info_name {
                            color : rgba(33, 33, 33, 0.7) !important;
                        }
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget .line {
                            border-color : rgba(0,0,0,0.2) !important;
                        }
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover span,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .inline_widget a.btn_text:hover i,
                        .doz_sys .hover_section_bg:hover #w202010057a9ed5ea188ec .info_name:hover {
                              color : #212121 !important;
                        }
                    }
            
            
                #w20201116664ca316c9038 .btn_53S2M1CK30 span {color:#000000 !important;}#w20201116664ca316c9038 .btn_472216c85c500 span {color:#000000 !important;}
                    #w20201116664ca316c9038 .inline_widget i.simple {
                        vertical-align: initial;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn {
                        position: relative;
                    }
                    #w20201116664ca316c9038 .inline_widget .line {
                        margin-left:2.5px;
                        margin-right:2.5px;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item {
                        margin: 0 5px ;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item.badge_class > a .badge_wrap {
                        padding-left: 2px;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn_text {
                        position: relative;
                        background: transparent !important;
                        color:#000000 !important;
                        display: inline-block;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn_text i {
                        color:#000000 !important;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn_text:hover .text,
                    #w20201116664ca316c9038 .inline_widget a.btn_text:hover i,
                    #w20201116664ca316c9038 .inline_widget a.info_name:hover {
                        color              : #2c9900 !important;
                        -o-transition      : .3s;
                        -ms-transition     : .3s;
                        -moz-transition    : .3s;
                        -webkit-transition : .3s;
                        transition         : .3s;
                    }
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.btn_text,
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.btn_text span,
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.btn_text i {
                        color:#000000 !important;
                    }
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.btn_text:hover .text,
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.btn_text:hover i,
                    .scroll-to-fixed-fixed #w20201116664ca316c9038 .inline_widget a.info_name:hover {
                        color: #2c9900 !important;
                    }
                    #w20201116664ca316c9038 .inline_widget a span.text,
                    #w20201116664ca316c9038 .inline_widget .use_info .info_name {
                        font-size: 14px;
                    }
                    #w20201116664ca316c9038 .inline_widget a span.icon_class {
                        display: inline-block;
                        vertical-align: middle;
                        font-size: 25px;
                        line-height: 1;
                    }
                    #w20201116664ca316c9038 .inline_widget .use_info .info_img ~ .info_name {
                        padding-left: 0.4em;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn.custom_class .text {
                        font-size: 14px;
                    }
                    #w20201116664ca316c9038 .inline_widget a.btn .text {
                        font-size: 14px;
                    }
            
                    #w20201116664ca316c9038 .inline_widget a span.icon_class ~ .text {
                        padding-left: 0.4em;
                        display: inline-block;
                        vertical-align: middle;
                    }
                    #w20201116664ca316c9038 .inline_widget a span.icon_class ~ .text.no_text {
                        padding-left: 0;
                    }
            
                    #w20201116664ca316c9038 .inline_widget.button_text .inline-blocked {
                        position:relative;
                    }
                    #w20201116664ca316c9038 .inline_widget.button_text .inline-blocked .tooltip {
                        z-index: 99;
                    }
                    #w20201116664ca316c9038 .inline_widget.button_text .inline-blocked .use_info img {
                        border-radius: 50%;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn .inline-blocked:first-child{
                        margin-left: 0 !important;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn .inline-blocked:last-child {
                        margin-right: 0 !important;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn div.tooltip-inner {
                        min-width: auto;
                        white-space: nowrap;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn a .badge {
                        position: absolute;
                        top: 0;
                        color: #ffffff;
                        font-family: Arial;
                        right: 0;
                        letter-spacing: 0;
                        padding: 0;
                        width: 15px;
                        height: 15px;
                        text-align: center;
                        line-height: 15px;
                        font-size: 10px;
                        z-index: 10;
                        cursor: pointer;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn a .badge[disabled] {
                        visibility: hidden;
                    }
            
                    #w20201116664ca316c9038 .inline_widget.login_btn a.btn_text .badge {
                        left: auto;
                        margin-top: 0;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn a.info_img .badge {
                        margin-top: 0;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn .nameimg a .badge {
                        left: auto;
                        right: -10px;
                    }
                    #w20201116664ca316c9038 .inline_widget.login_btn .badge {
                        display: none;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                        word-wrap: break-word;
                        word-break: keep-all;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip .tooltip-inner {
                        background-color: #00b8ff !important;
                        color: #fff !important;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.top .tooltip-arrow {
                        border-top-color :#00b8ff;
                    }
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.bottom .tooltip-arrow {
                        border-bottom-color :#00b8ff;
                    }
            
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow {
                        border-left-color :#00b8ff;
                    }
            
                    #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        border-right-color :#00b8ff;
                    }
                    .new_fixed_header #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow,
                    .new_fixed_header #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        top: 50% !important;
                    }
                    .new_fixed_header #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left,
                    .new_fixed_header #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right {
                        top: 0 !important;
                    }
            
                    @media (max-width: 991px) {
                        #w20201116664ca316c9038 .inline_widget.button_text .inline-blocked .tooltip {
                            display: none !important;
                        }
                        #w20201116664ca316c9038 .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                            display: block !important;
            
                        }
                    }
                    @media (min-width: 767px) {
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text span,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text i,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .info_name {
                            color : #000000 !important;
                        }
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget .line {
                            border-color : rgba(0,0,0,0.2) !important;
                        }
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text:hover,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text:hover span,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .inline_widget a.btn_text:hover i,
                        .doz_sys .hover_section_bg:hover #w20201116664ca316c9038 .info_name:hover {
                              color : #2c9900 !important;
                        }
                    }
            
            
            
              #w20201005e715bc7616745 .search_btn a {
                display: flex;
                align-items: center;
                justify-content: center;
              }
                #w20201005e715bc7616745 .search_btn i {
                    max-width: 100%;
                    max-height: 100%;
                    display: block;
                    position: relative;
                    top:0;
                    line-height: inherit;
                }
                #w20201005e715bc7616745 .search_btn i.fa {
                    font-size: inherit;
                    width: auto;
                    height: auto;
                    vertical-align: inherit;
                    line-height: initial;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type a {
                        color : #212121		}
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type01 a{
                        color : rgba(33, 33, 33, 0.7) ;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type03 a{
                        color: #fff;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type04 a{
                        color: #fff;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type a:hover {
                          ;
                              color: #999;
                      }
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type01 a:hover{
                          color: #212121;
                      }
                    .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type03 a:hover,
                  .doz_sys .hover_section_bg:hover #w20201005e715bc7616745 .search_type.search_btn_type04 a:hover{
                          color: #fff;
                          background-color: #05b2f5;
                          border: 1px solid #05b2f5;
                      }
                }
                #w20201005e715bc7616745 .search_type a {
                    ;
                    color: #212121;
                    font-size: 12px;
                            background: #00B8FF	}
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type a {
                    ;
                    color: #212121;
                            background: #00B8FF	}
                #w20201005e715bc7616745 .search_type a:hover {
                    ;
                    color: #999;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type a:hover {
                    ;
                    color: #999;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type03 input.search_btn_form,
                #w20201005e715bc7616745 .search_type.search_btn_type04 input.search_btn_form{
                    flex: 1;
                }
                #w20201005e715bc7616745 input.search_btn_form,
                #w20201005e715bc7616745 .search_type.search_btn_type02 {
                    width: 100%;
                    height: 34px;
                    line-height: 34px;
                    padding: 0 10px;
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                    border-radius: 3px;
                    ;
                    color: #212121;
                    font-size: 14px;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type02 {
                    width: 100%;
                    border:0;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type02:before {
                    border: 1px solid #dadada;
                    border-radius: 3px;
                    content:'';
                    position: absolute;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type02 input.search_btn_form {
                    flex: 1;
                    border: 0;
                    background: transparent;
                    border-radius: 0;
                    padding: 0 10px 0 0;
                    float:left;
                    height: 34px;
                    line-height: 34px;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type01 a {
                    background: transparent !important;
                    padding: 0px 0px;
                    color: rgba(33, 33, 33, 0.7);
                    line-height: 1;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type01 a:hover {
                    color: #212121;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type01 a {
                    color:rgba(33, 33, 33, 0.7);
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type01 a:hover {
                    color: #212121;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type02 a {
                    height: 100%;
                    position : relative;
                    right: 0;
                    top: 0;
                    line-height: 34px;
                    background: transparent !important;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type02 a i {
                    height: 100%;
                    vertical-align: 0;
                 }
                #w20201005e715bc7616745 form{
                    max-width: 150px;
                    width: 150px;
                    display: flex;
                    align-items: center;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type01 form{
                    max-width: 100%;
                    width: 100%;
                    display: flex;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type03 form.clearfix,
                #w20201005e715bc7616745 .search_type.search_btn_type04 form.clearfix{
            
                }
                #w20201005e715bc7616745 .search_type.search_btn_type03 .search_btn_form {
                    float:left;
                    border-top-right-radius: 0;
                    border-bottom-right-radius: 0;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type03 a {
                    height: 34px;
                    padding: 0 10px;
                    border-top-right-radius: 3px;
                    border-bottom-right-radius: 3px;
                    border-left:1px solid #dadada;
                    color:#fff;
                    line-height: 34px;
                    float: left;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type03 a {
                    border-left:1px solid #dadada;
                    color:#fff;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type03 a:hover,
                #w20201005e715bc7616745 .search_type.search_btn_type04 a:hover {
                    color: #fff;
                    background-color: #05b2f5;
                    border: 1px solid #05b2f5;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type03 a:hover,
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type04 a:hover {
                    color: #fff;
                    background-color: #05b2f5;
                    border: 1px solid #05b2f5;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type04,
                #w20201005e715bc7616745 .search_type.search_btn_type05 {
                    height: 34px;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type04 input.search_btn_form {
                    float:left
                }
                #w20201005e715bc7616745 .search_type.search_btn_type04 a {
                    height: 34px;
                    padding: 0 10px;
                    border :1px solid #00B8FF;
                    border-radius: 3px;
                    float: right;
                    margin-left: 5px;
                    color:#fff;
                    line-height: 34px;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type04 a {
                    border :1px solid #00B8FF;
                    color:#fff;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type05 {
                    width: 150px;
                    height: 34px;
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                    border-radius: 3px;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type05 {
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type04 a i {
                    vertical-align: inherit;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type05 > div {
                    width: 100%;
                    margin-top: -1px;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type05 input.search_btn_form {
                    flex: 1;
                    padding: 0;
                    background: transparent;
                    border :0;
                    border-radius: 0;
                    width: 100%;
                    padding-left:10px;
                    vertical-align: middle;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type05 a {
                    line-height: 34px;
                    background: transparent !important;
                    text-align: left;
                    padding-left:10px;
                    vertical-align: middle;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type05 i {
                    vertical-align: initial;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type06 .search_btn_form {
                    border: 0;
                    border-radius: 0;
                    border-bottom:1px solid #dadada;
                    background: transparent;
                    padding-left: 0;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type06 .search_btn_form {
                    border-bottom:1px solid #dadada;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type06  .search_btn_form:focus {
                    border-color: ;
                }
                #w20201005e715bc7616745 .search_type.search_btn_type06 a {
                    background: transparent;
                    position: absolute;
                    right: 0;
                    line-height: 32px;
                    top: 50%;
                transform: translateY(-50%);
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 input.search_btn_form,
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type02 {
                    ;
                    background: #fff;
                    ;
                    color: #212121;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 input.search_btn_form {
                    border:1px solid #dadada;
                }
                .scroll-to-fixed-fixed #w20201005e715bc7616745 .search_type.search_btn_type02:before {
                    border:1px solid #dadada;
                }
                    #w20201005e715bc7616745 .search_btn input::-webkit-input-placeholder {
                    color:  !important;
                }
                #w20201005e715bc7616745 .search_btn input::-moz-placeholder {
                    color:  !important;
                }
                #w20201005e715bc7616745 .search_btn input:-ms-input-placeholder{
                    color:  !important;
                }
                #w20201005e715bc7616745 .search_btn input:-moz-placeholder {
                    color:  !important;
                }
            
                #w2020100593e1d0b9309b8 .vertical_line .full-width {
                    padding: 0 5px;
                }
                #w2020100593e1d0b9309b8 .vertical_line .real_line {
                    display: inline-block;
                    border-width: 0 1px 0 0;
                    border-style: solid;
                    border-color: rgba(0, 0, 0, 0.1);
                    height: 25px;
                }
                .scroll-to-fixed-fixed #w2020100593e1d0b9309b8 hr {
                    border-color: rgba(0, 0, 0, 0.1) !important;
                }
                .scroll-to-fixed-fixed #w2020100593e1d0b9309b8 .vertical_line .real_line {
                    border-color: rgba(0, 0, 0, 0.1);
                }
            
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w2020100593e1d0b9309b8 hr {
                        border-color: rgba(0, 0, 0, 0.1) !important;
                    }
                    .doz_sys .hover_section_bg:hover #w2020100593e1d0b9309b8 .real_line{
                        border-color: rgba(0, 0, 0, 0.1) !important;
                    }
                }
            
                #w20201005c70a70dc73d1d .inline_widget.icon.no_bg:hover i {
                    background: none !important;
                    border: 0 !important;
                }
                #w20201005c70a70dc73d1d .inline_widget.icon:hover i {
                    background: #f2f2f2 !important;
                    color: #137e28 !important;
                    border-color: #dbdbdb !important;
                }
                .scroll-to-fixed-fixed #w20201005c70a70dc73d1d .inline_widget.icon i {
                    color: #16d426 !important;
                    background: #e7e7e7 !important;
                    border-color: #ccc !important;
                }
                .scroll-to-fixed-fixed #w20201005c70a70dc73d1d .inline_widget.icon.no_bg i,
                .scroll-to-fixed-fixed #w20201005c70a70dc73d1d .inline_widget.icon.no_bg:hover i {
                    background: none !important;
                    border: 0 !important;
                }
                .scroll-to-fixed-fixed #w20201005c70a70dc73d1d .inline_widget.icon:hover i {
                    background: #f2f2f2 !important;
                    color: #137e28 !important;
                    border-color: #137e28 !important;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w20201005c70a70dc73d1d .icon i{
                        color: #16d426 !important;
                    }
                }
            
                            #s202010059784a742cc092 .inline-inside {
                                max-width: 1280px;
                                margin: 0 auto;
                                padding-left:30px;
                                padding-right:30px;
                            }
                            .admin.new_header_mode {
                                overflow-x: auto;
                            }
                            .new_header_mode #edit_wrap {
                                min-width: 1280px;
                            }
                            #s202010059784a742cc092 .section_bg {
                                ;
                                background-position:;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            .new_header_overlay #s202010059784a742cc092 .section_bg {
                                background-image:none;;
                            }
                            .new_header_overlay .new_fixed_header #s202010059784a742cc092 .section_bg {
                                ;
                            }
                            .scroll-to-fixed-fixed#s202010059784a742cc092 .section_bg {
                                ;
                                background-position: ;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            #s202010059784a742cc092 .inline-col-group {
                                padding-top:10px;
                                padding-bottom:10px;
                                height : 64px;
                            }
                            #s202010059784a742cc092 .inline-col-group > .inline-col {
                                padding-left: 15px;
                            }
                            #s202010059784a742cc092 .inline-col-group > .inline-col:first-child {
                                padding-left:  0 !important;
                            }
                            #s202010059784a742cc092 .inline-row > .inline-col {
                                padding-left: 15px;
                            }
                            #s202010059784a742cc092 .inline-row > .inline-col:first-child {
                                padding-left: 0 !important;
                            }
                            #s202010059784a742cc092.extend .inline-inside {
                                max-width: 100% !important;
                            }
                            #s202010059784a742cc092 .inline_widget.image .text,
                            #s202010059784a742cc092 .inline_widget.logo a,
                            #s202010059784a742cc092 .inline_widget.icon,
                            #s202010059784a742cc092 .inline_widget.login_btn a,
                            #s202010059784a742cc092 .viewport-nav > li > a,
                            #s202010059784a742cc092 .inline-col .inline_global_dropdown a,
                            #s202010059784a742cc092 .inline_widget.widget_text_wrap {
                                color: ;
                            }
            
                            .new_header_overlay #s202010059784a742cc092.scroll-to-fixed-fixed .viewport-nav > li > a {
                                color: ;
                            }
                            .new_header_overlay #s202010059784a742cc092.scroll-to-fixed-fixed .section_bg_color {
                                background-color: #ffffff !important;
                            }
                            #s202010059784a742cc092 .inline_widget.padding > div {
                                ;
                            }
                            #s202010059784a742cc092 .inline-col .inline_global_dropdown a i.arrow {
                                border-top-color: ;
                            }
                            #s202010059784a742cc092 {
                              border-width: 0 0 0px;
                              border-color: #e7e7e7;
                              border-style: solid;
                            }
                            .scroll-to-fixed-fixed#s202010059784a742cc092 {
                              border-color: #e7e7e7;
                              -webkit-transform: translate3d(0, 0, 0);
                                transform : translate3d(0, 0, 0);
                            } 
                            #s202010059784a742cc092 .inline-col-group,
                             #s202010059784a742cc092 .inline-col-group .inline-col {
                                vertical-align: middle ;
                            }
                            #inline_header_mobile #s202010059784a742cc092 .inline-inside {
                                padding-left:0px !important;
                                padding-right:0px !important;
                            }
                            #s202010059784a742cc092 .btn:not(.btn-primary):not(.btn_custom) {
                                ;
                                background-color: #ffffff;
                                ;
                                color:;
                                ;
                            }
                            #s202010059784a742cc092 .btn:not(.btn-primary):not(.btn_custom):hover {
                                border-color:;
                            }
                            #s202010059784a742cc092 .btn-primary span {
                                color:#00dce0;
                            }
                            @media (min-width: 991px) {
                                .doz_sys #s202010059784a742cc092 .btn-primary:hover span, #s202010059784a742cc092 .widget_text_wrap .btn:hover span {
                                    color:#ffffff;
                                }
                            }
                            @media all and (min-width: 768px) {
                                #s202010059784a742cc092.hover_section_bg:hover .section_bg_color {
                                    background-color:  !important;
                                }
                                #s202010059784a742cc092.hover_section_bg:hover .section_bg {
                                    ;
                                }
                                #s202010059784a742cc092.hover_section_bg:hover img.normal_logo {
                                    opacity: 0;
                                }
                                #s202010059784a742cc092.hover_section_bg:hover img.scroll_logo {
                                    opacity: 1;
                                }
                            }
                            @media all and (max-width: 767px) {
                                .inline_header_design {
                                    overflow-x: hidden;
                                }
                            }
            
                    .doz_sys #logo_w20201005a5f513e27edff.logo .logo_title a {
                        font-family: '';
                        font-size: 24px;
                    letter-spacing: 0px;
                    font-weight: bold;
                    font-style: normal;
                    ;
                    color: #212121;
                    line-height: inherit;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #logo_w20201005a5f513e27edff.logo .logo_title a {
                        color : #212121		}
                }
                .scroll-to-fixed-fixed #logo_w20201005a5f513e27edff .logo_title a {
                     !important;
                    color: #212121 !important;
                }
              #logo_w20201005a5f513e27edff {
                display: flex;
                align-items: center;
              }
                #logo_w20201005a5f513e27edff > div {
                    display: block;
                }
                    #logo_w20201005a5f513e27edff .img_box ~ .logo_title {
                    padding-left: 0px;
                }
                    /*@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none) {*/
                /*	#logo_*//* .normal_logo,*/
                /*	#logo_*//* .scroll_logo {*/
                /*		width: auto;*/
                /*	}*/
                /*}*/
            
                            #w20201005d27fe010e40db .viewport-nav > li:last-child > a {
                            }
                    @media (min-width: 767px) {
                        .doz_sys .hover_section_bg:hover #w20201005d27fe010e40db .viewport-nav > li.dropdown > a {
                            color : #212121			}
                        .doz_sys .hover_section_bg:hover #w20201005d27fe010e40db .viewport-nav > li.dropdown > a:hover {
                            color : rgba(33, 33, 33, 0.5)		 	}
                    }
            
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active,
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active{
                                                 font-weight: bold;
                                                 border : 0;
                                                 border-style : solid;
                                             ;
                                                 color: #ff2f2f;
            
                                             color: #ff2f2f;
                                             }
            
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active,
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active {
                                                                    ;
                                                                        color: #ff2f2f;
                                                                    color: #ff2f2f;														}
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active span,
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active span {
                                                 border: 0;
                                                                                  border-style : solid;
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active span,
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active span {
                                                                        border:0;
                                                                                                                                border-style : solid;
                                                                    }
                    #w20201005d27fe010e40db .viewport-nav > li > a {
                                                 padding: 15px;
                                             }
            
                    #w20201005d27fe010e40db .viewport-nav>.dropdown.use_sub_name:hover>a>.plain_name:before {
                       display: inline-flex;
                   }
                    #w20201005d27fe010e40db .viewport-nav > .active > a,
                    #w20201005d27fe010e40db .viewport-nav > .active > a:hover,
                    #w20201005d27fe010e40db .viewport-nav > .active > a:focus {
                                             ;
                                                 color: ;
                                                 background-color: transparent;
                                             }
                    #w20201005d27fe010e40db .viewport-nav > .disabled > a,
                    #w20201005d27fe010e40db .viewport-nav > .disabled > a:hover,
                    #w20201005d27fe010e40db .viewport-nav > .disabled > a:focus {
                                                 color: #ccc;
                                                 background-color: transparent;
                                             }
            
                    #w20201005d27fe010e40db .dropdown-menu a {
                                                 font-weight: inherit;
                                                 font-style: normal;
                                                                              }
                    #w20201005d27fe010e40db .viewport-nav > li > a.dropdown-more {
                                                 cursor: pointer;
                                             }
            
                    #w20201005d27fe010e40db {
                    ;
                        background: ;
                        font-family: montserrat,SUITE, sans-serif;
                        height:70px;
                        min-height: auto;
                        display: table-cell;
                        vertical-align: middle;
                    }
            
                    #w20201005d27fe010e40db .viewport-nav {
                                                 height:70px;
                                             }
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a,
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > a {
                                             ;
                                                 color: #212121;
                                                 font-size: 18px;
                                                 letter-spacing: 1px;
                                                 padding: 0 15px;
                                                 font-weight: bold;
                                                 font-style: normal;
                                                                                  height:70px;
                                                 display: table-cell;
                                                 vertical-align: middle;
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a,
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > a {
                                                                        color: #212121;
                                                                    }
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown.use_sub_name:hover>a>.plain_name:before {
                                                 color: rgba(33, 33, 33, 0.5);
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown.use_sub_name:hover>a>.plain_name:before {
                                                                        color: rgba(33, 33, 33, 0.5);
                                                                    }
                    /*	#doz_header #*//* .viewport-nav > li:first-child > a{*/
                    /*											 padding-left: *//*px !important;*/
                    /*										 }*/
                    /*	#doz_header #*//* .viewport-nav > li:last-child > a {*/
                    /*											 padding-right: *//*px !important;*/
                    /*										 }*/
                    #doz_header #w20201005d27fe010e40db .sub_mega_drop .viewport-nav > li {
                                                             float: left;
                                                             display: table;
                                                         }
                    /*	#doz_header #*//* .sub_mega_drop .viewport-nav > li a{*/
                    /*											 text-align: center;*/
                    /*										 }*/
                    #w20201005d27fe010e40db .dropdown-menu {
            
                                             }
                    #w20201005d27fe010e40db .dropdown-menu {
                                                 margin-top: 0;
                                             left: 15px;
                                             }
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a:hover,
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > a:hover {
                                             color : #212121;;
                                                 color: rgba(33, 33, 33, 0.5);
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a:hover,
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > a:hover,
                                                                    .scroll-to-fixed-fixed #w20201005d27fe010e40db {
                    color : #212121;;
                        color: rgba(33, 33, 33, 0.5);
                    }
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active:before,
                    #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active:before{
                                                                              }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > .notranslate a.active:before,
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .viewport-nav > li.dropdown > a.active:before{
                                                                                                                            }
                    #w20201005d27fe010e40db li.dropdown > ul.dropdown-menu {
                                                 visibility: hidden;
                                                 display: block;
                                                 opacity: 0;
                                                 -o-transition: .3s;
                                                 -ms-transition: .3s;
                                                 -moz-transition: .3s;
                                                 -webkit-transition: .3s;
                                                 transition: .3s;
                                             }
                    #w20201005d27fe010e40db li.dropdown:hover > ul.dropdown-menu {
                                                 visibility: visible;
                                                 opacity: 1;
                                                 display: block;
                                             }
                    #w20201005d27fe010e40db li.dropdown > ul.dropdown-menu.init-hover-guard::after {
                                                content: "";
                                                position: absolute;
                                                inset-inline: 0;
                                                inset-block-start: 100%;
                                                display: block;
                                                height: 150px;
                                                background-color: transparent;
                                             }
                    #inline_header_normal *[data-type=col-group]:has(*[data-widget-type=inline_menu]).overflow-last-dropdown #w20201005d27fe010e40db .viewport-nav.desktop li.dropdown:last-of-type > ul.dropdown-menu {
                                                  right: 0;
                                                  left: auto;
                    }
                    #w20201005d27fe010e40db li.dropdown.pulldown-hide > ul.dropdown-menu,
                    #w20201005d27fe010e40db li.dropdown.pulldown-hide:hover > ul.dropdown-menu {
                                                 display: none;
                                             }
                    #w20201005d27fe010e40db li.dropdown-icon:focus > ul.dropdown-menu {
                                                 visibility: visible;
                                                 opacity: 1;
                                                 display: block;
                                             }
                    #w20201005d27fe010e40db .dropdown-menu {
                                             ;
                                                 background: #fff;
                                                 font-size: 13px;
                                                 border-radius: 0px;
                                                 -webkit-box-shadow: none;
                                                 box-shadow: none;
                                                 padding: 0;
                                                 border: 0px solid  #e5e5e5;
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu {
                                                                    ;
                                                                        background: #fff;
                                                                        border: 0px solid  #e5e5e5;
                                                                    }
                    #w20201005d27fe010e40db .dropdown-menu > li > a {
                                                 font-size: 13px;
                                             ;
                                                 color: #212121;
                                                 padding: 10px 20px;
                                                 letter-spacing: 0px;
                                                 border-top: 0px solid  #e5e5e5;
                                             }
                    #w20201005d27fe010e40db .dropdown-menu > li.dropdown-submenu.sub-active > a {
                                                padding-right: 30px;
                    }
                    #w20201005d27fe010e40db .dropdown-menu > li > a:focus {
                                                 outline: none;
                                             }
                    #w20201005d27fe010e40db .dropdown-menu > li.use_sub_name:hover>a>.plain_name:before {
                                                 color: #fff !important;
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu > li > a {
                                                                    ;
                                                                        color: #212121;
                                                                        border-top: 0px solid  #e5e5e5;
                                                                    }
            
                    #w20201005d27fe010e40db .dropdown-menu > li:first-child > a {
                                                 border-top: 0;
                                             }
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu > li.use_sub_name:hover>a>.plain_name:before {
                                                                        color: #fff !important;
                                                                    }
                    #w20201005d27fe010e40db .dropdown-menu > li > a:hover,
                    #w20201005d27fe010e40db .dropdown-menu > li > a:active,
                    #w20201005d27fe010e40db .dropdown-menu > li > a:focus {
                                             ;
                                                 color: #fff !important;
                                             background-color : #212121;;
                                                 background-color: rgba(33, 33, 33, 0.89) !important;
                                                 font-size: 13px;
                                             }
            
                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu > li > a:hover,
                                                                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu > li > a:active,
                                                                                                                    .scroll-to-fixed-fixed #w20201005d27fe010e40db .dropdown-menu > li > a:focus {
                                                                                                                                                                    ;
                                                                                                                                                                        color: #fff !important;
                                                                                                                                                                    background-color : #212121;;
                                                                                                                                                                        background-color: rgba(33, 33, 33, 0.89) !important;
                                                                                                                                                                    }
            
                    #w20201005d27fe010e40db .dropdown-menu > li:last-child > a,
                    #w20201005d27fe010e40db .dropdown-menu > li:last-child > a:hover {
                                                 border-bottom-left-radius: 0px;
                                                 border-bottom-right-radius: 0px;
                                             }
                    #w20201005d27fe010e40db .dropdown-menu > li:first-child > a,
                    #w20201005d27fe010e40db .dropdown-menu > li:first-child > a:hover {
                                                 border-top-left-radius: 0px;
                                                 border-top-right-radius: 0px;
                                             }
            
                    #w20201005d27fe010e40db .nav .open > a,
                    #w20201005d27fe010e40db  .nav .open > a:hover,
                    #w20201005d27fe010e40db  .nav .open > a:focus {
                                                  background: transparent;
                                                  border-color : transparent;
                                              }
                    .dropdown-menu.preview_drop_down > li > a.hover {
                    ;
                        color: #fff !important;
                    background-color : #212121;;
                        background-color: rgba(33, 33, 33, 0.89) !important;
                    }
            
            
                            #s20201005a79c3af52564c .inline-inside {
                                max-width: 1280px;
                                margin: 0 auto;
                                padding-left:15px;
                                padding-right:15px;
                            }
                            .admin.new_header_mode {
                                overflow-x: auto;
                            }
                            .new_header_mode #edit_wrap {
                                min-width: 1280px;
                            }
                            #s20201005a79c3af52564c .section_bg {
                                ;
                                background-position:;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            .new_header_overlay #s20201005a79c3af52564c .section_bg {
                                background-image:none;;
                            }
                            .new_header_overlay .new_fixed_header #s20201005a79c3af52564c .section_bg {
                                ;
                            }
                            .scroll-to-fixed-fixed#s20201005a79c3af52564c .section_bg {
                                ;
                                background-position: ;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            #s20201005a79c3af52564c .inline-col-group {
                                padding-top:0px;
                                padding-bottom:0px;
                                height : 115px;
                            }
                            #s20201005a79c3af52564c .inline-col-group > .inline-col {
                                padding-left: 20px;
                            }
                            #s20201005a79c3af52564c .inline-col-group > .inline-col:first-child {
                                padding-left:  0 !important;
                            }
                            #s20201005a79c3af52564c .inline-row > .inline-col {
                                padding-left: 20px;
                            }
                            #s20201005a79c3af52564c .inline-row > .inline-col:first-child {
                                padding-left: 0 !important;
                            }
                            #s20201005a79c3af52564c.extend .inline-inside {
                                max-width: 100% !important;
                            }
                            #s20201005a79c3af52564c .inline_widget.image .text,
                            #s20201005a79c3af52564c .inline_widget.logo a,
                            #s20201005a79c3af52564c .inline_widget.icon,
                            #s20201005a79c3af52564c .inline_widget.login_btn a,
                            #s20201005a79c3af52564c .viewport-nav > li > a,
                            #s20201005a79c3af52564c .inline-col .inline_global_dropdown a,
                            #s20201005a79c3af52564c .inline_widget.widget_text_wrap {
                                color: ;
                            }
            
                            .new_header_overlay #s20201005a79c3af52564c.scroll-to-fixed-fixed .viewport-nav > li > a {
                                color: ;
                            }
                            .new_header_overlay #s20201005a79c3af52564c.scroll-to-fixed-fixed .section_bg_color {
                                background-color: #fff !important;
                            }
                            #s20201005a79c3af52564c .inline_widget.padding > div {
                                ;
                            }
                            #s20201005a79c3af52564c .inline-col .inline_global_dropdown a i.arrow {
                                border-top-color: ;
                            }
                            #s20201005a79c3af52564c {
                              border-width: 0 0 0px;
                              border-color: #e7e7e7;
                              border-style: solid;
                            }
                            .scroll-to-fixed-fixed#s20201005a79c3af52564c {
                              border-color: #e7e7e7;
                              -webkit-transform: translate3d(0, 0, 0);
                                transform : translate3d(0, 0, 0);
                            } 
                            #s20201005a79c3af52564c .inline-col-group,
                             #s20201005a79c3af52564c .inline-col-group .inline-col {
                                vertical-align: middle ;
                            }
                            #inline_header_mobile #s20201005a79c3af52564c .inline-inside {
                                padding-left:15px !important;
                                padding-right:15px !important;
                            }
                            #s20201005a79c3af52564c .btn:not(.btn-primary):not(.btn_custom) {
                                ;
                                background-color: #fff;
                                ;
                                color:;
                                ;
                            }
                            #s20201005a79c3af52564c .btn:not(.btn-primary):not(.btn_custom):hover {
                                border-color:;
                            }
                            #s20201005a79c3af52564c .btn-primary span {
                                color:#00dce0;
                            }
                            @media (min-width: 991px) {
                                .doz_sys #s20201005a79c3af52564c .btn-primary:hover span, #s20201005a79c3af52564c .widget_text_wrap .btn:hover span {
                                    color:#ffffff;
                                }
                            }
                            @media all and (min-width: 768px) {
                                #s20201005a79c3af52564c.hover_section_bg:hover .section_bg_color {
                                    background-color:  !important;
                                }
                                #s20201005a79c3af52564c.hover_section_bg:hover .section_bg {
                                    ;
                                }
                                #s20201005a79c3af52564c.hover_section_bg:hover img.normal_logo {
                                    opacity: 0;
                                }
                                #s20201005a79c3af52564c.hover_section_bg:hover img.scroll_logo {
                                    opacity: 1;
                                }
                            }
                            @media all and (max-width: 767px) {
                                .inline_header_design {
                                    overflow-x: hidden;
                                }
                            }
            
                #padding_w202010073b859bbc57d86 {
                    height: 12px;
                    width: 30px;
                }
                .doz_sys .inline_widget.padding {
                    margin: 0;
                }
                .inline_header_design .inline_widget.padding {
                    border-width : 1px;
                    border-style: dashed;
                    border-color: rgba(0,0,0,0.1);
                }
                .inline_header_design .new_header_overlay .inline_widget.padding {
                    border-color: #aaa;
                }
            
                            #s2020100700e8f1f61f7bc .inline-inside {
                                max-width: 1280px;
                                margin: 0 auto;
                                padding-left:15px;
                                padding-right:15px;
                            }
                            .admin.new_header_mode {
                                overflow-x: auto;
                            }
                            .new_header_mode #edit_wrap {
                                min-width: 1280px;
                            }
                            #s2020100700e8f1f61f7bc .section_bg {
                                ;
                                background-position:;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            .new_header_overlay #s2020100700e8f1f61f7bc .section_bg {
                                background-image:none;;
                            }
                            .new_header_overlay .new_fixed_header #s2020100700e8f1f61f7bc .section_bg {
                                ;
                            }
                            .scroll-to-fixed-fixed#s2020100700e8f1f61f7bc .section_bg {
                                ;
                                background-position: ;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            #s2020100700e8f1f61f7bc .inline-col-group {
                                padding-top:0px;
                                padding-bottom:0px;
                                height : 21px;
                            }
                            #s2020100700e8f1f61f7bc .inline-col-group > .inline-col {
                                padding-left: 10px;
                            }
                            #s2020100700e8f1f61f7bc .inline-col-group > .inline-col:first-child {
                                padding-left:  0 !important;
                            }
                            #s2020100700e8f1f61f7bc .inline-row > .inline-col {
                                padding-left: 10px;
                            }
                            #s2020100700e8f1f61f7bc .inline-row > .inline-col:first-child {
                                padding-left: 0 !important;
                            }
                            #s2020100700e8f1f61f7bc.extend .inline-inside {
                                max-width: 100% !important;
                            }
                            #s2020100700e8f1f61f7bc .inline_widget.image .text,
                            #s2020100700e8f1f61f7bc .inline_widget.logo a,
                            #s2020100700e8f1f61f7bc .inline_widget.icon,
                            #s2020100700e8f1f61f7bc .inline_widget.login_btn a,
                            #s2020100700e8f1f61f7bc .viewport-nav > li > a,
                            #s2020100700e8f1f61f7bc .inline-col .inline_global_dropdown a,
                            #s2020100700e8f1f61f7bc .inline_widget.widget_text_wrap {
                                color: ;
                            }
            
                            .new_header_overlay #s2020100700e8f1f61f7bc.scroll-to-fixed-fixed .viewport-nav > li > a {
                                color: ;
                            }
                            .new_header_overlay #s2020100700e8f1f61f7bc.scroll-to-fixed-fixed .section_bg_color {
                                background-color: #fff !important;
                            }
                            #s2020100700e8f1f61f7bc .inline_widget.padding > div {
                                ;
                            }
                            #s2020100700e8f1f61f7bc .inline-col .inline_global_dropdown a i.arrow {
                                border-top-color: ;
                            }
                            #s2020100700e8f1f61f7bc {
                              border-width: 0 0 0px;
                              border-color: #ccc;
                              border-style: solid;
                            }
                            .scroll-to-fixed-fixed#s2020100700e8f1f61f7bc {
                              border-color: #ccc;
                              -webkit-transform: translate3d(0, 0, 0);
                                transform : translate3d(0, 0, 0);
                            } 
                            #s2020100700e8f1f61f7bc .inline-col-group,
                             #s2020100700e8f1f61f7bc .inline-col-group .inline-col {
                                vertical-align: middle ;
                            }
                            #inline_header_mobile #s2020100700e8f1f61f7bc .inline-inside {
                                padding-left:15px !important;
                                padding-right:15px !important;
                            }
                            #s2020100700e8f1f61f7bc .btn:not(.btn-primary):not(.btn_custom) {
                                ;
                                background-color: #fff;
                                ;
                                color:;
                                ;
                            }
                            #s2020100700e8f1f61f7bc .btn:not(.btn-primary):not(.btn_custom):hover {
                                border-color:;
                            }
                            #s2020100700e8f1f61f7bc .btn-primary span {
                                color:#00dce0;
                            }
                            @media (min-width: 991px) {
                                .doz_sys #s2020100700e8f1f61f7bc .btn-primary:hover span, #s2020100700e8f1f61f7bc .widget_text_wrap .btn:hover span {
                                    color:#ffffff;
                                }
                            }
                            @media all and (min-width: 768px) {
                                #s2020100700e8f1f61f7bc.hover_section_bg:hover .section_bg_color {
                                    background-color:  !important;
                                }
                                #s2020100700e8f1f61f7bc.hover_section_bg:hover .section_bg {
                                    ;
                                }
                                #s2020100700e8f1f61f7bc.hover_section_bg:hover img.normal_logo {
                                    opacity: 0;
                                }
                                #s2020100700e8f1f61f7bc.hover_section_bg:hover img.scroll_logo {
                                    opacity: 1;
                                }
                            }
                            @media all and (max-width: 767px) {
                                .inline_header_design {
                                    overflow-x: hidden;
                                }
                            }
            
                .fixed-menu-on .scroll_position {
                    top: -179px;
                }
            
                    @media (max-width: 991px){
                        .doz_sys .section_first.visual_section .full_screen_show .owl-theme .item .op,
                        .doz_sys .section_first.visual_section .full_screen_show .owl-theme .item .op .header-content {
                            height: calc(100vh - 95px) !important;
                        }
                    }
            
                #w202010055157a37ed6a07 .icon_type_menu:not(.st02) {
                    line-height: 1;
                }
                #w202010055157a37ed6a07 .icon_type_menu .badge {
                    width: 15px;
                    font-size: 10px;
                    display: inline-block;
                    position: absolute;
                    color: #ffffff;
                    font-family: Arial;
                    left: auto;
                    right: -8px;;
                    letter-spacing: 0;
                    padding: 0;
                    height: 15px;
                    text-align: center;
                    line-height: 15px;
                    z-index: 10;
                    top: 35%;
                    margin-top: -10px;
                }
                #w202010055157a37ed6a07 .icon_type_menu a {
                    font-size :18px;
                    color: #212121;
                    background: rgba(255, 255, 255, 0);
                    border: 0px solid #ccc;
                    border-radius: 0px;
                    text-align: center;
                    padding-left:10px;
                    padding-right:10px;
                    padding-top:15px;
                    padding-bottom:15px
                }
                #w202010055157a37ed6a07 .icon_type_menu a .icon_code {
                    vertical-align: top;
                }
                .scroll-to-fixed-fixed #w202010055157a37ed6a07 .icon_type_menu a {
                    color: #212121;
                    background: rgba(255, 255, 255, 0);
                    border: 0px solid #ccc;
                }
            
                #w202010055157a37ed6a07 .icon_type_menu a span.text {
                    display: none;
                }
            
            
                #w202010055157a37ed6a07 .icon_type_menu a .fa {
                    width:auto;
                    height:auto;
                }
                #w202010055157a37ed6a07 .icon_type_menu.st01 a {
                    border-radius: 50%;
                    padding: 5px;
                }
                #w202010055157a37ed6a07 .icon_type_menu.st02 a {
                    color: #212121;
                    padding: 15px 10px;
                }
                .scroll-to-fixed-fixed #w202010055157a37ed6a07 .icon_type_menu.st02 a {
                    color: #212121;
            
                }
            
            
                #w202010055157a37ed6a07 .icon_type_menu.st02 a:before{
                    content:"";
                    display:inline-block;
                    vertical-align:middle;
                    height:100%;
                }
                #w202010055157a37ed6a07 .icon_type_menu.st02 a .icon_code {
                    display: none;
                }
                #w202010055157a37ed6a07 .icon_type_menu.st02 .badge {
                    right: -10px;
                }
                #w202010055157a37ed6a07 .icon_type_menu.st02 a span.text {
                    max-width:100%;
                    max-height:100%;
                    display:inline-block;
                }
                @media (min-width: 991px) {
                    #w202010055157a37ed6a07 .icon_type_menu a:hover {
                        color:rgba(0, 0, 0, 0.5);
                        background: rgba(0, 0, 0, 0);
                        border-color: rgba(0, 0, 0, 0);
                    }
                    .scroll-to-fixed-fixed #w202010055157a37ed6a07 .icon_type_menu a:hover {
                        color:rgba(0, 0, 0, 0.5);
                        background: rgba(0, 0, 0, 0);
                        border-color: rgba(0, 0, 0, 0);
                    }
                    #w202010055157a37ed6a07 .icon_type_menu.st02 a:hover {
                        color: rgba(0, 0, 0, 0.5);
                    }
                    .scroll-to-fixed-fixed #w202010055157a37ed6a07 .icon_type_menu.st02 a:hover {
                        color: rgba(0, 0, 0, 0.5);
                    }
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w202010055157a37ed6a07 .icon_type_menu a {
                        color : #212121!important;
                    }
                    .doz_sys .hover_section_bg:hover #w202010055157a37ed6a07 .icon_type_menu a:hover {
                          color : rgba(0, 0, 0, 0.5)!important;
                      }
                }
            
            
                    .doz_sys #logo_w20201005ffaa369844eed.logo .logo_title a {
                        font-family: montserrat;
                        font-size: 20px;
                    letter-spacing: 0px;
                    font-weight: bold;
                    font-style: normal;
                    ;
                    color: #212121;
                    line-height: inherit;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #logo_w20201005ffaa369844eed.logo .logo_title a {
                        color : #212121		}
                }
                .scroll-to-fixed-fixed #logo_w20201005ffaa369844eed .logo_title a {
                     !important;
                    color: #212121 !important;
                }
              #logo_w20201005ffaa369844eed {
                display: flex;
                align-items: center;
              }
                #logo_w20201005ffaa369844eed > div {
                    display: block;
                }
                    #logo_w20201005ffaa369844eed .img_box ~ .logo_title {
                    padding-left: 10px;
                }
                    /*@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none) {*/
                /*	#logo_*//* .normal_logo,*/
                /*	#logo_*//* .scroll_logo {*/
                /*		width: auto;*/
                /*	}*/
                /*}*/
            
                    #w20201005ded3aae02af59 .inline_widget i.simple {
                        vertical-align: initial;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn {
                        position: relative;
                    }
                    #w20201005ded3aae02af59 .inline_widget .line {
                        margin-left:2.5px;
                        margin-right:2.5px;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item {
                        margin: 0 5px ;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item.badge_class > a .badge_wrap {
                        padding-left: 2px;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn_text {
                        position: relative;
                        background: transparent !important;
                        color:#212121 !important;
                        display: inline-block;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn_text i {
                        color:#212121 !important;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn_text:hover .text,
                    #w20201005ded3aae02af59 .inline_widget a.btn_text:hover i,
                    #w20201005ded3aae02af59 .inline_widget a.info_name:hover {
                        color              : #ccc !important;
                        -o-transition      : .3s;
                        -ms-transition     : .3s;
                        -moz-transition    : .3s;
                        -webkit-transition : .3s;
                        transition         : .3s;
                    }
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.btn_text,
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.btn_text span,
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.btn_text i {
                        color:#212121 !important;
                    }
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.btn_text:hover .text,
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.btn_text:hover i,
                    .scroll-to-fixed-fixed #w20201005ded3aae02af59 .inline_widget a.info_name:hover {
                        color: #ccc !important;
                    }
                    #w20201005ded3aae02af59 .inline_widget a span.text,
                    #w20201005ded3aae02af59 .inline_widget .use_info .info_name {
                        font-size: 12px;
                    }
                    #w20201005ded3aae02af59 .inline_widget a span.icon_class {
                        display: inline-block;
                        vertical-align: middle;
                        font-size: 20px;
                        line-height: 1;
                    }
                    #w20201005ded3aae02af59 .inline_widget .use_info .info_img ~ .info_name {
                        padding-left: 0.4em;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn.custom_class .text {
                        font-size: 12px;
                    }
                    #w20201005ded3aae02af59 .inline_widget a.btn .text {
                        font-size: 14px;
                    }
            
                    #w20201005ded3aae02af59 .inline_widget a span.icon_class ~ .text {
                        padding-left: 0.4em;
                        display: inline-block;
                        vertical-align: middle;
                    }
                    #w20201005ded3aae02af59 .inline_widget a span.icon_class ~ .text.no_text {
                        padding-left: 0;
                    }
            
                    #w20201005ded3aae02af59 .inline_widget.button_text .inline-blocked {
                        position:relative;
                    }
                    #w20201005ded3aae02af59 .inline_widget.button_text .inline-blocked .tooltip {
                        z-index: 99;
                    }
                    #w20201005ded3aae02af59 .inline_widget.button_text .inline-blocked .use_info img {
                        border-radius: 50%;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn .inline-blocked:first-child{
                        margin-left: 0 !important;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn .inline-blocked:last-child {
                        margin-right: 0 !important;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn div.tooltip-inner {
                        min-width: auto;
                        white-space: nowrap;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn a .badge {
                        position: absolute;
                        top: 0;
                        color: #ffffff;
                        font-family: Arial;
                        right: 0;
                        letter-spacing: 0;
                        padding: 0;
                        width: 15px;
                        height: 15px;
                        text-align: center;
                        line-height: 15px;
                        font-size: 10px;
                        z-index: 10;
                        cursor: pointer;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn a .badge[disabled] {
                        visibility: hidden;
                    }
            
                    #w20201005ded3aae02af59 .inline_widget.login_btn a.btn_text .badge {
                        left: auto;
                        margin-top: 0;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn a.info_img .badge {
                        margin-top: 0;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn .nameimg a .badge {
                        left: auto;
                        right: -10px;
                    }
                    #w20201005ded3aae02af59 .inline_widget.login_btn .badge {
                        display: ;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                        word-wrap: break-word;
                        word-break: keep-all;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip .tooltip-inner {
                        background-color:  !important;
                        color: #fff !important;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.top .tooltip-arrow {
                        border-top-color :;
                    }
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.bottom .tooltip-arrow {
                        border-bottom-color :;
                    }
            
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow {
                        border-left-color :;
                    }
            
                    #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        border-right-color :;
                    }
                    .new_fixed_header #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left .tooltip-arrow,
                    .new_fixed_header #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right .tooltip-arrow {
                        top: 50% !important;
                    }
                    .new_fixed_header #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.left,
                    .new_fixed_header #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip.right {
                        top: 0 !important;
                    }
            
                    @media (max-width: 991px) {
                        #w20201005ded3aae02af59 .inline_widget.button_text .inline-blocked .tooltip {
                            display: none !important;
                        }
                        #w20201005ded3aae02af59 .inline_widget .login_btn_item .join_tooltip ~ .tooltip {
                            display: block !important;
            
                        }
                    }
                    @media (min-width: 767px) {
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text span,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text i,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .info_name {
                            color : #212121 !important;
                        }
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget .line {
                            border-color : rgba(0,0,0,0.2) !important;
                        }
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text:hover,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text:hover span,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .inline_widget a.btn_text:hover i,
                        .doz_sys .hover_section_bg:hover #w20201005ded3aae02af59 .info_name:hover {
                              color : #ccc !important;
                        }
                    }
            
            
            
              #w20201005a8dce1cb98dd0 .search_btn a {
                display: flex;
                align-items: center;
                justify-content: center;
              }
                #w20201005a8dce1cb98dd0 .search_btn i {
                    max-width: 100%;
                    max-height: 100%;
                    display: block;
                    position: relative;
                    top:0;
                    line-height: inherit;
                }
                #w20201005a8dce1cb98dd0 .search_btn i.fa {
                    font-size: inherit;
                    width: auto;
                    height: auto;
                    vertical-align: inherit;
                    line-height: initial;
                }
                @media (min-width: 767px) {
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type a {
                        color : #212121		}
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a{
                        color : #212121 ;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a{
                        color: #fff;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a{
                        color: #fff;
                    }
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type a:hover {
                          ;
                              color: #999;
                      }
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a:hover{
                          color: #999;
                      }
                    .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a:hover,
                  .doz_sys .hover_section_bg:hover #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a:hover{
                          color: #fff;
                          background-color: #05b2f5;
                          border: 1px solid #05b2f5;
                      }
                }
                #w20201005a8dce1cb98dd0 .search_type a {
                    ;
                    color: #212121;
                    font-size: 20px;
                            background: #00B8FF	}
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type a {
                    ;
                    color: #212121;
                            background: #00B8FF	}
                #w20201005a8dce1cb98dd0 .search_type a:hover {
                    ;
                    color: #999;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type a:hover {
                    ;
                    color: #999;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 input.search_btn_form,
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 input.search_btn_form{
                    flex: 1;
                }
                #w20201005a8dce1cb98dd0 input.search_btn_form,
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 {
                    width: 100%;
                    height: 34px;
                    line-height: 34px;
                    padding: 0 10px;
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                    border-radius: 3px;
                    ;
                    color: #212121;
                    font-size: 14px;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 {
                    width: 100%;
                    border:0;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02:before {
                    border: 1px solid #dadada;
                    border-radius: 3px;
                    content:'';
                    position: absolute;
                    left: 0;
                    top: 0;
                    width: 100%;
                    height: 100%;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 input.search_btn_form {
                    flex: 1;
                    border: 0;
                    background: transparent;
                    border-radius: 0;
                    padding: 0 10px 0 0;
                    float:left;
                    height: 34px;
                    line-height: 34px;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a {
                    background: transparent !important;
                    padding: 0px 0px;
                    color: #212121;
                    line-height: 1;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a:hover {
                    color: #999;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a {
                    color:#212121;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 a:hover {
                    color: #999;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 a {
                    height: 100%;
                    position : relative;
                    right: 0;
                    top: 0;
                    line-height: 34px;
                    background: transparent !important;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 a i {
                    height: 100%;
                    vertical-align: 0;
                 }
                #w20201005a8dce1cb98dd0 form{
                    max-width: 150px;
                    width: 150px;
                    display: flex;
                    align-items: center;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type01 form{
                    max-width: 100%;
                    width: 100%;
                    display: flex;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 form.clearfix,
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 form.clearfix{
            
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 .search_btn_form {
                    float:left;
                    border-top-right-radius: 0;
                    border-bottom-right-radius: 0;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a {
                    height: 34px;
                    padding: 0 10px;
                    border-top-right-radius: 3px;
                    border-bottom-right-radius: 3px;
                    border-left:1px solid #dadada;
                    color:#fff;
                    line-height: 34px;
                    float: left;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a {
                    border-left:1px solid #dadada;
                    color:#fff;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a:hover,
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a:hover {
                    color: #fff;
                    background-color: #05b2f5;
                    border: 1px solid #05b2f5;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type03 a:hover,
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a:hover {
                    color: #fff;
                    background-color: #05b2f5;
                    border: 1px solid #05b2f5;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04,
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 {
                    height: 34px;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 input.search_btn_form {
                    float:left
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a {
                    height: 34px;
                    padding: 0 10px;
                    border :1px solid #00B8FF;
                    border-radius: 3px;
                    float: right;
                    margin-left: 5px;
                    color:#fff;
                    line-height: 34px;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a {
                    border :1px solid #00B8FF;
                    color:#fff;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 {
                    width: 150px;
                    height: 34px;
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                    border-radius: 3px;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 {
                    ;
                    background: #fff;
                    border:1px solid #dadada;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type04 a i {
                    vertical-align: inherit;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 > div {
                    width: 100%;
                    margin-top: -1px;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 input.search_btn_form {
                    flex: 1;
                    padding: 0;
                    background: transparent;
                    border :0;
                    border-radius: 0;
                    width: 100%;
                    padding-left:10px;
                    vertical-align: middle;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 a {
                    line-height: 34px;
                    background: transparent !important;
                    text-align: left;
                    padding-left:10px;
                    vertical-align: middle;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type05 i {
                    vertical-align: initial;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type06 .search_btn_form {
                    border: 0;
                    border-radius: 0;
                    border-bottom:1px solid #dadada;
                    background: transparent;
                    padding-left: 0;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type06 .search_btn_form {
                    border-bottom:1px solid #dadada;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type06  .search_btn_form:focus {
                    border-color: ;
                }
                #w20201005a8dce1cb98dd0 .search_type.search_btn_type06 a {
                    background: transparent;
                    position: absolute;
                    right: 0;
                    line-height: 32px;
                    top: 50%;
                transform: translateY(-50%);
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 input.search_btn_form,
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type02 {
                    ;
                    background: #fff;
                    ;
                    color: #212121;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 input.search_btn_form {
                    border:1px solid #dadada;
                }
                .scroll-to-fixed-fixed #w20201005a8dce1cb98dd0 .search_type.search_btn_type02:before {
                    border:1px solid #dadada;
                }
            
                            #s20201005b3138cd5be549 .inline-inside {
                                max-width: 1280px;
                                margin: 0 auto;
                                padding-left:15px;
                                padding-right:15px;
                            }
                            .admin.new_header_mode {
                                overflow-x: auto;
                            }
                            .new_header_mode #edit_wrap {
                                min-width: 1280px;
                            }
                            #s20201005b3138cd5be549 .section_bg {
                                ;
                                background-position:;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            .new_header_overlay_mobile #s20201005b3138cd5be549 .section_bg {
                                background-image:none;;
                            }
                            .new_header_overlay_mobile .new_fixed_header #s20201005b3138cd5be549 .section_bg {
                                ;
                            }
                            .scroll-to-fixed-fixed#s20201005b3138cd5be549 .section_bg {
                                ;
                                background-position: ;
                                background-size: cover; background-repeat: no-repeat;;
                            }
                            #s20201005b3138cd5be549 .inline-col-group {
                                padding-top:0px;
                                padding-bottom:0px;
                                height : 49px;
                            }
                            #s20201005b3138cd5be549 .inline-col-group > .inline-col {
                                padding-left: 10px;
                            }
                            #s20201005b3138cd5be549 .inline-col-group > .inline-col:first-child {
                                padding-left:  0 !important;
                            }
                            #s20201005b3138cd5be549 .inline-row > .inline-col {
                                padding-left: 10px;
                            }
                            #s20201005b3138cd5be549 .inline-row > .inline-col:first-child {
                                padding-left: 0 !important;
                            }
                            #s20201005b3138cd5be549.extend .inline-inside {
                                max-width: 100% !important;
                            }
                            #s20201005b3138cd5be549 .inline_widget.image .text,
                            #s20201005b3138cd5be549 .inline_widget.logo a,
                            #s20201005b3138cd5be549 .inline_widget.icon,
                            #s20201005b3138cd5be549 .inline_widget.login_btn a,
                            #s20201005b3138cd5be549 .viewport-nav > li > a,
                            #s20201005b3138cd5be549 .inline-col .inline_global_dropdown a,
                            #s20201005b3138cd5be549 .inline_widget.widget_text_wrap {
                                color: ;
                            }
            
                            .new_header_overlay_mobile #s20201005b3138cd5be549.scroll-to-fixed-fixed .viewport-nav > li > a {
                                color: ;
                            }
                            .new_header_overlay_mobile #s20201005b3138cd5be549.scroll-to-fixed-fixed .section_bg_color {
                                background-color: #ffffff !important;
                            }
                            #s20201005b3138cd5be549 .inline_widget.padding > div {
                                ;
                            }
                            #s20201005b3138cd5be549 .inline-col .inline_global_dropdown a i.arrow {
                                border-top-color: ;
                            }
                            #s20201005b3138cd5be549 {
                              border-width: 0 0 1px;
                              border-color: #e7e7e7;
                              border-style: solid;
                            }
                            .scroll-to-fixed-fixed#s20201005b3138cd5be549 {
                              border-color: #e7e7e7;
                              -webkit-transform: translate3d(0, 0, 0);
                                transform : translate3d(0, 0, 0);
                            } 
                            #s20201005b3138cd5be549 .inline-col-group,
                             #s20201005b3138cd5be549 .inline-col-group .inline-col {
                                vertical-align: middle ;
                            }
                            #inline_header_mobile #s20201005b3138cd5be549 .inline-inside {
                                padding-left:10px !important;
                                padding-right:10px !important;
                            }
                            #s20201005b3138cd5be549 .btn:not(.btn-primary):not(.btn_custom) {
                                ;
                                background-color: #ffffff;
                                ;
                                color:;
                                ;
                            }
                            #s20201005b3138cd5be549 .btn:not(.btn-primary):not(.btn_custom):hover {
                                border-color:;
                            }
                            #s20201005b3138cd5be549 .btn-primary span {
                                color:#00dce0;
                            }
                            @media (min-width: 991px) {
                                .doz_sys #s20201005b3138cd5be549 .btn-primary:hover span, #s20201005b3138cd5be549 .widget_text_wrap .btn:hover span {
                                    color:#ffffff;
                                }
                            }
                            @media all and (min-width: 768px) {
                                #s20201005b3138cd5be549.hover_section_bg:hover .section_bg_color {
                                    background-color:  !important;
                                }
                                #s20201005b3138cd5be549.hover_section_bg:hover .section_bg {
                                    ;
                                }
                                #s20201005b3138cd5be549.hover_section_bg:hover img.normal_logo {
                                    opacity: 0;
                                }
                                #s20201005b3138cd5be549.hover_section_bg:hover img.scroll_logo {
                                    opacity: 1;
                                }
                            }
                            @media all and (max-width: 767px) {
                                .inline_header_design {
                                    overflow-x: hidden;
                                }
                            }
            
                @media all and (max-width : 767px) {
                    .fixed-menu-on .scroll_position {
                        top: -95px !important;
                    }
                    .fixed-menu-on.new_fixed_header_disable .scroll_position {
                        top: 0 !important;
                    }
                }
            
                .mobile_carousel_nav.home_disable {
                    opacity: 0.5;
                }
                .mobile_carousel_nav .mobile_nav_depth {
                    padding: 0 15px;
                    white-space: nowrap;
                    overflow: hidden;
                    position: relative;
                    overflow-x: scroll;
                    -ms-overflow-style: none;
                    overflow: -moz-scrollbars-none;
                }
                .mobile_carousel_nav .depth_first {
                    border-bottom: 1px solid #e7e7e7;
                }
                .scroll-to-fixed-fixed .mobile_carousel_nav .depth_first {
                    border-bottom: 1px solid #e7e7e7;
                }
                .mobile_carousel_nav .depth_first::-webkit-scrollbar {
                    display: none;
                    height: 0;
                    width: 0;
                }
                .mobile_carousel_nav.box_shadow_on {
                    box-shadow: rgba(0, 0, 0, 0.2) 0 1px 3px 0;
                }
                .mobile_carousel_nav .nav-item {
                    height: 45px;
                    display: inline-block;
                }
                .mobile_carousel_nav .nav-item.active > a {
                    ;
                }
                .mobile_carousel_nav .nav-item > a {
                    font-weight: ;
                }
                .mobile_carousel_nav .nav-item:before {
                    content: "";
                    display: inline-block;
                    vertical-align: middle;
                    height: 100%;
                }
                .mobile_carousel_nav .st00 .nav-item:before,
                .mobile_carousel_nav .st04 .nav-item:before,
                .mobile_carousel_nav .st05 .nav-item:before{
                    display: none;
                }
                .mobile_carousel_nav .st00 .nav-item a:before,
                .mobile_carousel_nav .st04 .nav-item a:before,
                .mobile_carousel_nav .st05 .nav-item a:before {
                    content: "";
                    display: inline-block;
                    vertical-align: middle;
                    height: 100%;
                }
                .mobile_carousel_nav .st00 .nav-item,
                .mobile_carousel_nav .st04 .nav-item,
                .mobile_carousel_nav .st05 .nav-item {
                    padding-top: 0 !important;
                    padding-bottom: 0 !important;
                }
                .mobile_carousel_nav .st00 .nav-item a,
                .mobile_carousel_nav .st04 .nav-item a,
                .mobile_carousel_nav .st05 .nav-item a {
                    height: 45px;
                    line-height: 45px;
                }
                .mobile_carousel_nav .nav-item {
                    margin: 0 0px;
                }
                .mobile_carousel_nav .nav-item:first-child {
                    margin-left: 0;
                }
                .mobile_carousel_nav .nav-item:last-child {
                    margin-right: 0;
                }
                .mobile_carousel_nav .nav-item > a {
                    font-size: 13px;
                    color: #212121;
                    letter-spacing: 1px;
                    display: inline-block;
                    vertical-align: middle;
                }
                .mobile_carousel_nav .nav-item.use_sub_name:hover>a>.plain_name {
                    display: inline-block;
                }
                .mobile_carousel_nav .nav-item.use_sub_name:hover>a>.plain_name:before {
                    color: #212121;
                }
                .scroll-to-fixed-fixed .mobile_carousel_nav .nav-item > a,
                .scroll-to-fixed-fixed .mobile_carousel_nav .nav-item.use_sub_name:hover>a>.plain_name:before {
                    color: #212121;
                }
                .mobile_carousel_nav .nav-item > a:focus {
                    outline: none;
                }
                /*
                * depth_first 스타일
                */
                .mobile_carousel_nav{
                    touch-action: none;
                }
                .mobile_nav_depth  {
                    background-color: #fff;
                }
                .scroll-to-fixed-fixed .mobile_nav_depth {
                    background-color: #fff;
                }
                .mobile_carousel_nav .active > a {
                    background: ;
                    color: #212121;
                    padding: 4px 13px;
                    border: 1px solid ;
                }
            
                .scroll-to-fixed-fixed .mobile_carousel_nav .active > a{
                    background: ;
                    color: #212121;
                    border: 1px solid ;
                }
                .mobile_carousel_nav .st00 .active > a,
                .mobile_carousel_nav .st04 .active > a,
                .mobile_carousel_nav .st05 .active > a,
                .mobile_carousel_nav .st06 .active > a {
                    background: transparent;
                    padding: 0;
                    border: 0;
                }
                .mobile_carousel_nav .st01 .active > a {
                    border-radius: 15px;
                }
                .mobile_carousel_nav .st02 .active > a {
                    border-radius: 3px;
                }
                .mobile_carousel_nav .st03 .active > a {
                    border-radius: 0;
                }
                .mobile_carousel_nav .st04 .active {
                    padding: 4px 13px;
                    border: 1px solid #212121;
                    background: #212121;
                    color: #fff	}
                .scroll-to-fixed-fixed .mobile_carousel_nav .st04 .active {
                    border: 1px solid #212121;
                    background: #212121;
                    color: #fff	}
                .mobile_carousel_nav .st04 .active,
                .scroll-to-fixed-fixed .mobile_carousel_nav .st04 .active {
                    border: 0;
                }
                .mobile_carousel_nav .st05 .nav-item {
                    padding: 4px 13px;
                }
            
                .mobile_carousel_nav .st05 .active {
                    border-bottom: 2px solid #212121;
                    padding: 4px 13px;
                }
            
                .scroll-to-fixed-fixed .mobile_carousel_nav .st05 .active {
                    border-bottom: 2px solid #212121;
                }
            
            
                .mobile_carousel_nav .st05 .active > a {
                    color: #212121;
                }
            
                .scroll-to-fixed-fixed .mobile_carousel_nav .st05 .active > a {
                    color: #212121;
                }
                .mobile_carousel_nav .st06 .active > a {
                    border-bottom: 2px solid #212121;
                    color: #212121;
                }
            
                .scroll-to-fixed-fixed .mobile_carousel_nav .st06 .active > a {
                    border-bottom: 2px solid #212121;
                    color: #212121;
                }
                .mobile_carousel_nav .depth_first.st01 .active > a,
                .mobile_carousel_nav .depth_first.st02 .active > a,
                .mobile_carousel_nav .depth_first.st03 .active > a,
                .mobile_carousel_nav .depth_first.st04 .active > a {
                    color:#fff;
                    background: #212121;
                    border-color: #212121;
                }
            
                .scroll-to-fixed-fixed .mobile_carousel_nav .depth_first.st01 .active > a,
                .scroll-to-fixed-fixed .mobile_carousel_nav .depth_first.st02 .active > a,
                .scroll-to-fixed-fixed .mobile_carousel_nav .depth_first.st03 .active > a,
                .scroll-to-fixed-fixed .mobile_carousel_nav .depth_first.st04 .active > a {
                    color:#fff;
                    background: #212121;
                    border-color: #212121;
                }
            
                .before_btn_wrap {
                    display: none;
                }
                .move_btn_on .before_btn_wrap a {
                    color: #212121;
                    line-height:45px;
                    padding: 0 10px;
                }
            
                .scroll-to-fixed-fixed .move_btn_on .before_btn_wrap a {
                    color: #212121;
                }
                .move_btn_on .before_btn_wrap {
                    display: block;
                    position : absolute;
                    z-index :1;
                    font-size: 13px;
                    left: 5px;
                }
                .mobile_carousel_nav.move_btn_on .depth_first {
                    padding-left: 40px;
                }
            
            
                        .shop_view .s202309183d6f4281c58f0.xzoom-preview {
                            ;
                            background: ;
                        }
                        .shop_view #s202309183d6f4281c58f0 select.form-control option {
                            color:  !important;
                            background: ;
                        }
                        .is-ie .shop_view #s202309183d6f4281c58f0 select.form-control option {
                            color: #000 !important;
                        }
                        .admin #s202309183d6f4281c58f0 .widget.padding > div {
                            ;
                        }
                        .admin #s202309183d6f4281c58f0 .ibg-bg {
                            height: 100% !important;
                        }
                        .admin #s202309183d6f4281c58f0 .widget_drag_bar,
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-e:hover:after,
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-w:hover:after,
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-e.active:after,
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-w.active:after,
                        .admin .doz_sys #s202309183d6f4281c58f0 .drop_line {
                            background-color: ;
                        }
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-n:hover:after,
                        .admin .doz_sys #s202309183d6f4281c58f0 .ui-resizable-handle.ui-resizable-s:hover:after {
                            border-bottom:2px solid  ;
                        }
                        #s202309183d6f4281c58f0 {
                            color: ;
                        }
                        #s202309183d6f4281c58f0.side_basic main .inside,
                        #s202309183d6f4281c58f0 .site_prod_nav_wrap.scroll-to-fixed-fixed ul.site_prod_nav,
                        .doz_sys #s202309183d6f4281c58f0 .col-dz-12 .extend_thumbs {
                            max-width: 1280px;
                        }
                        .modal_site_modal_menu #s202309183d6f4281c58f0.side_basic main .inside,
                        .menu_type_modal #s202309183d6f4281c58f0.side_basic main .inside {
                            max-width: 550px;
                        }
                        .doz_sys .modal_site_modal_menu .modal-header,
                        .menu_type_modal .doz_modal_header {
                            border-width: 0 0 1px 0;
                            border-style: solid;
                            ;
                        }
                        .menu_type_modal #s202309183d6f4281c58f0,
                        .menu_type_modal .doz_modal_header {
                        ;
                            background: ;
                        ;
                            color:  ;
                        }
                        .menu_type_modal .doz_modal_header .bt.bt-flat.bt-default {
                        ;
                            color:  ;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .col-dz-12 .inside .extend_thumbs {
                            max-width: inherit;
                        }
                        #s202309183d6f4281c58f0.extend_section main {
                            padding-left: 15px;
                            padding-right: 15px;
                        }
                        #s202309183d6f4281c58f0.section_wrap.extend_section main .widget.board .grid_ignore.bg_on {
                            margin-left: -15px;
                            margin-right: -15px;
                            width: calc(100% + 15px + 15px);
                        }
                        #s202309183d6f4281c58f0 .booking_day .body_font_color_20,
                        #s202309183d6f4281c58f0 .booking_list.waiting .title {
                            ; 
                        }
            
                        #s202309183d6f4281c58f0.extend_section main > .inside {
                            max-width: 100% !important;
                        }
                        #s202309183d6f4281c58f0 .li_table ul:nth-of-type(2),
                        #s202309183d6f4281c58f0 .li_board ul li,
                        #s202309183d6f4281c58f0 .radio-styled:not(ie8).radio_color_option.small input ~ span span {
                            ;
                        }
                        #s202309183d6f4281c58f0 .checkbox-styled:not(ie8) input ~ span:before,
                        #s202309183d6f4281c58f0 .radio-styled:not(ie8) input ~ span:before {
            
                        }
                        #s202309183d6f4281c58f0 .board_view .grid_ignore header a, #s202309183d6f4281c58f0 .widget.board .grid_ignore .author .date, #s202309183d6f4281c58f0 .widget.board .grid_ignore a.board, #s202309183d6f4281c58f0 .widget.board .grid_ignore .author .write, .editor_box .add_map .info > div.phone, #s202309183d6f4281c58f0 .content-tit .board {
                            ;
                        }
                        #s202309183d6f4281c58f0 select.form-control,
                        #s202309183d6f4281c58f0 input.form-control,
                        #s202309183d6f4281c58f0 textarea.form-control {
                            ;
                            color: #212121;
                            background: #ffffff;
                        }
                        #s202309183d6f4281c58f0 .input_block .select-block .selectbox select {
                            border: none;
                            background: none;
                            color: #212121;
                        }
                        #s202309183d6f4281c58f0 .phonenumber_wrap .line {
            
                        }
                        #s202309183d6f4281c58f0 .shop-content.shop-style-b.open .opt-group .btn_clse > span {
            
                        }
                        .shop_view #s202309183d6f4281c58f0 .shop-content select.form-control,
                        .shop_view #s202309183d6f4281c58f0 .shop-content input.form-control,
                        .shop_view #s202309183d6f4281c58f0 .shop-content textarea.form-control,
                        .booking_view #s202309183d6f4281c58f0 .booking_opt select.form-control,
                        .shop_view #s202309183d6f4281c58f0 .form-select-wrap .dropdown-menu,
                        .shop_view #s202309183d6f4281c58f0 .form-select-wrap .dropdown-menu .dropdown-item {
                            ;
                            background: ;
                        }
                        #s202309183d6f4281c58f0 .seemore_wrap .open:before {
                            background-image: linear-gradient(to bottom, ,  66%,  83%,  98%, );
                        }
                        #s202309183d6f4281c58f0 .item_detail select.form-control,
                        #s202309183d6f4281c58f0 .item_detail input.form-control,
                        #s202309183d6f4281c58f0 .item_detail textarea.form-control,
                        #s202309183d6f4281c58f0 .booking_opt select.form-control,
                        #s202309183d6f4281c58f0 .goods_select textarea.form-control,
                        #s202309183d6f4281c58f0 .goods_select select.form-control,
                        #s202309183d6f4281c58f0 .goods_select input.form-control,
                        #s202309183d6f4281c58f0 .form-select-wrap:before {
                             !important;
                            color: ;
                        }
                        #s202309183d6f4281c58f0 .form-select-wrap .dropdown-menu .dropdown-item:hover {
                            ;
                        }
                        #s202309183d6f4281c58f0 .board_summary .write, #s202309183d6f4281c58f0 .board_view .grid_ignore .author .date, #s202309183d6f4281c58f0 .board_view .grid_ignore .author .hit-count, .doz_sys #s202309183d6f4281c58f0 label, .doz_sys #s202309183d6f4281c58f0 label.control-label, #s202309183d6f4281c58f0 .shop-table > tbody > tr.payment-info > td.pay-txt, #s202309183d6f4281c58f0 .nick.text-default-dark, #s202309183d6f4281c58f0 .text-default-dark, #s202309183d6f4281c58f0 .shop_mypage .mypage .my-box a, #s202309183d6f4281c58f0 .shop_mypage .item-detail a, #s202309183d6f4281c58f0 .shop_mypage .item-detail p, #s202309183d6f4281c58f0 .shop_mypage h6, #s202309183d6f4281c58f0 .shop_mypage .table-wrap p, #s202309183d6f4281c58f0 .shop_payment h1, #s202309183d6f4281c58f0 .shop_payment h6, #s202309183d6f4281c58f0 .shop-content p, #s202309183d6f4281c58f0 .shop_payment, #s202309183d6f4281c58f0 .shop-content span, #s202309183d6f4281c58f0 .shop-content .shop-item .item-icon .im-icon.im-ico-liked, #s202309183d6f4281c58f0 .shop-content .price, #s202309183d6f4281c58f0,#s202309183d6f4281c58f0 .shop-tit,#s202309183d6f4281c58f0 .board_view .board_txt_area,#s202309183d6f4281c58f0 .board.widget .grid_ignore .view_tit,.doz_sys #s202309183d6f4281c58f0 .shop-content input.form-control, .doz_sys #s202309183d6f4281c58f0 .shop-content select.form-control, #s202309183d6f4281c58f0 .widget_menu_title,#s202309183d6f4281c58f0 .comment_area,body.shop_mypage #s202309183d6f4281c58f0 .comment_area,
                        #s202309183d6f4281c58f0 .list_review_inner .use_summary, #s202309183d6f4281c58f0 .list_review_inner .use_summary a, #s202309183d6f4281c58f0 .list_review_inner .fold, #s202309183d6f4281c58f0 .list_review_inner .comment_area, #s202309183d6f4281c58f0 .booking_nav_tools span {
                            ;
                            color:  ;
                        }
                        #s202309183d6f4281c58f0 .shop-content span.sale-price-text {
                            color : #212121 !important;
                        }
                        .doz_sys #s202309183d6f4281c58f0 a.use-info {
                            color : #00dce0;
                        }
                        #s202309183d6f4281c58f0 .shop-content span.sale-price-text-done, 
                        .doz_sys #s202309183d6f4281c58f0 a.use-info-download-done {
                            color: #999999 !important;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .shop-content .down-btn select.form-control {
                            ;
                            color:  !important;
                        }
                        #s202309183d6f4281c58f0 .shop-content.mypage .bg-bright a, #s202309183d6f4281c58f0 .shop-content.mypage .bg-bright p, #s202309183d6f4281c58f0 .shop-content.mypage .bg-bright span, #s202309183d6f4281c58f0 .shop-content.mypage .bg-bright div {
                            color: #212121;
                        }
                        #s202309183d6f4281c58f0 .shop-content.mypage .bg-bright .use_grade .ug_btn .btn,
                        #s202309183d6f4281c58f0 .shop-content span.ug_name .btn {
                            border-color: #D5D5D5;
                        }
                        #s202309183d6f4281c58f0 .shop-content h6 span {
                        ;
                            color: ;
                        }
                        #s202309183d6f4281c58f0 .left-menu ul li.on a,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_count .owl-dots .owl-dot span:before,
                        .menu_type_modal #s202309183d6f4281c58f0,
                        #s202309183d6f4281c58f0 .list_review_inner .comment .tools .text-gray-bright {
                            ;
                            color:  !important;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_count.slide_02 .owl-dots .owl-dot.active span:before {
                            color: #fff !important;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_dot .owl-dots .owl-dot span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_big_dot .owl-dots .owl-dot span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_line .owl-dots .owl-dot span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_count.paging_type_count02 .owl-dots .owl-dot.active span:before,
                        #s202309183d6f4281c58f0 .list_review_inner, 
                        #s202309183d6f4281c58f0 .list_review_inner .fold.cmt,
                        #s202309183d6f4281c58f0 .list_review_wrap,
                        #s202309183d6f4281c58f0 .list_review_inner .textarea_block,
                        #s202309183d6f4281c58f0 .list_review_inner .comment .main_comment,
                        #s202309183d6f4281c58f0 .list_review_inner .txt_delete:before,
                        #s202309183d6f4281c58f0 .form-select-wrap.open .dropdown-toggle, 
                        #s202309183d6f4281c58f0 .form-select-wrap.open .dropdown-menu,
                        #s202309183d6f4281c58f0 .form-select-wrap.open .dropdown-menu .dropdown-item {
                            border-color: ;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_dot02 .owl-dots .owl-dot span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_dot .owl-dots .owl-dot.active span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_line .owl-dots .owl-dot.active span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_big_dot .owl-dots .owl-dot span,
                        .doz_sys #s202309183d6f4281c58f0 .paging_type_line .owl-dots .owl-dot span {
                            background: ;
                        }
                        #s202309183d6f4281c58f0 .form-control:focus {
                            border-color:#00dce0;
                        }
                        #s202309183d6f4281c58f0 .sub_depth li a, #s202309183d6f4281c58f0 .sub_depth li span {
                            ;
                        }
                        #s202309183d6f4281c58f0 .slide_03.owl-theme .owl-dots .owl-dot span {
                            ;
                        } 
                        #s202309183d6f4281c58f0 .pagination > li > a,
                        #s202309183d6f4281c58f0 .pagination > li > span,
                        #s202309183d6f4281c58f0 .pagination > li > a:focus,
                        #s202309183d6f4281c58f0 .pagination > li > span:focus,
                        #s202309183d6f4281c58f0 .map-inner .pagination li.active a,
                        #s202309183d6f4281c58f0 .pagination li > a.disabled:hover,
                        #s202309183d6f4281c58f0 .pagination li > a.disabled:focus {
                            ;
                        }
                        #s202309183d6f4281c58f0 .form-select-wrap.open .dropdown-menu .dropdown-item {
                            ;
                        }
                        #s202309183d6f4281c58f0 .pagination > .active > a,
                        #s202309183d6f4281c58f0 .pagination > .active > span,
                        #s202309183d6f4281c58f0 .pagination > .active > a:hover,
                        #s202309183d6f4281c58f0 .pagination > .active > span:hover,
                        #s202309183d6f4281c58f0 .pagination > .active > a:focus,
                        #s202309183d6f4281c58f0 .pagination > .active > span:focus,
                        #s202309183d6f4281c58f0 .pagination > li > a:hover,
                        #s202309183d6f4281c58f0 .pagination > li > span:hover,
                        #s202309183d6f4281c58f0 .sub_depth li a.active,
                        .doz_sys #s202309183d6f4281c58f0 a, #s202309183d6f4281c58f0 .li_table ul li,
                        #s202309183d6f4281c58f0 .list-style .list.line > small,
                        .doz_sys #s202309183d6f4281c58f0 div[data-widget-type="board"] .title.title-block a{
                            ;
                            color: ;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .board_contents a:not(.btn),
                        .doz_sys #s202309183d6f4281c58f0 .board_contents a:not(.btn):hover,
                        #s202309183d6f4281c58f0 .board_txt_area a,
                        #s202309183d6f4281c58f0 .board_txt_area a:hover,
                        #s202309183d6f4281c58f0 .board_txt_area a:active,
                        #s202309183d6f4281c58f0 .board_txt_area a:focus,
                        #s202309183d6f4281c58f0 .editor_box .fr-view a {
                            color: #00dce0;
                        }
                        #s202309183d6f4281c58f0 div[data-widget-type="icon"] i {
                            color: ;
                        }
                        .doz_sys #s202309183d6f4281c58f0 a.body_font_color_30:not(.active) {
                            ;
                        }
                       #s202309183d6f4281c58f0 .text_tab .after_line:not(:last-child):after {
                            ;
                       }
                       #s202309183d6f4281c58f0 .text_tab ul.site_prod_nav > li a.active {
                        background: none;
                       }
                        #s202309183d6f4281c58f0 .map-toolbar select.form-control {
                            ;
                            color:  !important;
                            font-size: 14px;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .body_font_color_40,
                        #s202309183d6f4281c58f0 .li_board ul.li_body li.name, 
                        #s202309183d6f4281c58f0 .li_board ul.li_body li.time, 
                        #s202309183d6f4281c58f0 .li_board ul.li_body li.like,
                        #s202309183d6f4281c58f0 .li_board ul.li_body li.read {
                            ;
                        }
                        #s202309183d6f4281c58f0 .review_table .summary,
                        #s202309183d6f4281c58f0 .review_table.li_board ul.li_body li,
                        #s202309183d6f4281c58f0 .review_table .list_text_title.lock_on {
                            ;
                        }
            
                        .doz_sys #s202309183d6f4281c58f0 .body_font_color_50 {
                            ;
                        }
                        #s202309183d6f4281c58f0 .li_board,
                        #s202309183d6f4281c58f0 .acd_row:first-child,
                        #s202309183d6f4281c58f0 .acd_row {
                            border-color: ;
                        }
                        #s202309183d6f4281c58f0 .list-style .list-header,
                        #s202309183d6f4281c58f0 .list-style .list,
                        #s202309183d6f4281c58f0 .list-style .list.line, 
                        #s202309183d6f4281c58f0 .list-style .list.line > .table-cell,
                        #s202309183d6f4281c58f0 .li_table.row_04 .acd_collapse[aria-expanded="true"], .li_table.row_04 .acd_collapse.in {
                            ;
                        }
                        #s202309183d6f4281c58f0 .btn, #s202309183d6f4281c58f0 .visual_section a, #s202309183d6f4281c58f0 a.select-star, #s202309183d6f4281c58f0 .star-pointer .dropdown-menu a.dropdown-item {
                        ;
                            background-color: ;
                            ;
                            color:;
                            ;
                        }
                        #s202309183d6f4281c58f0 .star-pointer .dropdown-menu {
                            background-color: ;
                        }
                        #s202309183d6f4281c58f0 .btn:hover, #s202309183d6f4281c58f0 .visual_section a:hover {
                            border-color:;
                        }
                        #s202309183d6f4281c58f0 a.select-star:hover {
                            background-color: ;
                        }
                        #s202309183d6f4281c58f0 .star-pointer .dropdown-menu a.dropdown-item:hover {
                            background-color:  !important;
                        }
                        #s202309183d6f4281c58f0 .widget_text_wrap .btn {
                            background-color:#ffffff;
                            border-color:#00dce0;
                            color:#00dce0;
                            border-width:1px;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .btn-primary{
                        ;
                            background-color:#ffffff;
                            border-color:#00dce0;
                            color:#00dce0;
                            border-width:1px;
                        }
                        .doz_sys.shop_view #s202309183d6f4281c58f0 .btn-primary span,
                        .doz_sys.booking_view #s202309183d6f4281c58f0 .btn-primary span,
                        .doz_sys.shop_mypage #s202309183d6f4281c58f0 .btn-primary span  {
                            color:#00dce0;
                        }
                        #s202309183d6f4281c58f0 .coupon-wrap:after,
                        #s202309183d6f4281c58f0 .board_view .file_area ul li {
                            background: ;
                        }
                        #s202309183d6f4281c58f0 .text-gray-dark, #s202309183d6f4281c58f0 .shop-table > thead > tr > th, #s202309183d6f4281c58f0 .shop_mypage .left-menu ul li a, #s202309183d6f4281c58f0 .shop_mypage .item-detail p.sale_pay,.doz_sys #s202309183d6f4281c58f0 .product-notify-group .product-notify-label {
                            ;
                        }
                        #s202309183d6f4281c58f0 .mypage .my-box a, #s202309183d6f4281c58f0 .mypage .shop-table > tbody > tr,
                        #s202309183d6f4281c58f0 .mypage .tip-off,
                        #s202309183d6f4281c58f0 .im-order-detail-table,
                        #s202309183d6f4281c58f0 .im-order-price {
                            ;
                        }
                        #s202309183d6f4281c58f0 .mypage .my-box.on a {
                            background-color:#00dce0;
                            ;
                            color:#fff;
                        }
                        #s202309183d6f4281c58f0 .mypage .my-box.on a p {
                            color:#fff;
                        }
                        #s202309183d6f4281c58f0 .option_btn_tools a, #s202309183d6f4281c58f0 .map-inner .pagination li a {
                            color:#212121;
                        }
                        .doz_sys #s202309183d6f4281c58f0 .list-style-card .card-body .text a {
                            color:#757575;
                        }
                        #s202309183d6f4281c58f0 .card .title a {
                            color: #212121;
                        }
                        #s202309183d6f4281c58f0 .section_bg.fixed_bg.fixed_bg_none {
                                background-attachment : inherit;
                            }
                        #s202309183d6f4281c58f0 ul.site_prod_nav > li,
                        #s202309183d6f4281c58f0 .prod_detail_badge {
                            ;
                        }
                        #s202309183d6f4281c58f0 .site_prod_nav_wrap.scroll-to-fixed-fixed {
                            background: ;
                            box-shadow: inset 0 -1px 0 0 rgba(0, 0, 0, 0.1);
                        }
                        #s202309183d6f4281c58f0 .buy_footer_fixed {
                            background: ;
                            border-width: 1px 0 0 0;
                            border-style: solid;
                            ;
                        }
                        #s202309183d6f4281c58f0 .opt-group {
                            background: ;
                        }
                        #s202309183d6f4281c58f0 ul.site_prod_nav > li a.active {
                            ;
                        }
            
                        #s202309183d6f4281c58f0 .background_tab ul.site_prod_nav > li a.active >  span.braket-badge {
                            background-color: none;
                            ;
                            color:;
                        }
            
                        #s202309183d6f4281c58f0 .input-block .checkbox-styled:not(ie8) input ~ span {
                            ;
                            color:;
                        }
                        .section_fixed_disable #s202309183d6f4281c58f0[class*="section_first"],
                        .section_fixed_disable #s202309183d6f4281c58f0[class*="section_first"] .doz_aside {
                            position: relative !important;
                            top: 0 !important;
                            left: 0 !important;
                            z-index: auto !important;
                        }
                        .section_fixed_disable #s202309183d6f4281c58f0 .doz_aside.scroll-to-fixed-fixed ~ .spacer,
                        .section_fixed_disable #s202309183d6f4281c58f0.scroll-to-fixed-fixed ~ .spacer {
                            height: 0 !important;
                            display: none !important;
                        }
                        #s202309183d6f4281c58f0.scroll-to-fixed-fixed {
                            width: 100% !important;
                        }
                        #s202309183d6f4281c58f0 .doz_aside.scroll-to-fixed-fixed-end {
                            bottom: 0 !important;
                            top: auto !important;
                        }
                        .device_type_m #s202309183d6f4281c58f0.mobile_section main .inside {
                                padding-left: 15px;
                                padding-right: 15px;
                        }
                        .device_type_m #s202309183d6f4281c58f0 .mypage .left-menu ul li a,
                        .device_type_m #s202309183d6f4281c58f0 .cart .left-menu ul li a {
                            ;
                        }
                        #s202309183d6f4281c58f0 .im-cart-result-table {
                            border-top: 1px solid ;
                            border-bottom: 1px solid ;
                        }
                        #s202309183d6f4281c58f0 .shop-table > tbody > tr > td.img .opt .more {
                            ;
                        }
                        #s202309183d6f4281c58f0 .im-cart-info {
                            ;
                        }
                        #s202309183d6f4281c58f0 .shop-table > thead > tr > th,
                        #s202309183d6f4281c58f0 .shop-table > tbody > tr > td,
                        #s202309183d6f4281c58f0 .mypage .shop-table > tbody > tr,
                        #s202309183d6f4281c58f0 .shop-table > tbody > tr > td.img img,
                        #s202309183d6f4281c58f0 .shop-table > tbody > tr > td + td,
                        #s202309183d6f4281c58f0 .mypage .tip-off,
                        #s202309183d6f4281c58f0 .mypage .shop-table img,
                        #s202309183d6f4281c58f0 .im-order-detail-table,
                        #s202309183d6f4281c58f0 .im-order-price,
                        #s202309183d6f4281c58f0 .im-order-detail-table thead tr,
                        #s202309183d6f4281c58f0 .im-order-detail-table tr + tr,
                        #s202309183d6f4281c58f0 .im-order-detail-table img,
                        #s202309183d6f4281c58f0 .im-order-detail-table .im-deliv-price,
                        #s202309183d6f4281c58f0 .im-order-price-header,
                        #s202309183d6f4281c58f0 .im-order-price-body {
                            ;
                        }
                        #s202309183d6f4281c58f0 .shop-table .list_badge {
                            border-color: ;
                        }
                        #s202309183d6f4281c58f0 .im-cart-result-table thead>tr>th,
                        #s202309183d6f4281c58f0 #shop_cart_list .shop-table > colgroup + thead > tr:first-child > th,
                        #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tbody > tr > td + td,
                        #s202309183d6f4281c58f0 #shop_cart_list .shop-table > thead > tr > th,
                        #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tbody > tr > td {
                            ;
                        }
                        #s202309183d6f4281c58f0 .shop-content.mypage .shop-item .item-icon .im-icon.im-ico-liked{
                            color: #00dce0
                        }
                        @media (min-width: 991px) {
                            .doz_sys #s202309183d6f4281c58f0 .btn-primary:hover, #s202309183d6f4281c58f0 .widget_text_wrap .btn:hover {
                            ;
                                background-color:#00dce0;
                                border-color:rgba(0,220,224,1);
                                color:#ffffff;
                                border-width:1px;
                            }
                            .doz_sys.shop_view #s202309183d6f4281c58f0 .btn-primary:hover span,
                            .doz_sys.booking_view #s202309183d6f4281c58f0 .btn-primary:hover span,
                            .doz_sys.shop_mypage #s202309183d6f4281c58f0 .btn-primary:hover span  {
                                color:#ffffff;
                            }
                        }
                        @media all and (max-width : 768px) {
                            .doz_sys #s202309183d6f4281c58f0 .fixed_view a,
                            .doz_sys #s202309183d6f4281c58f0 .fixed_view select.form-control,
                            .doz_sys #s202309183d6f4281c58f0 .fixed_view .form-select-wrap:before {
                                color: #212121;
                            }
                            .doz_sys #s202309183d6f4281c58f0 .fixed_view .body_font_color_50 {
                                color: rgba(33, 33, 33, 0.5);
                            }
                            .doz_sys #s202309183d6f4281c58f0 .fixed_view .body_font_color_20 {
                                color: rgba(33, 33, 33, 0.2);
                            }
                            .booking_view #s202309183d6f4281c58f0 .fixed_view .booking_opt select.form-control {
                                background-color: #fff;
                            }
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-tit,
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > thead > tr,
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tfoot .payment-info,
                            #s202309183d6f4281c58f0 .im-price-result {
                                ;
                            }
                            #s202309183d6f4281c58f0 .shop-table > tbody > tr > td.img .opt .more + .more,
                            #s202309183d6f4281c58f0 .im-order-row + .im-order-row {
                                ;
                            }
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table,
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tbody > tr.im-tr-shipping + tr,
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tfoot,
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > tfoot .payment-info {
                                ;
                            }
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > thead > tr,
                            #s202309183d6f4281c58f0 .im-order-detail-table .im-space {
                                background-color: ;
                            }
                            #s202309183d6f4281c58f0 #shop_cart_list .shop-table > thead > tr.scroll-to-fixed-fixed-end {
                                top: auto !important;
                                bottom: 0;
                            }
                        }
                        .device_type_m #s202309183d6f4281c58f0 .section_bg.fixed_bg_wrap { 
                             background-attachment: fixed;
                        }
            
                        .device_type_m #s202309183d6f4281c58f0 .section_bg.fixed_bg_wrap .fixed_bg {
                          display: none;
                        }
                        #s202309183d6f4281c58f0 .section_bg.fixed_bg_wrap .fixed_bg {
                             display: none;
                            }
                        @media (max-width: 991px) {
                            #s202309183d6f4281c58f0 .section_bg {
                                background-attachment : inherit;
                            }
            
                            #s202309183d6f4281c58f0 .section_bg.fixed_bg_wrap { 
                                background-image : none !important;
                                clip-path: inset(0);
                                overflow: hidden;
                            }
                            #s202309183d6f4281c58f0 .section_bg.fixed_bg_wrap .fixed_bg {
                              display: block;
                              object-fit: cover;
                              position: fixed;
                              left: 0;
                              top: 0;
                              width: 100%; 
                              height: 100vh;
                            }
                            #s202309183d6f4281c58f0 .buy_btns .social_btn, #s202309183d6f4281c58f0 .buy_btns .cart_btn, #s202309183d6f4281c58f0 .layer_pop .bottom-btn, #s202309183d6f4281c58f0 .shop-table > thead, #s202309183d6f4281c58f0 .left-menu, #s202309183d6f4281c58f0 .shop-table > tbody > tr, {
                            ;
                            }
                            #s202309183d6f4281c58f0 main, #s202309183d6f4281c58f0 .section_wrap.extend_section main, #s202309183d6f4281c58f0 .doz_sys.shop_payment .inside, .doz_sys.shop_payment .inside .col-dz, {
                                padding-left:0;
                                padding-right:0;
                            }
                            #s202309183d6f4281c58f0.mobile_section main .inside {
                                padding-left: 15px;
                                padding-right: 15px;
                            }
                            #s202309183d6f4281c58f0.section_wrap.extend_section main .widget.board .grid_ignore.bg_on {
                                margin-left: -15px;
                                margin-right: -15px;
                                width: calc(100% + 30px);
                            }
                            #s202309183d6f4281c58f0 .mypage .left-menu ul li a,
                            #s202309183d6f4281c58f0 .cart .left-menu ul li a,
                            #s202309183d6f4281c58f0 .mypage .left-menu .cart-menu-slide  {
                                ;
                            }
                            .section_wrap .side_gutter {
                                display:none !important;
                            }
                            #s202309183d6f4281c58f0 .coupon-wrap:after {
                                background:  !important;
                            }
                        }
                        @media (max-width: 767px) {
                            #s202309183d6f4281c58f0 .nav_gradient.slide_left {
                                background: linear-gradient(to left, rgba(255, 255, 255, 0), rgba(255,255,255,1));
                            }
                            #s202309183d6f4281c58f0 .nav_gradient.slide_right {
                                background: linear-gradient(to right, rgba(255, 255, 255, 0), rgba(255,255,255,1));
                            }
                            #s202309183d6f4281c58f0 .button_tab .scroll-to-fixed-fixed ul.site_prod_nav > li {
                                border-top: 0;
                                border-bottom: 0;
                            }
                            #s202309183d6f4281c58f0 .background_tab .scroll-to-fixed-fixed ul.site_prod_nav > li a.active {
                                box-shadow: inset 0 -1px 0 0 rgba(0, 0, 0, 0.1);
                            }
                        }
                        @media (min-width: 768px) {
                            #s202309183d6f4281c58f0 .opt-group .btn_clse {
                                background-color: ;
                            }
                            #s202309183d6f4281c58f0 .opt-group .btn_clse:after {
                                ;
                            }
                        }
            
                            .doz_sys #s202309183d6f4281c58f0 .bg-brand,
                            .doz_sys #s202309183d6f4281c58f0 .bg-brand span,
                            .doz_sys #s202309183d6f4281c58f0 .btn-brand {
                            ;
                                background-color:#00dce0;
                                border-color:#00dce0;
                                border-width: 1px;
                                color:#fff;
                            }
                            .doz_sys #s202309183d6f4281c58f0 .bg-brand:hover {
                                background-color:rgba(0,170,173,1);-ms-filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#ff00170173,endColorstr=#ff00170173);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#ff00170173,endColorstr=#ff00170173);	zoom: 1;;
                                border-color:rgb(0,170,173) ;border-color:rgba(0,170,173,1) ;;
                            }
            
                /*#*//* .widget.image img {*/
                /*	transition: .3s ease;*/
                /*}*/
                .admin #w20230918a0ab7cb212206 .widget.image img {
                    transition: none;
                }
            
                .admin #w20230918a0ab7cb212206 .disable-selection img {
                    visibility: visible !important;
                }
                #w20230918a0ab7cb212206 .widget.image .overlay, #w20230918a0ab7cb212206 .widget.image .hover_overlay {
                    background: rgba(0, 0, 0, 0);
                    transition: opacity .3s, background-color .3s;
                }
                #w20230918a0ab7cb212206 .widget.image:hover .hover_overlay {
                    background: rgba(0, 0, 0, 0);
                    z-index: 6;
                    opacity: 1;
                }
                .admin #w20230918a0ab7cb212206 .widget.image:hover .hover_overlay,
                #w20230918a0ab7cb212206 .widget.image.hover_image_hidden:hover .hover_overlay {
                    opacity: 0 !important;
                }
                #w20230918a0ab7cb212206 .widget.image.text_position_overlay .txt .txt_body {
                    color: #fff;
                    font-size:14px;;
                    line-height: 1.2;
                    padding: 1em;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_text_position_overlay:hover .hover_txt .txt_body {
                    color: #fff;
                    font-size:14px;;
                    padding: 1em;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_text_position_overlay:hover .hover_txt .txt_body {
                    line-height: 1.2;
                }
                #w20230918a0ab7cb212206 .widget.image.img_circle .overlay,
                #w20230918a0ab7cb212206 .widget.image.img_circle .hover_overlay {
                    border-radius: 50%;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_scale:hover .hover_overlay,
                #w20230918a0ab7cb212206 .widget.image.same_overlay:hover .overlay {
                    transform: scale(1.1);
                    transition: opacity .3s;
                }
                #w20230918a0ab7cb212206 .widget.image.hide_default_img:hover .img_wrap > img,
                #w20230918a0ab7cb212206 .widget.image:hover .overlay,
                #w20230918a0ab7cb212206 .widget.image .hover_overlay,
                #w20230918a0ab7cb212206 .widget.image.hover_image_hidden:hover .hover_img,
                #w20230918a0ab7cb212206 .widget.image.hover_scale .hover_img,
                #w20230918a0ab7cb212206 .widget.image.hover_scale.hover_image_hidden:hover .hover_img {
                    opacity: 0;
                }
                #w20230918a0ab7cb212206 .widget.image.hide_default_img:hover .img_wrap > img{
                    opacity: 0 !important;
            
                }
                #w20230918a0ab7cb212206 .widget.image.hover_scale img {
                    transition: transform 0.4s ease-out;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_scale img,
                #w20230918a0ab7cb212206 .widget.image.hover_scale:hover .hover_img,
                #w20230918a0ab7cb212206 .widget.image.hover_scale.hover_image_hidden:hover img,
                #w20230918a0ab7cb212206 .widget.image.org_image_hidden.hover_image_hidden:hover .img_wrap > img,
                #w20230918a0ab7cb212206 .widget.image.hover_img_hide.hover_scale:hover img,
                #w20230918a0ab7cb212206 .widget.image.same_overlay:hover .overlay  {
                    opacity : 1;
                }
                #w20230918a0ab7cb212206 .widget.image.no_effect .hover_overlay,
                #w20230918a0ab7cb212206 .widget.image.no_effect .hover_img {
                    transition: none;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_img_hide .hover_img {
                    display: none;
                }
                #w20230918a0ab7cb212206 .widget.image.hover_img_hide:hover .hover_overlay {
                    transition: opacity .3s;
                }
                #w20230918a0ab7cb212206 .widget.image.hide_default_img:hover .org_image,
                #w20230918a0ab7cb212206 .widget.image.same_overlay:hover .hover_overlay {
                    opacity: 0;
                }
                #w20230918a0ab7cb212206 .widget.image.same_overlay:hover .overlay {
                    opacity: 1;
                }
            
                    #w20230918a0ab7cb212206 .widget.image .hover_img {
                    image-rendering: -webkit-optimize-contrast;
                }
            
                @media all and (max-width : 767px) {
                    #w20230918a0ab7cb212206 .widget.image:hover .hover_txt,
                    #w20230918a0ab7cb212206 .widget.image:hover .hover_img,
                    #w20230918a0ab7cb212206 .widget.image:hover .overlay,
                    #w20230918a0ab7cb212206 .widget.image:hover .hover_overlay {
                        opacity: 0;
                        transform: none !important;
                    }
                    #w20230918a0ab7cb212206 .widget.image.org_image_hidden:hover .img_wrap > img {
                        opacity: 1;
                    }
                    #w20230918a0ab7cb212206 .widget.image:hover .txt {
                        opacity: 1;
                        visibility: visible;
                    }
                    #w20230918a0ab7cb212206 .widget.hover_scale:hover img {
                        transform: none !important;
                    }
                }
            
                /* 공통 적용 */
                #w202309186d42fd05ae820 .nav li a {
                    font-size  : 20px;
                    color : #757575;
                    letter-spacing:0px ;
                }
                #w202309186d42fd05ae820 .h-menu-type1 .use_sub_name:hover>a>.plain_name:before,
                #w202309186d42fd05ae820 .h-menu-type2 .use_sub_name:hover>a>.plain_name:before {
                   display: inline-flex;
               }
                #w202309186d42fd05ae820 .nav li.use_sub_name:hover>a>.plain_name:before {
                                       color : #000;
                                   }
                #w202309186d42fd05ae820 .nav li li a {
                                       font-size : 16px;
                                   }
                @media (min-width: 991px) {
                #w202309186d42fd05ae820 .nav li a:hover {
                    color : #000	}
                }
                    /* 타입 별 적용 */
                    /* v 타입*/
                    #w202309186d42fd05ae820 li {
                                       display: none;
                                   }
                #w202309186d42fd05ae820 li.depth-01 {
                                       display: block;
                                   }
                #w202309186d42fd05ae820 li.active > ul > li {
                                       display: block;
                                   }
                    #w202309186d42fd05ae820 .nav li li a {
                                       font-size : 14px;
                                   }
                    #w202309186d42fd05ae820 .nav li a {
                                       padding: 15px 0 15px 15px;
                                   }
                #w202309186d42fd05ae820 .nav li li a {
                                       padding: 12px 0 12px 30px;
                                   }
                #w202309186d42fd05ae820 .nav li li li a {
                                       padding: 12px 0 12px 45px;
                                   }
                        #w202309186d42fd05ae820 .nav > ul > li > a.active {
                                       background-color:#009721;
                                       color: #ffffff;
                                   }
                #w202309186d42fd05ae820 .nav  > ul > li > ul a.active{
                                       color:#009721;
                                   }
                #w202309186d42fd05ae820 .nav > ul{
                                       border-radius: 0px;
                                       border : 1px solid;
                                       border-color: #009721;
                                   }
            
            
                #w20230918f38bb09ff75c8 .list-group .addon-badge {
                    background:#FF635D;
                    color:#fff;
                    display: inline-block;
                    height:18px;
                    width:18px;
                    text-align: center;
                    vertical-align: 2px;
                    border-radius: 50%;
                    font-size:11px;
                    font-weight: bold;
                    font-family: Arial;
                    line-height: 18px;
                    font-style: normal;
                }
                #w20230918f38bb09ff75c8 .list-group .icons {
                                             padding-left: 4px;
                                         }
                #w20230918f38bb09ff75c8 .search_form_hide .tools {
                                             display: none !important;
                                         }
                @media (max-width: 767px) {
                #w20230918f38bb09ff75c8 .search_form_hide .tools {
                    display: block !important;
                }
                }
            
                .device_type_m .pc_section #padding_w20230918f8d54e7c86e9b {
                    height: 54px !important;
                }
                @media all and (max-width:768px) {
                    .pc_section #padding_w20230918f8d54e7c86e9b {
                        height: 54px !important;
                    }
                }
            
                .footer-section {
                background-color : #383838;;
                    background-color                                                               : rgba(56,56,56,1);
                color : #ffffff;;
                    color                                                                          : rgba(255,255,255,1);
                    font-size        :12px;
                ;
                 background-size : cover; background-repeat: no-repeat; background-position : ; text-align : center;
                    padding-top                                                                    : 30px;
                    padding-bottom                                                                 : 30px;
                }
            
                .doz_sys .footer-section a {
                color : #ffffff;;
                    color   : rgba(255,255,255,1) !important;
                }
                .doz_sys .footer-section .use_sub_name:hover>a>.plain_name:before {
                    color   : rgba(255,255,255,1);
                }
                .footer-section .custom-text {
                    margin-top : 5px;
                    margin-bottom: 10px;
                }
            
                .footer-section .custom-text .custom-text-info {
                    font-size        :12px;
                }
            
                .foot-main-nav {
                    font-size        :12px;
                }
            
                .foot-foot-nav {
                    font-size        :12px;
                }
            
                .foot-foot-nav .policy_menu, .foot-foot-nav .footer_menu {
                    float : left;
                }
                .footer-section .site-brand {
                    font-size        :12px;
                    margin-bottom : 0.8em;
                }
            
                .footer-section .copryright-area {
                    font-size        :12px;
                }
            
                .footer-section .nav.nav-stacked.footer-all-nav {
                    display     : inline-block;
                }
            
                .footer-section .nav.nav-stacked.footer-all-nav li {
                    float : left;
                }
            
                .footer-section .nav.nav-stacked.footer-all-nav li a {
                    padding   : 3px 7.5px;
                    font-size        :12px;
                }
            
            
                .footer-section .nav.nav-stacked.footer-all-nav li a:hover {
                    background : none;
                    opacity    : 1;
                }
            
                .nav-stacked > li + li {
                    margin-top : 0;
                }
            
                .footer-section .foot-sociallink {
                    display : inline-block;
                }
            
                .footer-section .foot-sociallink .btn-group {
                    display : block;
                }
            
                .footer-section .foot-sociallink .btn-group .btn {
                    background    : none;
                    font-size     : 20px;
                    border-radius : 0;
                    border        : none;
                    border-color: transparent;
                    padding       : 0 12px;
                }
            
                .footer-section .foot-sociallink .btn-group .btn i {
                color : #ffffff;;
                    color : rgba(255,255,255,1);
                }
                .footer-section .foot-sociallink .btn-group .btn i.icon_naver {
                    font-family: "Arial Black", "AvenirNext-Heavy";
                    transform: translateY(-1px);
                    font-style: normal;
                }
                .footer-section .foot-sociallink .btn-group .btn:hover {
                    opacity : 0.7;
                    color   : inherit;
                }
                #doz_footer .footer-section .foot-app-menu {
                    margin-top: 30px;
                    display: inline-block;
                }
                #doz_footer .footer-section .foot-app-menu > div {
                    float:left;
                    margin: 2.5px;
                }
                #doz_footer .footer-section .foot-app-menu .btn {
                    width: 195px;
                    height: 60px;
                    padding: 0 24px;
                    color:#fff;
                }
                #doz_footer .footer-section .foot-app-menu .sm-txt {
                    font-size: 11px;
                    color: #999;
                    letter-spacing: 0;
                }
                #doz_footer .footer-section .foot-app-menu .lg-txt {
                    font-size: 15px;
                    font-weight: bold;
                    letter-spacing: 0;
                    color: #fff;
                }
                @media (max-width : 992px) {
                    .foot-main-nav, .foot-foot-nav, .footer-section .foot-sociallink {
                        margin : 7px 0;
                    }
            
                    .footer-section {
                        font-size : 14px;
                    }
            
                    .footer-section .footer-wrap {
                        padding : 0;
                    }
            
                    .footer-section .foot-sociallink {
                        position : inherit;
                        order    : 4;
                    }
            
                    .footer-section .nav.nav-stacked.footer-all-nav li, .foot-foot-nav .policy_menu, .foot-foot-nav .footer_menu {
                        float   : none;
                        display : inline-block;
                    }
                }
                @media (max-width:640px) {
                    #doz_footer .footer-section .foot-app-menu {
                        display: table;
                        margin-top: 20px;
                        width: 100%;
                    }
                    #doz_footer .footer-section .foot-app-menu .btn {
                        width: 100%;
                        padding: 0 10px;
                        letter-spacing: 0;
                    }
                    #doz_footer .footer-section .foot-app-menu > div {
                        float: none;
                        margin: 0;
                        display: table-cell;
                        padding: 0 2.5px 0 0;
                        width: 50%;
                    }
                    #doz_footer .footer-section .foot-app-menu > div.apple {
                        padding: 0 0 0 2.5px;
                    }
                    #doz_footer .footer-section .foot-app-menu .lg-txt {
                        font-size:14px;
                    }
            
                }
                @media all and (min-width:320px) and (max-width:639px) {
                    #doz_footer .footer-section .foot-app-menu .btn {
                        padding: 0 8px;
                    }
                }
            </style><script src="https://www.youtube.com/iframe_api" id="youtube_player_api"></script><script type="module" async="" src="//static.imweb.me/brand-scope/bs.esm.js"></script><script src="https://vendor-cdn.imweb.me/js/jquery.js?1627517460"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery-ui.design.js?1627517437"></script>
            <script src="https://vendor-cdn.imweb.me/js/lodash.min.js?1656295899"></script>
            <script src="//unpkg.com/vue@3/dist/vue.global.prod.js"></script>
            <script src="https://vendor-cdn.imweb.me/js/axios.min.js?1689048978"></script>
            
            <script>
                var IS_IADMIN = false;
                var CUSTOM_IMAGE_WIDTH = 1600;
                var IS_MOBILE = false;
                var IS_IE = false;
                var IS_SUPPORT_CSS3 = true;
                var UPLOAD_URL = '/upload/';
                var CDN_UPLOAD_URL = 'https://cdn.imweb.me/upload/';
                var CDN_OPTIMIZED_URL= 'https://cdn-optimized.imweb.me/upload/';
                var IS_MAIN = false;
                var CURRENT_URL = 'LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D';
                var CURRENT_DOMAIN = 'xn--v42b19i81d99c.com';
                var THUMBNAIL_URL= '/thumbnail/';
                var CDN_THUMBNAIL_URL= 'https://cdn.imweb.me/thumbnail/';
                var SITE_CODE = 'S20200715a3c5f9a178ae1';
                var UNIT_CODE = 'u202007155f0edb3adaedd';
                var MAIN_DOMAIN = 'xn--v42b19i81d99c.com';
                var VENDOR_DOMAIN = 'https://vendor-cdn.imweb.me';
                var GOOGLE_API_KEY = 'AIzaSyA8CCexf9XTJcH09mStr-HRW4nin4k8J7w';
                var FROALA_VERSION = 311;
                var FROALA_KEY = '6LF5g1B3D3F3C6C3E2F-11SLJCKHXOSLMc1YGSGb1ZXHSe1CgB5A4D4C3E3C2A13A19B7B2==';
                    var IS_ANDROID_APP = 'N';
                var IS_IOS_APP = 'N';
                var APP_VERSION = '0';
                    var IS_APP = IS_ANDROID_APP == "Y" || IS_IOS_APP == "Y";
                var IE_VERSION = '11';
                var TEST_SERVER = false;
                var MENU_SNS_INIT_DATA = {"_main_url":"https:\/\/xn--v42b19i81d99c.com","_site_name":"\uc0dd\uba85\uc548\uc804\uc5f0\uad6c\uc18c","_subject":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4","_body":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4\ucc44\ub110 T.me\/Pepe_Garden\ubb38\uc758 @pepegarden\uc624\ud508\ud1a1t.me\/+D-_3LaM0RAg5OWMy\ub5a8,\ub5a8\uc561 \ub450\uac00\uc9c0\ub9cc \ucde8\uae09\ud569\ub2c8\ub2e4.\uc624\ud508\ud1a1\uacfc \ucc44\ub110 \uc6b4\uc601\uc911\uc774\uace0\ud569\ub9ac\uc801\uc778\uac00\uaca9\uc73c\ub85c \uc6b4\uc601\ud569\ub2c8\ub2e4.\ud558\uc774\ucf54\ub9ac\uc544 \uc5d0\uc11c \ubbf8\ubbf8\uc6d4\ub4dc\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc \uc804\ubd80 \uacaa\uc5b4\uc654\uc2b5\ub2c8\ub2e4.\uc624\ub798\ub41c \uacbd\ud5d8\uc73c\ub85c \ucd5c\uc0c1\uae09 \ud004\ub9ac\ud2f0\ub85c \uc548\uc804\ud558\uac8c \ub098\ub214\ud558\uaca0\ub2c8\ub2e4.#\ub5a8\ud31d\ub2c8\ub2e4#\ub5a8\ud314\uc544\uc694#\uac15\ub0a8\ub5a8#\uc6a9\uc0b0\ub5a8#\ud64d\ub300\ub5a8#\ub5a8\uc778\uc99d\ub51c\ub7ec#\ub5a8\uc0bd\ub2c8\ub2e4#\ud558\uc774\ucf54\ub9ac\uc544#\ud558\uc774\ucf54\ub9ac\uc544\ub124\uc624#\ub5a8\uc528\uc557#\ubbf8\ubbf8\uc6d4\ub4dc#\uc704\ub2c8\ud50c#\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc#\ubc84\ub4dc\ud31d\ub2c8\ub2e4#\uac04\uc790\ud31d\ub2c8\ub2e4#\ub5a8\ub4dc\ub78d#\ub5a8\uc120\ub4dc\ub78d#\uc218\uc6d0\ub5a8#\uc778\ucc9c\ub5a8#\uc81c\uc8fc\ub5a8#\ubd80\uc0b0\ub5a8#\ub300\ub9c8\ud6a8\ub2a5#\ub300\ub9c8\ud569\ubc95#\ub300\ub9c8\ucd08\ud31d\ub2c8\ub2e4#\ub300\ub9c8\ud31d\ub2c8\ub2e4#\ub5a8\ud314\uc544\uc694#\uad11\uc8fc\ub5a8#\ub5a8\uc561\ud31d\ub2c8\ub2e4#\ub5a8\uc561\ud314\uc544\uc694#\ub5a8\uc561\uc0bd\ub2c8\ub2e4#\ub5a8\uc561#\ub300\ub9c8\uc561\uc0c1#\ub300\ub9c8\uc528\uc557#\ub300\ub9c8\uc7ac\ubc30#\ub300\ub9c8\ucd08#\ub3d9\uc791\ub5a8#\uad11\uc9c4\ub5a8#\ub9c8\ud3ec\ub5a8#\ucc9c\uc548\ub5a8#\ub300\uad6c\ub5a8#\ub300\uc804\ub5a8#\uc548\uc0b0\ub5a8#\uccad\uc8fc\ub5a8#\uc81c\uc8fc\ub3c4\ub5a8#\uac15\ubd81\ub5a8#\ub17c\ud604\ub5a8#\ud074\ub7fd\ub5a8#\ub5a8\ud310\ub9e4#Thc#cbd#\ud64d\ub300\ub5a8#\ud55c\uad6d\ub525\uc6f9#\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc#\ud558\uc774\ucf54\ub9ac\uc544\ub124\uc624#\ud0d1\ucf54\ub9ac\uc544#\uac74\ub300\ub5a8#\ub5a8\uc0ac\uc694#\ub5a8\uc778\uc99d\ub51c\ub7ec#\ub5a8\ud31d\ub2c8\ub2e4#\ub5a8\uc0ac\ub294\uacf3#\ucfe0\uc26c\ud31d\ub2c8\ub2e4#\ud0dc\uad6d\ub5a8#\ubd81\ubbf8\ub5a8#\ub5a8\uc528\uc557\ubc30\uc1a1#\ub5a8\uc528\uc557\uad6d\uc81c\ud0dd\ubc30#\uc758\ub8cc\uc6a9\ub300\ub9c8#\ube14\ub8e8\ub4dc\ub9bc#\ub808\ubaac\ud5e4\uc774\uc988#\uc624\uc9c0\ucfe0\uc26c#\uc624\uc950\ucfe0\uc26c#ak47\ucfe0\uc26c#\ud654\uc774\ud2b8\uc704\ub3c4\uc6b0#\uac1c\uc778\uc7a5#\ubc95\uc778\uc7a5#\uac15\ub0a8\uc624\ud53c#\uac15\ub0a8\uc720\ud765#\ud1a0\ud1a0\ucd1d\ud310#\ubc14\uce74\ub77c\uc0ac\uc774\ud2b8#\ucd94\ucc9c\uc778\ucf54\ub4dc#\uce74\uc9c0\ub178\uc0ac\uc774\ud2b8#\uc0ac\uc124\uce74\uc9c0\ub178#\ud1a0\ud1a0\ubc30\ud305","_post_url":"https:\/\/xn--v42b19i81d99c.com\/186\/?bmode=view&idx=95396760","_img":"https:\/\/cdn.imweb.me\/thumbnail\/20240906\/73f4554761eca.jpg","_security_post_url":"aHR0cHM6Ly94bi0tdjQyYjE5aTgxZDk5Yy5jb20vMTg2Lz9ibW9kZT12aWV3JmlkeD05NTM5Njc2MA=="};
                var LIMIT_API_LIST = ["kakao_link","kakaostory_link"];
                var NO_IMAGE_URL = '/img/transparency.png';
                var SITE_COUNTRY_CODE = 'kr';
                var KOREA_COUNTRY_CODE = 'kr';
                var LANG_CODE = 'KR';
                var IS_GUEST = true;
                var MEMBER_UID = '';
                var MEMBER_HASH = '';
                var USE_OMS = true;
                var CHECK_OFFICE = false;
            
                //var LOGIN_MEMBER_DATA = {"name": "", "point": ""};
                </script><script src="https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js"></script><script src="https://player.vimeo.com/api/player.js"></script><script type="application/ld+json">{"@context":"http:\/\/schema.org","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":""},"datePublished":"2024-09-06T16:51:17+09:00","dateModified":"2024-09-06T16:51:17+09:00","headline":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4","description":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4\ucc44\ub110 T.me\/Pepe_Garden\ubb38\uc758 @pepegarden\uc624\ud508\ud1a1t.me\/+D-_3LaM0RAg5OWMy\ub5a8,\ub5a8\uc561 \ub450\uac00\uc9c0\ub9cc \ucde8\uae09\ud569\ub2c8\ub2e4.\uc624\ud508\ud1a1\uacfc \ucc44\ub110 \uc6b4\uc601... ","image":["https:\/\/cdn.imweb.me\/upload\/S20200715a3c5f9a178ae1\/75aaf517d1dca.jpg"],"author":{"@type":"Person","name":"\uc704\ucee4"},"publisher":{"@type":"Organization","name":"\uc0dd\uba85\uc548\uc804\uc5f0\uad6c\uc18c","logo":{"@type":"ImageObject","url":"https:\/\/cdn.imweb.me\/upload\/"}}}</script>    <!-- <script>
                    const dataProd = JSON.parse(document.getElementById('prod_goods_form').dataset.prod)
            
                    function addCartItem () {
                        SITE_SHOP_DETAIL.addCart();
                        return window.foShopService.addCartItem({
                            prodCode: dataProd,
                            skyCode:
                        })
                    }
                </script> -->
            
            <script type="text/javascript" async="" src="https://ssl.pstatic.net/melona/libs/gfp-nac-module/synchronizer.js"></script></head>
            <body class="doz_sys  _body_menu_m20230918fca804513d525  mobile-nav-on  mobile_nav_dep2  page  new_header_site   post_view new_fixed_header_disable fixed-menu-on" style=";" id="doz_body">
            
            
            
            <div id="site_alarm_slidemenu_container" class="notification-canvas-container">
                <div class="notification-canvas-backdrop" id="site_alarm_slidemenu_backdrop" style="display: none"></div>
                <div id="site_alarm_slidemenu" class="notification-canvas alarm-pane alarm_slide">
            
                    <div class="tse-scrollable _scroll_wrap">
                        <div class="tse-content tab-content _is_tse_content" style="padding-top: 60px;">
                            <div class="site-alarm-head _alarm_header">
                                <header id="site_alarm_title">알림</header>
                                                    <a href="javascript:;" class="btn btn-flat goback " onclick="ALARM_MENU.showAlarmSlide();"><i class="btm bt-arrow-left" aria-hidden="true"></i><span class="sr-only">뒤로</span></a>
                            </div>
                            <div class="site-alarm-head _setting_header" style="display: none">
                                <header id="site_alarm_title_setting">알림 설정</header>
                                <a href="javascript:;" class="btn btn-flat goback " onclick="ALARM_MENU.toggleAlarmSetting();"><i class="btm bt-arrow-left" aria-hidden="true"></i><span class="sr-only">뒤로</span></a>
                            </div>
                            <div id="site_alarm_list_wrap" class="site_alarm_list_wrap">
                                <!--알림 리스트-->
            
                                <div id="site_alarm_tab" class="notify-body"></div>
            
                                <div id="site_alarm_more_btn" class="notify-body" style="display: none;">
                                    <a class="tile more" href="javascript:;" onclick="ALARM_MENU.getHeaderAlarmList()">
                                        <div class="tile-content">
                                            더보기							</div>
                                    </a>
                                </div>
            
                            </div>
                            <div id="site_alarm_setting_wrap" style="display: none;" class="site_alarm_setting_wrap">
            
                                <div class="offcanvas-block alarm-setting">
                                    <div class="_scroll_wrap" id="site_alarm_menu_tap_wrap">
                                        <div class="tab-content">
                                            <div class="tab-pane active">
                                                <div class="notify-body">
                                                    <a href="javascript:;" class="board-alaram tile">게시물 알림</a>
                                                    <a class="tile" href="javascript:;" onclick="ALARM_MENU.changeAlarmSetting($(this),'','my_post')">
                                                        <div class="tile-content">
                                                            <div class="tile-text">
                                                                내 글 반응													<div class="text-sm text-gray-bright">내가 작성한 게시물이나 댓글에 다른 사람이 댓글이나 답글을 작성하면 알려줍니다.</div>
                                                                <div class="check ">
                                                                    <div class="checkbox checkbox-styled">
                                                                        <label>
                                                                            <input title="내 글 반응" type="checkbox" value="ok"><span></span>
                                                                        </label>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </a>
                                                    <a class="tile" href="javascript:;" onclick="ALARM_MENU.changeAlarmSetting($(this),'','notice')">
                                                        <div class="tile-content">
                                                            <div class="tile-text">
                                                                공지사항													<div class="text-sm text-gray-bright">사이트에서 보내는 중요한 공지를 실시간으로 알려줍니다.</div>
                                                                <div class="check">
                                                                    <div class="checkbox checkbox-styled">
                                                                        <label>
                                                                            <input title="공지사항" type="checkbox" value="ok"><span></span>
                                                                        </label>
                                                                    </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </a>
                                                                                        </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
            
                        </div>
                    </div>
                    <div class="site-alarm-body">
            
                        <!--//알림 리스트-->
                        <!--알림 설정-->
            
                    </div>
                </div>
            </div>
            <!-- end#offcanvas-help --><ul class="dropdown-menu animation-dock member_profile" id="member_profile">
                <li class="dropdown-profile text-center">
                    <a href="javascript:;" class="nav-btn-icon profile alarm-toggle _show_alarm" onclick="ALARM_MENU.showAlarmSlide();" id="slide-alarm" style="right: 0; position:absolute; right: 0; top:0; font-size:20px; padding:20px; "><i class="icon-bell"></i><span class="sr-only">Alarm</span></a>
                    <span class="profile-info">
                        <div onclick="SITE_MEMBER.editProfile()">
                            <img src="/common/img/default_profile.png" class="img-circle dropdown-avatar-big _profile_img" alt="프로필 이미지">
                        </div>
                        <div class="sm-padding no-padding-bottom">
                                                    </div>
                                </span>
                </li>
                <li class="profile-footer btn-group-justified">
                    <a href="javascript:;" onclick="SITE_MEMBER.openLogin('L3Nob3BfbXlwYWdl','mypage');" class="btn btn-flat">마이페이지</a>
                            <a href="/logout.cm?back_url=LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D" class="btn btn-flat right">로그아웃</a>
                </li>
            </ul><div id="mobile_slide_menu_wrap" class="mobile_slide_menu_container">
                <div id="mobile_slide_menu" class="mobile_slide_menu slide_menu _slide_menu">
                    <ul class="nav navbar-nav navbar-right">
            
                        <div class="viewport-nav mobile _menu_wrap " style="position:relative">
                            <!-- 모바일 메뉴서랍내 프로필 -->
                            <input type="hidden" value="/common/img/app_login.png" id="imagepath">						<div class="profile-area">
                                        <a href="javascript:;" onclick="SITE_MEMBER.openLogin('LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D', 'null', null, 'Y');" class="btn nav-btn-icon profile no-padding btn-flat full-width">
                                            <div class="member-info guest full-width">
                                                <span>로그인이 필요합니다.</span>
                                                <button>로그인</button>
                                            </div>
                                        </a>
                                        <div class="btn-group">
            
                                        </div>
                                    </div>
            
            
            
                                    <li style="" class="depth-01  " data-code="m202007153a95dcf3ec499">
                                        <a href="/index" data-url="index" data-has_child="Y" data-is_folder_menu="N" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">생명안전연구소</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="1" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m2020111603a1025a4e5e1">
                                                <a tabindex="-1" data-url="110" data-has_child="N" data-is_folder_menu="N" href="/110" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">회사소개</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202010096d3ef24ed6db0">
                                                <a tabindex="-1" data-url="73" data-has_child="N" data-is_folder_menu="N" href="/73" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">파트너</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20230817fc13f57c5b9d4">
                                                <a tabindex="-1" data-url="184" data-has_child="N" data-is_folder_menu="N" href="/184" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">조직도 및 업무분장</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202309184d258bbf730df">
                                                <a tabindex="-1" data-url="185" data-has_child="N" data-is_folder_menu="N" href="/185" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">보유장비</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m202301087c08bf593a4f2">
                                        <a href="/152" data-url="152" data-has_child="Y" data-is_folder_menu="Y" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">재해예방기술지도</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="6" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m2023060712c08010b9ac4">
                                                <a tabindex="-1" data-url="156" data-has_child="N" data-is_folder_menu="N" href="/156" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">재해예방기술지도 법적 근거</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m2023060752245f81c8aba">
                                                <a tabindex="-1" data-url="157" data-has_child="N" data-is_folder_menu="N" href="/157" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">재해예방기술지도 업무 절차</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202306075c25617c52d9e">
                                                <a tabindex="-1" data-url="158" data-has_child="N" data-is_folder_menu="N" href="/158" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">발주자 건축주의 건설현장  안전확보 프로세스</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20201008028950bdedb06">
                                        <a href="/51" data-url="51" data-has_child="Y" data-is_folder_menu="N" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">위험성평가</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="10" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m20201008fa5194f00c596">
                                                <a tabindex="-1" data-url="52" data-has_child="Y" data-is_folder_menu="N" href="/52" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">위험성평가</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="11" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20201129305965257c7fa">
                                                    <a tabindex="-1" data-url="123" data-has_child="N" data-is_folder_menu="N" href="/123" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">위험성평가 개요 및 절차</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20230607589080ca5550b">
                                                    <a tabindex="-1" data-url="171" data-has_child="N" data-is_folder_menu="N" href="/171" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">위험성평가 실시주체</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m202306074c8ed3e036d93">
                                                    <a tabindex="-1" data-url="172" data-has_child="N" data-is_folder_menu="N" href="/172" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">위험성평가 실시시기</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220625d82c1325c2f8d">
                                                    <a tabindex="-1" data-url="134" data-has_child="N" data-is_folder_menu="N" href="/134" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">위험성평가 인정심사 신청대상 및 혜택</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m202206260610058766310">
                                                    <a tabindex="-1" data-url="151" data-has_child="N" data-is_folder_menu="N" href="/151" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">교육시설위험성평가</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626083313f0562a2">
                                                    <a tabindex="-1" data-url="143" data-has_child="N" data-is_folder_menu="N" href="/143" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건설공사 위험성평가의 절차</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20201009739c7a5ab0768">
                                                <a tabindex="-1" data-url="83" data-has_child="Y" data-is_folder_menu="Y" href="/83" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">공종별 위험성평가</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="18" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m202206267350424c10e05">
                                                    <a tabindex="-1" data-url="141" data-has_child="N" data-is_folder_menu="N" href="/141" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건설공사 기초파일작업 유해위험요인 </span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626cfc0e1350450a">
                                                    <a tabindex="-1" data-url="142" data-has_child="N" data-is_folder_menu="N" href="/142" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건설공사 굴착작업 유해위험요인</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20201129942917f599a23">
                                                <a tabindex="-1" data-url="119" data-has_child="Y" data-is_folder_menu="N" href="/119" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">안전관리 수준평가</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="21" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m2020112973c19d66b1e49">
                                                    <a tabindex="-1" data-url="120" data-has_child="N" data-is_folder_menu="N" href="/120" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">안전관리 수준평가란?</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m202011291f4f3f9fb1c89">
                                                    <a tabindex="-1" data-url="121" data-has_child="N" data-is_folder_menu="N" href="/121" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">안전관리 수준평가의 대상</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2020112949e059c86c20a">
                                                    <a tabindex="-1" data-url="122" data-has_child="N" data-is_folder_menu="N" href="/122" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">안전관리 수준평가 업무처리흐름도</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626760e2e3ec6965">
                                                    <a tabindex="-1" data-url="138" data-has_child="N" data-is_folder_menu="N" href="/138" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">안전관리 수준평가 결과 공개</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20200715c98907fb8a5d2">
                                        <a href="/menu2" data-url="menu2" data-has_child="Y" data-is_folder_menu="N" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">안전보건대장 등</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="26" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m202009110323e79db0990">
                                                <a tabindex="-1" data-url="28" data-has_child="Y" data-is_folder_menu="N" href="/28" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">안전보건대장</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="27" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m2020111771cb19cac79f1">
                                                    <a tabindex="-1" data-url="118" data-has_child="Y" data-is_folder_menu="N" href="/118" class="has_child" onclick="">
                                                        <span class="plain_name" data-hover="">기본안전보건대장</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                <ul data-index="28" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20220605c849ac0588a54">
                                                    <a tabindex="-1" data-url="126" data-has_child="N" data-is_folder_menu="N" href="/126" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">기본안전보건대장 실제 작성 사례 </span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2022060658c8c7f92bb57">
                                                    <a tabindex="-1" data-url="128" data-has_child="N" data-is_folder_menu="N" href="/128" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">기본안전보건대장 실제 작성 1</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220606191d02cc97445">
                                                    <a tabindex="-1" data-url="129" data-has_child="N" data-is_folder_menu="N" href="/129" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">기본안전보건대장 실제 작성2</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20201012c7f7e4d5b18e0">
                                                    <a tabindex="-1" data-url="106" data-has_child="Y" data-is_folder_menu="N" href="/106" class="has_child" onclick="">
                                                        <span class="plain_name" data-hover="">설계안전보건대장</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                <ul data-index="32" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m2022060717de90aa9340e">
                                                    <a tabindex="-1" data-url="130" data-has_child="N" data-is_folder_menu="N" href="/130" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">설계안전보건대장 실제작성1</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220607aa547ef85fad2">
                                                    <a tabindex="-1" data-url="131" data-has_child="N" data-is_folder_menu="N" href="/131" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">설계안전보건대장 실제 작성 2</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2020101200b3716cb8e49">
                                                    <a tabindex="-1" data-url="107" data-has_child="Y" data-is_folder_menu="N" href="/107" class="has_child" onclick="">
                                                        <span class="plain_name" data-hover="">공사안전보건대장</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                <ul data-index="35" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20220612f62b75c2fb7c3">
                                                    <a tabindex="-1" data-url="132" data-has_child="N" data-is_folder_menu="N" href="/132" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">공사안전보건대장 실제 작성 1</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20201008bf7b25a8b3902">
                                                <a tabindex="-1" data-url="53" data-has_child="Y" data-is_folder_menu="N" href="/53" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">설계안전성검토</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="37" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m202010087c32af4760374">
                                                    <a tabindex="-1" data-url="54" data-has_child="N" data-is_folder_menu="N" href="/54" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">DFS 개요</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202010083ecddc475460d">
                                                <a tabindex="-1" data-url="46" data-has_child="Y" data-is_folder_menu="N" href="/46" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">유해위험방지계획서</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="39" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20201018f49f4c5447b1b">
                                                    <a tabindex="-1" data-url="108" data-has_child="N" data-is_folder_menu="N" href="/108" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">제출기한 및 서류</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20201018cddface657596">
                                                    <a tabindex="-1" data-url="109" data-has_child="N" data-is_folder_menu="N" href="/109" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">심사 및 절차</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20201203ab388be0c66fb">
                                                <a tabindex="-1" data-url="124" data-has_child="N" data-is_folder_menu="N" href="/124" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">건축물관리계획서</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m2020100993bd262cb1acf">
                                                <a tabindex="-1" data-url="74" data-has_child="Y" data-is_folder_menu="N" href="/74" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">안전관리계획서</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="43" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20201009268d602236ffc">
                                                    <a tabindex="-1" data-url="79" data-has_child="N" data-is_folder_menu="N" href="/79" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">목적 및 제출시기</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2020111761e92fe61b47d">
                                                    <a tabindex="-1" data-url="113" data-has_child="N" data-is_folder_menu="N" href="/113" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">프로세스</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2022062562d4d950666bd">
                                                    <a tabindex="-1" data-url="133" data-has_child="N" data-is_folder_menu="N" href="/133" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">안전관리계획서 수립기준</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626c39271ea72e47">
                                                    <a tabindex="-1" data-url="150" data-has_child="N" data-is_folder_menu="N" href="/150" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">소규모안전관리계획서</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20201008571c986518bab">
                                                <a tabindex="-1" data-url="49" data-has_child="Y" data-is_folder_menu="N" href="/49" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">안전보건개선계획서</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="48" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m202010083c76824b39dd7">
                                                    <a tabindex="-1" data-url="50" data-has_child="N" data-is_folder_menu="N" href="/50" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">개요</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20220626ca344ca973638">
                                                <a tabindex="-1" data-url="144" data-has_child="Y" data-is_folder_menu="N" href="/144" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">해체계획서</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="50" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20220626c0308f49283d3">
                                                    <a tabindex="-1" data-url="145" data-has_child="N" data-is_folder_menu="N" href="/145" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">해체계획서의 중요성</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m202206262ae4caa7b9f30">
                                                    <a tabindex="-1" data-url="146" data-has_child="N" data-is_folder_menu="N" href="/146" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건축물 해체공사 착공신고제 도입</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m202206261ae732304d725">
                                                    <a tabindex="-1" data-url="147" data-has_child="N" data-is_folder_menu="N" href="/147" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건축물 해체공사 안전강화방안</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626eb90850d56006">
                                                    <a tabindex="-1" data-url="148" data-has_child="N" data-is_folder_menu="N" href="/148" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">해체공사 붕괴사고 조사보고서</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20220626b135562ddd2ea">
                                                    <a tabindex="-1" data-url="149" data-has_child="N" data-is_folder_menu="N" href="/149" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">건축물 해체계획서의 작성 및 감리업무 등에 관한 기준</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20230607be042518d1092">
                                        <a href="/161" data-url="161" data-has_child="Y" data-is_folder_menu="Y" class="active   open has_child" onclick="">
                                            <span class="plain_name" data-hover="">중대재해처벌법</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="56" class="in" style="display: block;">
            
                                            <li class="depth-02  " style="" data-code="m20230607825da55b762d7">
                                                <a tabindex="-1" data-url="162" data-has_child="N" data-is_folder_menu="N" href="/162" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">주요내용</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20230607963f2782ecd29">
                                                <a tabindex="-1" data-url="163" data-has_child="N" data-is_folder_menu="N" href="/163" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">정의 및 적용대상</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20230607e5ab8e80c5243">
                                                <a tabindex="-1" data-url="165" data-has_child="N" data-is_folder_menu="N" href="/165" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">경영책임자의 안전 및 보건 확보 의무</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202306079883115cf5318">
                                                <a tabindex="-1" data-url="164" data-has_child="N" data-is_folder_menu="N" href="/164" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">벌칙규정</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20230918fca804513d525">
                                                <a tabindex="-1" data-url="186" data-has_child="N" data-is_folder_menu="N" href="/186" class=" active   active-real " onclick="">
                                                    <span class="plain_name" data-hover="">중대재해사례</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20220625cf513fbd2f810">
                                        <a href="/135" data-url="135" data-has_child="Y" data-is_folder_menu="Y" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">안전보건관리체계</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="62" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m202101063dc79a99589f7">
                                                <a tabindex="-1" data-url="125" data-has_child="N" data-is_folder_menu="N" href="/125" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">안전보건관리체계(중대재해처벌법)</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202206259fb15431fd8ab">
                                                <a tabindex="-1" data-url="136" data-has_child="N" data-is_folder_menu="N" href="/136" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">안전보건계획 이사회 보고 및 승인</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20220625e458b94d69600">
                                                <a tabindex="-1" data-url="137" data-has_child="N" data-is_folder_menu="N" href="/137" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">회사의 안전보건계획 수립과 10대 건설사 안전임원 간담회</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20200715eb5a7908604cd">
                                        <a href="/menu3" data-url="menu3" data-has_child="Y" data-is_folder_menu="Y" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">건설안전보건교육</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="66" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m20201009ab6052f55f07a">
                                                <a tabindex="-1" data-url="68" data-has_child="N" data-is_folder_menu="N" href="/68" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">건설안전보건교육</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202010096284ec0c569fa">
                                                <a tabindex="-1" data-url="81" data-has_child="N" data-is_folder_menu="N" href="/81" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">관리감독자교육</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202010091a1833532994c">
                                                <a tabindex="-1" data-url="78" data-has_child="N" data-is_folder_menu="N" href="/78" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">특별안전보건교육</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m20201009e4e08d6495ffb">
                                        <a href="/80" data-url="80" data-has_child="Y" data-is_folder_menu="Y" class="has_child" onclick="">
                                            <span class="plain_name" data-hover="">자료실</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                        <ul data-index="70" style="height: 0px;">
            
                                            <li class="depth-02  " style="" data-code="m202010097da87b41cefc4">
                                                <a tabindex="-1" data-url="77" data-has_child="Y" data-is_folder_menu="N" href="/77" class="has_child" onclick="">
                                                    <span class="plain_name" data-hover="">관련 법규 </span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                                <ul data-index="71" style="height: 0px;">
            
                                                    <li class="depth-03  " style="" data-code="m20230607a61946d0ec928">
                                                    <a tabindex="-1" data-url="166" data-has_child="N" data-is_folder_menu="N" href="/166" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">산업안전보건법</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20230607a6ad8a09bcabb">
                                                    <a tabindex="-1" data-url="167" data-has_child="N" data-is_folder_menu="N" href="/167" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">산업안전보건법 시행령</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m2023060750300ea89e735">
                                                    <a tabindex="-1" data-url="168" data-has_child="N" data-is_folder_menu="N" href="/168" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">산업안전보건법 시행규칙</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20230607eaf15ee939cf4">
                                                    <a tabindex="-1" data-url="169" data-has_child="N" data-is_folder_menu="N" href="/169" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">산업안전보건기준에 관한규칙</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                    <li class="depth-03  " style="" data-code="m20230607c3dc5f752bd0a">
                                                    <a tabindex="-1" data-url="170" data-has_child="N" data-is_folder_menu="N" href="/170" class=" " onclick="">
                                                        <span class="plain_name" data-hover="">사업장 위험성평가에 관한 지침</span>
                                                        <span class="_toggle_btn toggle-btn"></span>
                                                    </a>
            
                                                    </li>
            
                                                </ul>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202306128a9a641eca1ff">
                                                <a tabindex="-1" data-url="177" data-has_child="N" data-is_folder_menu="N" href="/177" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">법규 개정</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m202306123bac3348334b0">
                                                <a tabindex="-1" data-url="178" data-has_child="N" data-is_folder_menu="N" href="/178" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">안전보건자료실</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m2020100903ca9f8c40fe0">
                                                <a tabindex="-1" data-url="84" data-has_child="N" data-is_folder_menu="N" href="/84" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">사고사례</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                            <li class="depth-02  " style="" data-code="m20230607048fd6c76623a">
                                                <a tabindex="-1" data-url="175" data-has_child="N" data-is_folder_menu="N" href="/175" class=" " onclick="">
                                                    <span class="plain_name" data-hover="">안전소식</span>
                                                    <span class="_toggle_btn toggle-btn"></span>
                                                </a>
            
                                            </li>
            
                                        </ul>
            
                                    </li>
            
                                    <li style="" class="depth-01  " data-code="m202010099f7d1fb8f299e">
                                        <a href="/67" data-url="67" data-has_child="N" data-is_folder_menu="N" class=" " onclick="">
                                            <span class="plain_name" data-hover="">고객센터</span>
                                            <span class="_toggle_btn toggle-btn"></span>
                                        </a>
            
                                    </li>
            
                                            </div>
                    </ul>
                    <div class="im-mobile-slide-footer">
                                            </div>
                </div>
                <button type="button" class="navbar-toggle close slide-close" onclick="MOBILE_SLIDE_MENU.slideNavToggle();"><i class="btm bt-times" aria-hidden="true"></i><span class="sr-only">닫기</span></button>
            
                <style>
                    .new_header_site .mobile_slide_menu_container.slide_open .mobile_slide_menu,
                    .new_header_site .mobile_slide_menu_container .mobile_slide_menu,
                    .admin.new_header_mode .mobile_slide_menu_container.slide_open .mobile_slide_menu,
                    .admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu {
                        background: #fff !important;
                    }
                    .new_header_site .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul,
                    .admin.new_header_mode .mobile_slide_menu_container .mobile_slide_menu .viewport-nav.mobile li li ul {
                        background: transparent;
                    }
                    .mobile_slide_menu_container .mobile_slide_menu .profile-area {
                        background: #2b2b2b;
                        margin-bottom:0 ;
                    }
                    .mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info,
                    .mobile_slide_menu_container .mobile_slide_menu .profile-area .btn-group,
                    .mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
                        color: #fff;
                    }
                    .mobile_slide_menu_container .mobile_slide_menu .profile-area .member-info.guest button {
                            border-color:rgb(255,255,255) ;border-color:rgba(255,255,255,0.2) ;		}
                    .mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open > span,
                    .mobile_slide_menu_container .viewport-nav.mobile li li a.has_child.open:after,
                    .mobile_slide_menu_container .viewport-nav.mobile li li a span {
                        color: rgba(33, 33, 33, 0.89);
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li a {
                        color: rgba(33, 33, 33, 0.89);
                        letter-spacing: 0px;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li.use_sub_name:hover>a:not(.active)>.plain_name:before {
                        color: rgba(33, 33, 33, 0.89);
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name {
                        color: transparent;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li li.use_sub_name:hover>a:not(.active)>.plain_name:before {
                        position: absolute;
                        color: rgba(33, 33, 33, 0.89);
                        left: auto;
                        right: auto;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li a.active-real {
                        background: #f5f5f5;
                        color: #111;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li a.active-real span,
                    .mobile_slide_menu_container .viewport-nav.mobile li a.has_child.open.active-real span {
                        color: #111;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li.depth-01 {
                        border-top: 1px solid #f3f3f3;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li.depth-01:last-child {
                        border-bottom: 1px solid #f3f3f3;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li.depth-01 ul{
                        display : none; 		}
                    .mobile_slide_menu_container .viewport-nav.mobile li.depth-01 > a {
                        font-size: 14px;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li li a {
                        font-size: 13px !important;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li li:last-child a,
                    .mobile_slide_menu_container .viewport-nav.mobile li li li:last-child a,
                    .mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse,
                    .mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse,
                    .mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=false],
                    .mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=false] {
                        margin-bottom : 0;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li > ul,
                    .mobile_slide_menu_container .viewport-nav.mobile li li > ul,
                    .mobile_slide_menu_container .viewport-nav.mobile li > ul.collapse.in,
                    .mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapse.in,
                    .mobile_slide_menu_container .viewport-nav.mobile li > ul.collapsing[aria-expanded=true],
                    .mobile_slide_menu_container .viewport-nav.mobile li li > ul.collapsing[aria-expanded=true] {
                        margin-bottom: 14px;
                    }
                    .mobile_slide_menu_container .viewport-nav.mobile li li li:first-child a {
                        margin-top: 0;
                    }
                            .viewport-nav.mobile li a.has_child > .toggle-btn:after {
                                        font-size: 13.3px;
                                }
                    .viewport-nav.mobile li li a.has_child > .toggle-btn:after {
                                        font-size: 12.35px;
                                }
                    .navbar-nav .profile-more.open .dropdown-menu li > a {
                        background: transparent;
                        color: #212121;
                        padding: 8px 16px;
                    }
                                    .im-globe .globe_icon {
                        display: inline-block;
                    }
                    .im-globe .globe_square,
                    .im-globe .globe_circle {
                        display: none !important;
                    }
                            .im-mobile-slide-footer {
                        background: #fff;
                        color: rgba(33, 33, 33, 0.89);
                    }
                    .im-mobile-slide-footer .btn {
                        color: rgba(33, 33, 33, 0.89);
                    }
                </style>
            </div><header id="doz_header_wrap"><div id="doz_header" data-newheader="Y"><div class="new_org_header _new_org_header"><div id="inline_header_normal" style="min-height: 30px;" class="first_scroll_fixed">	<div data-type="section-wrap" class="inline-section-wrap fixed_transform _fixed_header_section" id="s202010059784a742cc092"><div class="section_bg _section_bg fixed_transform _interactive_bg  "></div><div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#ffffff;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div><div data-type="inside" class="inline-inside _inline-inside"><div data-type="section" class="inline-section" section-code="s202010059784a742cc092"><div data-type="col-group" data-col-group="left" class="inline-col-group inline-col-group-left" style="width:225px;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w2020100507117ad06f801" class="inline-widget"><div class="_widget_data" data-widget-type="inline_global_btn"><div class="unfolding_mode inline-blocked " style="margin:0 2.5px; "><a href="/?redirect=no" class="_global_link_KR"><img src="/common/img/flag_shapes/flag_kr_square.png?12412413" width="24px" style="border: 1px solid rgba(128,128,128,0.2)" alt=""><span class="sr-only">언어 변경</span></a></div><div class="dropdown inline-blocked global-dropdown _show_global inline_global_dropdown ">
                <div class="widget inline_widget">
                        </div>
                <ul class="dropdown-menu" style="min-width:150px; width:auto;">
                    <li class="dropdown-submenu"><a href="/?redirect=no" class="dropdown-toggle _global_link_KR"><span>한국어</span></a></li>	</ul>
            </div>
            
            </div></div></div></div><div data-type="col-group" data-col-group="right" class="inline-col-group inline-col-group-right" style="width:1025px;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w202010057a9ed5ea188ec" class="inline-widget"><div class="_widget_data" data-widget-type="inline_login_btn">	<div class="widget inline_widget login_btn button   txt_l text-xx-small">
                            <div></div>					</div>
            
            
            
            
            
            </div></div></div><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201116664ca316c9038" class="inline-widget"><div class="_widget_data" data-widget-type="inline_login_btn">	<div class="widget inline_widget login_btn button  button_text txt_l text-xx-small">
                            <div><div class="inline-blocked login_btn_item "><a class="_fade_link   btn_text btn_53S2M1CK30   btn_custom " href="javascript:;" onclick="SITE_MEMBER.openLogin('LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D', 'null', null, 'Y');" style="border-radius:0px; "><span class="sr-only">로그인 위젯 문구</span><span class="icon_class "><i class="fixed_transform simple icon-login" aria-hidden="true"></i></span><span class="text fixed_transform no_text"></span></a></div><div class="inline-blocked login_btn_item "><a class="_fade_link   btn_text btn_472216c85c500   btn_custom " href="javascript:;" onclick="SITE_MEMBER.openJoinPatternChoice('LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D', '');" style="border-radius:0px; "><span class="sr-only">로그인 위젯 문구</span><span class="icon_class "><i class="fixed_transform simple icon-user" aria-hidden="true"></i></span><span class="text fixed_transform no_text"></span></a></div></div>					</div>
            
            
            
            
            
            </div></div></div><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005e715bc7616745" class="inline-widget"><div class="_widget_data" data-widget-type="inline_search_btn">
            
            <div class="widget inline_widget search_btn">
                <div class="search_type fixed_transform search_btn_type06">
                    <div class="inline-blocked holder">
                        <form class=" icon_on" action="/search" method="get" id="inline_s_form_w20201005e715bc7616745">
                            <input class="search_btn_form" name="keyword" style="display: " placeholder="Search" value="" title="검색"><a class="fixed_transform " href="#" onclick="SITE_SEARCH.inlineSearch('w20201005e715bc7616745');"><i class="simple icon-magnifier"></i><span class="sr-only">site search</span></a>			<ul id="image_list" style="display: none"></ul></form>
                    </div>
                </div>
            </div>
            
            
            
            
            
            
            </div></div></div><div data-type="grid" class="inline-col"><div data-type="widget" id="w2020100593e1d0b9309b8" class="inline-widget"><div class="_widget_data" data-widget-type="inline_hr">
            <div class="widget inline_widget line vertical_line " style="margin:px 0">
                <hr class="fixed_transform" style="display:none; width:25px; border-top:1px solid rgba(0, 0, 0, 0.1); ">
                <div class="full-width" style="display:inline-block;">
                    <div class="vertical-middle fixed_transform real_line"></div>
                </div>
            </div>
            
            </div></div></div><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005c70a70dc73d1d" class="inline-widget"><div class="_widget_data" data-widget-type="inline_icon"><div class="widget inline_widget icon  no_bg">
                <a class="inline-blocked fixed_transform _fade_link " href="https://blog.naver.com/safety3423" target="_blank">	<i aria-hidden="true" class="fixed_transform ii ii-nblog " style="color: #16d426;font-size: 40px;padding: 0px;display: inline-block;line-height:1;  "></i>
                <span class="sr-only">icon</span></a></div>
            </div></div></div></div></div></div>
                        </div><div></div><div data-type="section-wrap" class="inline-section-wrap fixed_transform _fixed_header_section" id="s20201005a79c3af52564c"><div class="section_bg _section_bg fixed_transform _interactive_bg  "></div><div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#fff;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div><div data-type="inside" class="inline-inside _inline-inside"><div data-type="section" class="inline-section" section-code="s20201005a79c3af52564c"><div data-type="col-group" data-col-group="left" class="inline-col-group inline-col-group-left" style="width:167px;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005a5f513e27edff" class="inline-widget"><div class="_widget_data" data-widget-type="inline_logo">
            <div class="widget inline_widget logo  text_inline" id="logo_w20201005a5f513e27edff">
                        <div class="img_box _img_box" style="position: relative;">
                        <a class="" href="/"><span class="sr-only">사이트 로고</span>			<img class="normal_logo _front_img" src="https://cdn.imweb.me/thumbnail/20230109/c11d7f570889f.jpg" alt="생명안전연구소" width="166.75" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;">
                        <img class="scroll_logo fixed_transform" src="https://cdn.imweb.me/thumbnail/20230109/c11d7f570889f.jpg" alt="생명안전연구소" width="166.75" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;">
                        </a>
                    </div>
                    </div>
            
            </div></div></div></div><div data-type="col-group" data-col-group="right" class="inline-col-group inline-col-group-right" style="width: 1083px; visibility: visible;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005d27fe010e40db" class="inline-widget"><div class="_widget_data" data-widget-type="inline_menu">	<ul class="nav navbar-nav _inline_menu_container " style="visibility: visible;">
                    <div class="viewport-nav desktop _main_menu"><li class="dropdown _show_m202007153a95dcf3ec499" style="" id="dropdown_m202007153a95dcf3ec499" data-code="m202007153a95dcf3ec499">
                            <a href="/index" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="index" data-toggle="dropdown">
                                <span class="_txt_m202007153a95dcf3ec499 plain_name" data-hover="">생명안전연구소</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m2020111603a1025a4e5e1   " data-code="m2020111603a1025a4e5e1" style="">
                                    <a tabindex="-1" href="/110" data-url="110" class="_txt_m2020111603a1025a4e5e1   _fade_link "><span class="plain_name" data-hover="">회사소개</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010096d3ef24ed6db0   " data-code="m202010096d3ef24ed6db0" style="">
                                    <a tabindex="-1" href="/73" data-url="73" class="_txt_m202010096d3ef24ed6db0   _fade_link "><span class="plain_name" data-hover="">파트너</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230817fc13f57c5b9d4   " data-code="m20230817fc13f57c5b9d4" style="">
                                    <a tabindex="-1" href="/184" data-url="184" class="_txt_m20230817fc13f57c5b9d4   _fade_link "><span class="plain_name" data-hover="">조직도 및 업무분장</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202309184d258bbf730df   " data-code="m202309184d258bbf730df" style="">
                                    <a tabindex="-1" href="/185" data-url="185" class="_txt_m202309184d258bbf730df   _fade_link "><span class="plain_name" data-hover="">보유장비</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _show_m202301087c08bf593a4f2" style="" id="dropdown_m202301087c08bf593a4f2" data-code="m202301087c08bf593a4f2">
                            <a href="/152" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="152" data-toggle="dropdown">
                                <span class="_txt_m202301087c08bf593a4f2 plain_name" data-hover="">재해예방기술지도</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m2023060712c08010b9ac4   " data-code="m2023060712c08010b9ac4" style="">
                                    <a tabindex="-1" href="/156" data-url="156" class="_txt_m2023060712c08010b9ac4   _fade_link "><span class="plain_name" data-hover="">재해예방기술지도 법적 근거</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2023060752245f81c8aba   " data-code="m2023060752245f81c8aba" style="">
                                    <a tabindex="-1" href="/157" data-url="157" class="_txt_m2023060752245f81c8aba   _fade_link "><span class="plain_name" data-hover="">재해예방기술지도 업무 절차</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306075c25617c52d9e   " data-code="m202306075c25617c52d9e" style="">
                                    <a tabindex="-1" href="/158" data-url="158" class="_txt_m202306075c25617c52d9e   _fade_link "><span class="plain_name" data-hover="">발주자 건축주의 건설현장  안전확보 프로세스</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _show_m20201008028950bdedb06" style="" id="dropdown_m20201008028950bdedb06" data-code="m20201008028950bdedb06">
                            <a href="/51" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="51" data-toggle="dropdown">
                                <span class="_txt_m20201008028950bdedb06 plain_name" data-hover="">위험성평가</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m20201008fa5194f00c596    sub-active" data-code="m20201008fa5194f00c596" style="">
                                    <a tabindex="-1" href="/52" data-url="52" class="_txt_m20201008fa5194f00c596   _fade_link "><span class="plain_name" data-hover="">위험성평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201129305965257c7fa dropdown-submenu   " data-code="m20201129305965257c7fa" style="">
                                         <a tabindex="-1" href="/123" data-url="123" class="_txt_m20201129305965257c7fa   _fade_link "><span class="plain_name" data-hover="">위험성평가 개요 및 절차</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607589080ca5550b dropdown-submenu   " data-code="m20230607589080ca5550b" style="">
                                         <a tabindex="-1" href="/171" data-url="171" class="_txt_m20230607589080ca5550b   _fade_link "><span class="plain_name" data-hover="">위험성평가 실시주체</span></a>
            
                                         </li>
            
                                        <li class="_show_m202306074c8ed3e036d93 dropdown-submenu   " data-code="m202306074c8ed3e036d93" style="">
                                         <a tabindex="-1" href="/172" data-url="172" class="_txt_m202306074c8ed3e036d93   _fade_link "><span class="plain_name" data-hover="">위험성평가 실시시기</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220625d82c1325c2f8d dropdown-submenu   " data-code="m20220625d82c1325c2f8d" style="">
                                         <a tabindex="-1" href="/134" data-url="134" class="_txt_m20220625d82c1325c2f8d   _fade_link "><span class="plain_name" data-hover="">위험성평가 인정심사 신청대상 및 혜택</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206260610058766310 dropdown-submenu   " data-code="m202206260610058766310" style="">
                                         <a tabindex="-1" href="/151" data-url="151" class="_txt_m202206260610058766310   _fade_link "><span class="plain_name" data-hover="">교육시설위험성평가</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626083313f0562a2 dropdown-submenu   " data-code="m20220626083313f0562a2" style="">
                                         <a tabindex="-1" href="/143" data-url="143" class="_txt_m20220626083313f0562a2   _fade_link "><span class="plain_name" data-hover="">건설공사 위험성평가의 절차</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201009739c7a5ab0768    sub-active" data-code="m20201009739c7a5ab0768" style="">
                                    <a tabindex="-1" href="/83" data-url="83" class="_txt_m20201009739c7a5ab0768   _fade_link "><span class="plain_name" data-hover="">공종별 위험성평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202206267350424c10e05 dropdown-submenu   " data-code="m202206267350424c10e05" style="">
                                         <a tabindex="-1" href="/141" data-url="141" class="_txt_m202206267350424c10e05   _fade_link "><span class="plain_name" data-hover="">건설공사 기초파일작업 유해위험요인 </span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626cfc0e1350450a dropdown-submenu   " data-code="m20220626cfc0e1350450a" style="">
                                         <a tabindex="-1" href="/142" data-url="142" class="_txt_m20220626cfc0e1350450a   _fade_link "><span class="plain_name" data-hover="">건설공사 굴착작업 유해위험요인</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201129942917f599a23    sub-active" data-code="m20201129942917f599a23" style="">
                                    <a tabindex="-1" href="/119" data-url="119" class="_txt_m20201129942917f599a23   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2020112973c19d66b1e49 dropdown-submenu   " data-code="m2020112973c19d66b1e49" style="">
                                         <a tabindex="-1" href="/120" data-url="120" class="_txt_m2020112973c19d66b1e49   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가란?</span></a>
            
                                         </li>
            
                                        <li class="_show_m202011291f4f3f9fb1c89 dropdown-submenu   " data-code="m202011291f4f3f9fb1c89" style="">
                                         <a tabindex="-1" href="/121" data-url="121" class="_txt_m202011291f4f3f9fb1c89   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가의 대상</span></a>
            
                                         </li>
            
                                        <li class="_show_m2020112949e059c86c20a dropdown-submenu   " data-code="m2020112949e059c86c20a" style="">
                                         <a tabindex="-1" href="/122" data-url="122" class="_txt_m2020112949e059c86c20a   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가 업무처리흐름도</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626760e2e3ec6965 dropdown-submenu   " data-code="m20220626760e2e3ec6965" style="">
                                         <a tabindex="-1" href="/138" data-url="138" class="_txt_m20220626760e2e3ec6965   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가 결과 공개</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _show_m20200715c98907fb8a5d2" style="" id="dropdown_m20200715c98907fb8a5d2" data-code="m20200715c98907fb8a5d2">
                            <a href="/menu2" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="menu2" data-toggle="dropdown" aria-expanded="false">
                                <span class="_txt_m20200715c98907fb8a5d2 plain_name" data-hover="">안전보건대장 등</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m202009110323e79db0990    sub-active" data-code="m202009110323e79db0990" style="">
                                    <a tabindex="-1" href="/28" data-url="28" class="_txt_m202009110323e79db0990   _fade_link "><span class="plain_name" data-hover="">안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2020111771cb19cac79f1 dropdown-submenu    sub-active" data-code="m2020111771cb19cac79f1" style="">
                                         <a tabindex="-1" href="/118" data-url="118" class="_txt_m2020111771cb19cac79f1   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220605c849ac0588a54 dropdown-submenu   " data-code="m20220605c849ac0588a54" style="">
                                         <a tabindex="-1" href="/126" data-url="126" class="_txt_m20220605c849ac0588a54   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성 사례 </span></a>
            
                                         </li>
            
                                        <li class="_show_m2022060658c8c7f92bb57 dropdown-submenu   " data-code="m2022060658c8c7f92bb57" style="">
                                         <a tabindex="-1" href="/128" data-url="128" class="_txt_m2022060658c8c7f92bb57   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성 1</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220606191d02cc97445 dropdown-submenu   " data-code="m20220606191d02cc97445" style="">
                                         <a tabindex="-1" href="/129" data-url="129" class="_txt_m20220606191d02cc97445   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성2</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                        <li class="_show_m20201012c7f7e4d5b18e0 dropdown-submenu    sub-active" data-code="m20201012c7f7e4d5b18e0" style="">
                                         <a tabindex="-1" href="/106" data-url="106" class="_txt_m20201012c7f7e4d5b18e0   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2022060717de90aa9340e dropdown-submenu   " data-code="m2022060717de90aa9340e" style="">
                                         <a tabindex="-1" href="/130" data-url="130" class="_txt_m2022060717de90aa9340e   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장 실제작성1</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220607aa547ef85fad2 dropdown-submenu   " data-code="m20220607aa547ef85fad2" style="">
                                         <a tabindex="-1" href="/131" data-url="131" class="_txt_m20220607aa547ef85fad2   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장 실제 작성 2</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                        <li class="_show_m2020101200b3716cb8e49 dropdown-submenu    sub-active" data-code="m2020101200b3716cb8e49" style="">
                                         <a tabindex="-1" href="/107" data-url="107" class="_txt_m2020101200b3716cb8e49   _fade_link "><span class="plain_name" data-hover="">공사안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220612f62b75c2fb7c3 dropdown-submenu   " data-code="m20220612f62b75c2fb7c3" style="">
                                         <a tabindex="-1" href="/132" data-url="132" class="_txt_m20220612f62b75c2fb7c3   _fade_link "><span class="plain_name" data-hover="">공사안전보건대장 실제 작성 1</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201008bf7b25a8b3902    sub-active" data-code="m20201008bf7b25a8b3902" style="">
                                    <a tabindex="-1" href="/53" data-url="53" class="_txt_m20201008bf7b25a8b3902   _fade_link "><span class="plain_name" data-hover="">설계안전성검토</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202010087c32af4760374 dropdown-submenu   " data-code="m202010087c32af4760374" style="">
                                         <a tabindex="-1" href="/54" data-url="54" class="_txt_m202010087c32af4760374   _fade_link "><span class="plain_name" data-hover="">DFS 개요</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010083ecddc475460d    sub-active" data-code="m202010083ecddc475460d" style="">
                                    <a tabindex="-1" href="/46" data-url="46" class="_txt_m202010083ecddc475460d   _fade_link "><span class="plain_name" data-hover="">유해위험방지계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201018f49f4c5447b1b dropdown-submenu   " data-code="m20201018f49f4c5447b1b" style="">
                                         <a tabindex="-1" href="/108" data-url="108" class="_txt_m20201018f49f4c5447b1b   _fade_link "><span class="plain_name" data-hover="">제출기한 및 서류</span></a>
            
                                         </li>
            
                                        <li class="_show_m20201018cddface657596 dropdown-submenu   " data-code="m20201018cddface657596" style="">
                                         <a tabindex="-1" href="/109" data-url="109" class="_txt_m20201018cddface657596   _fade_link "><span class="plain_name" data-hover="">심사 및 절차</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201203ab388be0c66fb   " data-code="m20201203ab388be0c66fb" style="">
                                    <a tabindex="-1" href="/124" data-url="124" class="_txt_m20201203ab388be0c66fb   _fade_link "><span class="plain_name" data-hover="">건축물관리계획서</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2020100993bd262cb1acf    sub-active" data-code="m2020100993bd262cb1acf" style="">
                                    <a tabindex="-1" href="/74" data-url="74" class="_txt_m2020100993bd262cb1acf   _fade_link "><span class="plain_name" data-hover="">안전관리계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201009268d602236ffc dropdown-submenu   " data-code="m20201009268d602236ffc" style="">
                                         <a tabindex="-1" href="/79" data-url="79" class="_txt_m20201009268d602236ffc   _fade_link "><span class="plain_name" data-hover="">목적 및 제출시기</span></a>
            
                                         </li>
            
                                        <li class="_show_m2020111761e92fe61b47d dropdown-submenu   " data-code="m2020111761e92fe61b47d" style="">
                                         <a tabindex="-1" href="/113" data-url="113" class="_txt_m2020111761e92fe61b47d   _fade_link "><span class="plain_name" data-hover="">프로세스</span></a>
            
                                         </li>
            
                                        <li class="_show_m2022062562d4d950666bd dropdown-submenu   " data-code="m2022062562d4d950666bd" style="">
                                         <a tabindex="-1" href="/133" data-url="133" class="_txt_m2022062562d4d950666bd   _fade_link "><span class="plain_name" data-hover="">안전관리계획서 수립기준</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626c39271ea72e47 dropdown-submenu   " data-code="m20220626c39271ea72e47" style="">
                                         <a tabindex="-1" href="/150" data-url="150" class="_txt_m20220626c39271ea72e47   _fade_link "><span class="plain_name" data-hover="">소규모안전관리계획서</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201008571c986518bab    sub-active" data-code="m20201008571c986518bab" style="">
                                    <a tabindex="-1" href="/49" data-url="49" class="_txt_m20201008571c986518bab   _fade_link "><span class="plain_name" data-hover="">안전보건개선계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202010083c76824b39dd7 dropdown-submenu   " data-code="m202010083c76824b39dd7" style="">
                                         <a tabindex="-1" href="/50" data-url="50" class="_txt_m202010083c76824b39dd7   _fade_link "><span class="plain_name" data-hover="">개요</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20220626ca344ca973638    sub-active" data-code="m20220626ca344ca973638" style="">
                                    <a tabindex="-1" href="/144" data-url="144" class="_txt_m20220626ca344ca973638   _fade_link "><span class="plain_name" data-hover="">해체계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220626c0308f49283d3 dropdown-submenu   " data-code="m20220626c0308f49283d3" style="">
                                         <a tabindex="-1" href="/145" data-url="145" class="_txt_m20220626c0308f49283d3   _fade_link "><span class="plain_name" data-hover="">해체계획서의 중요성</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206262ae4caa7b9f30 dropdown-submenu   " data-code="m202206262ae4caa7b9f30" style="">
                                         <a tabindex="-1" href="/146" data-url="146" class="_txt_m202206262ae4caa7b9f30   _fade_link "><span class="plain_name" data-hover="">건축물 해체공사 착공신고제 도입</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206261ae732304d725 dropdown-submenu   " data-code="m202206261ae732304d725" style="">
                                         <a tabindex="-1" href="/147" data-url="147" class="_txt_m202206261ae732304d725   _fade_link "><span class="plain_name" data-hover="">건축물 해체공사 안전강화방안</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626eb90850d56006 dropdown-submenu   " data-code="m20220626eb90850d56006" style="">
                                         <a tabindex="-1" href="/148" data-url="148" class="_txt_m20220626eb90850d56006   _fade_link "><span class="plain_name" data-hover="">해체공사 붕괴사고 조사보고서</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626b135562ddd2ea dropdown-submenu   " data-code="m20220626b135562ddd2ea" style="">
                                         <a tabindex="-1" href="/149" data-url="149" class="_txt_m20220626b135562ddd2ea   _fade_link "><span class="plain_name" data-hover="">건축물 해체계획서의 작성 및 감리업무 등에 관한 기준</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _show_m20230607be042518d1092" style="" id="dropdown_m20230607be042518d1092" data-code="m20230607be042518d1092">
                            <a href="/161" class="fixed_transform dropdown-toggle disabled _header_dropdown  active   _fade_link " data-url="161" data-toggle="dropdown" aria-expanded="false">
                                <span class="_txt_m20230607be042518d1092 plain_name" data-hover="">중대재해처벌법</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m20230607825da55b762d7   " data-code="m20230607825da55b762d7" style="">
                                    <a tabindex="-1" href="/162" data-url="162" class="_txt_m20230607825da55b762d7   _fade_link "><span class="plain_name" data-hover="">주요내용</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607963f2782ecd29   " data-code="m20230607963f2782ecd29" style="">
                                    <a tabindex="-1" href="/163" data-url="163" class="_txt_m20230607963f2782ecd29   _fade_link "><span class="plain_name" data-hover="">정의 및 적용대상</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607e5ab8e80c5243   " data-code="m20230607e5ab8e80c5243" style="">
                                    <a tabindex="-1" href="/165" data-url="165" class="_txt_m20230607e5ab8e80c5243   _fade_link "><span class="plain_name" data-hover="">경영책임자의 안전 및 보건 확보 의무</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306079883115cf5318   " data-code="m202306079883115cf5318" style="">
                                    <a tabindex="-1" href="/164" data-url="164" class="_txt_m202306079883115cf5318   _fade_link "><span class="plain_name" data-hover="">벌칙규정</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230918fca804513d525   " data-code="m20230918fca804513d525" style="">
                                    <a tabindex="-1" href="/186" data-url="186" class="_txt_m20230918fca804513d525  active   _fade_link "><span class="plain_name" data-hover="">중대재해사례</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _show_m20220625cf513fbd2f810" style="" id="dropdown_m20220625cf513fbd2f810" data-code="m20220625cf513fbd2f810">
                            <a href="/135" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="135" data-toggle="dropdown">
                                <span class="_txt_m20220625cf513fbd2f810 plain_name" data-hover="">안전보건관리체계</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu" style="transform: translateY(0px);">
            
                                <li class="dropdown-submenu _show_m202101063dc79a99589f7   " data-code="m202101063dc79a99589f7" style="">
                                    <a tabindex="-1" href="/125" data-url="125" class="_txt_m202101063dc79a99589f7   _fade_link "><span class="plain_name" data-hover="">안전보건관리체계(중대재해처벌법)</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202206259fb15431fd8ab   " data-code="m202206259fb15431fd8ab" style="">
                                    <a tabindex="-1" href="/136" data-url="136" class="_txt_m202206259fb15431fd8ab   _fade_link "><span class="plain_name" data-hover="">안전보건계획 이사회 보고 및 승인</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20220625e458b94d69600   " data-code="m20220625e458b94d69600" style="">
                                    <a tabindex="-1" href="/137" data-url="137" class="_txt_m20220625e458b94d69600   _fade_link "><span class="plain_name" data-hover="">회사의 안전보건계획 수립과 10대 건설사 안전임원 간담회</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="dropdown _more_menu"><a data-toggle="dropdown" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" aria-expanded="false"><i class="icon-options vertical-middle" aria-hidden="true"></i></a><ul class="dropdown-menu more_list _more_list" style="transform: translateY(0px);"><li class="_show_m20200715eb5a7908604cd dropdown-submenu sub-active" style="" id="dropdown_m20200715eb5a7908604cd" data-code="m20200715eb5a7908604cd">
                            <a href="/menu3" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="menu3" data-toggle="dropdown">
                                <span class="_txt_m20200715eb5a7908604cd plain_name" data-hover="">건설안전보건교육</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m20201009ab6052f55f07a   " data-code="m20201009ab6052f55f07a" style="">
                                    <a tabindex="-1" href="/68" data-url="68" class="_txt_m20201009ab6052f55f07a   _fade_link "><span class="plain_name" data-hover="">건설안전보건교육</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010096284ec0c569fa   " data-code="m202010096284ec0c569fa" style="">
                                    <a tabindex="-1" href="/81" data-url="81" class="_txt_m202010096284ec0c569fa   _fade_link "><span class="plain_name" data-hover="">관리감독자교육</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010091a1833532994c   " data-code="m202010091a1833532994c" style="">
                                    <a tabindex="-1" href="/78" data-url="78" class="_txt_m202010091a1833532994c   _fade_link "><span class="plain_name" data-hover="">특별안전보건교육</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="_show_m20201009e4e08d6495ffb dropdown-submenu sub-active" style="" id="dropdown_m20201009e4e08d6495ffb" data-code="m20201009e4e08d6495ffb">
                            <a href="/80" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="80" data-toggle="dropdown">
                                <span class="_txt_m20201009e4e08d6495ffb plain_name" data-hover="">자료실</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m202010097da87b41cefc4    sub-active" data-code="m202010097da87b41cefc4" style="">
                                    <a tabindex="-1" href="/77" data-url="77" class="_txt_m202010097da87b41cefc4   _fade_link "><span class="plain_name" data-hover="">관련 법규 </span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20230607a61946d0ec928 dropdown-submenu   " data-code="m20230607a61946d0ec928" style="">
                                         <a tabindex="-1" href="/166" data-url="166" class="_txt_m20230607a61946d0ec928   _fade_link "><span class="plain_name" data-hover="">산업안전보건법</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607a6ad8a09bcabb dropdown-submenu   " data-code="m20230607a6ad8a09bcabb" style="">
                                         <a tabindex="-1" href="/167" data-url="167" class="_txt_m20230607a6ad8a09bcabb   _fade_link "><span class="plain_name" data-hover="">산업안전보건법 시행령</span></a>
            
                                         </li>
            
                                        <li class="_show_m2023060750300ea89e735 dropdown-submenu   " data-code="m2023060750300ea89e735" style="">
                                         <a tabindex="-1" href="/168" data-url="168" class="_txt_m2023060750300ea89e735   _fade_link "><span class="plain_name" data-hover="">산업안전보건법 시행규칙</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607eaf15ee939cf4 dropdown-submenu   " data-code="m20230607eaf15ee939cf4" style="">
                                         <a tabindex="-1" href="/169" data-url="169" class="_txt_m20230607eaf15ee939cf4   _fade_link "><span class="plain_name" data-hover="">산업안전보건기준에 관한규칙</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607c3dc5f752bd0a dropdown-submenu   " data-code="m20230607c3dc5f752bd0a" style="">
                                         <a tabindex="-1" href="/170" data-url="170" class="_txt_m20230607c3dc5f752bd0a   _fade_link "><span class="plain_name" data-hover="">사업장 위험성평가에 관한 지침</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306128a9a641eca1ff   " data-code="m202306128a9a641eca1ff" style="">
                                    <a tabindex="-1" href="/177" data-url="177" class="_txt_m202306128a9a641eca1ff   _fade_link "><span class="plain_name" data-hover="">법규 개정</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306123bac3348334b0   " data-code="m202306123bac3348334b0" style="">
                                    <a tabindex="-1" href="/178" data-url="178" class="_txt_m202306123bac3348334b0   _fade_link "><span class="plain_name" data-hover="">안전보건자료실</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2020100903ca9f8c40fe0   " data-code="m2020100903ca9f8c40fe0" style="">
                                    <a tabindex="-1" href="/84" data-url="84" class="_txt_m2020100903ca9f8c40fe0   _fade_link "><span class="plain_name" data-hover="">사고사례</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607048fd6c76623a   " data-code="m20230607048fd6c76623a" style="">
                                    <a tabindex="-1" href="/175" data-url="175" class="_txt_m20230607048fd6c76623a   _fade_link "><span class="plain_name" data-hover="">안전소식</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li><li class="_show_m202010099f7d1fb8f299e dropdown-submenu" style="" id="dropdown_m202010099f7d1fb8f299e" data-code="m202010099f7d1fb8f299e">
                            <a href="/67" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="67" data-toggle="dropdown">
                                <span class="_txt_m202010099f7d1fb8f299e plain_name" data-hover="">고객센터</span>
                            </a>
            
            
            
                        </li></ul></li></div>
                <div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px; display: none;"><div class="viewport-nav desktop _main_clone_menu main_clone_menu">
            
            
                        <li class="dropdown _show_m202007153a95dcf3ec499" style="" id="dropdown_m202007153a95dcf3ec499" data-code="m202007153a95dcf3ec499">
                            <a href="/index" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="index" data-toggle="dropdown">
                                <span class="_txt_m202007153a95dcf3ec499 plain_name" data-hover="">생명안전연구소</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m2020111603a1025a4e5e1   " data-code="m2020111603a1025a4e5e1" style="">
                                    <a tabindex="-1" href="/110" data-url="110" class="_txt_m2020111603a1025a4e5e1   _fade_link "><span class="plain_name" data-hover="">회사소개</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010096d3ef24ed6db0   " data-code="m202010096d3ef24ed6db0" style="">
                                    <a tabindex="-1" href="/73" data-url="73" class="_txt_m202010096d3ef24ed6db0   _fade_link "><span class="plain_name" data-hover="">파트너</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230817fc13f57c5b9d4   " data-code="m20230817fc13f57c5b9d4" style="">
                                    <a tabindex="-1" href="/184" data-url="184" class="_txt_m20230817fc13f57c5b9d4   _fade_link "><span class="plain_name" data-hover="">조직도 및 업무분장</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202309184d258bbf730df   " data-code="m202309184d258bbf730df" style="">
                                    <a tabindex="-1" href="/185" data-url="185" class="_txt_m202309184d258bbf730df   _fade_link "><span class="plain_name" data-hover="">보유장비</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m202301087c08bf593a4f2" style="" id="dropdown_m202301087c08bf593a4f2" data-code="m202301087c08bf593a4f2">
                            <a href="/152" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="152" data-toggle="dropdown">
                                <span class="_txt_m202301087c08bf593a4f2 plain_name" data-hover="">재해예방기술지도</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m2023060712c08010b9ac4   " data-code="m2023060712c08010b9ac4" style="">
                                    <a tabindex="-1" href="/156" data-url="156" class="_txt_m2023060712c08010b9ac4   _fade_link "><span class="plain_name" data-hover="">재해예방기술지도 법적 근거</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2023060752245f81c8aba   " data-code="m2023060752245f81c8aba" style="">
                                    <a tabindex="-1" href="/157" data-url="157" class="_txt_m2023060752245f81c8aba   _fade_link "><span class="plain_name" data-hover="">재해예방기술지도 업무 절차</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306075c25617c52d9e   " data-code="m202306075c25617c52d9e" style="">
                                    <a tabindex="-1" href="/158" data-url="158" class="_txt_m202306075c25617c52d9e   _fade_link "><span class="plain_name" data-hover="">발주자 건축주의 건설현장  안전확보 프로세스</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20201008028950bdedb06" style="" id="dropdown_m20201008028950bdedb06" data-code="m20201008028950bdedb06">
                            <a href="/51" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="51" data-toggle="dropdown">
                                <span class="_txt_m20201008028950bdedb06 plain_name" data-hover="">위험성평가</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m20201008fa5194f00c596    sub-active" data-code="m20201008fa5194f00c596" style="">
                                    <a tabindex="-1" href="/52" data-url="52" class="_txt_m20201008fa5194f00c596   _fade_link "><span class="plain_name" data-hover="">위험성평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201129305965257c7fa dropdown-submenu   " data-code="m20201129305965257c7fa" style="">
                                         <a tabindex="-1" href="/123" data-url="123" class="_txt_m20201129305965257c7fa   _fade_link "><span class="plain_name" data-hover="">위험성평가 개요 및 절차</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607589080ca5550b dropdown-submenu   " data-code="m20230607589080ca5550b" style="">
                                         <a tabindex="-1" href="/171" data-url="171" class="_txt_m20230607589080ca5550b   _fade_link "><span class="plain_name" data-hover="">위험성평가 실시주체</span></a>
            
                                         </li>
            
                                        <li class="_show_m202306074c8ed3e036d93 dropdown-submenu   " data-code="m202306074c8ed3e036d93" style="">
                                         <a tabindex="-1" href="/172" data-url="172" class="_txt_m202306074c8ed3e036d93   _fade_link "><span class="plain_name" data-hover="">위험성평가 실시시기</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220625d82c1325c2f8d dropdown-submenu   " data-code="m20220625d82c1325c2f8d" style="">
                                         <a tabindex="-1" href="/134" data-url="134" class="_txt_m20220625d82c1325c2f8d   _fade_link "><span class="plain_name" data-hover="">위험성평가 인정심사 신청대상 및 혜택</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206260610058766310 dropdown-submenu   " data-code="m202206260610058766310" style="">
                                         <a tabindex="-1" href="/151" data-url="151" class="_txt_m202206260610058766310   _fade_link "><span class="plain_name" data-hover="">교육시설위험성평가</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626083313f0562a2 dropdown-submenu   " data-code="m20220626083313f0562a2" style="">
                                         <a tabindex="-1" href="/143" data-url="143" class="_txt_m20220626083313f0562a2   _fade_link "><span class="plain_name" data-hover="">건설공사 위험성평가의 절차</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201009739c7a5ab0768    sub-active" data-code="m20201009739c7a5ab0768" style="">
                                    <a tabindex="-1" href="/83" data-url="83" class="_txt_m20201009739c7a5ab0768   _fade_link "><span class="plain_name" data-hover="">공종별 위험성평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202206267350424c10e05 dropdown-submenu   " data-code="m202206267350424c10e05" style="">
                                         <a tabindex="-1" href="/141" data-url="141" class="_txt_m202206267350424c10e05   _fade_link "><span class="plain_name" data-hover="">건설공사 기초파일작업 유해위험요인 </span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626cfc0e1350450a dropdown-submenu   " data-code="m20220626cfc0e1350450a" style="">
                                         <a tabindex="-1" href="/142" data-url="142" class="_txt_m20220626cfc0e1350450a   _fade_link "><span class="plain_name" data-hover="">건설공사 굴착작업 유해위험요인</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201129942917f599a23    sub-active" data-code="m20201129942917f599a23" style="">
                                    <a tabindex="-1" href="/119" data-url="119" class="_txt_m20201129942917f599a23   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2020112973c19d66b1e49 dropdown-submenu   " data-code="m2020112973c19d66b1e49" style="">
                                         <a tabindex="-1" href="/120" data-url="120" class="_txt_m2020112973c19d66b1e49   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가란?</span></a>
            
                                         </li>
            
                                        <li class="_show_m202011291f4f3f9fb1c89 dropdown-submenu   " data-code="m202011291f4f3f9fb1c89" style="">
                                         <a tabindex="-1" href="/121" data-url="121" class="_txt_m202011291f4f3f9fb1c89   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가의 대상</span></a>
            
                                         </li>
            
                                        <li class="_show_m2020112949e059c86c20a dropdown-submenu   " data-code="m2020112949e059c86c20a" style="">
                                         <a tabindex="-1" href="/122" data-url="122" class="_txt_m2020112949e059c86c20a   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가 업무처리흐름도</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626760e2e3ec6965 dropdown-submenu   " data-code="m20220626760e2e3ec6965" style="">
                                         <a tabindex="-1" href="/138" data-url="138" class="_txt_m20220626760e2e3ec6965   _fade_link "><span class="plain_name" data-hover="">안전관리 수준평가 결과 공개</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20200715c98907fb8a5d2" style="" id="dropdown_m20200715c98907fb8a5d2" data-code="m20200715c98907fb8a5d2">
                            <a href="/menu2" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="menu2" data-toggle="dropdown" aria-expanded="false">
                                <span class="_txt_m20200715c98907fb8a5d2 plain_name" data-hover="">안전보건대장 등</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m202009110323e79db0990    sub-active" data-code="m202009110323e79db0990" style="">
                                    <a tabindex="-1" href="/28" data-url="28" class="_txt_m202009110323e79db0990   _fade_link "><span class="plain_name" data-hover="">안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2020111771cb19cac79f1 dropdown-submenu    sub-active" data-code="m2020111771cb19cac79f1" style="">
                                         <a tabindex="-1" href="/118" data-url="118" class="_txt_m2020111771cb19cac79f1   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220605c849ac0588a54 dropdown-submenu   " data-code="m20220605c849ac0588a54" style="">
                                         <a tabindex="-1" href="/126" data-url="126" class="_txt_m20220605c849ac0588a54   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성 사례 </span></a>
            
                                         </li>
            
                                        <li class="_show_m2022060658c8c7f92bb57 dropdown-submenu   " data-code="m2022060658c8c7f92bb57" style="">
                                         <a tabindex="-1" href="/128" data-url="128" class="_txt_m2022060658c8c7f92bb57   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성 1</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220606191d02cc97445 dropdown-submenu   " data-code="m20220606191d02cc97445" style="">
                                         <a tabindex="-1" href="/129" data-url="129" class="_txt_m20220606191d02cc97445   _fade_link "><span class="plain_name" data-hover="">기본안전보건대장 실제 작성2</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                        <li class="_show_m20201012c7f7e4d5b18e0 dropdown-submenu    sub-active" data-code="m20201012c7f7e4d5b18e0" style="">
                                         <a tabindex="-1" href="/106" data-url="106" class="_txt_m20201012c7f7e4d5b18e0   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m2022060717de90aa9340e dropdown-submenu   " data-code="m2022060717de90aa9340e" style="">
                                         <a tabindex="-1" href="/130" data-url="130" class="_txt_m2022060717de90aa9340e   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장 실제작성1</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220607aa547ef85fad2 dropdown-submenu   " data-code="m20220607aa547ef85fad2" style="">
                                         <a tabindex="-1" href="/131" data-url="131" class="_txt_m20220607aa547ef85fad2   _fade_link "><span class="plain_name" data-hover="">설계안전보건대장 실제 작성 2</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                        <li class="_show_m2020101200b3716cb8e49 dropdown-submenu    sub-active" data-code="m2020101200b3716cb8e49" style="">
                                         <a tabindex="-1" href="/107" data-url="107" class="_txt_m2020101200b3716cb8e49   _fade_link "><span class="plain_name" data-hover="">공사안전보건대장</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220612f62b75c2fb7c3 dropdown-submenu   " data-code="m20220612f62b75c2fb7c3" style="">
                                         <a tabindex="-1" href="/132" data-url="132" class="_txt_m20220612f62b75c2fb7c3   _fade_link "><span class="plain_name" data-hover="">공사안전보건대장 실제 작성 1</span></a>
            
                                         </li>
            
                                    </ul>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201008bf7b25a8b3902    sub-active" data-code="m20201008bf7b25a8b3902" style="">
                                    <a tabindex="-1" href="/53" data-url="53" class="_txt_m20201008bf7b25a8b3902   _fade_link "><span class="plain_name" data-hover="">설계안전성검토</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202010087c32af4760374 dropdown-submenu   " data-code="m202010087c32af4760374" style="">
                                         <a tabindex="-1" href="/54" data-url="54" class="_txt_m202010087c32af4760374   _fade_link "><span class="plain_name" data-hover="">DFS 개요</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010083ecddc475460d    sub-active" data-code="m202010083ecddc475460d" style="">
                                    <a tabindex="-1" href="/46" data-url="46" class="_txt_m202010083ecddc475460d   _fade_link "><span class="plain_name" data-hover="">유해위험방지계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201018f49f4c5447b1b dropdown-submenu   " data-code="m20201018f49f4c5447b1b" style="">
                                         <a tabindex="-1" href="/108" data-url="108" class="_txt_m20201018f49f4c5447b1b   _fade_link "><span class="plain_name" data-hover="">제출기한 및 서류</span></a>
            
                                         </li>
            
                                        <li class="_show_m20201018cddface657596 dropdown-submenu   " data-code="m20201018cddface657596" style="">
                                         <a tabindex="-1" href="/109" data-url="109" class="_txt_m20201018cddface657596   _fade_link "><span class="plain_name" data-hover="">심사 및 절차</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201203ab388be0c66fb   " data-code="m20201203ab388be0c66fb" style="">
                                    <a tabindex="-1" href="/124" data-url="124" class="_txt_m20201203ab388be0c66fb   _fade_link "><span class="plain_name" data-hover="">건축물관리계획서</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2020100993bd262cb1acf    sub-active" data-code="m2020100993bd262cb1acf" style="">
                                    <a tabindex="-1" href="/74" data-url="74" class="_txt_m2020100993bd262cb1acf   _fade_link "><span class="plain_name" data-hover="">안전관리계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20201009268d602236ffc dropdown-submenu   " data-code="m20201009268d602236ffc" style="">
                                         <a tabindex="-1" href="/79" data-url="79" class="_txt_m20201009268d602236ffc   _fade_link "><span class="plain_name" data-hover="">목적 및 제출시기</span></a>
            
                                         </li>
            
                                        <li class="_show_m2020111761e92fe61b47d dropdown-submenu   " data-code="m2020111761e92fe61b47d" style="">
                                         <a tabindex="-1" href="/113" data-url="113" class="_txt_m2020111761e92fe61b47d   _fade_link "><span class="plain_name" data-hover="">프로세스</span></a>
            
                                         </li>
            
                                        <li class="_show_m2022062562d4d950666bd dropdown-submenu   " data-code="m2022062562d4d950666bd" style="">
                                         <a tabindex="-1" href="/133" data-url="133" class="_txt_m2022062562d4d950666bd   _fade_link "><span class="plain_name" data-hover="">안전관리계획서 수립기준</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626c39271ea72e47 dropdown-submenu   " data-code="m20220626c39271ea72e47" style="">
                                         <a tabindex="-1" href="/150" data-url="150" class="_txt_m20220626c39271ea72e47   _fade_link "><span class="plain_name" data-hover="">소규모안전관리계획서</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20201008571c986518bab    sub-active" data-code="m20201008571c986518bab" style="">
                                    <a tabindex="-1" href="/49" data-url="49" class="_txt_m20201008571c986518bab   _fade_link "><span class="plain_name" data-hover="">안전보건개선계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m202010083c76824b39dd7 dropdown-submenu   " data-code="m202010083c76824b39dd7" style="">
                                         <a tabindex="-1" href="/50" data-url="50" class="_txt_m202010083c76824b39dd7   _fade_link "><span class="plain_name" data-hover="">개요</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20220626ca344ca973638    sub-active" data-code="m20220626ca344ca973638" style="">
                                    <a tabindex="-1" href="/144" data-url="144" class="_txt_m20220626ca344ca973638   _fade_link "><span class="plain_name" data-hover="">해체계획서</span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20220626c0308f49283d3 dropdown-submenu   " data-code="m20220626c0308f49283d3" style="">
                                         <a tabindex="-1" href="/145" data-url="145" class="_txt_m20220626c0308f49283d3   _fade_link "><span class="plain_name" data-hover="">해체계획서의 중요성</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206262ae4caa7b9f30 dropdown-submenu   " data-code="m202206262ae4caa7b9f30" style="">
                                         <a tabindex="-1" href="/146" data-url="146" class="_txt_m202206262ae4caa7b9f30   _fade_link "><span class="plain_name" data-hover="">건축물 해체공사 착공신고제 도입</span></a>
            
                                         </li>
            
                                        <li class="_show_m202206261ae732304d725 dropdown-submenu   " data-code="m202206261ae732304d725" style="">
                                         <a tabindex="-1" href="/147" data-url="147" class="_txt_m202206261ae732304d725   _fade_link "><span class="plain_name" data-hover="">건축물 해체공사 안전강화방안</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626eb90850d56006 dropdown-submenu   " data-code="m20220626eb90850d56006" style="">
                                         <a tabindex="-1" href="/148" data-url="148" class="_txt_m20220626eb90850d56006   _fade_link "><span class="plain_name" data-hover="">해체공사 붕괴사고 조사보고서</span></a>
            
                                         </li>
            
                                        <li class="_show_m20220626b135562ddd2ea dropdown-submenu   " data-code="m20220626b135562ddd2ea" style="">
                                         <a tabindex="-1" href="/149" data-url="149" class="_txt_m20220626b135562ddd2ea   _fade_link "><span class="plain_name" data-hover="">건축물 해체계획서의 작성 및 감리업무 등에 관한 기준</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20230607be042518d1092" style="" id="dropdown_m20230607be042518d1092" data-code="m20230607be042518d1092">
                            <a href="/161" class="fixed_transform dropdown-toggle disabled _header_dropdown  active   _fade_link " data-url="161" data-toggle="dropdown" aria-expanded="false">
                                <span class="_txt_m20230607be042518d1092 plain_name" data-hover="">중대재해처벌법</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m20230607825da55b762d7   " data-code="m20230607825da55b762d7" style="">
                                    <a tabindex="-1" href="/162" data-url="162" class="_txt_m20230607825da55b762d7   _fade_link "><span class="plain_name" data-hover="">주요내용</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607963f2782ecd29   " data-code="m20230607963f2782ecd29" style="">
                                    <a tabindex="-1" href="/163" data-url="163" class="_txt_m20230607963f2782ecd29   _fade_link "><span class="plain_name" data-hover="">정의 및 적용대상</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607e5ab8e80c5243   " data-code="m20230607e5ab8e80c5243" style="">
                                    <a tabindex="-1" href="/165" data-url="165" class="_txt_m20230607e5ab8e80c5243   _fade_link "><span class="plain_name" data-hover="">경영책임자의 안전 및 보건 확보 의무</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306079883115cf5318   " data-code="m202306079883115cf5318" style="">
                                    <a tabindex="-1" href="/164" data-url="164" class="_txt_m202306079883115cf5318   _fade_link "><span class="plain_name" data-hover="">벌칙규정</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230918fca804513d525   " data-code="m20230918fca804513d525" style="">
                                    <a tabindex="-1" href="/186" data-url="186" class="_txt_m20230918fca804513d525  active   _fade_link "><span class="plain_name" data-hover="">중대재해사례</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20220625cf513fbd2f810" style="" id="dropdown_m20220625cf513fbd2f810" data-code="m20220625cf513fbd2f810">
                            <a href="/135" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="135" data-toggle="dropdown">
                                <span class="_txt_m20220625cf513fbd2f810 plain_name" data-hover="">안전보건관리체계</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m202101063dc79a99589f7   " data-code="m202101063dc79a99589f7" style="">
                                    <a tabindex="-1" href="/125" data-url="125" class="_txt_m202101063dc79a99589f7   _fade_link "><span class="plain_name" data-hover="">안전보건관리체계(중대재해처벌법)</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202206259fb15431fd8ab   " data-code="m202206259fb15431fd8ab" style="">
                                    <a tabindex="-1" href="/136" data-url="136" class="_txt_m202206259fb15431fd8ab   _fade_link "><span class="plain_name" data-hover="">안전보건계획 이사회 보고 및 승인</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20220625e458b94d69600   " data-code="m20220625e458b94d69600" style="">
                                    <a tabindex="-1" href="/137" data-url="137" class="_txt_m20220625e458b94d69600   _fade_link "><span class="plain_name" data-hover="">회사의 안전보건계획 수립과 10대 건설사 안전임원 간담회</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20200715eb5a7908604cd" style="" id="dropdown_m20200715eb5a7908604cd" data-code="m20200715eb5a7908604cd">
                            <a href="/menu3" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="menu3" data-toggle="dropdown">
                                <span class="_txt_m20200715eb5a7908604cd plain_name" data-hover="">건설안전보건교육</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m20201009ab6052f55f07a   " data-code="m20201009ab6052f55f07a" style="">
                                    <a tabindex="-1" href="/68" data-url="68" class="_txt_m20201009ab6052f55f07a   _fade_link "><span class="plain_name" data-hover="">건설안전보건교육</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010096284ec0c569fa   " data-code="m202010096284ec0c569fa" style="">
                                    <a tabindex="-1" href="/81" data-url="81" class="_txt_m202010096284ec0c569fa   _fade_link "><span class="plain_name" data-hover="">관리감독자교육</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202010091a1833532994c   " data-code="m202010091a1833532994c" style="">
                                    <a tabindex="-1" href="/78" data-url="78" class="_txt_m202010091a1833532994c   _fade_link "><span class="plain_name" data-hover="">특별안전보건교육</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m20201009e4e08d6495ffb" style="" id="dropdown_m20201009e4e08d6495ffb" data-code="m20201009e4e08d6495ffb">
                            <a href="/80" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="80" data-toggle="dropdown">
                                <span class="_txt_m20201009e4e08d6495ffb plain_name" data-hover="">자료실</span>
                            </a>
            
            
                            <ul class="dropdown-menu" role="menu">
            
                                <li class="dropdown-submenu _show_m202010097da87b41cefc4    sub-active" data-code="m202010097da87b41cefc4" style="">
                                    <a tabindex="-1" href="/77" data-url="77" class="_txt_m202010097da87b41cefc4   _fade_link "><span class="plain_name" data-hover="">관련 법규 </span></a>
            
                                    <ul class="dropdown-menu" role="menu">
            
                                        <li class="_show_m20230607a61946d0ec928 dropdown-submenu   " data-code="m20230607a61946d0ec928" style="">
                                         <a tabindex="-1" href="/166" data-url="166" class="_txt_m20230607a61946d0ec928   _fade_link "><span class="plain_name" data-hover="">산업안전보건법</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607a6ad8a09bcabb dropdown-submenu   " data-code="m20230607a6ad8a09bcabb" style="">
                                         <a tabindex="-1" href="/167" data-url="167" class="_txt_m20230607a6ad8a09bcabb   _fade_link "><span class="plain_name" data-hover="">산업안전보건법 시행령</span></a>
            
                                         </li>
            
                                        <li class="_show_m2023060750300ea89e735 dropdown-submenu   " data-code="m2023060750300ea89e735" style="">
                                         <a tabindex="-1" href="/168" data-url="168" class="_txt_m2023060750300ea89e735   _fade_link "><span class="plain_name" data-hover="">산업안전보건법 시행규칙</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607eaf15ee939cf4 dropdown-submenu   " data-code="m20230607eaf15ee939cf4" style="">
                                         <a tabindex="-1" href="/169" data-url="169" class="_txt_m20230607eaf15ee939cf4   _fade_link "><span class="plain_name" data-hover="">산업안전보건기준에 관한규칙</span></a>
            
                                         </li>
            
                                        <li class="_show_m20230607c3dc5f752bd0a dropdown-submenu   " data-code="m20230607c3dc5f752bd0a" style="">
                                         <a tabindex="-1" href="/170" data-url="170" class="_txt_m20230607c3dc5f752bd0a   _fade_link "><span class="plain_name" data-hover="">사업장 위험성평가에 관한 지침</span></a>
            
                                         </li>
            
                                    </ul>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306128a9a641eca1ff   " data-code="m202306128a9a641eca1ff" style="">
                                    <a tabindex="-1" href="/177" data-url="177" class="_txt_m202306128a9a641eca1ff   _fade_link "><span class="plain_name" data-hover="">법규 개정</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m202306123bac3348334b0   " data-code="m202306123bac3348334b0" style="">
                                    <a tabindex="-1" href="/178" data-url="178" class="_txt_m202306123bac3348334b0   _fade_link "><span class="plain_name" data-hover="">안전보건자료실</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m2020100903ca9f8c40fe0   " data-code="m2020100903ca9f8c40fe0" style="">
                                    <a tabindex="-1" href="/84" data-url="84" class="_txt_m2020100903ca9f8c40fe0   _fade_link "><span class="plain_name" data-hover="">사고사례</span></a>
            
                                </li>
            
                                <li class="dropdown-submenu _show_m20230607048fd6c76623a   " data-code="m20230607048fd6c76623a" style="">
                                    <a tabindex="-1" href="/175" data-url="175" class="_txt_m20230607048fd6c76623a   _fade_link "><span class="plain_name" data-hover="">안전소식</span></a>
            
                                </li>
            
                            </ul>
            
            
                        </li>
            
                        <li class="dropdown _show_m202010099f7d1fb8f299e" style="" id="dropdown_m202010099f7d1fb8f299e" data-code="m202010099f7d1fb8f299e">
                            <a href="/67" class="fixed_transform dropdown-toggle disabled _header_dropdown   _fade_link " data-url="67" data-toggle="dropdown">
                                <span class="_txt_m202010099f7d1fb8f299e plain_name" data-hover="">고객센터</span>
                            </a>
            
            
            
                        </li>
            
                            </div></div><div class="_main_clone_menu_wrap" style="position: absolute; top: -9999px; left: -9999px;"><div class="viewport-nav desktop main_clone_menu"><li class="dropdown _more_menu"><a data-toggle="dropdown" class="fixed_transform dropdown-toggle disabled dropdown-more _header_dropdown" aria-expanded="false"><i class="icon-options vertical-middle" aria-hidden="true"></i></a><ul class="dropdown-menu more_list _more_list"></ul></li></div></div></ul>
                <!-- 템플릿별 레이아웃 구조 -->
                <!-- 템플릿별 레이아웃 구조 -->
            
            
            
            
            
            
            </div></div></div></div></div></div>
                        </div><div></div><div data-type="section-wrap" class="  inline-section-wrap fixed_transform" id="s2020100700e8f1f61f7bc"><div class="section_bg _section_bg fixed_transform _interactive_bg  "></div><div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#fff;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div><div data-type="inside" class="inline-inside _inline-inside"><div data-type="section" class="inline-section" section-code="s2020100700e8f1f61f7bc"><div data-type="col-group" data-col-group="center" class="inline-col-group inline-col-group-center"><div data-type="grid" class="inline-col"><div data-type="widget" id="w202010073b859bbc57d86" class="inline-widget"><div class="_widget_data" data-widget-type="inline_padding"><div class="widget inline_widget padding" data-height="12" data-width="30">
                <div id="padding_w202010073b859bbc57d86" style="min-width:5px; min-height:5px; height:12px;"></div>
            </div>
            </div></div></div></div></div></div>
                        </div>	</div><div id="inline_header_mobile" style="min-height: 30px;" class="first_scroll_fixed">	<div data-type="section-wrap" class="inline-section-wrap fixed_transform _fixed_header_section" id="s20201005b3138cd5be549"><div class="section_bg _section_bg fixed_transform _interactive_bg  "></div><div class="section_bg_color _section_bg_color fixed_transform" style="background-color:#ffffff;  position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div><div data-type="inside" class="inline-inside _inline-inside"><div data-type="section" class="inline-section" section-code="s20201005b3138cd5be549"><div data-type="col-group" data-col-group="left" class="inline-col-group inline-col-group-left" style="width:81px;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w202010055157a37ed6a07" class="inline-widget"><div class="_widget_data" data-widget-type="inline_menu_btn"><div class="widget inline_widget icon_type_menu st00">
                <a href="javascript:;" class="_no_hover fixed_transform inline-blocked" onclick="MOBILE_SLIDE_MENU.slideNavToggle($(this))">
                    <span class="holder icon_code btm bt-bars" id="inline_menu_alarm_badge"></span>
                    <span class="text">MENU</span>
                </a>
            </div>
            
            
            
            
            
            </div></div></div></div><div data-type="col-group" data-col-group="center" class="inline-col-group inline-col-group-center"><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005ffaa369844eed" class="inline-widget"><div class="_widget_data" data-widget-type="inline_logo">
            <div class="widget inline_widget logo  text_inline" id="logo_w20201005ffaa369844eed">
                        <div class="logo_title ">
                        <a class=" fixed_transform" style="display: block" href="/">생명안전연구소</a>
                    </div>
                    </div>
            
            </div></div></div></div><div data-type="col-group" data-col-group="right" class="inline-col-group inline-col-group-right" style="width:81px;"><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005ded3aae02af59" class="inline-widget"><div class="_widget_data" data-widget-type="inline_login_btn">	<div class="widget inline_widget login_btn button   txt_l text-xx-small">
                            <div></div>					</div>
            
            
            
            
            
            </div></div></div><div data-type="grid" class="inline-col"><div data-type="widget" id="w20201005a8dce1cb98dd0" class="inline-widget"><div class="_widget_data" data-widget-type="inline_search_btn">
            
            <div class="widget inline_widget search_btn">
                <div class="search_type fixed_transform search_btn_type01">
                    <div class="inline-blocked holder">
                        <form class=" icon_on" action="/search" method="get" id="inline_s_form_w20201005a8dce1cb98dd0">
                            <input class="search_btn_form" name="keyword" style="display: none" placeholder="Search" value="" title="검색"><a class="fixed_transform " href="#" onclick="SITE_SEARCH.openSearch(search_option_data_w20201005a8dce1cb98dd0);"><i class="simple icon-magnifier"></i><span class="sr-only">site search</span></a>			<ul id="image_list" style="display: none"></ul></form>
                    </div>
                </div>
            </div>
            
            
            
            
            
            
            </div></div></div></div></div></div>
                        </div><div></div>	<div data-type="carousel_menu" class="inline-section-wrap" id="mobile_carousel_menu"><div class="inline-inside _inline-inside"><div class="mobile_carousel_nav fixed_transform _mobile_nav " id="mobile_carousel_nav">
                <div class="mobile_nav_depth depth_0 depth_first st05 _mobile_navigation_menu" id="mobile_carousel_menu_0">
            
                                            <div class="nav-item _item   " data-code="m202007153a95dcf3ec499" data-url="index">
                                                <a href="/index" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">생명안전연구소</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m202301087c08bf593a4f2" data-url="152">
                                                <a href="/152" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">재해예방기술지도</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m20201008028950bdedb06" data-url="51">
                                                <a href="/51" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">위험성평가</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m20200715c98907fb8a5d2" data-url="menu2">
                                                <a href="/menu2" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">안전보건대장 등</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item  active   " data-code="m20230607be042518d1092" data-url="161">
                                                <a href="/161" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">중대재해처벌법</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m20220625cf513fbd2f810" data-url="135">
                                                <a href="/135" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">안전보건관리체계</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m20200715eb5a7908604cd" data-url="menu3">
                                                <a href="/menu3" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">건설안전보건교육</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m20201009e4e08d6495ffb" data-url="80">
                                                <a href="/80" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">자료실</span>
                                                </a>
                                            </div>
            
                                            <div class="nav-item _item   " data-code="m202010099f7d1fb8f299e" data-url="67">
                                                <a href="/67" class=" _fade_link " style="">
                                                    <span class="plain_name" data-hover="">고객센터</span>
                                                </a>
                                            </div>
            
                                        </div></div>
            
            
            </div>
            </div></div></div></div></header><div doz_type="section" class="section_wrap  pc_section    section_first _section_first   mobile_section_first    side_basic     " id="s202309183d6f4281c58f0" style="; ; ;" doz_change_mobile="N" doz_aside="N" doz_side_width="230" doz_side_margin="0" doz_extend="N" doz_mobile_section="N" doz_mobile_hide="N" doz_header_repeat="N" doz_footer_repeat="N" doz_category="default"><div class="section_bg _section_bg _interactive_bg  " style="   background-size:cover; background-repeat: no-repeat; position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div><div class="section_bg_color _section_bg_color" style="  position: absolute;left: 0;top: 0;right: 0; bottom: 0;"></div>
            
            
            
                    <main> 		 	 			 		 		 	 			 		 			 			 			 		 			 			 			 		 			 			 			 		 			 			 			 		 			 			 			 		 			 			 			 		 			 			 			 		<div doz_type="inside" class="inside"><div doz_type="row" doz_grid="12" class="doz_row"><div doz_type="grid" doz_grid="12" class="col-dz col-dz-12"><div doz_type="widget" id="w20230918a0ab7cb212206"><div class="_widget_data " data-widget-name="이미지" data-widget-type="image" data-widget-anim="none" data-widget-anim-duration="0.7" data-widget-anim-delay="0" data-widget-parent-is-mobile="N"><div class="widget image  _image_wrap text_position_bottom hover_text_position_bottom visibility hover_image_hidden org_size  hover_img_hide   ">
                <div class="_img_box img_wrap "><img id="img_w20230918a0ab7cb212206" src="https://cdn.imweb.me/thumbnail/20230109/85b710ef9e721.jpg" style="visibility: visible; image-rendering: -webkit-optimize-contrast; display: inline-block; width: 1250px; height: 239px; margin-left: auto; margin-right: auto;" class=" org_image" alt=""><div class="_hover_image hover_img" style="position: absolute; top: 50%; left: 50%; margin-top: -120px; margin-left: -625px; width: 1250px; height: 239px; background-image: url(&quot;https://cdn.imweb.me/thumbnail/20230109/85b710ef9e721.jpg&quot;); background-size: cover; background-repeat: no-repeat; background-position: 50% 50%;"></div></div></div>
            
            
            
            </div></div></div></div><div doz_type="row" doz_grid="12" class="doz_row"><div doz_type="grid" doz_grid="12" class="col-dz col-dz-12"><div doz_type="row" doz_grid="12" class="doz_row"><div doz_type="grid" doz_grid="3" doz_clear="Y" class="col-dz col-dz-3   col-xdz-clear"><div doz_type="widget" id="w202309186d42fd05ae820"><div class="_widget_data " data-widget-name="메뉴/카테고리" data-widget-type="sub_menu" data-widget-anim="none" data-widget-anim-duration="0.7" data-widget-anim-delay="0" data-widget-parent-is-mobile="N"><div class="widget">
                <div class="nav sub-menu sub_menu_hide  v-menu-type5 menu-vertical row-cnt-3 row-cnt-mobile-3">
                    <ul class="">
            
                <li style="" class="depth-01    " data-code="m20230607825da55b762d7">
                    <a href="/162" data-url="162" data-has_child="N" data-is_folder_menu="N" class=" _fade_link   ">
                        <span class="plain_name" data-hover="">주요내용</span>
                    </a>
            
                </li>
            
                <li style="" class="depth-01    " data-code="m20230607963f2782ecd29">
                    <a href="/163" data-url="163" data-has_child="N" data-is_folder_menu="N" class=" _fade_link   ">
                        <span class="plain_name" data-hover="">정의 및 적용대상</span>
                    </a>
            
                </li>
            
                <li style="" class="depth-01    " data-code="m20230607e5ab8e80c5243">
                    <a href="/165" data-url="165" data-has_child="N" data-is_folder_menu="N" class=" _fade_link   ">
                        <span class="plain_name" data-hover="">경영책임자의 안전 및 보건 확보 의무</span>
                    </a>
            
                </li>
            
                <li style="" class="depth-01    " data-code="m202306079883115cf5318">
                    <a href="/164" data-url="164" data-has_child="N" data-is_folder_menu="N" class=" _fade_link   ">
                        <span class="plain_name" data-hover="">벌칙규정</span>
                    </a>
            
                </li>
            
                <li style="" class="depth-01  active   active-real   " data-code="m20230918fca804513d525">
                    <a href="/186" data-url="186" data-has_child="N" data-is_folder_menu="N" class=" _fade_link   active   active-real ">
                        <span class="plain_name" data-hover="">중대재해사례</span>
                    </a>
            
                </li>
            
                </ul>	</div>
            </div>
            
            
            
            </div></div></div><div doz_type="grid" doz_grid="9" doz_clear="Y" class="col-dz col-dz-9   col-xdz-clear"><div doz_type="widget" id="w20230918f38bb09ff75c8"><div class="_widget_data " data-widget-name="게시판" data-widget-type="board" data-widget-anim="none" data-widget-anim-duration="0.7" data-widget-anim-delay="0" data-widget-parent-is-mobile="N">
            <div class="scroll_position" id="scroll_w20230918f38bb09ff75c8"></div>
            <div class="widget board _list_wrap m-margin-on">
            
                        <div class="doz_row">
                            <div class="col-dz col-dz-12">
                                <div class="board_view ">
            
            
                            <header class="board-title holder">
            
                                <p class="view_tit">텔레pepegarden떨팝니다</p>
                            </header>
                            <div class="board_summary">
                                <div class="left">
                                    <div class="avatar"><img alt="" src="/common/img/default_profile.png" class="avatar-image"></div>
                                    <div class="author">
                                        <div class="write">위커</div>
                                        <div class="board_name">
                                            <a href="/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9">
                                                중대재해사례
                                            </a>
                                        </div>
                                        <div class="date body_font_color_70">2024-09-06</div>
                                        <div class="hit-count body_font_color_70">조회수 878</div>
                                        <div class="tools txt"><a href="javascript:;" onclick="SECRET_ARTICLE.confirmSecret(event,'b202306232eec78bf35a7d','p202409061b0e4b9231e36','/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;bmode=write&amp;idx=95396760&amp;back_url=LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D&amp;board=b202306232eec78bf35a7d&amp;back_page_num=1','POST')" class="permission_require_pass" style="margin-right: 10px;">수정</a><a href="javascript:;" onclick="SECRET_ARTICLE.confirmSecret(event,'b202306232eec78bf35a7d','p202409061b0e4b9231e36',function(res){POST.deletePost('b202306232eec78bf35a7d','p202409061b0e4b9231e36','/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9',res)},'POST')" class="permission_require_pass" style="margin-right: 10px;">지우기</a></div>
                                    </div>
                                </div>
                                <div class="tools"><div class="mobile_right dropdown"><button class="dropdown-toggle" type="button" data-toggle="dropdown" aria-expanded="true"><i aria-hidden="true" class="vertical-middle icon-options board-summary-icon"></i></button>
                                                <ul class="dropdown-menu" role="menu"><li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:;" onclick="SECRET_ARTICLE.confirmSecret(event,'b202306232eec78bf35a7d','p202409061b0e4b9231e36','/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;bmode=write&amp;idx=95396760&amp;back_url=LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D&amp;board=b202306232eec78bf35a7d&amp;back_page_num=1','POST')" class="permission_require_pass">수정</a></li><li role="presentation"><a role="menuitem" tabindex="-1" href="javascript:;" onclick="SECRET_ARTICLE.confirmSecret(event,'b202306232eec78bf35a7d','p202409061b0e4b9231e36',function(res){POST.deletePost('b202306232eec78bf35a7d','p202409061b0e4b9231e36','/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9',res)},'POST')" class="permission_require_pass">지우기</a></li></ul></div></div>
                            </div>
            
            
                            <div class="board_txt_area fr-view">
                                <div class="margin-top-xxl _comment_body_"><p>텔레pepegarden떨팝니다<br><br>채널 T.me/Pepe_Garden<br>문의 @pepegarden<br>오픈톡<br>t.me/+D-_3LaM0RAg5OWMy<br><br>떨,떨액 두가지만 취급합니다.<br>오픈톡과 채널 운영중이고<br>합리적인가격으로 운영합니다.<br><br>하이코리아 에서 미미월드<br>위니드플라워 전부 겪어왔습니다.<br><br>오래된 경험으로 최상급 퀄리티로 안전하게 나눔하겠니다.<br><br>#떨팝니다#떨팔아요#강남떨#용산떨#홍대떨#떨인증딜러#떨삽니다#하이코리아#하이코리아네오#떨씨앗#미미월드#위니플#위니드플라워#버드팝니다#간자팝니다#떨드랍#떨선드랍#수원떨#인천떨#제주떨#부산떨#대마효능#대마합법#대마초팝니다#대마팝니다#떨팔아요#광주떨#떨액팝니다#떨액팔아요#떨액삽니다#떨액#대마액상#대마씨앗#대마재배#대마초#동작떨#광진떨#마포떨#천안떨#대구떨#대전떨#안산떨#청주떨#제주도떨#강북떨#논현떨#클럽떨#떨판매#Thc#cbd#홍대떨#한국딥웹#위니드플라워#하이코리아네오#탑코리아#건대떨#떨사요#떨인증딜러#떨팝니다#떨사는곳#쿠쉬팝니다#태국떨#북미떨#떨씨앗배송#떨씨앗국제택배#의료용대마#블루드림#레몬헤이즈#오지쿠쉬#오쥐쿠쉬#ak47쿠쉬#화이트위도우#개인장#법인장#강남오피#강남유흥#토토총판#바카라사이트#추천인코드#카지노사이트#사설카지노#토토배팅</p><p style="text-align: left"><img class="fr-dii _img_light_gallery cursor_pointer" src="https://cdn.imweb.me/upload/S20200715a3c5f9a178ae1/75aaf517d1dca.jpg" data-src="https://cdn.imweb.me/upload/S20200715a3c5f9a178ae1/75aaf517d1dca.jpg"></p></div>
                                <div class="file_area"></div>
                            </div>
                                     <div class="comment_section" id="comment_area">
                        <div class="comment-block">
                           <div class="btn-gruop-wrap clearfix">
                              <div class="btn-gruop btn-group-comment">
                                 <a onclick="viewLikeClick();" href="javascript:;" class="comment_num btn btn-flat  no-padding-x" data-toggle="tooltip" data-placement="top" id="view_like_btn_p202409061b0e4b9231e36" data-original-title="" title=""><i aria-hidden="true" class="btm bt-heart"></i> <em id="view_like_count_p202409061b0e4b9231e36">0</em></a>
                                 <span class="comment_num btn btn-flat no-padding-x no-pointer"><i aria-hidden="true" class="icon-bubble icon holder" style="top: 1px;"></i> <em id="comment_count">0</em></span>
                              </div>
            
                              <div class="tools">
                                 <div class="mobile_right">
                                    <button class="comment_num btn btn-flat" type="button" onclick="SITE.setSnsShare()"><i aria-hidden="true" class="btm bt-share board-summary-icon"></i></button>
                                    <button class="comment_num btn btn-flat hidden-xs hidden-sm" type="button" onclick="javascript:window.print();"><i aria-hidden="true" class="btm bt-fax board-summary-icon"></i></button>
                                 </div>
                              </div>
                           </div>
                        </div>
            
            
            
                        <div class="comment_list" id="comment_container">
            
                        </div>
                        <div class="comment_textarea">
                           <form id="comment_form">
                              <input type="hidden" name="post_code" value="p202409061b0e4b9231e36">
                              <input type="hidden" name="board_code" value="b202306232eec78bf35a7d">
                              <input type="hidden" name="comment_token" value="s4JfgV9H8X3grZJBhH8Pu7W6xTINxHFHBs7F4pfsiHEx6SoFppiQ18QW4xFe/y+4HN9lvAawpUWLqd0Sxs7mnA9E8mXKevqr1VRCiHcIslqkDo5yqhUC35WA/0cTAk+w" class="_tk_obj">
                              <input type="hidden" name="comment_token_key" value="1829" class="_tk_obj">
                              <div class="postmeta comment-comment"><!--댓글에 댓글을 입력할 경우-->
                                 <div class="non-member"><input title="nick" type="text" id="comment_nink" name="nick" placeholder="이름"><input title="password" type="password" name="secret_pass" placeholder="비밀번호"></div>
                                 <div class="textarea_block">
                                    <textarea title="댓글을 남겨주세요" placeholder="댓글을 남겨주세요" rows="1" name="body" id="comment_body" data-action="btn_c_p202409061b0e4b9231e36" data-autosize-on="true" style="overflow: hidden; overflow-wrap: break-word; height: 62px;"></textarea>
                                    <div class="file-add-block" style="display: none" id="comment_image_box"></div>
                                    <button class="btn btn-primary btn-sm" onclick="POST_COMMENT.add(); return false;">작성</button>
                                    <div class="inline-blocked holder">
                                       <i aria-hidden="true" class="icon-picture icon vertical-middle"></i>
                                       <input title="comment image upload" type="file" class="comment_image_upload" multiple="" name="comment_images" id="comment_image_upload_btn">
                                    </div>
                                    <!--<i class="zmdi zmdi-play-circle"></i>-->
                                 </div>
                              </div>
                           <ul id="image_list" style="display: none"></ul></form>
                        </div>
                     </div>
                            <div class="comment_section">
                                <div class="list_tap">
                                    <a href="/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;bmode=view&amp;idx=96391790&amp;t=board"><i aria-hidden="true" class="icon-arrow-up"></i><span class="secret_icon">텔레pepegarden떨팝니다</span></a>
                                    <a href="/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;bmode=view&amp;idx=54838879&amp;t=board"><i aria-hidden="true" class="icon-arrow-down"></i><span class="secret_icon">강남오피 ` 【오피쓰.com】강남건마 () 강남출장샵 / 출장샵강남 ! 강남휴게텔 ^ 강남op</span></a>
                                </div>
                                <div class="table_bottom over_h action-area">
                                    <a class="btn btn-primary btn-sm float_l" href="/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;page=1" role="button">
                                        목록
                                    </a>
                                    <a class="btn btn-primary btn-sm float_r" role="button" href="/186/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&amp;board=b202306232eec78bf35a7d&amp;bmode=write&amp;back_url=LzE4Ni8%2FYm1vZGU9dmlldyZpZHg9OTUzOTY3NjA%3D">글쓰기</a>
                                </div>
                            </div>
            
                            </div></div></div></div>
            
            
            
            </div></div></div></div><div doz_type="row" doz_grid="12" class="doz_row"><div doz_type="grid" doz_grid="12" class="col-dz col-dz-12"><div doz_type="widget" id="w20230918f8d54e7c86e9b"><div class="_widget_data _ds_animated_except" data-widget-name="여백" data-widget-type="padding" data-widget-parent-is-mobile="N"><div class="widget padding" data-height="108" style="margin-top:px; margin-bottom:px;">
                <div id="padding_w20230918f8d54e7c86e9b" style="width:100%; min-height:1px; height:108px; "></div>
            </div>
            </div></div></div></div></div></div></div></main></div><footer id="doz_footer_wrap"><div id="doz_footer"> 	
                <div class="footer-section footer-type05 _footer_font_preview footer_align_center footer_align_right">		<div class="inside">
                        <div class="doz_row">
                            <div class="col-dz-12 col-xdz-12 col-dz">
                                                        <div class="foot-sociallink _sns_link">
                                        <div class="btn-group _sns_link_list" role="group">
                                            <a type="button" class="btn _E0275g617n " href="" style="display: none;" target="_blank"><i class="fa fa-facebook"></i><span class="sr-only">SNS 바로가기</span></a>							</div>
                                    </div>
            
            
                                <div class="foot-custom">
                                    <div class="custom-text _footer_text">
                                                                    <div class="custom-text-info _text_editor fr-view">
                                            <p><span style="font-size: 18px;">생명안전연구소&nbsp;</span></p><p><br></p><p>[계좌]</p><p>예금주 : 허선형(생명안전연구소)</p><p>농협 302-1489-4757-11</p><p><br></p><p>대표자 : 허선형 &nbsp; &nbsp;사업자 등록번호 : 110-36-23099</p><p>연락처 : 010 9303 3423 &nbsp; &nbsp;이메일 : <a href="mailto:safety3423@naver.com">safety3423@naver.com</a></p><p>주소 : 서울특별시 구로구 남부순환로 105길 14, 315호</p><p style="margin-top:10px;">Copyright ⓒ Portfolio</p><p style="text-align: center;"><a href="https://imweb.me/" target="_blank">Hosting by I'MWEB</a></p>							</div>
                                    </div>
                                                                                                        </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            </footer><iframe name="hidden_frame" id="hidden_frame" title="hidden frame" src="about:blank" style="position: absolute; left: -9999px; width: 1px; height: 1px; top:-9999px;"></iframe>
            <div class="modal" id="cocoaModal" role="dialog" aria-hidden="false">
                <div class="modal-dialog">
                    <div class="modal-content"></div>
                </div>
            </div>
            <div class="modal submodal" role="dialog" id="cocoaSubModal" aria-hidden="false" style="z-index: 17001">
                <div class="modal-dialog">
                    <div class="modal-content"></div>
                </div>
            </div>
            <script src="https://vendor-cdn.imweb.me/js/bootstrap.min.js?1630317768"></script>
            <!--[if lte IE 9]>
            <script  src='https://vendor-cdn.imweb.me/js/html5shiv.min.js?1577682292'></script>
            <![endif]-->
            <!--[if lte IE 9]>
            <script  src='https://vendor-cdn.imweb.me/js/respond.min.js?1577682292'></script>
            <![endif]-->
            <!--[if lte IE 9]>
            <script  src='https://vendor-cdn.imweb.me/js/placeholders.min.js?1577682292'></script>
            <![endif]-->
            <!--[if lte IE 8]>
            <script  src='https://vendor-cdn.imweb.me/js/PIE_IE678.js?1577682292'></script>
            <![endif]-->
            <script src="https://vendor-cdn.imweb.me/js/jquery.fileupload.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.lazyload.min.js?1577682292"></script>
            <script src="/js/localize/KR_KRW_currency.js?1732533790"></script>
            <script>
            LOCALIZE.설명_전체평점보기 = function(){ return LOCALIZE.convArguments("전체 평점 보기", arguments); };
            LOCALIZE.설명_나쁨 = function(){ return LOCALIZE.convArguments("나쁨", arguments); };
            LOCALIZE.설명_별로 = function(){ return LOCALIZE.convArguments("별로", arguments); };
            LOCALIZE.설명_보통 = function(){ return LOCALIZE.convArguments("보통", arguments); };
            LOCALIZE.설명_좋음 = function(){ return LOCALIZE.convArguments("좋음", arguments); };
            LOCALIZE.설명_최고 = function(){ return LOCALIZE.convArguments("최고", arguments); };
            LOCALIZE.타이틀_상품준비 = function(){ return LOCALIZE.convArguments("상품준비", arguments); };
            LOCALIZE.타이틀_배송대기 = function(){ return LOCALIZE.convArguments("배송대기", arguments); };
            LOCALIZE.타이틀_추가상품 = function(){ return LOCALIZE.convArguments("추가 상품", arguments); };
            LOCALIZE.설명_판매마감안내 = function(){ return LOCALIZE.convArguments("판매 기간이 마감된 상품입니다.", arguments); };
            LOCALIZE.설명_판매시작시간안내 = function(){ return LOCALIZE.convArguments("이 상품은 %1 부터 판매됩니다.", arguments); };
            LOCALIZE.설명_상품구매취소반환n = function(){ return LOCALIZE.convArguments("상품구매 취소 반환 %1", arguments); };
            LOCALIZE.설명_주문요약 = function(){ return LOCALIZE.convArguments("주문 요약", arguments); };
            LOCALIZE.설명_새쿠폰알림 = function(){ return LOCALIZE.convArguments("쿠폰이 발행되어 마이페이지에서 받을 수 있어요.", arguments); };
            LOCALIZE.설명_이미제출한입력폼입니다 = function(){ return LOCALIZE.convArguments("이미 제출한 입력폼입니다.", arguments); };
            LOCALIZE.타이틀_정기구독신청완료 = function(){ return LOCALIZE.convArguments("정기구독 신청이 완료되었습니다.", arguments); };
            LOCALIZE.타이틀_새로운정기구독신청접수 = function(){ return LOCALIZE.convArguments("새로운 정기구독 신청이 접수되었습니다.", arguments); };
            LOCALIZE.타이틀_정기구독결제실패 = function(){ return LOCALIZE.convArguments("정기구독 결제가 실패되었습니다.", arguments); };
            LOCALIZE.타이틀_정기구독결제실패접수 = function(){ return LOCALIZE.convArguments("정기구독 결제가 실패가 접수되었습니다.", arguments); };
            LOCALIZE.타이틀_정기구독해지완료 = function(){ return LOCALIZE.convArguments("정기구독이 해지되었습니다.", arguments); };
            LOCALIZE.타이틀_정기구독해지접수 = function(){ return LOCALIZE.convArguments("정기구독이 해지가 접수되었습니다.", arguments); };
            LOCALIZE.타이틀_구독해지상품 = function(){ return LOCALIZE.convArguments("구독 해지 상품", arguments); };
            LOCALIZE.설명_일부상품만건너뛰기 = function(){ return LOCALIZE.convArguments("일부 상품만 건너뛰기 / 정기구독 해지 등으로 결제 예정된 주문의 구성이 달라질 경우 할인 혜택 및 배송비가 달라질 수 있습니다.", arguments); };
            LOCALIZE.설명_해지된정기구독주문건은 = function(){ return LOCALIZE.convArguments("해지된 정기구독 주문 건은 재개가 불가하며, 다시 신청을 진행해야 합니다.", arguments); };
            LOCALIZE.설명_정기구독등록실패 = function(){ return LOCALIZE.convArguments("정기구독 등록 실패", arguments); };
            LOCALIZE.타이틀_정기구독관리 = function(){ return LOCALIZE.convArguments("정기구독 관리", arguments); };
            LOCALIZE.타이틀_응답이정상적으로접수되었습니다 = function(){ return LOCALIZE.convArguments("응답이 정상적으로 접수되었습니다.", arguments); };
            LOCALIZE.타이틀_응답에참여해주셔서감사합니다 = function(){ return LOCALIZE.convArguments("응답에 참여해 주셔서 감사합니다.", arguments); };
            LOCALIZE.버튼_정기구독 = function(){ return LOCALIZE.convArguments("정기구독", arguments); };
            LOCALIZE.버튼_정기구독신청 = function(){ return LOCALIZE.convArguments("정기구독 신청", arguments); };
            LOCALIZE.설명_결제후마이페이지구독주기변경가능 = function(){ return LOCALIZE.convArguments("* 결제 후 마이페이지 > 정기구독 관리에서 구독주기 변경이 가능합니다.", arguments); };
            LOCALIZE.설명_다음예상결제일과에서확인가능 = function(){ return LOCALIZE.convArguments("* 다음 예상 결제일은 %1입니다.<br>* 구독 일정은 마이페이지 > 정기구독 관리에서 확인 가능합니다.", arguments); };
            LOCALIZE.타이틀_정기구독신청목록 = function(){ return LOCALIZE.convArguments("정기구독 신청 목록", arguments); };
            LOCALIZE.타이틀_정기구독신청상세 = function(){ return LOCALIZE.convArguments("정기구독 신청 상세", arguments); };
            LOCALIZE.타이틀_정기구독해지상세 = function(){ return LOCALIZE.convArguments("정기구독 해지 상세", arguments); };
            LOCALIZE.타이틀_정기구독일정안내 = function(){ return LOCALIZE.convArguments("정기구독 일정 안내", arguments); };
            LOCALIZE.버튼_정기구독해지 = function(){ return LOCALIZE.convArguments("정기구독 해지", arguments); };
            LOCALIZE.버튼_정기구독전체해지 = function(){ return LOCALIZE.convArguments("정기구독 전체해지", arguments); };
            LOCALIZE.설명_정기구독내역이없음 = function(){ return LOCALIZE.convArguments("정기구독 신청 내역이 없습니다.<br>자주 사는 물건이라면, 정기배송 서비스를 이용해보세요.", arguments); };
            LOCALIZE.설명_정기구독해지내역이없음 = function(){ return LOCALIZE.convArguments("정기구독 해지 내역이 없습니다.", arguments); };
            LOCALIZE.설명_구매자의요청에의해정구기독이해지되었습니다 = function(){ return LOCALIZE.convArguments("구매자 요청에 의해 정기구독이 해지되었습니다.", arguments); };
            LOCALIZE.설명_판매자에의해정기구독이해지되었습니다 = function(){ return LOCALIZE.convArguments("판매자에 의해 정기구독이 해지되었습니다.", arguments); };
            LOCALIZE.설명_해당상품의정기구독서비스가종료되어자동해지되었습니다 = function(){ return LOCALIZE.convArguments("해당 상품의 정기구독 서비스가 종료되어 자동 해지되었습니다.", arguments); };
            LOCALIZE.설명_정기구독확인해주세요안내사항 = function(){ return LOCALIZE.convArguments("<li>등록한 카드 정보로 설정된 배송주기에 따라 자동 결제가 진행됩니다.</li><li>상품 가격은 다음 주기에 변경될 수 있으며, 결제 시점의 가격으로 결제됩니다.</li><li>최초 신청 시 적용된 할인 수단 및 내역이 제외되거나 변동될 수 있습니다.</li><li>잔액 부족 등 일정 시간 결제되지 않을 경우 자동 주문 취소됩니다.</li><li>결제 회차에 일부 상품이 품절이거나 옵션이 삭제됐을 경우, 해당 상품은 주문 시 제외됩니다.</li><li>일부 상품만 건너뛰기 / 정기구독 해지할 경우 추가 배송비가 부과될 수 있습니다.</li>", arguments); };
            LOCALIZE.설명_진행중인정기구독주문이있어카드삭제불가 = function(){ return LOCALIZE.convArguments("현재 진행 중인 정기구독 주문이 있어 카드를 삭제할 수 없습니다.<br/>카드 변경 혹은 정기구독 해지 후 카드를 삭제해 주세요.", arguments); };
            LOCALIZE.설명_등록된자동결제카드를삭제하시겠습니까 = function(){ return LOCALIZE.convArguments("등록된 자동결제 카드를 <br class=\'hidden-lg hidden-md hidden-sm\'/>삭제하시겠습니까?", arguments); };
            LOCALIZE.설명_이번배송을건너뛰겠습니까다음구독일은n입니다 = function(){ return LOCALIZE.convArguments("이번 배송을 건너뛰겠습니까?<br/>해당 상품의 다음 구독일은<br class=\'hidden-lg hidden-md\'/> <strong>%1</strong> 입니다.", arguments); };
            LOCALIZE.설명_이번배송을건너뛰겠습니까다음구독일은n입니다선택옵션도함께 = function(){ return LOCALIZE.convArguments("이번 배송을 건너뛰겠습니까?<br/>해당 상품의 다음 구독일은<br class=\'hidden-lg hidden-md\'/> <strong>%1</strong> 입니다.<br>선택옵션도 함께 적용됩니다.", arguments); };
            LOCALIZE.설명_전체상품의정기구독을해지하시겠습니까 = function(){ return LOCALIZE.convArguments("전체 상품의 정기구독을 <br class=\'hidden-lg hidden-md hidden-sm\'/>해지하시겠습니까?", arguments); };
            LOCALIZE.설명_해당상품의정기구독을해지하시겠습니까 = function(){ return LOCALIZE.convArguments("해당 상품의 정기구독을 <br class=\'hidden-lg hidden-md hidden-sm\'/>해지하시겠습니까?", arguments); };
            LOCALIZE.설명_해당상품의정기구독을해지하시겠습니까선택옵션도함께 = function(){ return LOCALIZE.convArguments("해당 상품의 정기구독을 <br class=\'hidden-lg hidden-md hidden-sm\'/>해지하시겠습니까?<br>선택옵션도 함께 해지됩니다.", arguments); };
            LOCALIZE.타이틀_정기구독신청이완료되었습니다 = function(){ return LOCALIZE.convArguments("정기구독 신청이 완료되었습니다", arguments); };
            LOCALIZE.설명_정기구독신청내역은마이페이지에서조회가능합니다 = function(){ return LOCALIZE.convArguments("정기구독 신청 내역은 마이페이지에서 조회 가능합니다", arguments); };
            LOCALIZE.설명_정기구독결제 = function(){ return LOCALIZE.convArguments("정기구독 결제", arguments); };
            LOCALIZE.타이틀_반품교환택배사 = function(){ return LOCALIZE.convArguments("반품/교환 택배사", arguments); };
            LOCALIZE.타이틀_반품배송비편도 = function(){ return LOCALIZE.convArguments("반품 배송비(편도)", arguments); };
            LOCALIZE.타이틀_교환배송비왕복 = function(){ return LOCALIZE.convArguments("교환 배송비(왕복)", arguments); };
            LOCALIZE.타이틀_반품교환주소지 = function(){ return LOCALIZE.convArguments("반품/교환 주소지", arguments); };
            LOCALIZE.타이틀_반품교환신청기준일 = function(){ return LOCALIZE.convArguments("반품/교환 신청 기준일", arguments); };
            LOCALIZE.타이틀_반품교환불가능사유 = function(){ return LOCALIZE.convArguments("반품/교환 불가능 사유", arguments); };
            LOCALIZE.설명_상품수령후n일이내기타 = function(){ return LOCALIZE.convArguments("단, 제품이 표시광고 내용과 다르거나 불량 등 계약과 다르게 이행된 경우는 제품 수령일로부터 3개월이내나 그 사실을 안 날 또는 알 수 있었던 날부터 30일 이내 교환/반품이 가능", arguments); };
            LOCALIZE.설명_타임세일종료까지n일 = function(){ return LOCALIZE.convArguments("타임세일 종료까지 %1일", arguments); };
            LOCALIZE.설명_상세페이지타임세일종료까지n일 = function(){ return LOCALIZE.convArguments("<label class=\'text-bold text-brand\'>타임세일</label> 종료까지 <strong>%1일</strong>", arguments); };
            LOCALIZE.설명_상세페이지타임세일종료까지n1시n2분n3초남음 = function(){ return LOCALIZE.convArguments("<label class=\'text-bold text-brand\'>타임세일</label> 종료까지 <strong>%1:%2:%3</strong> 남음", arguments); };
            LOCALIZE.타이틀_개인정보수집동의 = function(){ return LOCALIZE.convArguments("개인정보 수집동의", arguments); };
            LOCALIZE.설명_탈퇴후같은계정으로재가입시 = function(){ return LOCALIZE.convArguments("탈퇴 후 같은 계정으로 재가입 시 기존에 가지고 있던 적립금은 복원되지 않으며, 사용 및 다운로드했던 쿠폰도 사용 불가능합니다.", arguments); };
            LOCALIZE.버튼_line계정으로가입 = function(){ return LOCALIZE.convArguments("LINE으로 시작하기", arguments); };
            LOCALIZE.버튼_line로그인 = function(){ return LOCALIZE.convArguments("LINE으로 시작하기", arguments); };
            LOCALIZE.설명_비공개페이지비밀번호입력 = function(){ return LOCALIZE.convArguments("비공개 페이지 입니다.<br/>비밀번호를 입력해 주세요.", arguments); };
            LOCALIZE.설명_결제예상금액임시 = function(){ return LOCALIZE.convArguments("총 상품금액(%1개)", arguments); };
            LOCALIZE.설명_이배송지로배송할수없습니다다른배송지를선택해주세요 = function(){ return LOCALIZE.convArguments("이 배송지로 배송할 수 없습니다. 다른 배송지를 선택해 주세요.", arguments); };
            LOCALIZE.설명_기본비밀번호입력 = function(){ return LOCALIZE.convArguments("기본 비밀번호 입력", arguments); };
            LOCALIZE.설명_접근권한이없는회원 = function(){ return LOCALIZE.convArguments("접근 권한이 없는 회원입니다.<br/>소유자에게 엑세스를 요청해주세요.", arguments); };
            LOCALIZE.설명_입력하신추천인코드는존재하지않거나 = function(){ return LOCALIZE.convArguments("입력하신 추천인 코드는 존재하지 않거나 더이상 사용이 불가합니다. 다시 확인해주세요.", arguments); };
            LOCALIZE.타이틀_추천인코드 = function(){ return LOCALIZE.convArguments("추천인 코드", arguments); };
            LOCALIZE.설명_추천인코드가복사되었습니다 = function(){ return LOCALIZE.convArguments("추천인 코드가 복사되었습니다!", arguments); };
            LOCALIZE.버튼_홈 = function(){ return LOCALIZE.convArguments("Home", arguments); };
            LOCALIZE.설명_구매조건확인및결제진행에동의하여주시기바랍니다 = function(){ return LOCALIZE.convArguments("구매조건 확인 및 결제진행에 동의하여 주시기 바랍니다.", arguments); };
            LOCALIZE.설명_가입한아이디 = function(){ return LOCALIZE.convArguments("가입한 아이디", arguments); };
            LOCALIZE.설명_옵션을입력해주세요 = function(){ return LOCALIZE.convArguments("옵션을 입력해 주세요", arguments); };
            LOCALIZE.버튼_휴대폰인증 = function(){ return LOCALIZE.convArguments("휴대폰 인증", arguments); };
            LOCALIZE.버튼_카드인증 = function(){ return LOCALIZE.convArguments("카드 인증", arguments); };
            LOCALIZE.타이틀_오늘출발상품 = function(){ return LOCALIZE.convArguments("오늘출발 상품", arguments); };
            LOCALIZE.타이틀_오늘도착상품 = function(){ return LOCALIZE.convArguments("오늘도착 상품", arguments); };
            LOCALIZE.타이틀_예약상품정보 = function(){ return LOCALIZE.convArguments("예약 상품 정보", arguments); };
            LOCALIZE.설명_쿠폰번호입력 = function(){ return LOCALIZE.convArguments("쿠폰 번호 입력", arguments); };
            LOCALIZE.버튼_배송지목록에추가 = function(){ return LOCALIZE.convArguments("배송지 목록에 추가", arguments); };
            LOCALIZE.설명_전체동의 = function(){ return LOCALIZE.convArguments("전체 동의", arguments); };
            LOCALIZE.설명_구매조건확인및결제진행에동의 = function(){ return LOCALIZE.convArguments("구매조건 확인 및 결제진행에 동의", arguments); };
            LOCALIZE.설명_배송메모를선택해주세요 = function(){ return LOCALIZE.convArguments("배송메모를 선택해 주세요.", arguments); };
            LOCALIZE.버튼_상세정보펼처보기 = function(){ return LOCALIZE.convArguments("상세정보 펼쳐보기", arguments); };
            LOCALIZE.버튼_상세정보접기 = function(){ return LOCALIZE.convArguments("상세정보 접기", arguments); };
            LOCALIZE.타이틀_추천인 = function(){ return LOCALIZE.convArguments("추천인", arguments); };
            LOCALIZE.설명_추천인코드를입력 = function(){ return LOCALIZE.convArguments("추천인 코드를 입력하세요.", arguments); };
            LOCALIZE.설명_구매평작성완료 = function(){ return LOCALIZE.convArguments("구매평 작성 완료", arguments); };
            LOCALIZE.설명_군 = function(){ return LOCALIZE.convArguments("군", arguments); };
            LOCALIZE.설명_성 = function(){ return LOCALIZE.convArguments("성", arguments); };
            LOCALIZE.버튼_아이디비밀번호찾기 = function(){ return LOCALIZE.convArguments("아이디 · 비밀번호 찾기", arguments); };
            LOCALIZE.버튼_비밀번호찾기 = function(){ return LOCALIZE.convArguments("비밀번호 찾기", arguments); };
            LOCALIZE.설명_이름또는닉네임 = function(){ return LOCALIZE.convArguments("이름 또는 닉네임", arguments); };
            LOCALIZE.설명_쿠폰이발급되었습니다 = function(){ return LOCALIZE.convArguments("쿠폰이 발급 되었습니다.", arguments); };
            LOCALIZE.설명_이용이제한된페이지안내 = function(){ return LOCALIZE.convArguments("현재 접속하신 <span class=\'text-primary\'>%1</span>의 이용관련 문의는<br/><a href=\'mailto:%2\'><span class=\'text-primary\'>%2</span></a> 또는 <a href=\'sms:%3\'><span class=\'text-primary\'>%3</span></a>로 문의해주시기 바랍니다.", arguments); };
            LOCALIZE.설명_기타택배 = function(){ return LOCALIZE.convArguments("기타택배", arguments); };
            LOCALIZE.설명_상품은어떠셨나요 = function(){ return LOCALIZE.convArguments("상품은 어떠셨나요?", arguments); };
            LOCALIZE.설명_어떤점이좋으셨나요 = function(){ return LOCALIZE.convArguments("어떤 점이 좋으셨나요?", arguments); };
            LOCALIZE.설명_이메일또는아이디 = function(){ return LOCALIZE.convArguments("이메일 또는 아이디", arguments); };
            LOCALIZE.설명_새비밀번호확인 = function(){ return LOCALIZE.convArguments("새 비밀번호 확인", arguments); };
            LOCALIZE.타이틀_배송수단 = function(){ return LOCALIZE.convArguments("배송수단", arguments); };
            LOCALIZE.설명_접속하신국가는접속이제한되었습니다 = function(){ return LOCALIZE.convArguments("접속하신 국가는 접속이 제한되었습니다.", arguments); };
            LOCALIZE.버튼_카카오페이결제 = function(){ return LOCALIZE.convArguments("카카오페이", arguments); };
            LOCALIZE.타이틀_예약가능뱃지 = function(){ return LOCALIZE.convArguments("가", arguments); };
            LOCALIZE.타이틀_예약완료뱃지 = function(){ return LOCALIZE.convArguments("완", arguments); };
            LOCALIZE.타이틀_입금대기뱃지 = function(){ return LOCALIZE.convArguments("대", arguments); };
            LOCALIZE.버튼_마케팅활용동의및광고수신동의 = function(){ return LOCALIZE.convArguments("마케팅 활용 동의 및 광고 수신 동의", arguments); };
            LOCALIZE.타이틀_주문상품정보 = function(){ return LOCALIZE.convArguments("주문 상품 정보", arguments); };
            LOCALIZE.타이틀_배송지정보 = function(){ return LOCALIZE.convArguments("배송지 정보", arguments); };
            LOCALIZE.설명_상품이없습니다 = function(){ return LOCALIZE.convArguments("상품이 없습니다.", arguments); };
            LOCALIZE.설명_n개구매 = function(){ return LOCALIZE.convArguments("%1개 구매", arguments); };
            LOCALIZE.설명_n개구매평 = function(){ return LOCALIZE.convArguments("%1개 구매평", arguments); };
            LOCALIZE.설명_포토구매평모아보기 = function(){ return LOCALIZE.convArguments("포토 구매평 모아보기", arguments); };
            LOCALIZE.설명_최소n글자이상 = function(){ return LOCALIZE.convArguments("최소 %1글자 이상", arguments); };
            LOCALIZE.설명_대문자 = function(){ return LOCALIZE.convArguments("대문자", arguments); };
            LOCALIZE.설명_숫자 = function(){ return LOCALIZE.convArguments("숫자", arguments); };
            LOCALIZE.설명_특수문자 = function(){ return LOCALIZE.convArguments("특수문자", arguments); };
            LOCALIZE.설명_포함필수 = function(){ return LOCALIZE.convArguments("%1 포함필수", arguments); };
            LOCALIZE.타이틀_반품배송비차감 = function(){ return LOCALIZE.convArguments("반품 배송비 차감", arguments); };
            LOCALIZE.타이틀_PC모드로보기 = function(){ return LOCALIZE.convArguments("PC 모드로 보기", arguments); };
            LOCALIZE.설명_남은다운로드n회 = function(){ return LOCALIZE.convArguments("남은 다운로드: %1회", arguments); };
            LOCALIZE.타이틀_취소사유 = function(){ return LOCALIZE.convArguments("취소사유", arguments); };
            LOCALIZE.타이틀_취소요청사유 = function(){ return LOCALIZE.convArguments("취소요청사유", arguments); };
            LOCALIZE.타이틀_취소조회 = function(){ return LOCALIZE.convArguments("취소 조회", arguments); };
            LOCALIZE.설명_배송국가 = function(){ return LOCALIZE.convArguments("배송 국가", arguments); };
            LOCALIZE.설명_가입승인되지않은아이디입니다 = function(){ return LOCALIZE.convArguments("가입승인 대기 중입니다. 운영자의 승인 후 이용하실 수 있습니다.", arguments); };
            LOCALIZE.설명_회원등급할인 = function(){ return LOCALIZE.convArguments("회원등급 할인", arguments); };
            LOCALIZE.설명_결제예상금액 = function(){ return LOCALIZE.convArguments("총 상품금액(%1개)", arguments); };
            LOCALIZE.타이틀_n님의가입이승인되었습니다 = function(){ return LOCALIZE.convArguments("님의 가입이 승인되었어요", arguments); };
            LOCALIZE.내용_정상적으로사이트이용가능 = function(){ return LOCALIZE.convArguments("이제 정상적으로 사이트 이용이 가능합니다.", arguments); };
            LOCALIZE.설명_면제 = function(){ return LOCALIZE.convArguments("면제", arguments); };
            LOCALIZE.설명_회원탈퇴를진행하시겠습니까 = function(){ return LOCALIZE.convArguments("회원 탈퇴를 진행하시겠습니까?", arguments); };
            LOCALIZE.버튼_포토구매평 = function(){ return LOCALIZE.convArguments("포토 구매평", arguments); };
            LOCALIZE.설명_누적구매금액s = function(){ return LOCALIZE.convArguments("누적 구매금액: %1", arguments); };
            LOCALIZE.타이틀_s님안녕하세요 = function(){ return LOCALIZE.convArguments("%1 님 안녕하세요.", arguments); };
            LOCALIZE.타이틀_s회원가 = function(){ return LOCALIZE.convArguments("%1 회원가", arguments); };
            LOCALIZE.타이틀_판매가 = function(){ return LOCALIZE.convArguments("판매가", arguments); };
            LOCALIZE.설명_현재재고부족으로N개이상구매할수없습니다 = function(){ return LOCALIZE.convArguments("현재 재고 부족으로 %1개 이상 구매할 수 없습니다.", arguments); };
            LOCALIZE.타이틀_주류의통신판매신고에따른명령위임고시 = function(){ return LOCALIZE.convArguments("주류의 통신판매 신고에 따른 명령위임고시", arguments); };
            LOCALIZE.설명_관계법령에따라미셩년자는구매할수없음 = function(){ return LOCALIZE.convArguments("관계법령에 따라 미성년자는 구매할 수 없으며,<br/>19세 이상 성인인증을 하셔야 구매 가능한 상품입니다.", arguments); };
            LOCALIZE.타이틀_탈퇴한회원 = function(){ return LOCALIZE.convArguments("탈퇴한 회원", arguments); };
            LOCALIZE.타이틀_쇼핑입력폼 = function(){ return LOCALIZE.convArguments("추가정보 입력", arguments); };
            LOCALIZE.버튼_엑심베이 = function(){ return LOCALIZE.convArguments("엑심베이", arguments); };
            LOCALIZE.버튼_IDPW회원가입 = function(){ return LOCALIZE.convArguments("ID/PW 회원가입", arguments); };
            LOCALIZE.설명_암호길이가짧습니다_n자이상 = function(){ return LOCALIZE.convArguments("암호 길이가 짧습니다.(%1자이상)", arguments); };
            LOCALIZE.설명_처리대기 = function(){ return LOCALIZE.convArguments("처리대기", arguments); };
            LOCALIZE.설명_답변완료 = function(){ return LOCALIZE.convArguments("답변완료", arguments); };
            LOCALIZE.버튼_상품문의 = function(){ return LOCALIZE.convArguments("상품문의", arguments); };
            LOCALIZE.버튼_장바구니가기 = function(){ return LOCALIZE.convArguments("장바구니", arguments); };
            LOCALIZE.설명_가입하시면이용약관에동의하게됩니다tag = function(){ return LOCALIZE.convArguments("가입하시면 <a href=\'javascript:;\' %1>이용약관</a>에 동의하게됩니다.", arguments); };
            LOCALIZE.설명_포토_구매평만_보기 = function(){ return LOCALIZE.convArguments("포토 구매평만 보기", arguments); };
            LOCALIZE.버튼_구매평작성 = function(){ return LOCALIZE.convArguments("구매평 작성", arguments); };
            LOCALIZE.설명_SMS수신동의 = function(){ return LOCALIZE.convArguments("SMS 수신 동의", arguments); };
            LOCALIZE.설명_Email수신동의 = function(){ return LOCALIZE.convArguments("E-Mail 수신 동의", arguments); };
            LOCALIZE.버튼_필수및선택사항모두동의 = function(){ return LOCALIZE.convArguments("%1에 모두 동의합니다.", arguments); };
            LOCALIZE.설명_적립금액은쿠폰적용에따라달라짐 = function(){ return LOCALIZE.convArguments("적립금액은 할인 쿠폰 적용 및 옵션 가격, 수량을 기준으로 적립되므로 최종 적립금액은 쿠폰 사용 여부 및 옵션 가격, 수량에 따라 달라질 수 있습니다.", arguments); };
            LOCALIZE.설명_재고 = function(){ return LOCALIZE.convArguments("재고", arguments); };
            LOCALIZE.타이틀_남은재고 = function(){ return LOCALIZE.convArguments("남은 재고", arguments); };
            LOCALIZE.설명_상품최소구매수량 = function(){ return LOCALIZE.convArguments("%1 상품의 최소 구매수량은 %2개 입니다.", arguments); };
            LOCALIZE.설명_이상품은현재판매기간이아닙니다 = function(){ return LOCALIZE.convArguments("이 상품은 현재 판매기간이 아닙니다.", arguments); };
            LOCALIZE.설명_회원당최대구매수량 = function(){ return LOCALIZE.convArguments("1인당 최대 구매수량은 %1개 입니다.", arguments); };
            LOCALIZE.설명_비회원은회원당최대구매수량제한상품주문불가 = function(){ return LOCALIZE.convArguments("비회원은 1인 구매 시 최대 수량 제한이 걸린 상품을 주문할 수 없습니다.", arguments); };
            LOCALIZE.타이틀_최소구매수량 = function(){ return LOCALIZE.convArguments("최소 구매수량", arguments); };
            LOCALIZE.설명_최소구매수량 = function(){ return LOCALIZE.convArguments("최소 구매수량은 %1개 입니다.", arguments); };
            LOCALIZE.타이틀_제조사 = function(){ return LOCALIZE.convArguments("제조사", arguments); };
            LOCALIZE.타이틀_브랜드 = function(){ return LOCALIZE.convArguments("브랜드", arguments); };
            LOCALIZE.타이틀_사이트준비중 = function(){ return LOCALIZE.convArguments("사이트 준비중", arguments); };
            LOCALIZE.타이틀_현재사이트는준비중 = function(){ return LOCALIZE.convArguments("현재 사이트는 준비중입니다.", arguments); };
            LOCALIZE.버튼_관리자로그인 = function(){ return LOCALIZE.convArguments("관리자 로그인", arguments); };
            LOCALIZE.버튼_개인정보제3자제공동의 = function(){ return LOCALIZE.convArguments("개인정보 제3자 제공 동의", arguments); };
            LOCALIZE.버튼_위사항을확인하였으며개인정보제3자제공에동의합니다 = function(){ return LOCALIZE.convArguments("개인정보 제3자 제공에 대해 동의합니다.", arguments); };
            LOCALIZE.설명_개인정보제3자제공에동의하여주시기바랍니다 = function(){ return LOCALIZE.convArguments("개인정보 제 3자 제공에 동의하여 주시기 바랍니다.", arguments); };
            LOCALIZE.타이틀_게시판카테고리 = function(){ return LOCALIZE.convArguments("카테고리", arguments); };
            LOCALIZE.타이틀_게시판카테고리전체보기 = function(){ return LOCALIZE.convArguments("전체보기", arguments); };
            LOCALIZE.타이틀_글쓰기카테고리선택 = function(){ return LOCALIZE.convArguments("카테고리", arguments); };
            LOCALIZE.타이틀_추가정보입력 = function(){ return LOCALIZE.convArguments("추가정보 입력", arguments); };
            LOCALIZE.설명_주문후n시간미입금시자동취소 = function(){ return LOCALIZE.convArguments("주문 후 %1시간 동안 미입금시 자동 취소됩니다.", arguments); };
            LOCALIZE.설명_배송받을국가를선택해주세요 = function(){ return LOCALIZE.convArguments("배송 받을 국가를 선택해주세요.", arguments); };
            LOCALIZE.설명_무료결제안내문구2 = function(){ return LOCALIZE.convArguments("다른 결제수단을 이용하시려면 %1 사용금액을 변경해주세요.", arguments); };
            LOCALIZE.설명_성별을선택하세요 = function(){ return LOCALIZE.convArguments("성별을 선택하세요.", arguments); };
            LOCALIZE.타이틀_구매혜택 = function(){ return LOCALIZE.convArguments("구매혜택", arguments); };
            LOCALIZE.타이틀_item = function(){ return LOCALIZE.convArguments("item", arguments); };
            LOCALIZE.설명_거리주소 = function(){ return LOCALIZE.convArguments("거리주소 (Street address, P.O box, company name, c/o)", arguments); };
            LOCALIZE.설명_건물명 = function(){ return LOCALIZE.convArguments("건물명 (Apartment, suite, unit, building, floor, etc.)", arguments); };
            LOCALIZE.설명_도시명 = function(){ return LOCALIZE.convArguments("도시명 (City)", arguments); };
            LOCALIZE.설명_도시군 = function(){ return LOCALIZE.convArguments("도시군 (State/Province/Region)", arguments); };
            LOCALIZE.설명_방문하실일자및시간대를입력해주세요 = function(){ return LOCALIZE.convArguments("방문하실 일자 및 시간대를 입력해주세요", arguments); };
            LOCALIZE.설명_배송메모직접입력 = function(){ return LOCALIZE.convArguments("직접입력", arguments); };
            LOCALIZE.설명_입금자명미입력시주문자명 = function(){ return LOCALIZE.convArguments("입금자명 (미입력시 주문자명)", arguments); };
            LOCALIZE.설명_n개 = function(){ return LOCALIZE.convArguments("%1 개", arguments); };
            LOCALIZE.타이틀_교환사유 = function(){ return LOCALIZE.convArguments("교환사유", arguments); };
            LOCALIZE.타이틀_교환요청사유 = function(){ return LOCALIZE.convArguments("교환요청사유", arguments); };
            LOCALIZE.타이틀_교환배송비결제방법 = function(){ return LOCALIZE.convArguments("결제방법", arguments); };
            LOCALIZE.타이틀_교환수거정보 = function(){ return LOCALIZE.convArguments("교환 수거정보", arguments); };
            LOCALIZE.설명_교환배송비수거시박스에동봉 = function(){ return LOCALIZE.convArguments("수거시 박스에 동봉", arguments); };
            LOCALIZE.설명_교환배송비판매자에게송금 = function(){ return LOCALIZE.convArguments("판매자에게 송금", arguments); };
            LOCALIZE.설명_반품배송비수거시박스에동봉 = function(){ return LOCALIZE.convArguments("수거시 박스에 동봉", arguments); };
            LOCALIZE.타이틀_반품사유및환불계좌 = function(){ return LOCALIZE.convArguments("반품 사유 및 환불계좌", arguments); };
            LOCALIZE.타이틀_반품요청사유 = function(){ return LOCALIZE.convArguments("반품요청사유", arguments); };
            LOCALIZE.타이틀_반품배송비결제방법 = function(){ return LOCALIZE.convArguments("결제방법", arguments); };
            LOCALIZE.타이틀_주문자정보 = function(){ return LOCALIZE.convArguments("주문자 정보", arguments); };
            LOCALIZE.타이틀_교환비용구매자부담 = function(){ return LOCALIZE.convArguments("교환비용 구매자 부담", arguments); };
            LOCALIZE.타이틀_환불진행중 = function(){ return LOCALIZE.convArguments("환불진행중", arguments); };
            LOCALIZE.설명_예약취소사유다른상품으로변경 = function(){ return LOCALIZE.convArguments("다른 상품으로 변경", arguments); };
            LOCALIZE.설명_쇼핑클레임사유구매의사취소 = function(){ return LOCALIZE.convArguments("구매 의사 취소", arguments); };
            LOCALIZE.설명_쇼핑클레임사유색상및사이즈변경 = function(){ return LOCALIZE.convArguments("색상 및 사이즈 변경", arguments); };
            LOCALIZE.설명_쇼핑클레임사유다른상품잘못주문 = function(){ return LOCALIZE.convArguments("다른 상품 잘못 주문", arguments); };
            LOCALIZE.설명_쇼핑클레임사유서비스및상품불만족 = function(){ return LOCALIZE.convArguments("서비스 및 상품 불만족", arguments); };
            LOCALIZE.설명_쇼핑클레임사유배송지연 = function(){ return LOCALIZE.convArguments("배송 지연", arguments); };
            LOCALIZE.설명_쇼핑클레임사유배송누락 = function(){ return LOCALIZE.convArguments("배송 누락", arguments); };
            LOCALIZE.설명_쇼핑클레임사유상품품절 = function(){ return LOCALIZE.convArguments("상품 품절", arguments); };
            LOCALIZE.설명_쇼핑클레임사유상품파손 = function(){ return LOCALIZE.convArguments("상품 파손", arguments); };
            LOCALIZE.설명_쇼핑클레임사유상품정보상이 = function(){ return LOCALIZE.convArguments("상품 정보 상이", arguments); };
            LOCALIZE.설명_쇼핑클레임사유오배송 = function(){ return LOCALIZE.convArguments("오배송", arguments); };
            LOCALIZE.설명_쇼핑클레임사유색상등이다른상품을잘못배송 = function(){ return LOCALIZE.convArguments("색상 등이 다른 상품을 잘못 배송", arguments); };
            LOCALIZE.타이틀_예약시요청사 = function(){ return LOCALIZE.convArguments("예약시 요청사항", arguments); };
            LOCALIZE.타이틀_배송지역 = function(){ return LOCALIZE.convArguments("배송 지역", arguments); };
            LOCALIZE.설명_국가를선택해주세요 = function(){ return LOCALIZE.convArguments("국가를 선택해주세요.", arguments); };
            LOCALIZE.버튼_주문상세보기 = function(){ return LOCALIZE.convArguments("주문 상세보기", arguments); };
            LOCALIZE.타이틀_결제방법 = function(){ return LOCALIZE.convArguments("결제방법", arguments); };
            LOCALIZE.설명_우편번호 = function(){ return LOCALIZE.convArguments("우편번호", arguments); };
            LOCALIZE.설명_마이페이지취소요청설명1 = function(){ return LOCALIZE.convArguments("주문하신 상품 단위로 취소요청이 가능합니다.(수량 부분취소 불가)<br/>상품이 발송되기 전에 취소요청을 하실 수 있습니다.", arguments); };
            LOCALIZE.설명_마이페이지취소요청설명2 = function(){ return LOCALIZE.convArguments("단, 상품을 이미 발송한 경우 취소처리가 거부될 수 있습니다.<br/>쿠폰을 사용한 주문을 취소/반품하여 쿠폰 사용이 취소된 경우 유효기간이 경과하지 않았으면 반환되어 다시 사용이 가능합니다.<br/>(쿠폰의 경우 모든 상품을 취소/반품해야 반환됩니다.)", arguments); };
            LOCALIZE.타이틀_취소처리중 = function(){ return LOCALIZE.convArguments("취소처리중", arguments); };
            LOCALIZE.타이틀_교환재배송중 = function(){ return LOCALIZE.convArguments("교환재배송중", arguments); };
            LOCALIZE.설명_선택 = function(){ return LOCALIZE.convArguments("(선택)", arguments); };
            LOCALIZE.타이틀_평점 = function(){ return LOCALIZE.convArguments("평점", arguments); };
            LOCALIZE.타이틀_배송안내 = function(){ return LOCALIZE.convArguments("배송 안내", arguments); };
            LOCALIZE.버튼_가나다 = function(){ return LOCALIZE.convArguments("이름순", arguments); };
            LOCALIZE.버튼_가나다역순 = function(){ return LOCALIZE.convArguments("이름역순", arguments); };
            LOCALIZE.타이틀_대표이미지설정 = function(){ return LOCALIZE.convArguments("대표 이미지 설정", arguments); };
            LOCALIZE.설명_비밀번호확인 = function(){ return LOCALIZE.convArguments("비밀번호 확인", arguments); };
            LOCALIZE.타이틀_여행약관 = function(){ return LOCALIZE.convArguments("여행약관", arguments); };
            LOCALIZE.타이틀_국내여행약관 = function(){ return LOCALIZE.convArguments("국내 여행약관", arguments); };
            LOCALIZE.타이틀_국외여행약관 = function(){ return LOCALIZE.convArguments("국외 여행약관", arguments); };
            LOCALIZE.타이틀_주문취소요청 = function(){ return LOCALIZE.convArguments("주문 취소요청", arguments); };
            LOCALIZE.타이틀_월 = function(){ return LOCALIZE.convArguments("월", arguments); };
            LOCALIZE.타이틀_일 = function(){ return LOCALIZE.convArguments("일", arguments); };
            LOCALIZE.설명_soldout = function(){ return LOCALIZE.convArguments("SOLDOUT", arguments); };
            LOCALIZE.설명_n님이댓글을작성하였습니다 = function(){ return LOCALIZE.convArguments("%1님이 댓글을 남겼어요.", arguments); };
            LOCALIZE.설명_비밀번호가필요합니다 = function(){ return LOCALIZE.convArguments("비밀번호가 필요합니다.", arguments); };
            LOCALIZE.설명_상품금액 = function(){ return LOCALIZE.convArguments("상품금액", arguments); };
            LOCALIZE.설명_비밀글입니다 = function(){ return LOCALIZE.convArguments("비밀글입니다.", arguments); };
            LOCALIZE.설명_위치정보검색을허용해주세요 = function(){ return LOCALIZE.convArguments("위치정보 검색을 허용해주세요.", arguments); };
            LOCALIZE.설명_작성시등록하신비밀번호를입력해주세요 = function(){ return LOCALIZE.convArguments("작성시 등록하신 비밀번호를 입력해주세요.", arguments); };
            LOCALIZE.설명_성인인증안내문구 = function(){ return LOCALIZE.convArguments("<h4>이 정보 내용은 청소년 유해매체물로서 정보통신망 이용촉진 및 정보보호등에 관한 법률 및 청소년 보호법 규정에 의해 <span style=\"color:#FB2B45\">19세 미만 청소년</span>이 이용할 수 없습니다.</h4>", arguments); };
            LOCALIZE.설명_성인인증안내문구2 = function(){ return LOCALIZE.convArguments("본 서비스를 이용하기 위해서는 성인인증 절차가 필요합니다.", arguments); };
            LOCALIZE.버튼_19세미만나가기 = function(){ return LOCALIZE.convArguments("19세 미만 나가기", arguments); };
            LOCALIZE.설명_내용을입력하세요 = function(){ return LOCALIZE.convArguments("내용을 입력 하세요.", arguments); };
            LOCALIZE.내용_무통장입금알림 = function(){ return LOCALIZE.convArguments("입금계좌 [%1], %2", arguments); };
            LOCALIZE.설명_알림이없습니다 = function(){ return LOCALIZE.convArguments("알림이 없습니다", arguments); };
            LOCALIZE.설명_아이디를입력하세요 = function(){ return LOCALIZE.convArguments("아이디를 입력 하세요.", arguments); };
            LOCALIZE.설명_비밀번호를입력하세요 = function(){ return LOCALIZE.convArguments("비밀번호를 입력 하세요.", arguments); };
            LOCALIZE.설명_동의해주세요 = function(){ return LOCALIZE.convArguments("이용약관 및 개인정보 처리방침에 동의하셔야 가입이 가능합니다.", arguments); };
            LOCALIZE.설명_이메일을정확히입력하세요 = function(){ return LOCALIZE.convArguments("이메일을 정확히 입력하세요", arguments); };
            LOCALIZE.설명_새입력폼등록tag = function(){ return LOCALIZE.convArguments("<span style=\"color: %1\">새 입력폼 응답이 접수</span>되었습니다.", arguments); };
            LOCALIZE.설명_사이트에가입해주셔서진심으로감사드립니다tag = function(){ return LOCALIZE.convArguments("사이트에 가입해 주셔서 진심으로 감사드립니다.<br>많은 방문 부탁드려요~!", arguments); };
            LOCALIZE.설명_주문을완료하기위해서입금해주시기바랍니다tag = function(){ return LOCALIZE.convArguments("주문을 완료하기 위해서는 <span style=\"color:#FB2B45\">%1까지 아래 계좌로 입금<span>해 주시기 바랍니다.", arguments); };
            LOCALIZE.타이틀_회원가입을환영합니다 = function(){ return LOCALIZE.convArguments("회원가입을 환영합니다.", arguments); };
            LOCALIZE.버튼_문의작성 = function(){ return LOCALIZE.convArguments("문의 작성", arguments); };
            LOCALIZE.타이틀_적립예정 = function(){ return LOCALIZE.convArguments("적립예정", arguments); };
            LOCALIZE.타이틀_조건부무료배송 = function(){ return LOCALIZE.convArguments("%1 이상 무료배송", arguments); };
            LOCALIZE.버튼_회원탈퇴 = function(){ return LOCALIZE.convArguments("회원탈퇴", arguments); };
            LOCALIZE.버튼_파일올리기 = function(){ return LOCALIZE.convArguments("파일 올리기", arguments); };
            LOCALIZE.버튼_상세보기 = function(){ return LOCALIZE.convArguments("상세보기", arguments); };
            LOCALIZE.설명_주문 = function(){ return LOCALIZE.convArguments("주문", arguments); };
            LOCALIZE.설명_배송전에미리연락바랍니다 = function(){ return LOCALIZE.convArguments("배송 전에 미리 연락 바랍니다.", arguments); };
            LOCALIZE.설명_부재시경비실에맡겨주세요 = function(){ return LOCALIZE.convArguments("부재시 경비실에 맡겨주세요.", arguments); };
            LOCALIZE.설명_부재시전화나문자를남겨주세요 = function(){ return LOCALIZE.convArguments("부재시 전화나 문자를 남겨주세요.", arguments); };
            LOCALIZE.설명_직접입력 = function(){ return LOCALIZE.convArguments("직접입력", arguments); };
            LOCALIZE.설명_없음 = function(){ return LOCALIZE.convArguments("없음", arguments); };
            LOCALIZE.설명_가입한이메일또는아이디 = function(){ return LOCALIZE.convArguments("가입한 이메일 또는 아이디", arguments); };
            LOCALIZE.타이틀_판매가비공개 = function(){ return LOCALIZE.convArguments("판매가 비공개", arguments); };
            LOCALIZE.설명_소유자만구매가능1 = function(){ return LOCALIZE.convArguments("가격조회 및 구매가 허용되지 않은 상품입니다. 관리자에게 문의 바랍니다.", arguments); };
            LOCALIZE.설명_소유자만구매가능2 = function(){ return LOCALIZE.convArguments("가격조회 및 구매가 허용되지 않은 상품이 포함 되어 있습니다.", arguments); };
            LOCALIZE.설명_그룹만구매가능1 = function(){ return LOCALIZE.convArguments("특정 회원만 가격조회 및 구매가 가능한 상품입니다.", arguments); };
            LOCALIZE.타이틀_판매가회원공개 = function(){ return LOCALIZE.convArguments("판매가 회원공개", arguments); };
            LOCALIZE.타이틀_퀵서비스 = function(){ return LOCALIZE.convArguments("퀵서비스", arguments); };
            LOCALIZE.타이틀_착불및선결제 = function(){ return LOCALIZE.convArguments("착불 및 선결제", arguments); };
            LOCALIZE.타이틀_배송없음 = function(){ return LOCALIZE.convArguments("배송없음", arguments); };
            LOCALIZE.타이틀_무게별차등배송비 = function(){ return LOCALIZE.convArguments("무게별 차등 배송비", arguments); };
            LOCALIZE.타이틀_배송중 = function(){ return LOCALIZE.convArguments("배송중", arguments); };
            LOCALIZE.타이틀_배송완료 = function(){ return LOCALIZE.convArguments("배송완료", arguments); };
            LOCALIZE.타이틀_취소완료 = function(){ return LOCALIZE.convArguments("취소완료", arguments); };
            LOCALIZE.타이틀_개인통관고유부호 = function(){ return LOCALIZE.convArguments("개인통관고유부호", arguments); };
            LOCALIZE.타이틀_배송받을국가 = function(){ return LOCALIZE.convArguments("배송받을 국가", arguments); };
            LOCALIZE.타이틀_택배 = function(){ return LOCALIZE.convArguments("택배", arguments); };
            LOCALIZE.타이틀_직접배송 = function(){ return LOCALIZE.convArguments("직접배송", arguments); };
            LOCALIZE.설명_주문자연락처를입력해주세요 = function(){ return LOCALIZE.convArguments("주문자 연락처를 입력해주세요", arguments); };
            LOCALIZE.설명_생년월일 = function(){ return LOCALIZE.convArguments("생년월일", arguments); };
            LOCALIZE.타이틀_비밀번호찾기 = function(){ return LOCALIZE.convArguments("비밀번호 찾기", arguments); };
            LOCALIZE.버튼_반품교환 = function(){ return LOCALIZE.convArguments("반품/교환", arguments); };
            LOCALIZE.타이틀_결제완료 = function(){ return LOCALIZE.convArguments("결제완료", arguments); };
            LOCALIZE.설명_배송준비중입니다 = function(){ return LOCALIZE.convArguments("주문하신 상품을 배송준비중이에요. (주문번호 %1)", arguments); };
            LOCALIZE.타이틀_반품요청 = function(){ return LOCALIZE.convArguments("반품요청", arguments); };
            LOCALIZE.타이틀_반품수거진행중 = function(){ return LOCALIZE.convArguments("반품수거중", arguments); };
            LOCALIZE.타이틀_반품수거완료 = function(){ return LOCALIZE.convArguments("반품수거완료", arguments); };
            LOCALIZE.타이틀_반품완료 = function(){ return LOCALIZE.convArguments("반품완료", arguments); };
            LOCALIZE.타이틀_교환요청 = function(){ return LOCALIZE.convArguments("교환요청", arguments); };
            LOCALIZE.타이틀_교환수거진행중 = function(){ return LOCALIZE.convArguments("수거진행중", arguments); };
            LOCALIZE.타이틀_교환수거완료 = function(){ return LOCALIZE.convArguments("교환수거완료", arguments); };
            LOCALIZE.타이틀_교환완료 = function(){ return LOCALIZE.convArguments("교환완료", arguments); };
            LOCALIZE.설명_배송없음 = function(){ return LOCALIZE.convArguments("배송없음", arguments); };
            LOCALIZE.설명_까지 = function(){ return LOCALIZE.convArguments("%1 까지", arguments); };
            LOCALIZE.타이틀_보유쿠폰 = function(){ return LOCALIZE.convArguments("보유쿠폰", arguments); };
            LOCALIZE.타이틀_쿠폰번호 = function(){ return LOCALIZE.convArguments("쿠폰번호", arguments); };
            LOCALIZE.설명_사용가능한쿠폰이없습니다 = function(){ return LOCALIZE.convArguments("사용 가능한 쿠폰이 없습니다", arguments); };
            LOCALIZE.설명_받을수있는쿠폰이없습니다 = function(){ return LOCALIZE.convArguments("받을 수 있는 쿠폰이 없습니다.", arguments); };
            LOCALIZE.설명_등록일 = function(){ return LOCALIZE.convArguments("등록일", arguments); };
            LOCALIZE.버튼_쿠폰적용 = function(){ return LOCALIZE.convArguments("쿠폰적용", arguments); };
            LOCALIZE.버튼_코드확인 = function(){ return LOCALIZE.convArguments("코드확인", arguments); };
            LOCALIZE.타이틀_쿠폰받기 = function(){ return LOCALIZE.convArguments("쿠폰받기", arguments); };
            LOCALIZE.타이틀_내가받은쿠폰 = function(){ return LOCALIZE.convArguments("내가 받은 쿠폰", arguments); };
            LOCALIZE.타이틀_새입력폼응답이접수되었습니다 = function(){ return LOCALIZE.convArguments("새 입력폼 응답이 접수되었습니다.", arguments); };
            LOCALIZE.설명_배송비 = function(){ return LOCALIZE.convArguments("배송비", arguments); };
            LOCALIZE.설명_수량 = function(){ return LOCALIZE.convArguments("수량", arguments); };
            LOCALIZE.설명_주문금액 = function(){ return LOCALIZE.convArguments("주문금액", arguments); };
            LOCALIZE.설명_주문상품 = function(){ return LOCALIZE.convArguments("주문상품", arguments); };
            LOCALIZE.설명_배송지 = function(){ return LOCALIZE.convArguments("배송지", arguments); };
            LOCALIZE.설명_수령인 = function(){ return LOCALIZE.convArguments("수령인", arguments); };
            LOCALIZE.설명_최종결제금액 = function(){ return LOCALIZE.convArguments("최종 결제금액", arguments); };
            LOCALIZE.설명_신용카드 = function(){ return LOCALIZE.convArguments("신용카드", arguments); };
            LOCALIZE.설명_결제수단 = function(){ return LOCALIZE.convArguments("결제수단", arguments); };
            LOCALIZE.설명_총주문금액 = function(){ return LOCALIZE.convArguments("총 주문금액", arguments); };
            LOCALIZE.설명_결제정보 = function(){ return LOCALIZE.convArguments("결제정보", arguments); };
            LOCALIZE.설명_주문일자 = function(){ return LOCALIZE.convArguments("주문일자", arguments); };
            LOCALIZE.설명_주문번호 = function(){ return LOCALIZE.convArguments("주문번호", arguments); };
            LOCALIZE.설명_성별 = function(){ return LOCALIZE.convArguments("성별", arguments); };
            LOCALIZE.설명_남자 = function(){ return LOCALIZE.convArguments("남자", arguments); };
            LOCALIZE.설명_여자 = function(){ return LOCALIZE.convArguments("여자", arguments); };
            LOCALIZE.설명_추가인원 = function(){ return LOCALIZE.convArguments("%1명", arguments); };
            LOCALIZE.버튼_비회원주문예약조회 = function(){ return LOCALIZE.convArguments("비회원 주문예약 조회", arguments); };
            LOCALIZE.타이틀_상태 = function(){ return LOCALIZE.convArguments("상태", arguments); };
            LOCALIZE.설명_상품구매시할인차감 = function(){ return LOCALIZE.convArguments("상품구매시 할인 차감 %1", arguments); };
            LOCALIZE.버튼_확인 = function(){ return LOCALIZE.convArguments("확인", arguments); };
            LOCALIZE.버튼_완료 = function(){ return LOCALIZE.convArguments("완료", arguments); };
            LOCALIZE.설명_작성자이름 = function(){ return LOCALIZE.convArguments("작성자 이름", arguments); };
            LOCALIZE.버튼_1일동안보지않음 = function(){ return LOCALIZE.convArguments("1일 동안 보지 않음", arguments); };
            LOCALIZE.버튼_닫기 = function(){ return LOCALIZE.convArguments("닫기", arguments); };
            LOCALIZE.설명_신규회원쇼핑지원금 = function(){ return LOCALIZE.convArguments("신규회원 쇼핑지원금", arguments); };
            LOCALIZE.설명_상품구매적립 = function(){ return LOCALIZE.convArguments("상품구매 적립", arguments); };
            LOCALIZE.타이틀_가격없음 = function(){ return LOCALIZE.convArguments("가격문의", arguments); };
            LOCALIZE.타이틀_상세설명_참조 = function(){ return LOCALIZE.convArguments("가격문의(상세정보 참조)", arguments); };
            LOCALIZE.버튼_페이팔 = function(){ return LOCALIZE.convArguments("페이팔", arguments); };
            LOCALIZE.버튼_이동 = function(){ return LOCALIZE.convArguments("이동", arguments); };
            LOCALIZE.설명_주문이완료되어입금대기중입니다 = function(){ return LOCALIZE.convArguments("주문을 완료하기 위해 입금해주세요.  (주문번호 %1)", arguments); };
            LOCALIZE.설명_님이게시물을작성하였습니다 = function(){ return LOCALIZE.convArguments("%1님이 게시물을 남겼어요.", arguments); };
            LOCALIZE.설명_소유자에게액세스를요청 = function(){ return LOCALIZE.convArguments("소유자에게 액세스를 요청하거나<br/>권한이 있는 계정으로 로그인 하세요.", arguments); };
            LOCALIZE.설명_총n개 = function(){ return LOCALIZE.convArguments("<em class=\"hidden-lg hidden-md \">총</em> %1개", arguments); };
            LOCALIZE.설명_품절된상품입니다 = function(){ return LOCALIZE.convArguments("품절된 상품입니다.", arguments); };
            LOCALIZE.설명_필수옵션이모두선택되어있지않습니다 = function(){ return LOCALIZE.convArguments("필수옵션이 모두 선택되어있지 않습니다.", arguments); };
            LOCALIZE.설명_비밀번호를자리이상입력해주세요 = function(){ return LOCALIZE.convArguments("비밀번호를 4자리 이상 입력해주세요.", arguments); };
            LOCALIZE.설명_SALE = function(){ return LOCALIZE.convArguments("SALE", arguments); };
            LOCALIZE.설명_필수입력 = function(){ return LOCALIZE.convArguments("필수입력", arguments); };
            LOCALIZE.설명_주문카드취소문구 = function(){ return LOCALIZE.convArguments("카드 결제는 영업일 기준 3일 이내에<br>자동 취소처리 됩니다.<br>주문을 취소하시겠습니까?", arguments); };
            LOCALIZE.타이틀_비회원로그인 = function(){ return LOCALIZE.convArguments("비회원 주문조회", arguments); };
            LOCALIZE.타이틀_개인정보처리방침 = function(){ return LOCALIZE.convArguments("개인정보처리방침", arguments); };
            LOCALIZE.타이틀_이용약관 = function(){ return LOCALIZE.convArguments("이용약관", arguments); };
            LOCALIZE.타이틀_회원탈퇴 = function(){ return LOCALIZE.convArguments("회원탈퇴", arguments); };
            LOCALIZE.설명_탈퇴문구 = function(){ return LOCALIZE.convArguments("가입된 회원정보가 모두 삭제됩니다. 작성하신 게시물은 삭제되지 않습니다.", arguments); };
            LOCALIZE.버튼_탈퇴하기 = function(){ return LOCALIZE.convArguments("탈퇴하기", arguments); };
            LOCALIZE.버튼_메뉴더보기 = function(){ return LOCALIZE.convArguments("더보기", arguments); };
            LOCALIZE.설명_작성권한이없습니다 = function(){ return LOCALIZE.convArguments("작성 권한이 없습니다.", arguments); };
            LOCALIZE.설명_비밀번호가일치하지않습니다 = function(){ return LOCALIZE.convArguments("비밀번호가 일치하지 않습니다.", arguments); };
            LOCALIZE.설명_준비중입니다 = function(){ return LOCALIZE.convArguments("준비중입니다", arguments); };
            LOCALIZE.버튼_글쓰기 = function(){ return LOCALIZE.convArguments("글쓰기", arguments); };
            LOCALIZE.버튼_더보기 = function(){ return LOCALIZE.convArguments("더보기", arguments); };
            LOCALIZE.버튼_목록 = function(){ return LOCALIZE.convArguments("목록", arguments); };
            LOCALIZE.설명_권한이_없습니다 = function(){ return LOCALIZE.convArguments("권한이 없습니다.", arguments); };
            LOCALIZE.설명_로그인이_필요합니다 = function(){ return LOCALIZE.convArguments("로그인이 필요합니다.", arguments); };
            LOCALIZE.타이틀_조회수 = function(){ return LOCALIZE.convArguments("조회수", arguments); };
            LOCALIZE.타이틀_조회 = function(){ return LOCALIZE.convArguments("조회", arguments); };
            LOCALIZE.타이틀_공지 = function(){ return LOCALIZE.convArguments("공지", arguments); };
            LOCALIZE.버튼_댓글 = function(){ return LOCALIZE.convArguments("댓글", arguments); };
            LOCALIZE.설명_댓글을_남겨주세요 = function(){ return LOCALIZE.convArguments("댓글을 남겨주세요", arguments); };
            LOCALIZE.설명_내용을_입력해주세요 = function(){ return LOCALIZE.convArguments("내용을 입력해주세요", arguments); };
            LOCALIZE.설명_삭제된_댓글_입니다 = function(){ return LOCALIZE.convArguments("삭제된 댓글입니다.", arguments); };
            LOCALIZE.설명_이름 = function(){ return LOCALIZE.convArguments("이름", arguments); };
            LOCALIZE.설명_비밀번호 = function(){ return LOCALIZE.convArguments("비밀번호", arguments); };
            LOCALIZE.버튼_작성완료 = function(){ return LOCALIZE.convArguments("작성완료", arguments); };
            LOCALIZE.버튼_수정 = function(){ return LOCALIZE.convArguments("수정", arguments); };
            LOCALIZE.버튼_지우기 = function(){ return LOCALIZE.convArguments("지우기", arguments); };
            LOCALIZE.버튼_취소 = function(){ return LOCALIZE.convArguments("취소", arguments); };
            LOCALIZE.설명_권한이_없습니다_권한이_있는_계정으로_로그인_하세요 = function(){ return LOCALIZE.convArguments("권한이 없습니다.<br>권한이 있는 계정으로 로그인 하세요.", arguments); };
            LOCALIZE.버튼_로그인 = function(){ return LOCALIZE.convArguments("로그인", arguments); };
            LOCALIZE.설명_가입승인이_필요한_서비스입니다 = function(){ return LOCALIZE.convArguments("가입승인이 필요한 서비스입니다.", arguments); };
            LOCALIZE.타이틀_글쓴이 = function(){ return LOCALIZE.convArguments("글쓴이", arguments); };
            LOCALIZE.타이틀_작성시간 = function(){ return LOCALIZE.convArguments("작성시간", arguments); };
            LOCALIZE.타이틀_제목 = function(){ return LOCALIZE.convArguments("제목", arguments); };
            LOCALIZE.설명_게시물이_없습니다 = function(){ return LOCALIZE.convArguments("게시물이 없습니다.", arguments); };
            LOCALIZE.버튼_내_위치 = function(){ return LOCALIZE.convArguments("내 위치", arguments); };
            LOCALIZE.버튼_등록순 = function(){ return LOCALIZE.convArguments("등록순", arguments); };
            LOCALIZE.버튼_지도 = function(){ return LOCALIZE.convArguments("지도", arguments); };
            LOCALIZE.설명_지도_게시물이_없습니다 = function(){ return LOCALIZE.convArguments("지도 게시물이 없습니다", arguments); };
            LOCALIZE.설명_비밀글_입니다 = function(){ return LOCALIZE.convArguments("비밀글 입니다.", arguments); };
            LOCALIZE.타이틀_비회원 = function(){ return LOCALIZE.convArguments("비회원", arguments); };
            LOCALIZE.타이틀_좋아요 = function(){ return LOCALIZE.convArguments("좋아요", arguments); };
            LOCALIZE.설명_게시물을_조회하려면_로그인이_필요합니다 = function(){ return LOCALIZE.convArguments("게시물을 조회하려면 로그인이 필요합니다.", arguments); };
            LOCALIZE.설명_비밀번호를_입력해주세요 = function(){ return LOCALIZE.convArguments("비밀번호를 입력해주세요.", arguments); };
            LOCALIZE.버튼_비밀번호_입력 = function(){ return LOCALIZE.convArguments("비밀번호 입력", arguments); };
            LOCALIZE.버튼_답변 = function(){ return LOCALIZE.convArguments("답변", arguments); };
            LOCALIZE.버튼_작성 = function(){ return LOCALIZE.convArguments("작성", arguments); };
            LOCALIZE.타이틀_전체 = function(){ return LOCALIZE.convArguments("전체", arguments); };
            LOCALIZE.타이틀_작성자 = function(){ return LOCALIZE.convArguments("작성자", arguments); };
            LOCALIZE.설명_SEARCH = function(){ return LOCALIZE.convArguments("Search", arguments); };
            LOCALIZE.버튼_인기순 = function(){ return LOCALIZE.convArguments("인기순", arguments); };
            LOCALIZE.버튼_낮은가격순 = function(){ return LOCALIZE.convArguments("낮은가격순", arguments); };
            LOCALIZE.버튼_높은가격순 = function(){ return LOCALIZE.convArguments("높은가격순", arguments); };
            LOCALIZE.버튼_상품평많은순 = function(){ return LOCALIZE.convArguments("상품평 많은순", arguments); };
            LOCALIZE.설명_해당카테고리에상품이없습니다 = function(){ return LOCALIZE.convArguments("해당 카테고리에 상품이 없습니다.", arguments); };
            LOCALIZE.버튼_구매하기 = function(){ return LOCALIZE.convArguments("구매하기", arguments); };
            LOCALIZE.버튼_장바구니 = function(){ return LOCALIZE.convArguments("장바구니", arguments); };
            LOCALIZE.타이틀_장바구니 = function(){ return LOCALIZE.convArguments("장바구니", arguments); };
            LOCALIZE.설명_선택하신상품을장바구니에담았습니다 = function(){ return LOCALIZE.convArguments("선택하신 상품을 장바구니에 담았습니다.", arguments); };
            LOCALIZE.버튼_계속쇼핑 = function(){ return LOCALIZE.convArguments("계속쇼핑", arguments); };
            LOCALIZE.타이틀_상세정보 = function(){ return LOCALIZE.convArguments("상세정보", arguments); };
            LOCALIZE.타이틀_구매평 = function(){ return LOCALIZE.convArguments("구매평", arguments); };
            LOCALIZE.타이틀_QNA = function(){ return LOCALIZE.convArguments("Q&A", arguments); };
            LOCALIZE.타이틀_상품정보제공고시 = function(){ return LOCALIZE.convArguments("상품정보 제공고시", arguments); };
            LOCALIZE.버튼_다운로드 = function(){ return LOCALIZE.convArguments("다운로드", arguments); };
            LOCALIZE.타이틀_원산지 = function(){ return LOCALIZE.convArguments("원산지", arguments); };
            LOCALIZE.타이틀_배송비 = function(){ return LOCALIZE.convArguments("배송비", arguments); };
            LOCALIZE.타이틀_배송비착불 = function(){ return LOCALIZE.convArguments("배송(착불)", arguments); };
            LOCALIZE.타이틀_도서산간배송비 = function(){ return LOCALIZE.convArguments("도서산간배송비", arguments); };
            LOCALIZE.타이틀_결제하기 = function(){ return LOCALIZE.convArguments("결제하기", arguments); };
            LOCALIZE.버튼_결제하기 = function(){ return LOCALIZE.convArguments("결제하기", arguments); };
            LOCALIZE.타이틀_주문자 = function(){ return LOCALIZE.convArguments("주문자", arguments); };
            LOCALIZE.설명_연락처 = function(){ return LOCALIZE.convArguments("연락처", arguments); };
            LOCALIZE.설명_이메일 = function(){ return LOCALIZE.convArguments("이메일", arguments); };
            LOCALIZE.타이틀_배송방법 = function(){ return LOCALIZE.convArguments("배송 방법", arguments); };
            LOCALIZE.타이틀_배송정보 = function(){ return LOCALIZE.convArguments("배송 정보", arguments); };
            LOCALIZE.버튼_주문자정보와동일 = function(){ return LOCALIZE.convArguments("주문자 정보와 동일", arguments); };
            LOCALIZE.버튼_택배 = function(){ return LOCALIZE.convArguments("택배", arguments); };
            LOCALIZE.타이틀_착불 = function(){ return LOCALIZE.convArguments("착불", arguments); };
            LOCALIZE.버튼_착불 = function(){ return LOCALIZE.convArguments("착불", arguments); };
            LOCALIZE.설명_배송메모를입력해주세요 = function(){ return LOCALIZE.convArguments("배송메모를 입력해 주세요", arguments); };
            LOCALIZE.설명_주소 = function(){ return LOCALIZE.convArguments("주소", arguments); };
            LOCALIZE.설명_상세주소 = function(){ return LOCALIZE.convArguments("상세주소", arguments); };
            LOCALIZE.타이틀_배송메모 = function(){ return LOCALIZE.convArguments("배송메모", arguments); };
            LOCALIZE.버튼_전액사용 = function(){ return LOCALIZE.convArguments("전액사용", arguments); };
            LOCALIZE.타이틀_결제수단 = function(){ return LOCALIZE.convArguments("결제수단", arguments); };
            LOCALIZE.타이틀_위시 = function(){ return LOCALIZE.convArguments("위시", arguments); };
            LOCALIZE.타이틀_할인 = function(){ return LOCALIZE.convArguments("할인", arguments); };
            LOCALIZE.타이틀_수량 = function(){ return LOCALIZE.convArguments("수량", arguments); };
            LOCALIZE.타이틀_가격 = function(){ return LOCALIZE.convArguments("가격", arguments); };
            LOCALIZE.설명_품절 = function(){ return LOCALIZE.convArguments("품절", arguments); };
            LOCALIZE.버튼_장바구니변경 = function(){ return LOCALIZE.convArguments("변경", arguments); };
            LOCALIZE.버튼_장바구니주문 = function(){ return LOCALIZE.convArguments("주문", arguments); };
            LOCALIZE.타이틀_상품가격 = function(){ return LOCALIZE.convArguments("상품가격", arguments); };
            LOCALIZE.버튼_선택상품삭제 = function(){ return LOCALIZE.convArguments("선택상품 삭제", arguments); };
            LOCALIZE.버튼_주문하기 = function(){ return LOCALIZE.convArguments("주문하기", arguments); };
            LOCALIZE.버튼_계속쇼핑하기 = function(){ return LOCALIZE.convArguments("계속 쇼핑하기", arguments); };
            LOCALIZE.설명_장바구니가비어있습니다 = function(){ return LOCALIZE.convArguments("장바구니가 비어있습니다.", arguments); };
            LOCALIZE.타이틀_위시리스트 = function(){ return LOCALIZE.convArguments("위시리스트", arguments); };
            LOCALIZE.버튼_위시리스트더보기 = function(){ return LOCALIZE.convArguments("더보기", arguments); };
            LOCALIZE.설명_위시리스트가없습니다 = function(){ return LOCALIZE.convArguments("위시리스트가 없습니다.", arguments); };
            LOCALIZE.버튼_적립내역더보기 = function(){ return LOCALIZE.convArguments("더보기", arguments); };
            LOCALIZE.타이틀_주문번호 = function(){ return LOCALIZE.convArguments("주문번호", arguments); };
            LOCALIZE.설명_결제가완료되었습니다 = function(){ return LOCALIZE.convArguments("결제가 완료되었습니다<br/>주문배송은 마이페이지에서 조회 가능합니다", arguments); };
            LOCALIZE.타이틀_마이페이지 = function(){ return LOCALIZE.convArguments("마이페이지", arguments); };
            LOCALIZE.설명_컨텐츠상품은주문배송조회에서다운로드해주세요 = function(){ return LOCALIZE.convArguments("컨텐츠 상품은 <a href=\"/shop_mypage\" class=\"text-brand\">주문배송 조회</a>에서 다운로드 해주세요.", arguments); };
            LOCALIZE.타이틀_주문완료 = function(){ return LOCALIZE.convArguments("주문완료", arguments); };
            LOCALIZE.설명_무통장계좌안내 = function(){ return LOCALIZE.convArguments("아래 계좌정보로 입금해 주시면<br/>결제 완료처리가 됩니다", arguments); };
            LOCALIZE.타이틀_계좌정보 = function(){ return LOCALIZE.convArguments("계좌 정보", arguments); };
            LOCALIZE.타이틀_입금기간 = function(){ return LOCALIZE.convArguments("입금 기간", arguments); };
            LOCALIZE.타이틀_입금계좌안내 = function(){ return LOCALIZE.convArguments("입금계좌 안내", arguments); };
            LOCALIZE.버튼_홈으로 = function(){ return LOCALIZE.convArguments("홈으로", arguments); };
            LOCALIZE.타이틀_상품정보 = function(){ return LOCALIZE.convArguments("상품 정보", arguments); };
            LOCALIZE.타이틀_주문일자 = function(){ return LOCALIZE.convArguments("주문일자", arguments); };
            LOCALIZE.타이틀_주문정보 = function(){ return LOCALIZE.convArguments("주문 정보", arguments); };
            LOCALIZE.버튼_배송조회 = function(){ return LOCALIZE.convArguments("배송조회", arguments); };
            LOCALIZE.타이틀_결제정보 = function(){ return LOCALIZE.convArguments("결제정보", arguments); };
            LOCALIZE.타이틀_쿠폰 = function(){ return LOCALIZE.convArguments("쿠폰", arguments); };
            LOCALIZE.타이틀_총결제금액A = function(){ return LOCALIZE.convArguments("<em class=\"hidden-xs\">총</em> 결제금액", arguments); };
            LOCALIZE.타이틀_총결제금액B = function(){ return LOCALIZE.convArguments("총 결제금액", arguments); };
            LOCALIZE.버튼_신용카드 = function(){ return LOCALIZE.convArguments("신용카드", arguments); };
            LOCALIZE.버튼_실시간계좌이체 = function(){ return LOCALIZE.convArguments("실시간계좌이체", arguments); };
            LOCALIZE.버튼_가상계좌 = function(){ return LOCALIZE.convArguments("가상계좌", arguments); };
            LOCALIZE.버튼_핸드폰결제 = function(){ return LOCALIZE.convArguments("핸드폰결제", arguments); };
            LOCALIZE.버튼_무통장입금 = function(){ return LOCALIZE.convArguments("무통장입금", arguments); };
            LOCALIZE.버튼_주문서 = function(){ return LOCALIZE.convArguments("주문서", arguments); };
            LOCALIZE.타이틀_총금액 = function(){ return LOCALIZE.convArguments("총금액", arguments); };
            LOCALIZE.타이틀_일대일문의게시판 = function(){ return LOCALIZE.convArguments("1:1 문의게시판", arguments); };
            LOCALIZE.설명_무료 = function(){ return LOCALIZE.convArguments("무료", arguments); };
            LOCALIZE.타이틀_입금대기 = function(){ return LOCALIZE.convArguments("입금대기", arguments); };
            LOCALIZE.타이틀_배송준비 = function(){ return LOCALIZE.convArguments("배송준비", arguments); };
            LOCALIZE.타이틀_취소요청 = function(){ return LOCALIZE.convArguments("취소요청", arguments); };
            LOCALIZE.타이틀_반품교환 = function(){ return LOCALIZE.convArguments("반품/교환", arguments); };
            LOCALIZE.타이틀_주문조회A = function(){ return LOCALIZE.convArguments("주문 <span class=\"hidden-xs\">조회</span>", arguments); };
            LOCALIZE.타이틀_주문조회B = function(){ return LOCALIZE.convArguments("주문 조회", arguments); };
            LOCALIZE.타이틀_예약조회A = function(){ return LOCALIZE.convArguments("예약 <span class=\"hidden-xs\">조회</span>", arguments); };
            LOCALIZE.타이틀_주문예약조회A = function(){ return LOCALIZE.convArguments("주문/예약 <span class=\"hidden-xs\">조회</span>", arguments); };
            LOCALIZE.타이틀_위시리스트A = function(){ return LOCALIZE.convArguments("위시 <span class=\"hidden-xs\">리스트</span>", arguments); };
            LOCALIZE.타이틀_취소교환반품 = function(){ return LOCALIZE.convArguments("취소/교환/반품", arguments); };
            LOCALIZE.타이틀_일대일문의 = function(){ return LOCALIZE.convArguments("1:1 문의", arguments); };
            LOCALIZE.타이틀_정보수정 = function(){ return LOCALIZE.convArguments("정보 수정", arguments); };
            LOCALIZE.타이틀_주문리스트 = function(){ return LOCALIZE.convArguments("주문리스트", arguments); };
            LOCALIZE.타이틀_주문예약 = function(){ return LOCALIZE.convArguments("주문/예약", arguments); };
            LOCALIZE.타이틀_주문 = function(){ return LOCALIZE.convArguments("주문", arguments); };
            LOCALIZE.설명_취소내역이없습니다 = function(){ return LOCALIZE.convArguments("취소 내역이 없습니다.", arguments); };
            LOCALIZE.설명_주문내역이없습니다 = function(){ return LOCALIZE.convArguments("주문 내역이 없습니다.", arguments); };
            LOCALIZE.타이틀_주문예약번호 = function(){ return LOCALIZE.convArguments("주문/예약번호", arguments); };
            LOCALIZE.타이틀_주문예약상태 = function(){ return LOCALIZE.convArguments("주문/예약상태", arguments); };
            LOCALIZE.타이틀_주문상태 = function(){ return LOCALIZE.convArguments("주문상태", arguments); };
            LOCALIZE.버튼_추가인원 = function(){ return LOCALIZE.convArguments("추가인원", arguments); };
            LOCALIZE.설명_무료제공 = function(){ return LOCALIZE.convArguments("무료제공", arguments); };
            LOCALIZE.타이틀_예약종료 = function(){ return LOCALIZE.convArguments("예약 종료", arguments); };
            LOCALIZE.타이틀_후기 = function(){ return LOCALIZE.convArguments("후기", arguments); };
            LOCALIZE.설명_기준인원추가시 = function(){ return LOCALIZE.convArguments("기준인원 %1명, 추가시 %2", arguments); };
            LOCALIZE.버튼_예약하기 = function(){ return LOCALIZE.convArguments("예약하기", arguments); };
            LOCALIZE.타이틀_예약자정보 = function(){ return LOCALIZE.convArguments("예약자 정보", arguments); };
            LOCALIZE.타이틀_예약자 = function(){ return LOCALIZE.convArguments("예약자", arguments); };
            LOCALIZE.설명_요청사항 = function(){ return LOCALIZE.convArguments("요청사항", arguments); };
            LOCALIZE.타이틀_취소환불규정에대한동의 = function(){ return LOCALIZE.convArguments("취소/환불 규정에 대한 동의", arguments); };
            LOCALIZE.설명_취소불가능합니다 = function(){ return LOCALIZE.convArguments("취소 불가능합니다.", arguments); };
            LOCALIZE.설명_예약결제가완료되었습니다 = function(){ return LOCALIZE.convArguments("정상적으로 결제가 완료되었습니다<br/>예약은 마이페이지에서 조회 가능합니다", arguments); };
            LOCALIZE.타이틀_주중평일 = function(){ return LOCALIZE.convArguments("주중/평일", arguments); };
            LOCALIZE.타이틀_성수기 = function(){ return LOCALIZE.convArguments("성수기", arguments); };
            LOCALIZE.타이틀_준성수기 = function(){ return LOCALIZE.convArguments("준성수기", arguments); };
            LOCALIZE.설명_일예약불가 = function(){ return LOCALIZE.convArguments("%1은 예약이 마감 되었거나 예약 가능한 날이 아닙니다. 다른 날짜를 선택해 주세요.", arguments); };
            LOCALIZE.타이틀_입실 = function(){ return LOCALIZE.convArguments("입실", arguments); };
            LOCALIZE.타이틀_퇴실 = function(){ return LOCALIZE.convArguments("퇴실", arguments); };
            LOCALIZE.설명_등록된문의가없습니다 = function(){ return LOCALIZE.convArguments("등록된 문의가 없습니다", arguments); };
            LOCALIZE.설명_비밀문의입니다 = function(){ return LOCALIZE.convArguments("비밀글입니다.", arguments); };
            LOCALIZE.설명_무엇이든물어보세요 = function(){ return LOCALIZE.convArguments("무엇이든 물어보세요", arguments); };
            LOCALIZE.설명_등록된구매평이없습니다 = function(){ return LOCALIZE.convArguments("등록된 구매평이 없습니다.", arguments); };
            LOCALIZE.버튼_개인정보처리방침동의 = function(){ return LOCALIZE.convArguments("개인정보 수집 및 이용 동의", arguments); };
            LOCALIZE.버튼_위사항을확인하였으며개인정보처리방침에동의합니다 = function(){ return LOCALIZE.convArguments("개인정보 수집 및 이용에 동의합니다.", arguments); };
            LOCALIZE.버튼_응답수정 = function(){ return LOCALIZE.convArguments("응답 수정", arguments); };
            LOCALIZE.설명_개인정보처리방침에동의하여주시기바랍니다 = function(){ return LOCALIZE.convArguments("개인정보 수집 및 이용에 동의하여 주시기 바랍니다.", arguments); };
            LOCALIZE.설명_필수항목을입력하여주시기바랍니다 = function(){ return LOCALIZE.convArguments("필수 항목을 입력하여 주시기 바랍니다.", arguments); };
            LOCALIZE.버튼_일정추가 = function(){ return LOCALIZE.convArguments("일정 추가", arguments); };
            LOCALIZE.버튼_상세일정 = function(){ return LOCALIZE.convArguments("상세 일정", arguments); };
            LOCALIZE.타이틀_통합검색 = function(){ return LOCALIZE.convArguments("통합 검색", arguments); };
            LOCALIZE.타이틀_쇼핑 = function(){ return LOCALIZE.convArguments("쇼핑", arguments); };
            LOCALIZE.타이틀_게시판 = function(){ return LOCALIZE.convArguments("게시판", arguments); };
            LOCALIZE.타이틀_지도 = function(){ return LOCALIZE.convArguments("지도", arguments); };
            LOCALIZE.타이틀_갤러리 = function(){ return LOCALIZE.convArguments("갤러리", arguments); };
            LOCALIZE.버튼_자세히 = function(){ return LOCALIZE.convArguments("자세히", arguments); };
            LOCALIZE.설명_검색결과가없습니다 = function(){ return LOCALIZE.convArguments("검색 결과가 없습니다.", arguments); };
            LOCALIZE.설명_검색어를입력하고enter = function(){ return LOCALIZE.convArguments("검색어를 입력하고 enter 또는 검색 버튼을 클릭해주세요.", arguments); };
            LOCALIZE.설명_검색 = function(){ return LOCALIZE.convArguments("검색", arguments); };
            LOCALIZE.타이틀_주문배송 = function(){ return LOCALIZE.convArguments("주문배송", arguments); };
            LOCALIZE.버튼_로그아웃 = function(){ return LOCALIZE.convArguments("로그아웃", arguments); };
            LOCALIZE.버튼_관리 = function(){ return LOCALIZE.convArguments("관리", arguments); };
            LOCALIZE.타이틀_로그인 = function(){ return LOCALIZE.convArguments("로그인", arguments); };
            LOCALIZE.버튼_네이버로그인 = function(){ return LOCALIZE.convArguments("네이버로 시작하기", arguments); };
            LOCALIZE.버튼_카카오로그인 = function(){ return LOCALIZE.convArguments("카카오로 시작하기", arguments); };
            LOCALIZE.버튼_Facebook로그인 = function(){ return LOCALIZE.convArguments("Facebook으로 시작하기", arguments); };
            LOCALIZE.버튼_Google로그인 = function(){ return LOCALIZE.convArguments("Google로 시작하기", arguments); };
            LOCALIZE.버튼_네이버계정으로가입 = function(){ return LOCALIZE.convArguments("네이버로 시작하기", arguments); };
            LOCALIZE.버튼_카카오계정으로가입 = function(){ return LOCALIZE.convArguments("카카오로 시작하기", arguments); };
            LOCALIZE.버튼_Facebook계정으로가입 = function(){ return LOCALIZE.convArguments("Facebook으로 시작하기", arguments); };
            LOCALIZE.버튼_Google계정으로가입 = function(){ return LOCALIZE.convArguments("Google로 시작하기", arguments); };
            LOCALIZE.타이틀_또는 = function(){ return LOCALIZE.convArguments("또는", arguments); };
            LOCALIZE.버튼_로그인상태유지 = function(){ return LOCALIZE.convArguments("로그인상태유지", arguments); };
            LOCALIZE.설명_아이디 = function(){ return LOCALIZE.convArguments("아이디", arguments); };
            LOCALIZE.설명_홈페이지 = function(){ return LOCALIZE.convArguments("홈페이지", arguments); };
            LOCALIZE.설명_전화번호 = function(){ return LOCALIZE.convArguments("전화번호", arguments); };
            LOCALIZE.타이틀_회원가입 = function(){ return LOCALIZE.convArguments("회원가입", arguments); };
            LOCALIZE.타이틀_내계정찾기 = function(){ return LOCALIZE.convArguments("내 계정 찾기", arguments); };
            LOCALIZE.버튼_비회원주문 = function(){ return LOCALIZE.convArguments("비회원 주문", arguments); };
            LOCALIZE.버튼_비회원예약 = function(){ return LOCALIZE.convArguments("비회원 예약", arguments); };
            LOCALIZE.버튼_비회원주문배송조회 = function(){ return LOCALIZE.convArguments("비회원 주문배송 조회", arguments); };
            LOCALIZE.타이틀_약관동의 = function(){ return LOCALIZE.convArguments("약관동의", arguments); };
            LOCALIZE.버튼_이용약관동의 = function(){ return LOCALIZE.convArguments("이용약관 동의", arguments); };
            LOCALIZE.버튼_개인정보수집및이용 = function(){ return LOCALIZE.convArguments("개인정보 수집 및 이용", arguments); };
            LOCALIZE.설명_필수 = function(){ return LOCALIZE.convArguments("(필수)", arguments); };
            LOCALIZE.버튼_가입하기 = function(){ return LOCALIZE.convArguments("가입하기", arguments); };
            LOCALIZE.버튼_가입취소 = function(){ return LOCALIZE.convArguments("취소", arguments); };
            LOCALIZE.설명_비밀번호를변경하는경우입력 = function(){ return LOCALIZE.convArguments("비밀번호를 변경 하는 경우 입력하세요", arguments); };
            LOCALIZE.버튼_확인닫기 = function(){ return LOCALIZE.convArguments("확인", arguments); };
            LOCALIZE.설명_새버전업데이트문구 = function(){ return LOCALIZE.convArguments("새 버전 업데이트가 가능합니다.<br/>지금 업데이트 하시겠습니까?", arguments); };
            LOCALIZE.버튼_나중에 = function(){ return LOCALIZE.convArguments("나중에", arguments); };
            LOCALIZE.버튼_업데이트 = function(){ return LOCALIZE.convArguments("업데이트", arguments); };
            LOCALIZE.타이틀_알림 = function(){ return LOCALIZE.convArguments("알림", arguments); };
            LOCALIZE.버튼_설정 = function(){ return LOCALIZE.convArguments("설정", arguments); };
            LOCALIZE.타이틀_알림설정 = function(){ return LOCALIZE.convArguments("알림 설정", arguments); };
            </script>
            <script src="/js/brandscope.js?1730961205"></script>
            <script src="https://vendor-cdn.imweb.me/js/common.js?1728880688"></script>
            <script src="https://vendor-cdn.imweb.me/js/im_component.js?1719268490"></script>
            <script src="https://vendor-cdn.imweb.me/js/site_common.js?1672019750"></script>
            <script src="https://vendor-cdn.imweb.me/js/imagesloaded.pkgd.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.smooth-scroll.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/gambit-smoothscroll-min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/ThreeCanvas.js?1700717292"></script>
            <script src="https://vendor-cdn.imweb.me/js/snow.js?1700717292"></script>
            <script src="https://vendor-cdn.imweb.me/js/masonry.pkgd.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/lightgallery-all.min.js?1596595980"></script>
            <script src="https://vendor-cdn.imweb.me/js/bootstrap.slide-menu.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/bootstrap.slide-menu-alarm.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/bootstrap-hover-dropdown.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery-scrolltofixed.js?1669067096"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.trackpad-scroll-emulator.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/modernizr.custom.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/classie.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.exif.js?1577682292"></script><script type="text/vbscript">
            Function IEBinary_getByteAt(strBinary, iOffset)
                IEBinary_getByteAt = AscB(MidB(strBinary,iOffset+1,1))
            End Function
            Function IEBinary_getLength(strBinary)
                IEBinary_getLength = LenB(strBinary)
            End Function
            </script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.canvasResize.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/autosize.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/owl.carousel2.js?1638150602"></script>
            <!--[if lte IE 9]>
            <script  src='https://vendor-cdn.imweb.me/js/owl.carousel1.js?1577682292'></script>
            <![endif]-->
            <script src="https://vendor-cdn.imweb.me/js/slick.min.js?1577682292"></script>
            <script src="/js/preview_mode.js?1685942511"></script>
            <script src="/js/site.js?1732841435"></script>
            <script src="/js/site_member.js?1712780088"></script>
            <script src="/js/mobile_menu.js?1724648860"></script>
            <script src="/js/sns_share.js?1728892330"></script>
            <script src="/js/android_image_upload.js?1669163161"></script><ul id="image_list" style="display: none"></ul>
            <script src="/js/alarm_menu.js?1683615433"></script>
            <script src="/js/alarm_badge.js?1602469334"></script>
            <script src="/js/one_page.js?1721624794"></script>
            <script src="/js/site_coupon.js?1713335787"></script>
            <script src="/js/secret_article.js?1604286051"></script>
            <script src="/js/article_reaction.js?1586730656"></script>
            <script src="/js/site_shop.js?1733462923"></script>
            <script src="/js/board_common.js?1648107937"></script>
            <script src="/js/site_shop_mypage.js?1730277052"></script>
            <script src="/js/site_search.js?1669066661"></script>
            <script src="/js/zipcode_daum.js?1705876859"></script>
            <script src="/js/site_booking.js?1701211465"></script>
            <script src="/js/site_section.js?1731909968"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.number.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/nprogress.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/tinycolor-min.js?1577682292"></script>
            <script src="/js/app.js?1577682295"></script>
            <script src="/js/header_fixed_menu.js?1666824024"></script>
            <script src="/js/header_more_menu.js?1725863401"></script>
            <script src="/js/header_center_colgroup.js?1637043387"></script>
            <script src="/js/mobile_carousel_menu.js?1695010435"></script>
            <script src="/js/header_mega_dropdown.js?1675843337"></script>
            <script src="/js/header_overlay.js?1577682295"></script>
            <script src="/js/site_log.js?1728978908"></script>
            <script src="/js/advanced_trace.js?1597114502"></script>
            <script src="/js/site_animation.js?1731544964"></script>
            <script src="/js/site_event_check.js?1596495221"></script>
            <script src="/js/site_widget.js?1616721332"></script>
            <script src="https://vendor-cdn.imweb.me/js/moment.min.js?1629764594"></script>
            <script src="https://vendor-cdn.imweb.me/js/moment-with-locales.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/bootstrap-datepicker.js?1687222780"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.timepicker.min.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/ie-checker-min.js?1577682292"></script>
            <script src="/js/channel_plugin.js?1698643406"></script>
            <script src="https://vendor-cdn.imweb.me/js/jquery.chosen.js?1619084781"></script>
            <script src="/js/device_uuid.js?1692219094"></script>
            <script src="//wcs.naver.net/wcslog.js"></script>
            <script src="https://vendor-cdn.imweb.me/dist/oms-shop-bridge/oms-shop-bridge.iife.js?1727349396"></script>
            <script type="module" src="/js/oms/front-office.js?1733719561"></script>
            <script type="module" src="/js/fo-shop-my-page/main.js?1732595196"></script>
            <script src="https://static-cdn.crm.imweb.me/sdk/main.min.js"></script>
            <script src="https://vendor-cdn.imweb.me/js/codemirror.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/mode/xml/xml.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/mode/javascript/javascript.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/mode/css/css.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/js/mode/htmlmixed/htmlmixed.js?1577682292"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/froala_editor.min.js?1608673099"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/align.min.js?1607673165"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/char_counter.min.js?1607673165"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/code_beautifier.min.js?1607673167"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/code_view.min.js?1608643124"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/colors.min.js?1607673167"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/draggable.min.js?1607673168"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/emoticons.min.js?1669163161"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/entities.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/file.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/font_family.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/font_size.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/forms.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/fullscreen.min.js?1607673170"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/image.min.js?1607673172"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/image_manager.min.js?1607673172"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/inline_style.min.js?1607673173"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/line_breaker.min.js?1607673173"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/link.min.js?1607673173"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/lists.min.js?1607673174"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/paragraph_format.min.js?1607673174"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/paragraph_style.min.js?1607673174"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/quote.min.js?1607673174"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/save.min.js?1607673174"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/table.min.js?1607673177"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/url.min.js?1607673177"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/video.min.js?1625125569"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/plugins/line_height.min.js?1607673173"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/third_party/font_awesome.min.js?1607673192"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/ko.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/ja.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/zh_cn.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/zh_tw.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/es.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/froala_311/js/languages/vi.js?1669875597"></script>
            <script src="https://vendor-cdn.imweb.me/js/froala_with_emoticon.js?1669875619"></script>
            <script src="/js/image.js?1723425239"></script>
            <script src="/js/post.js?1725519147"></script>
            <script src="/js/post_comment.js?1712288084"></script>
            <script src="/js/post_view.js?1577682295"></script>
            <script src="/js/library_image.js?1680673561"></script>
            <script src="/js/board_common.js?1648107937"></script>
            <script src="https://sstatic-g.rmcnmv.naver.net/resources/js/naver_web_player_ugc_min.js"></script>
            <script></script><script></script><script>
            
              // youtube fullpage video function
              const handleFullscreenChange = function() {
                const body = document.body;
                const fullscreenElement = document.fullscreenElement;
                const is_youtube = fullscreenElement?.getAttribute('src').indexOf('youtube') > 0;
            
                if (document.fullscreenElement && is_youtube) {
                  // 전체화면일 때
                  body.classList.add('video_fullpage');
                } else {
                  // 전체화면이 아닐 때
                  body.classList.remove('video_fullpage');
                }
              }
            
              // event fullpage
              document.addEventListener('fullscreenchange', handleFullscreenChange );
            
                    // 비주얼섹션 배경 동영상 및 동영상 위젯 자동재생 환경 설정
                var section_youtube_list = [];
                var yt_player = {};
                var vimeo_player = [];
                var site_video_list = [];
                var video_autoplay_youtube_list = [];
                    function onYouTubeIframeAPIReady() {
                    $.each(section_youtube_list,function(_e, _data){
                        yt_player[_data.slide_code] = new SITE_SECTION_YOUTUBE();
                        yt_player[_data.slide_code].init(_data.type,_data.code,_data.id, _data.slide_code);
                    });
                    $.each(video_autoplay_youtube_list, function(k, v){
                        site_video_list[v].play();
                    })
                }
            
                    $(function(){
                    /* Bootstrap Sanitizer Custom */
                    var customTooltipAllowList = $.fn.tooltip.Constructor.DEFAULTS.whiteList;
                    customTooltipAllowList.table = [];
                    customTooltipAllowList.thead = [];
                    customTooltipAllowList.tbody = [];
                    customTooltipAllowList.tr = [];
                    customTooltipAllowList.td = ["rowspan", "colspan"];
                    customTooltipAllowList.th = [];
                    customTooltipAllowList.caption = [];
                    customTooltipAllowList["*"].push("style");
                    /* End Bootstrap Sanitizer Custom */
                    $('body').smoothScroll({
                        delegateSelector : 'a',
                        speed : 1200,
                        easing : 'easeInOutExpo'
                    });
                            $('.pms_check').remove();
                                    var recentScrollUrl = IMWEB_SESSIONSTORAGE.get('RECENT_PROD_SCROLL_URL');
                    if(recentScrollUrl && recentScrollUrl !== document.location.href){
                        IMWEB_SESSIONSTORAGE.remove('RECENT_PROD_SCROLL');
                        IMWEB_SESSIONSTORAGE.remove('RECENT_PROD_SCROLL_URL');
                    }
                        });
            </script>
            <script>$(function(){SITE.firstScrollFixed('inline_header_normal');});
            $(function(){$("#s202010059784a742cc092").scrollToFixed({ marginTop: ""});$("#s202010059784a742cc092").toggleClass("_fixed_header_section", true);});
            $(function(){$("body").toggleClass("new_fixed_header_disable", true);$("body").toggleClass("fixed-menu-on", true);});
            
                    $('.join_tooltip[data-toggle="tooltip"]').tooltip({
                        delay: {show: 500, hide: 1000000}
                    });
                    var $join_tooltip = $('#w202010057a9ed5ea188ec').find('.join_tooltip');
                    $join_tooltip.tooltip('show');
            
            
                    $('.join_tooltip[data-toggle="tooltip"]').tooltip({
                        delay: {show: 500, hide: 1000000}
                    });
                    var $join_tooltip = $('#w20201116664ca316c9038').find('.join_tooltip');
                    $join_tooltip.tooltip('show');
            
            var search_option_data_w20201005e715bc7616745 = {"window_background":"rgba(0, 0, 0, 0.5)","window_color":"#fff","btn_type":"type06","btn_text":"","btn_icon_color":"rgba(33, 33, 33, 0.7)","btn_icon_hover_color":"#212121","btn_color":"#212121","btn_color2":"#fff","btn_background":"#00B8FF","btn_font_size":"12","btn_border_check":"N","btn_border_color":"#00B8FF","btn_border_width":"1","form_height":"34","form_width":"150","form_margin":"10","form_background":"#fff","form_border_color":"#dadada","form_border_width":"1","form_border_radius":"3","font_size":"14","font_color":"#212121","text_value":"","text_placeholder":"","icon_type":"simple","icon_class":"icon-magnifier","btn_icon_padding_lr":"0","btn_icon_padding_tb":"0","hover_color":"#999","btn_hover_color":"#fff","btn_hover_background":"#05b2f5","btn_hover_border_color":"#05b2f5","overlay_type_data":{"window_background":" rgba(0,0,0,0.5)","window_color":"#fff","btn_type":"type01","btn_text":"","btn_icon_color":"#fff","btn_icon_hover_color":"rgba(255, 255, 255, 0.5)","btn_color":"#212121","btn_color2":"#fff","btn_background":"#00B8FF","btn_font_size":"14","btn_border_check":"N","btn_border_color":"#00B8FF","btn_border_width":"1","form_height":"34","form_width":"150","form_margin":"10","form_background":"#fff","form_border_color":"#dadada","form_border_width":"1","form_border_radius":"3","font_size":"14","font_color":"#212121","text_value":"","text_placeholder":"","icon_type":"simple","icon_class":"icon-magnifier","btn_icon_padding_lr":"10","btn_icon_padding_tb":"4","hover_color":"#999","btn_hover_color":"#fff","btn_hover_background":"#05b2f5","btn_hover_border_color":"#05b2f5"},"device_type":"pc","link":"","form_focus_border_color":"","text_placeholder_color":"","is_make_thumbnail":"N"};
            
                $(document).ready(function(){
                    var $sd_form = $('#inline_s_form_w20201005e715bc7616745');
                    var $_keyword = $sd_form.find('input[name=keyword]');
            
                    $_keyword.keydown(function(key){
                        if(key.keyCode === 13) {
                            $_keyword.val($_keyword.val().trim());
                        }
                    });
                })
            
            
                    $(function(){
                        var header_center_colgroup_s202010059784a742cc092 = new HEADER_CENTER_COLGROUP();
                        header_center_colgroup_s202010059784a742cc092.init('s202010059784a742cc092',{"top_bottom_margin":"10","col_margin":"15","design_setting_margin":"N","border_width":"0","border_style":"solid","border_color":"#e7e7e7","vertical-align":"middle","scroll_fixed":"Y","overlay_type_data":{"top_bottom_margin":"0","col_margin":"10","design_setting_margin":"Y","border_width":"0","border_style":"solid","border_color":"rgba(255, 255, 255, 0.2)","vertical-align":"middle","scroll_fixed":"N","background_repeat":"","background_position":"","color":"","background_image":"","background_color":"rgba(15, 15, 15, 0.8)"},"left_width":"225","center_width":"0","right_width":"1025","height":"64","background_repeat":"","background_position":"","color":"","left_right_margin":"30","left_right_margin_mobile":"0","background_image":"","extend":"N","background_color":"#ffffff","vertical_align":"middle","hover_section_bg":"N"})});
            
            $(function(){$("#s20201005a79c3af52564c").scrollToFixed({ marginTop: 64});$("#s20201005a79c3af52564c").toggleClass("_fixed_header_section", true);});
            $(function(){$("body").toggleClass("new_fixed_header_disable", true);$("body").toggleClass("fixed-menu-on", true);});
            
                    $(function(){
                        var more_menu_w20201005d27fe010e40db = new HEADER_MORE_MENU();
                        more_menu_w20201005d27fe010e40db.init($('#w20201005d27fe010e40db ._inline_menu_container'),false);
                        more_menu_w20201005d27fe010e40db.setWidgetCode('w20201005d27fe010e40db');
                        $('#w20201005d27fe010e40db ._inline_menu_container').data('header_more_menu',more_menu_w20201005d27fe010e40db);
                    });
            
            
                    $(function(){
                        $('#w20201005d27fe010e40db').find("li.dropdown").each(function(index){
                            $(this).find("li.dropdown-submenu").each(function(index){
                                if(!$(this).hasClass('pulldown-hide')){
                                    if($(this).find(".dropdown-menu > li").length > 0) $(this).addClass("sub-active");
                                }else{
                                    $(this).find('ul').removeClass('dropdown-menu');
                                    $(this).find('ul li').hide();
                                }
                            });
                        });
                        $('#w20201005d27fe010e40db').find('._header_dropdown').dropdownHover();
                    });
            
            
              ;(() => {
                if (![isSafari(), isIos()].some(Boolean)) return;
            
                const $menuLinks = Array.from(document.querySelectorAll('._mobile_nav a'));
                $menuLinks.forEach($menuLink => {
                  if (!$menuLink.hash) return;
            
                  $menuLink.addEventListener('click', () => setCookie('menu_link_hash', $menuLink.hash, 1));
                });
            
                const hash = getCookie('menu_link_hash');
                if (!hash) return;
            
                window.addEventListener('load', () => {
                  const $section = document.querySelector(hash);
                  scrollWindowToElement($section).then(() => deleteCookie('menu_link_hash'));
                });
              })();
            
            
                    $(function(){
                        var header_center_colgroup_s20201005a79c3af52564c = new HEADER_CENTER_COLGROUP();
                        header_center_colgroup_s20201005a79c3af52564c.init('s20201005a79c3af52564c',{"top_bottom_margin":"0","col_margin":"20","design_setting_margin":"Y","border_width":"0","border_style":"solid","border_color":"#e7e7e7","vertical-align":"middle","scroll_fixed":"Y","overlay_type_data":{"top_bottom_margin":"0","col_margin":"10","design_setting_margin":"Y","border_width":"0","border_style":"solid","border_color":"rgba(255, 255, 255, 0.2)","vertical-align":"middle","scroll_fixed":"N","background_repeat":"","background_position":"","color":"","background_image":""},"left_width":"167","center_width":"0","right_width":"1083","height":"115","background_repeat":"","background_position":"","color":"","left_right_margin":"30","left_right_margin_mobile":"0","background_image":"","extend":"N","background_color":"#fff","vertical_align":"middle","hover_section_bg":"N"})});
            
            
                    $(function(){
                        var header_center_colgroup_s2020100700e8f1f61f7bc = new HEADER_CENTER_COLGROUP();
                        header_center_colgroup_s2020100700e8f1f61f7bc.init('s2020100700e8f1f61f7bc',{"top_bottom_margin":"0","col_margin":"10","background_color":"#fff","design_setting_margin":"Y","hover_section_bg":"N","border_width":"0","border_style":"solid","border_color":"#ccc","vertical-align":"middle","scroll_fixed":"N","overlay_type_data":{"top_bottom_margin":"0","col_margin":"10","background_color":"rgba(255,255,255,0)","design_setting_margin":"Y","hover_section_bg":"N","border_width":"0","border_style":"solid","border_color":"rgba(255,255,255,0.5)","vertical-align":"middle","scroll_fixed":"N"},"left_width":"","center_width":"","right_width":"","height":"21"})});
            
            $(function(){SITE.firstScrollFixed('inline_header_mobile');});
            $(function(){$("#s20201005b3138cd5be549").scrollToFixed({ marginTop: ""});$("#s20201005b3138cd5be549").toggleClass("_fixed_header_section", true);});
            
                    $('.join_tooltip[data-toggle="tooltip"]').tooltip({
                        delay: {show: 500, hide: 1000000}
                    });
                    var $join_tooltip = $('#w20201005ded3aae02af59').find('.join_tooltip');
                    $join_tooltip.tooltip('show');
            
            var search_option_data_w20201005a8dce1cb98dd0 = {"window_background":" rgba(0,0,0,0.5)","window_color":"#fff","btn_type":"type01","btn_text":"","btn_icon_color":"#212121","btn_icon_hover_color":"#999","btn_color":"#212121","btn_color2":"#fff","btn_background":"#00B8FF","btn_font_size":"20","btn_border_check":"N","btn_border_color":"#00B8FF","btn_border_width":"1","form_height":"34","form_width":"150","form_margin":"10","form_background":"#fff","form_border_color":"#dadada","form_border_width":"1","form_border_radius":"3","font_size":"14","font_color":"#212121","text_value":"","text_placeholder":"","icon_type":"simple","icon_class":"icon-magnifier","btn_icon_padding_lr":"0","btn_icon_padding_tb":"0","hover_color":"#999","btn_hover_color":"#fff","btn_hover_background":"#05b2f5","btn_hover_border_color":"#05b2f5","overlay_type_data":{"window_background":" rgba(0,0,0,0.5)","window_color":"#fff","btn_type":"type01","btn_text":"","btn_icon_color":"#fff","btn_icon_hover_color":"rgba(255,255,255,0.5)","btn_color":"#212121","btn_color2":"#fff","btn_background":"#00B8FF","btn_font_size":"14","btn_border_check":"N","btn_border_color":"#00B8FF","btn_border_width":"1","form_height":"34","form_width":"150","form_margin":"10","form_background":"#fff","form_border_color":"#dadada","form_border_width":"1","form_border_radius":"3","font_size":"14","font_color":"#212121","text_value":"","text_placeholder":"","icon_type":"simple","icon_class":"icon-magnifier","btn_icon_padding_lr":"10","btn_icon_padding_tb":"4","hover_color":"#999","btn_hover_color":"#fff","btn_hover_background":"#05b2f5","btn_hover_border_color":"#05b2f5"},"device_type":"m","link":""};
            
                $(document).ready(function(){
                    var $sd_form = $('#inline_s_form_w20201005a8dce1cb98dd0');
                    var $_keyword = $sd_form.find('input[name=keyword]');
            
                    $_keyword.keydown(function(key){
                        if(key.keyCode === 13) {
                            $_keyword.val($_keyword.val().trim());
                        }
                    });
                })
            
            
                    $(function(){
                        var header_center_colgroup_s20201005b3138cd5be549 = new HEADER_CENTER_COLGROUP();
                        header_center_colgroup_s20201005b3138cd5be549.init('s20201005b3138cd5be549',{"top_bottom_margin":"0","col_margin":"10","design_setting_margin":"N","border_width":"1","border_style":"solid","border_color":"#e7e7e7","vertical-align":"middle","scroll_fixed":"Y","overlay_type_data":{"top_bottom_margin":"0","col_margin":"10","design_setting_margin":"Y","border_width":"0","border_style":"solid","border_color":"rgba(255, 255, 255, 0.3)","vertical-align":"middle","scroll_fixed":"N","background_repeat":"","background_position":"","color":"","background_image":""},"left_width":"81","center_width":"0","right_width":"81","height":"50","background_repeat":"","background_position":"","color":"","left_right_margin":"15","left_right_margin_mobile":"10","background_image":"","background_color":"#ffffff","extend":"N"})});
            
            
                var carousel_menu_script = new MOBILE_CAROUSEL_MENU($('#mobile_carousel_nav'));
            
            
                $(function(){
                    var img_w20230918a0ab7cb212206 = new IMAGE_RESIZE();
                    img_w20230918a0ab7cb212206.init('w20230918a0ab7cb212206',{"img_width":1920,"img_height":367,"img_ratio":"0.191145833333","img_init":"N","url":"S20200715a3c5f9a178ae1\/d201099a2fed7.jpg","description":"","hover_description":"","text_position":"bottom","hover_text_position":"same","overlay_color":"rgba(0, 0, 0, 0)","hover_overlay_color":"rgba(0, 0, 0, 0)","text_color":"#fff","hover_text_color":"#fff","text_size":"14","hover_text_size":"14","show_over":"N","link":"","link_code":"","use_link_code":"N","new_window":"N","circle":"N","lightbox":"N","org_size":"Y","use_hd":"N","grayscale":"N","hover_grayscale":"N","image_rendering":"Y","border_radius":"N","hide_default_img":"N","border_radius_value":"7","text_align":"0 50%","hover_text_align":"0 50%","ani_type":"none","ani_duration":"0.7","ani_delay":"0","idx":"52687956","member":"","code":"f202301091618ff9ba2088","site_code":"S20200715a3c5f9a178ae1","tmp_idx":"","target_code":"w202301094f3f32bab47dc","target":"image_widget","name":"d201099a2fed7.jpg","org_name":"2ee87ed011c38.jpg","down_cnt":"0","type":"image\/jpeg","size":"250454","version_data":"","wtime":"","mtime":"","error":"","doz_img":"N","is_image_edit":"N","thumb_url":"https:\/\/cdn.imweb.me\/thumbnail\/20230109\/85b710ef9e721.jpg","hover_thumb_url":"https:\/\/cdn.imweb.me\/thumbnail\/20230109\/85b710ef9e721.jpg","hover_img_url":"S20200715a3c5f9a178ae1\/d201099a2fed7.jpg"});
                    $('#img_w20230918a0ab7cb212206').data('image_resize',img_w20230918a0ab7cb212206);
                });
            
            
              ;(() => {
                if (![isSafari(), isIos()].some(Boolean)) return;
            
                const $menuLinks = Array.from(document.querySelectorAll('[data-widget-type="sub_menu"] a'));
                $menuLinks.forEach($menuLink => {
                  if (!$menuLink.hash) return;
            
                  $menuLink.addEventListener('click', () => setCookie('menu_link_hash', $menuLink.hash, 1));
                });
            
                const hash = getCookie('menu_link_hash');
                if (!hash) return;
            
                window.addEventListener('load', () => {
                  const $section = document.querySelector(hash);
                  scrollWindowToElement($section).then(() => deleteCookie('menu_link_hash'));
                });
              })();
            
            var post_like_reaction = new ARTICLE_REACTION();
                            post_like_reaction.setLikeToken();  
                            function viewLikeClick(){ 
                                post_like_reaction.init('post','p202409061b0e4b9231e36',$('#view_like_btn_p202409061b0e4b9231e36'),$('#view_like_count_p202409061b0e4b9231e36')); 
                                post_like_reaction.toggleLike();
                            }
            POST_COMMENT.init('p202409061b0e4b9231e36');SNS.init({"_main_url":"https:\/\/xn--v42b19i81d99c.com","_site_name":"\uc0dd\uba85\uc548\uc804\uc5f0\uad6c\uc18c","_subject":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4","_body":"\ud154\ub808pepegarden\ub5a8\ud31d\ub2c8\ub2e4\n\n\ucc44\ub110 T.me\/Pepe_Garden\n\ubb38\uc758 @pepegarden\n\uc624\ud508\ud1a1\nt.me\/+D-_3LaM0RAg5OWMy\n\n\ub5a8,\ub5a8\uc561 \ub450\uac00\uc9c0\ub9cc \ucde8\uae09\ud569\ub2c8\ub2e4.\n\uc624\ud508\ud1a1\uacfc \ucc44\ub110 \uc6b4\uc601\uc911\uc774\uace0\n\ud569\ub9ac\uc801\uc778\uac00\uaca9\uc73c\ub85c \uc6b4\uc601\ud569\ub2c8\ub2e4.\n\n\ud558\uc774\ucf54\ub9ac\uc544 \uc5d0\uc11c \ubbf8\ubbf8\uc6d4\ub4dc\n\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc \uc804\ubd80 \uacaa\uc5b4\uc654\uc2b5\ub2c8\ub2e4.\n\n\uc624\ub798\ub41c \uacbd\ud5d8\uc73c\ub85c \ucd5c\uc0c1\uae09 \ud004\ub9ac\ud2f0\ub85c \uc548\uc804\ud558\uac8c \ub098\ub214\ud558\uaca0\ub2c8\ub2e4.\n\n#\ub5a8\ud31d\ub2c8\ub2e4#\ub5a8\ud314\uc544\uc694#\uac15\ub0a8\ub5a8#\uc6a9\uc0b0\ub5a8#\ud64d\ub300\ub5a8#\ub5a8\uc778\uc99d\ub51c\ub7ec#\ub5a8\uc0bd\ub2c8\ub2e4#\ud558\uc774\ucf54\ub9ac\uc544#\ud558\uc774\ucf54\ub9ac\uc544\ub124\uc624#\ub5a8\uc528\uc557#\ubbf8\ubbf8\uc6d4\ub4dc#\uc704\ub2c8\ud50c#\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc#\ubc84\ub4dc\ud31d\ub2c8\ub2e4#\uac04\uc790\ud31d\ub2c8\ub2e4#\ub5a8\ub4dc\ub78d#\ub5a8\uc120\ub4dc\ub78d#\uc218\uc6d0\ub5a8#\uc778\ucc9c\ub5a8#\uc81c\uc8fc\ub5a8#\ubd80\uc0b0\ub5a8#\ub300\ub9c8\ud6a8\ub2a5#\ub300\ub9c8\ud569\ubc95#\ub300\ub9c8\ucd08\ud31d\ub2c8\ub2e4#\ub300\ub9c8\ud31d\ub2c8\ub2e4#\ub5a8\ud314\uc544\uc694#\uad11\uc8fc\ub5a8#\ub5a8\uc561\ud31d\ub2c8\ub2e4#\ub5a8\uc561\ud314\uc544\uc694#\ub5a8\uc561\uc0bd\ub2c8\ub2e4#\ub5a8\uc561#\ub300\ub9c8\uc561\uc0c1#\ub300\ub9c8\uc528\uc557#\ub300\ub9c8\uc7ac\ubc30#\ub300\ub9c8\ucd08#\ub3d9\uc791\ub5a8#\uad11\uc9c4\ub5a8#\ub9c8\ud3ec\ub5a8#\ucc9c\uc548\ub5a8#\ub300\uad6c\ub5a8#\ub300\uc804\ub5a8#\uc548\uc0b0\ub5a8#\uccad\uc8fc\ub5a8#\uc81c\uc8fc\ub3c4\ub5a8#\uac15\ubd81\ub5a8#\ub17c\ud604\ub5a8#\ud074\ub7fd\ub5a8#\ub5a8\ud310\ub9e4#Thc#cbd#\ud64d\ub300\ub5a8#\ud55c\uad6d\ub525\uc6f9#\uc704\ub2c8\ub4dc\ud50c\ub77c\uc6cc#\ud558\uc774\ucf54\ub9ac\uc544\ub124\uc624#\ud0d1\ucf54\ub9ac\uc544#\uac74\ub300\ub5a8#\ub5a8\uc0ac\uc694#\ub5a8\uc778\uc99d\ub51c\ub7ec#\ub5a8\ud31d\ub2c8\ub2e4#\ub5a8\uc0ac\ub294\uacf3#\ucfe0\uc26c\ud31d\ub2c8\ub2e4#\ud0dc\uad6d\ub5a8#\ubd81\ubbf8\ub5a8#\ub5a8\uc528\uc557\ubc30\uc1a1#\ub5a8\uc528\uc557\uad6d\uc81c\ud0dd\ubc30#\uc758\ub8cc\uc6a9\ub300\ub9c8#\ube14\ub8e8\ub4dc\ub9bc#\ub808\ubaac\ud5e4\uc774\uc988#\uc624\uc9c0\ucfe0\uc26c#\uc624\uc950\ucfe0\uc26c#ak47\ucfe0\uc26c#\ud654\uc774\ud2b8\uc704\ub3c4\uc6b0#\uac1c\uc778\uc7a5#\ubc95\uc778\uc7a5#\uac15\ub0a8\uc624\ud53c#\uac15\ub0a8\uc720\ud765#\ud1a0\ud1a0\ucd1d\ud310#\ubc14\uce74\ub77c\uc0ac\uc774\ud2b8#\ucd94\ucc9c\uc778\ucf54\ub4dc#\uce74\uc9c0\ub178\uc0ac\uc774\ud2b8#\uc0ac\uc124\uce74\uc9c0\ub178#\ud1a0\ud1a0\ubc30\ud305","_post_url":"https:\/\/xn--v42b19i81d99c.com\/186\/?bmode=view&idx=95396760","_security_post_url":"aHR0cHM6Ly94bi0tdjQyYjE5aTgxZDk5Yy5jb20vMTg2Lz9ibW9kZT12aWV3JmlkeD05NTM5Njc2MA==","_img":"https:\/\/cdn.imweb.me\/thumbnail\/20240906\/8686f5b82b01b.jpg","_share_type":"feed","_social":{"likeCount":0,"commentCount":0,"viewCount":878}});
            
                    $('.board_txt_area').find('img').each(function(){
                        if($(this).parent().get(0).tagName == 'A')
                            return true;
                                    $(this).attr('data-src', $(this).attr('src')).data('src', $(this).attr('src')).addClass('_img_light_gallery cursor_pointer');
                                });
                    $('.board_txt_area').lightGallery({
                        selector: '._img_light_gallery',
                        thumbnail: false,
                        animateThumb: false,
                        showThumbByDefault: false,
                        hash: false,
                        speed: 200
                    });
                    $('.board_txt_area').find("._table_responsive").addClass("table").wrap($("<div />").addClass("table-responsive"));
                    $('body').addClass('post_view');
            
                    // setTimeout(function(){
                    // 	setProgress($(window).outerWidth() < 992 ? "mobile" : "pc");
                    // },500);
                    //
                    // function setProgress (type){
                    // 	var $body = $('body');
                    // 	var fixedMenu = $body.hasClass('new_fixed_menu_on');
                    // 	var marginTop = 0;
                    // 	var $progressVar = $body.find('._bar_progress_wrap');
                    // 	var $fixed_header_disable = $('#inline_header_normal').find('._fixed_header_section');
                    //
                    // 	if ( type == 'mobile' ){
                    // 		$fixed_header_disable = $('#inline_header_mobile').find('._fixed_header_section');
                    // 	}
                    //
                    // 	if ( !fixedMenu || type == 'mobile' ) {
                    // 		for ( var i = 0; i < $fixed_header_disable.length; i++ ) {
                    // 			var target = $fixed_header_disable[i].getBoundingClientRect();
                    // 			marginTop += target.height;
                    // 		}
                    // 	}
                    //
                    // 	$(window).scroll(function() {
                    // 		var scrollTop = $(this).scrollTop();
                    // 		var containerHeight = $('.board._list_wrap').outerHeight(); //전체 페이지 높이
                    // 		var windowHeight = $(window).outerHeight(); //윈도우의 높이
                    // 		var height = containerHeight - windowHeight;
                    // 		var bar = (scrollTop / height) * 100;
                    //
                    // 		if ( fixedMenu && type != 'mobile') {
                    // 			marginTop = $('._new_fixed_header').height();
                    // 		}
                    //
                    // 		$progressVar.show();
                    // 		$progressVar.css('top', marginTop + 'px');
                    // 		$progressVar.find('.bar_progress').css('width', bar + '%');
                    // 	});
                    // }
            
            
            
                    var widget_code = 'w20230918f38bb09ff75c8';
                    SECRET_ARTICLE.init(widget_code);
            
                                    $('._list_wrap').addClass('m-margin-on ');
                            $(function () {
                        $('.image_cmt_lightbox').find('img').each(function(){
                            $(this).attr('data-src',$(this).attr('src')).data('src',$(this).attr('src')).addClass('_image_cmt');
                        });
                        $('.image_cmt_lightbox').lightGallery({
                            selector: '._image_cmt',
                            speed: 200
                        });
                    });
            
            </script><script>ALARM_BADGE.addBadgeArea($('#slide-alarm'),'<i aria-hidden="true" class="im-icon im-ico-bell"></i><sup class="badge style-danger _badge_cnt">{count}</sup>');</script><script>
                $(function(){
                    //첫방문 flag
                    var first_visit_menu = false;
                    //로컬 스토리지에서 방문한 메뉴 코드를 가져오기
                    var visited_menu_codes = localStorage.getItem('visited_menu_codes');
                    //방문한 메뉴 코드가 없다면 빈 배열로 초기화
                    var visited_menu_code_list = JSON.parse(visited_menu_codes) || [];
                    //현재 메뉴 코드를 처음 방문이미 로컬스토리지에 저장
                    if ( visited_menu_code_list.indexOf('m20230918fca804513d525') === -1 ) {
                        visited_menu_code_list.push('m20230918fca804513d525');
                        localStorage.setItem('visited_menu_codes', JSON.stringify(visited_menu_code_list));
                        //최초 접속 flag 변경
                        first_visit_menu = true;
                    }
                    SITE_VISIT_LOG.addVisitLog(document.referrer,'s4JfgV9H8X3grZJBhH8Pu7W6xTINxHFHBs7F4pfsiHESF3vDXvIgpy/7j5HA7RXyO4pEtoIrVBH+ECwkx5XYSb4LGZUQNXpDd3tZ85z4Ri7gNlfu0Dhxro09NgZFuzSU', '269','m20230918fca804513d525', first_visit_menu);
                });
            </script>
            
            <script>
                ALARM_MENU.init();
                    SITE_ANIMATION.init('N', 'Y');
            
            
            
                $(function () {
                    var gallery_id = 'img_lg';
                    var img_gallery_light_box = false;
                    $('body').lightGallery({
                        selector: '._image_widget_lightbox',
                        thumbnail: false,
                        animateThumb: false,
                        swipeThreshold : 20,
                        showThumbByDefault: false,
                        mode: 'lg-fade',
                        speed: 200,
                        galleryId: gallery_id,
                    });
            
                    if(history.replaceState && history.pushState){
                        var current_url = location.href.indexOf('#') === -1 ? location.href : location.href.substr(0, location.href.indexOf('#'));
                        var back_url = document.referrer.indexOf('#') === -1 ? document.referrer : document.referrer.substr(0, document.referrer.indexOf('#'));
                        var history_push_flag = true;
                        // 라이트박스 hash 커스텀(IE 10 이상)
                        $('body').on('onBeforeOpen.lg', function(){
                            history_push_flag = true;
                        });
                        $('body').on('onAfterOpen.lg', function(){
                            var current_url_lg_id = location.href.indexOf('#') === -1 ? location.href : location.href.substr(location.href.indexOf('#'), location.href.indexOf('&'));
                            if(current_url_lg_id.indexOf(gallery_id) > 0){
                                img_gallery_light_box = true;
                            }
                        })
                        $('body').on('onAfterSlide.lg', function(event, prevIndex, index){
                            if(img_gallery_light_box){
                                if(history_push_flag){
                                    history.replaceState(null, null, current_url);
                                    history_push_flag = false;
                                }
                                history.replaceState(null, null, current_url + '#lg=' + gallery_id + '&slide=' + index);		// 슬라이드 히스토리 교체
                            }
                        });
                        var history_back_flag = true;
                        $('body').on('onBeforeClose.lg', function(e){
                            if(img_gallery_light_box){
                                history_back_flag = true;
                                if(window.location.hash.indexOf('lg=' + gallery_id) !== -1){
                                    history.back();
                                    history_back_flag = false;
                                }
                            }
                        });
                        $('body').on('onCloseAfter.lg', function(){
                            if(img_gallery_light_box){
                                if(history_back_flag || window.location.hash.indexOf('lg=') !== -1){
                                    history.back();
                                }
                                history_back_flag = true;
                                img_gallery_light_box = false;
                            }
                        })
                    }
            
                    $('[data-toggle="tooltip"]').tooltip();
            
            
                        });
            
                $(document).ready(function() {
                    $('body').removeClass('page_ready');
                    $('._bookmark').on('click', function(e) {
                        var bookmarkURL = window.location.href;
                        var bookmarkTitle = document.title;
                        var triggerDefault = false;
            
                        if (window.sidebar && window.sidebar.addPanel) {
                            // Firefox version < 23
                            window.sidebar.addPanel(bookmarkTitle, bookmarkURL, '');
                        } else if ((window.sidebar && (navigator.userAgent.toLowerCase().indexOf('firefox') > -1)) || (window.opera && window.print)) {
                            // Firefox version >= 23 and Opera Hotlist
                            var $this = $(this);
                            $this.attr('href', bookmarkURL);
                            $this.attr('title', bookmarkTitle);
                            $this.attr('rel', 'sidebar');
                            $this.off(e);
                            triggerDefault = true;
                        } else if (window.external && ('AddFavorite' in window.external)) {
                            // IE Favorite
                            window.external.AddFavorite(bookmarkURL, bookmarkTitle);
                        } else {
                            // WebKit - Safari/Chrome
                            alert(LOCALIZE.설명_즐겨찾기등록키안내( (navigator.userAgent.toLowerCase().indexOf('mac') != -1 ? 'Cmd' : 'Ctrl') + '+D') );
                        }
            
                        return triggerDefault;
                    });
            
            
            
            
                    // CRM Squad 서비스 SDK
                    const c = window.crmService;
                    c.boot({
                        unitCode: 'u202007155f0edb3adaedd',
                        siteCode: 'S20200715a3c5f9a178ae1',
                        memberCode: '',
                        cartCode: '',
                        isRegularly: !!''
                    })
            
                    SITE.initTermsModeElements();
                });
            </script>
            
            
            
            <script>
            
                    if(LOCAL_STORAGE.getLocalStorage('AUTO_LOGOUT_TIME')) LOCAL_STORAGE.deleteLocalStorage('AUTO_LOGOUT_TIME');
                    if(LOCAL_STORAGE.getLocalStorage('IS_AUTO_LOGOUT')) LOCAL_STORAGE.deleteLocalStorage('IS_AUTO_LOGOUT');
            
                </script>
            </body></html>
            '''
        }
    },
    {
        'url': "http://127.0.0.1:5000/telegram/channel/scrape",
        'data': {
            "channel_name": "Hyde_Sandbox"
        }
    }
]

result = OrderedDict()
for bundle in test_set:
    response = requests.post(bundle['url'], json=bundle['data'])
    print(f"Test for {bundle['url']} is completed.")
    result[bundle['url']] = response.json()

with open("test_result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
