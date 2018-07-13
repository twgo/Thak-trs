from trs import _trs轉json
from unittest.case import TestCase


class 試驗(TestCase):
    def tearDown(self):
        self.assertEqual(_trs轉json.trs字串(self.原來), self.結果)

    def test_換逝(self):
        self.原來 = '''<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="3919.18400000001"/>
la0159214 過去 政府 e 國語 政策， gue4_ki4
<Event desc="ki3" type="lexical" extent="previous"/>
 zing4_hu4 e2 gok1_qi1 zing4_cik2
<Sync time="3921.48800000001"/>
la0159215 ga 咱e 台語 講做 是 北京語 e 方言， ga3 lan1_e2 dai3_qi4 gong1_zor4 si3 bak1_giann2_qi4 e2 hong2_qen5
<Sync time="3931.48800000001"/>
'''
        self.結果 = [
            {
                '開始時間': '3919.18400000001',
                '結束時間': '3921.48800000001',
                '語者': '市場商家2',
                'trs聽拍': (
                    'la0159214 過去 政府 e 國語 政策， gue4_ki4\n'
                    '<Event desc="ki3" type="lexical" extent="previous"/>\n'
                    ' zing4_hu4 e2 gok1_qi1 zing4_cik2'
                ),
            },
            {
                '開始時間': '3921.48800000001',
                '結束時間': '3931.48800000001',
                '語者': '市場商家2',
                'trs聽拍':
                'la0159215 ga 咱e 台語 講做 是 北京語 e 方言， ga3 lan1_e2 dai3_qi4 gong1_zor4 si3 bak1_giann2_qi4 e2 hong2_qen5',
            },
        ]

    def test_換逝有連字符(self):
        self.原來 = '''<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="5744.368"/>
sg0200223 漢人 最後 一次 武裝 抗日e「西來庵 事件」；han4-rin5 zue4-au2 zit3-cu3 vu1-zong1 kong4-rit2 e3 se2-lai3-an1 su3-giann2
<Sync time="5748.112"/>
sg0200224 有人 暢談 人文 哲學、 u3-lang2 ciong4-dam5 rin2-vun5 tik1-hak2
<Sync time="5750.208"/>
sg0200225 生態 倫理，致使 歸個 議題 變做 攏 失去 焦點。 sing2-tai3 lun3-li4,di4-su1 gui2-e3 qe3
<Event desc="qi3" type="lexical" extent="previous"/>
-de5 ben4-zor4 long1 sit1-ki1 ziau2-diam4
<Sync time="5754.48"/>
sg0200226 自從 戰後 國民黨 接手 e「大中國」愚民 教育， zu3-ziong3 zen4-au2 gok1-vin3-dong4 ziap1-ciu4 e3 dua3-diong2-gok2 qu2-vin5 gau4-iok2
<Sync time="5758.432"/>
sg0200227 非常 成功 deh 徹底 分化 台灣 族群 間 e 共同 意識。 hui2-siong4 sing3-gong1 de5 tit1(tet1)-de1 hun2-hua3 dai2-uan5 zok3-gun3 gan1 e3 giong3-dong5 i4-sik2
<Sync time="5763.408"/>
'''
        self.結果 = [
            {
                '開始時間': '5744.368',
                '結束時間': '5748.112',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200223 漢人 最後 一次 武裝 抗日e「西來庵 事件」；han4-rin5 zue4-au2 zit3-cu3 vu1-zong1 kong4-rit2 e3 se2-lai3-an1 su3-giann2',
            },
            {
                '開始時間': '5748.112',
                '結束時間': '5750.208',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200224 有人 暢談 人文 哲學、 u3-lang2 ciong4-dam5 rin2-vun5 tik1-hak2',
            },
            {
                '開始時間': '5750.208',
                '結束時間': '5754.48',
                '語者': '市場商家2',
                'trs聽拍': (
                    'sg0200225 生態 倫理，致使 歸個 議題 變做 攏 失去 焦點。 sing2-tai3 lun3-li4,di4-su1 gui2-e3 qe3\n'
                    '<Event desc="qi3" type="lexical" extent="previous"/>\n'
                    '-de5 ben4-zor4 long1 sit1-ki1 ziau2-diam4'
                )
            },
            {
                '開始時間': '5754.48',
                '結束時間': '5758.432',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200226 自從 戰後 國民黨 接手 e「大中國」愚民 教育， zu3-ziong3 zen4-au2 gok1-vin3-dong4 ziap1-ciu4 e3 dua3-diong2-gok2 qu2-vin5 gau4-iok2',
            },
            {
                '開始時間': '5758.432',
                '結束時間': '5763.408',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200227 非常 成功 deh 徹底 分化 台灣 族群 間 e 共同 意識。 hui2-siong4 sing3-gong1 de5 tit1(tet1)-de1 hun2-hua3 dai2-uan5 zok3-gun3 gan1 e3 giong3-dong5 i4-sik2',
            }, ]

    def test_字有中括號(self):
        self.原來 = '''<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="4484.28800000001"/>
la0005185 特別 是 學生 囡仔 歇熱 彼zam， dik3_bet3 si3 hak3_sing2 qin1_a4 hior4_ruah1 hit1_zam3
<Sync time="4486.68800000001"/>
la0005186 會用得 講， e3_iong3_dit1 gong4
<Sync time="4487.66400000001"/>
la0005187 逐日 下晡 四 五點仔 腳兜 [左右]， dak3_rit3 e3_bo1 si4 qo3_diam1_a1 ka2_dau1 zor1_iu2
<Sync time="4490.64000000001"/>
la0005188 阮 攏 會 來 zia- cit-tor， quan1 long1 e3 lai2 zia1 cit1_tor5
<Sync time="4493.07200000001"/>
la0005189 散步， san4_bo2
<Sync time="4493.87200000001"/>
'''
        self.結果 = [
            {
                '開始時間': '4484.28800000001',
                '結束時間': '4486.68800000001',
                '語者': '市場商家2',
                'trs聽拍': 'la0005185 特別 是 學生 囡仔 歇熱 彼zam， dik3_bet3 si3 hak3_sing2 qin1_a4 hior4_ruah1 hit1_zam3',
            },
            {
                '開始時間': '4486.68800000001',
                '結束時間': '4487.66400000001',
                '語者': '市場商家2',
                'trs聽拍': 'la0005186 會用得 講， e3_iong3_dit1 gong4',
            },
            {
                '開始時間': '4487.66400000001',
                '結束時間': '4490.64000000001',
                '語者': '市場商家2',
                'trs聽拍': 'la0005187 逐日 下晡 四 五點仔 腳兜 [左右]， dak3_rit3 e3_bo1 si4 qo3_diam1_a1 ka2_dau1 zor1_iu2',
            },
            {
                '開始時間': '4490.64000000001',
                '結束時間': '4493.07200000001',
                '語者': '市場商家2',
                'trs聽拍': 'la0005188 阮 攏 會 來 zia- cit-tor， quan1 long1 e3 lai2 zia1 cit1_tor5',
            },
            {
                '開始時間': '4493.07200000001',
                '結束時間': '4493.87200000001',
                '語者': '市場商家2',
                'trs聽拍': 'la0005189 散步， san4_bo2',
            },
        ]

# 	def test_無確定字(self):

    def test_有外文(self):
        self.原來 = '''<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="4617.984"/>
sg0184014 包括寫報告、/bau2-gua4-sia1-bor4-gor3-
<Sync time="4619.296"/>
sg0184015 工程圖面 ｅ打字、/gang2-ding5-do2-vin2, e2-dann1-ri2-
<Sync time="4621.104"/>
sg0184016 寫E-mail、 上網路 查詢各種資料，/sia1[//], zionn3-vang1-lo2, ca2-sun3-gok1-ziong1-zu2-liau2-
<Sync time="4624.368"/>
sg0184017 會使得講 無一天 不用電腦，/e3-sai1-dit1-gong1, vor2-zit3-gang2, vor2-iong3-den3-nau4-
<Sync time="4627.152"/>
sg0184018 當然電腦鍵盤 是最主要的 輸入工具；/dong2-ren5-den3-nau4-gen4-buann5, si3-zue4-zu1-iau3-e2, su2-rip3-gang2-gu2-
<Sync time="4630.736"/>'''
        self.結果 = [
            {
                '開始時間': '4617.984',
                '結束時間': '4619.296',
                '語者': '市場商家2',
                'trs聽拍': 'sg0184014 包括寫報告、/bau2-gua4-sia1-bor4-gor3-',
            },
            {
                '開始時間': '4619.296',
                '結束時間': '4621.104',
                '語者': '市場商家2',
                'trs聽拍': 'sg0184015 工程圖面 ｅ打字、/gang2-ding5-do2-vin2, e2-dann1-ri2-',
            },
            {
                '開始時間': '4621.104',
                '結束時間': '4624.368',
                '語者': '市場商家2',
                'trs聽拍': 'sg0184016 寫E-mail、 上網路 查詢各種資料，/sia1[//], zionn3-vang1-lo2, ca2-sun3-gok1-ziong1-zu2-liau2-',
            },
            {
                '開始時間': '4624.368',
                '結束時間': '4627.152',
                '語者': '市場商家2',
                'trs聽拍': 'sg0184017 會使得講 無一天 不用電腦，/e3-sai1-dit1-gong1, vor2-zit3-gang2, vor2-iong3-den3-nau4-',
            },
            {
                '開始時間': '4627.152',
                '結束時間': '4630.736',
                '語者': '市場商家2',
                'trs聽拍': 'sg0184018 當然電腦鍵盤 是最主要的 輸入工具；/dong2-ren5-den3-nau4-gen4-buann5, si3-zue4-zu1-iau3-e2, su2-rip3-gang2-gu2-',
            },
        ]

    def test_有外文標仔(self):
        self.原來 = '''
<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="5520.704" endTime="5569.332">
<Sync time="5520.704"/>
sg0200152 震驚 全 台灣。zin4-giann2 zuan2 dai2-uan5
<Sync time="5522.112"/>
sg0200153 日本 總督府 緊急 調派 各地 軍警 進攻 霧社，rit3-bun4 zong1-dok1-hu4 gin1-gip2 diau4-pai3 gok1-de2 gun2-ging3 zin4-gong2 vu3-sia2
<Sync time="5526.496"/>
sg0200154 莫那˙魯道gah抗日族人退守馬赫坡，
<Event desc="zh" type="language" extent="begin"/>
莫那魯道
<Event desc="zh" type="language" extent="end"/>
 gah1 kong4-rit2 zok3-rin5 tue4-siu1 ma1-hip1-por1
<Sync time="5530.208"/>
sg0200155 利用 天險 gah 日軍 對峙。 li3-iong3 ten2-hiam4 gah1 rit3-gun1 dui4-cai2
<Sync time="5532.88"/>
sg0200156 日方 則 利用 道澤蕃「以夷 制夷」， rit3-hong1 zik1 li3-iong3 dor3-dit1-huan1 i1-i5 ze4-i5
<Sync time="5536.4"/>
'''
        self.結果 = [
            {
                '開始時間': '5520.704',
                '結束時間': '5522.112',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200152 震驚 全 台灣。zin4-giann2 zuan2 dai2-uan5',
            },
            {
                '開始時間': '5522.112',
                '結束時間': '5526.496',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200153 日本 總督府 緊急 調派 各地 軍警 進攻 霧社，rit3-bun4 zong1-dok1-hu4 gin1-gip2 diau4-pai3 gok1-de2 gun2-ging3 zin4-gong2 vu3-sia2',
            },
            {
                '開始時間': '5526.496',
                '結束時間': '5530.208',
                '語者': '市場商家2',
                'trs聽拍': (
                    'sg0200154 莫那˙魯道gah抗日族人退守馬赫坡，\n'
                    '<Event desc="zh" type="language" extent="begin"/>\n'
                    '莫那魯道\n'
                    '<Event desc="zh" type="language" extent="end"/>\n'
                    ' gah1 kong4-rit2 zok3-rin5 tue4-siu1 ma1-hip1-por1'
                )
            },
            {
                '開始時間': '5530.208',
                '結束時間': '5532.88',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200155 利用 天險 gah 日軍 對峙。 li3-iong3 ten2-hiam4 gah1 rit3-gun1 dui4-cai2',
            },
            {
                '開始時間': '5532.88',
                '結束時間': '5536.4',
                '語者': '市場商家2',
                'trs聽拍': 'sg0200156 日方 則 利用 道澤蕃「以夷 制夷」， rit3-hong1 zik1 li3-iong3 dor3-dit1-huan1 i1-i5 ze4-i5',
            },
        ]

    def test_一句話兩逝(self):
        self.原來 = '''<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="4992.736"/>
sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2 
<Sync time="4996.976"/>
sg0103052 特殊 e 癖好、/dik3-su5 e3 pi4-hor4 
<Sync time="4998.256"/>
sg0103053 以及 溫柔 e 神情。/i1-gip3 un2-ru5 e3 sin2
<Event desc="sim2" type="lexical" extent="instantaneous"/>
-zing5 
<Sync time="5000.208"/>
sg0103054 而且， /li3-ciann1 
<Sync time="5001.072"/>
'''
        self.結果 = [
            {
                '開始時間': '4992.736',
                '結束時間': '4996.976',
                '語者': '市場商家2',
                'trs聽拍': 'sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2',
            },
            {
                '開始時間': '4996.976',
                '結束時間': '4998.256',
                '語者': '市場商家2',
                'trs聽拍': 'sg0103052 特殊 e 癖好、/dik3-su5 e3 pi4-hor4',
            },
            {
                '開始時間': '4998.256',
                '結束時間': '5000.208',
                '語者': '市場商家2',
                'trs聽拍': (
                    'sg0103053 以及 溫柔 e 神情。/i1-gip3 un2-ru5 e3 sin2\n'
                    '<Event desc="sim2" type="lexical" extent="instantaneous"/>\n'
                    '-zing5'
                ),
            },
            {
                '開始時間': '5000.208',
                '結束時間': '5001.072',
                '語者': '市場商家2',
                'trs聽拍': 'sg0103054 而且， /li3-ciann1',
            },
        ]

    def test_上尾無Sync(self):
        self.原來 = '''<Speaker id="spk21" name="市場商家1" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk21" startTime="4992.736" endTime="4996.976">
<Sync time="4992.736"/>
sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2
</Turn>
'''
        self.結果 = [
            {
                '開始時間': '4992.736',
                '結束時間': '4996.976',
                '語者': '市場商家1',
                'trs聽拍': 'sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2',
            },
        ]

    def test_上尾有Sync(self):
        self.原來 = '''<Speaker id="spk21" name="市場商家1" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk21" startTime="4992.736" endTime="4996.976">
<Sync time="4992.736"/>
sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2
<Sync time="4996.976"/>
</Turn>
'''
        self.結果 = [
            {
                '開始時間': '4992.736',
                '結束時間': '4996.976',
                '語者': '市場商家1',
                'trs聽拍': 'sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2',
            },
        ]

    def test_兩个人講話(self):
        self.原來 = '''<Speaker id="spk21" name="市場商家1" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk22" startTime="0" endTime="69.332">
<Sync time="0"/>
sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2
</Turn>
<Turn speaker="spk21" startTime="69.332" endTime="70.332">
<Sync time="69.332"/>
sg0103052 特殊 e 癖好、/dik3-su5 e3 pi4-hor4
</Turn>
'''
        self.結果 = [
            {
                '開始時間': '0',
                '結束時間': '69.332',
                '語者': '市場商家2',
                'trs聽拍': 'sg0103051 同時 思念 每一個 好朋友 變幻 咖啡 魔法 e 時陣， /dong2-si5 su2-liam3 mui1-zit3-e3 hor1-bing2-iu4 ben4-huan3 ga2-bi1 mo3-huat2 e3 si3-zun2',
            },
            {
                '開始時間': '69.332',
                '結束時間': '70.332',
                '語者': '市場商家1',
                'trs聽拍': 'sg0103052 特殊 e 癖好、/dik3-su5 e3 pi4-hor4',
            },
        ]

    def test_無註明語者(self):
        self.原來 = '''<Turn startTime="0" endTime="359.3665625">
<Sync time="0"/>
<Event desc="silence" type="noise" extent="instantaneous"/>
<Sync time="3.245"/>
011 細漢的時陣//de3-zap3-it-pinn1,se4-han3-e2-si2-zun2-
</Turn>
'''
        self.結果 = [
            {
                '開始時間': '0',
                '結束時間': '3.245',
                '語者': '無註明',
                'trs聽拍': '<Event desc="silence" type="noise" extent="instantaneous"/>',
            },
            {
                '開始時間': '3.245',
                '結束時間': '359.3665625',
                '語者': '無註明',
                'trs聽拍': '011 細漢的時陣//de3-zap3-it-pinn1,se4-han3-e2-si2-zun2-',
            },
        ]

    def test_後壁有恬的時間愛算入來(self):
        self.原來 = """<Turn startTime="1284.118" endTime="1286.999">
<Sync time="1284.118"/>
ah1-li1-gorh1-rin3-ui3,zeh1-vor2-li4-diorh2-vor3-
<Sync time="1285.634"/>
si3-an1-na4,ve3-dang4-gong4-
<Sync time="1286.928"/>
<Event desc="silence" type="noise" extent="instantaneous"/>
</Turn>"""
        self.結果 = [
            {
                '開始時間': '1284.118',
                '結束時間': '1285.634',
                '語者': '無註明',
                'trs聽拍': 'ah1-li1-gorh1-rin3-ui3,zeh1-vor2-li4-diorh2-vor3-',
            },
            {
                '開始時間': '1285.634',
                '結束時間': '1286.928',
                '語者': '無註明',
                'trs聽拍': 'si3-an1-na4,ve3-dang4-gong4-',
            },
            {
                '開始時間': '1286.928',
                '結束時間': '1286.999',
                '語者': '無註明',
                'trs聽拍': '<Event desc="silence" type="noise" extent="instantaneous"/>',
            },
        ]

    def test_後壁有無仝組的恬時間愛算入來(self):
        self.原來 = """<Speaker id="spk21" name="市場商家1" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk22" name="市場商家2" check="no" dialect="native" accent="" scope="local"/>
<Turn speaker="spk21" startTime="1284.118" endTime="1286.712">
<Sync time="1284.118"/>
ah1-li1-gorh1-rin3-ui3,zeh1-vor2-li4-diorh2-vor3-
<Sync time="1285.634"/>
si3-an1-na4,ve3-dang4-gong4-
</Turn>
<Turn speaker="spk22" startTime="1286.712" endTime="1393.712">
<Sync time="1286.712"/>
<Event desc="silence" type="noise" extent="instantaneous"/>
<Sync time="1289.634"/>
si3-an1-na4,ve3-dang4-gong4-
</Turn>"""
        self.結果 = [
            {
                '開始時間': '1284.118',
                '結束時間': '1285.634',
                '語者': '市場商家1',
                'trs聽拍': 'ah1-li1-gorh1-rin3-ui3,zeh1-vor2-li4-diorh2-vor3-',
            },
            {
                '開始時間': '1285.634',
                '結束時間': '1286.712',
                '語者': '市場商家1',
                'trs聽拍': 'si3-an1-na4,ve3-dang4-gong4-',
            },

            {
                '開始時間': '1286.712',
                '結束時間': '1289.634',
                '語者': '市場商家2',
                'trs聽拍': '<Event desc="silence" type="noise" extent="instantaneous"/>',
            },
            {
                '開始時間': '1289.634',
                '結束時間': '1393.712',
                '語者': '市場商家2',
                'trs聽拍': 'si3-an1-na4,ve3-dang4-gong4-',
            },
        ]

    def test_D_01_trs(self):
        self.原來 = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Trans SYSTEM "trans-14.dtd">
<Trans scribe="sann-pan" audio_filename="D-01" version="32" version_date="180702">
<Speakers>
<Speaker id="spk1" name="張素華" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk2" name="楊碧川" check="no" dialect="native" accent="" scope="local"/>
<Speaker id="spk4" name="黃越綏" check="no" dialect="native" accent="" scope="local"/>
</Speakers>
<Topics>
<Topic id="to1" desc="xx"/>
</Topics>
<Episode>
<Section type="report" topic="to1" startTime="0" endTime="1495.197">
<Turn speaker="spk1" startTime="0.000000" endTime="88.204">
<Sync time="0.000000"/>
漢字：各位 親愛 , 聽眾 朋友 , 逐家 冤 咱 , 我是 所 華
臺羅：kok8-ui7-tshin7-ai3,thiann7-tsiong2-ping7-iu2,tak10-ke7-uan1-an1,gua1-si3-soo2-hua5-
華語字幕：
</Turn>
</Section>
</Episode>
'''
        self.結果 = [
            {
                '開始時間': '0.000000',
                '結束時間': '88.204',
                '語者': '張素華',
                'trs聽拍': '漢字：各位 親愛 , 聽眾 朋友 , 逐家 冤 咱 , 我是 所 華\n'
                '臺羅：kok8-ui7-tshin7-ai3,thiann7-tsiong2-ping7-iu2,tak10-ke7-uan1-an1,gua1-si3-soo2-hua5-\n'
                '華語字幕：',
            },
        ]
