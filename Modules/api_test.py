import requests
from collections import OrderedDict
import json

test_set = [
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/preprocess/extract/web-promotion",
        'method': "POST",
        'data': {
            "html":
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
            </body></html>
            '''
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/preprocess/extract/web-promotion",
        'method': "POST",
        'data': {
            "html": "삐리삐리빠라빠라뽀"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/scrape",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox2"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/check-suspicious",
        'method': "POST",
        'data': {
            "channel_key": "+rFf0i3HFC4tiOGE1"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/crawl/links",
        'method': "POST",
        'data': {
            "queries": [
                # "t.me 아이스",
                "t.me 떨",
                # "t.me 케이",
                # "t.me LSD",
                # "t.me 캔디",
                # "t.me 빙두"
            ],
            "max_results": 20
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/crawl/html",
        'method': "POST",
        'data': {
            "link": "https://www.teia.co.kr/25/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTI7fQ%3D%3D&bmode=view&idx=139766712&t=board&category=0JV5F0VX73"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/monitoring",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox",
            "how": "start"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/monitoring",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox2",
            "how": "start"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/monitoring",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox",
            "how": "stop"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/monitoring",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox2",
            "how": "stop"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/info",
        'method': "POST",
        'data': {
            "channel_key": "Hyde_Sandbox2"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/info",
        'method': "POST",
        'data': {
            "channel_key": "frozen_talk"
        }
    },
    {
        'enabled': False,
        'url': "http://127.0.0.1:5000/telegram/channel/scrape",
        'method': "POST",
        'data': {
            "channel_key": 1890652954
        }
    },
    {
        'enabled': False | True,
        'url': "http://127.0.0.1:5000/watson/c/1890652954",
        'method': "POST",
        'data': {
            "question": "이 채널에서 마약이 판매되는 지역은 어디지?",
        }
    },
]

result = list()
for bundle in test_set:
    if not bundle['enabled']:
        continue
    if bundle['method'] == "GET":
        response = requests.get(bundle['url'], params=bundle['params'])
    elif bundle['method'] == "POST":
        response = requests.post(bundle['url'], json=bundle['data'])
    else:
        response = requests.models.Response()

    request_and_response = {
        'request': bundle['url'],
        'response': None,
    }
    result.append(request_and_response)
    if response.status_code == 200:
        request_and_response['response'] = response.json()
        print(f"{bundle['url']} 에 대한 테스트 완료.")
    else:
        try:
            request_and_response['response'] = response.json()
        except Exception as e:
            print(f"json 형태의 응답이 아님!")
            request_and_response['response'] = f"{response.status_code}: {response.reason}"
        print(f"{bundle['url']} 에 대한 테스트 오류 - {response.status_code}: {response.reason}")

with open("test_result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False, indent=4)
