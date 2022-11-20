因為我們的R跟C都是profile 決定的結果，所以corner的位置會隨著WS改變而跟著變化，這邊介紹每個conrer在不同pitch下的位置，先介紹minimum pitch的情況，這個圖是rc scattering，x軸是Rs，y軸是Ctotal,旁邊兩張的y軸分別是Cc和Cv,為什麼要有這兩張圖？Ctotal是2Cc+Cv,Cc是兩個metal coupling的電容， Cv是C vertical代表上下層金屬造成的電容，所以這張Ctotal的圖其實就是把這兩張圖疊加起來，我們在fitting的時候是看著component 去fitting,Ctotal只是兩個component疊加的結果，那我們來看Cc這張圖,為什麼這邊的rc corner幾乎跟Cbest Cworst 一樣？前面提到corner skew是反應metal profile還有IMD厚度的變化，Cbest跟rcworst的 metal profile是一樣的，所以Coupling的Cc差距不大，這兩個corner只有差在IMD的厚度，Cv這邊可以很明顯看到RC_worst比較大，是來自於IMD厚度變小，那C_worst跟RC_best也是一樣，Cc差不多，RC_best的Cv比較小，來自於IMD厚度變大，那我們剛剛有說Ctotal是2Cc+Cv，下方這邊有這兩個Component佔Ctotal的比例 ,Cc佔88%，Cv佔12%，在space很小的時候，coupling的電容很大，佔比遠高於Cv，所以Ctotal幾乎跟Cc這張圖長得一模一樣，代表RC corner其實會隨著pitch大小而變化，在minimum pitch RC_worst會跟C_best差不多，所以不是所有pitch的RC worst都是worst case，RC_best也是一樣，取決於Cc跟Cv之間的占比
下面是Iso pitch的RC scattering， Cv的占比遠大於Cc，Ctotal是Cv主導所以RC_worst跟RC_best開始朝C_worst跟C_best的方向叉開，
這一頁介紹Via corner，metal與metal之間要有Via存在才有辦法傳遞電流，所以Via的電阻對於backend來說也很重要，metal的電流方向是穿入紙面的，Via的電流是垂直經過金屬跟Via的截面，所以Via的電阻大小主要取決於這個截面的大小，截面變大電阻會變小，截面變小電阻則會變大，製程的variation會造成截面大小變化，Via的C_best,RC_best是截面變大，C_worst,RC_worst是截面變小，那為什麼會這樣定義呢，這樣定義的第一個原因是為了讓worst case是最worst的，best case是最best，第二個原因是這樣做model可以更靠近常態分佈，我們看右邊的這張圖，一樣是RC圖，但是x軸從Rs變成Rs+Rc，原本我們只看metal的corner，現在把Via的影響也加進來一起看，這四個紅點就是我們定義的3sigma corner，中間的橢圓形是Si data，這四個紅點圍起來的圖形跟中間Si的橢圓其實有些差異，Si會是橢圓形是因為全部製程的variation總合起來後會是一個常態分佈，那我們的model想要更接近常態分佈的話，C_best,RC_best要向左移動，C_worst,RC_worst要向右移動，變成藍色的點，圍出來的圖形會更接近Si的橢圓
