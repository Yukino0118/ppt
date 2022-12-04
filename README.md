1.	新增Rs公式
我們以前學過Rs= rho*L/A，A是電流方向的面積，所以這個面積大小會影響Rs的大小
2.	畫虛線metal profile skew
那backend最重要的就是Rs跟Ctotal(指)我們歸納了兩類會影響RC的variation
~~~~
第一種variation metal profile skew代表金屬的大小變化，會影響面積跟周圍金屬的距離，所以Rs跟Ctotal都會受到影響，這一列都打勾代表會影響，第二種variation上下層IMD厚度skew代表上下IMD的厚度變化，主要影響到Ctop跟Cbottom
Metal profile skew代表金屬會變大或變小，所以粉色梯形只有三種，變大3s,typ,變小3s，Rs也只會有三個位置，金屬變大R變小，typ，金屬變小R變大
再來看Ctotal的變化，metal profile變大金屬之間距離變近，Coupling電容變大，所以在typical上方，metal profile變小金屬之間距離變遠，coupling電容變小，所以在Typ下方，再搭配剛剛的Rs位置來看，R大C小的情況叫做Cbest，R小C大的情況叫做Cworst，剛剛有提到corner是兩個variation搭配出來的，我們base on這兩個corner再去加上IMD的variation，Cworst IMD厚度變厚，上下距離變遠，C變小往下移動，R小C小的情況叫做RCbest，Cbest IMD厚度變薄，上下距離變近，C變大往上移動，R大C大的情況叫做RCworst

這頁舉實際上model的例子，這是iso pitch的Typical profile，我們把金屬之間距離很遠的情況叫做iso pitch，在這情種情況下，Cc會變得很小，Ctop跟Cbottom會變很大，下面這張圖是iso pitch的corner位置，跟剛剛介紹的圖很像，
那Ctotal=2Cc+Cv，所以這張圖是這兩張圖的疊加，我們看這兩張圖就好
先看typ跟Cworst，metal profile變大，Rs變小，金屬之間互相靠近，但是iso pitch的space太大，靠近的距離遠小於這個space，所以Cc幾乎沒有變化，跟Typical差不多，Cv的部分，上下面積變大IMD距離變近Cv變大，搭配Rs的位置，所以Cv會在左上方，Cbest也是一樣的原理，再來看RCbest，metal profile一樣所以Rs位置一樣，他跟Cworst只差在IMD厚度，那IMD主要影響Cv，代表RCbest會離Cworst多遠取決於Cv變化量在Ctotal中的占比，先看Cv，因為IMD變厚上下距離變遠，Cv變小往下移動到這邊，Cv下降的時候，Cc受到電力線拉扯變得比Cworst大了一點，Ctotal=2Cc+Cv，這邊typical的Cc是0.004占了Ctotal 4%，Cv是0.13占了96%，所以Ctotal會跟這張Cv幾乎一樣，在Iso pitch，因為Cv dominated，IMD厚度影響占比很重，所以RC corner會遠離C corner


再來看比較特別的例子，這是minimum pitch的typical profile，實際上電路中最常用的是minimum pitch，minimum pitch是整個node線寬跟距離最小的金屬，在這種情況下，金屬之距離很近Cc會變得很大，Ctop跟Cbottom的電力線都被Cc拉走會變小，

一樣先看typ跟Cworst，metal profile變大，Rs變小，金屬之間互相靠近，Cc變大，所以在左上方，Cv的部分，上下面積變大IMD距離變近搭配這個Rs，所以Cv也會在左上方，Cbest也是一樣的原理，再來看RCbest，metal profile一樣所以Rs位置一樣，他跟Cworst只差在IMD厚度，IMD變厚上下距離變遠，Cv變小往下移動到這邊，Cc受到電力線拉扯變得比Cworst大了一點，Ctotal=2Cc+Cv，這邊typical的2Cc是0.004占了Ctotal 82%，Cv是0.13占了18%，所以Ctotal會跟Cc這張圖相似，但是RCbest因為Cv往下掉所以位置被拉下來在這邊
所以RC corner的位置是會跟著pitch大小而變化的，因為RC corner是base on C corner加上IMD厚度的變化，如果電容對IMD的變化不敏感，也就是Cc dominated的時候，那RC corner會近似於C corner，如果是Cv dominated，電容對IMD厚度變化很敏感，RC corner會遠離C corner

Metal與metal之間要有Via存在才能傳遞電流，所以Via的電阻對backend來說也很重要，這頁會介紹Via的corner
上面的梯形是金屬，下面是Via，metal的電流方向是垂直出入紙面，Via的電流方向是垂直經過metal跟Via的潔面，電阻的公式一樣是Rc=rho*L/A，Via電阻會跟截面積還有Via高度有關，剛剛有介紹metal corner的IMD厚度會改變，以process來說Via的大小會跟IMD厚度有關，IMD越厚Via會越大，IMD越薄，Via會越小，搭配剛剛的corner來看，Cbest,RCbest的IMD比較厚，Via變大Rc下降，Cworst,RCworst的IMD厚度比較薄，Via變小Rc上升，那Rs加上Via Rc之後corner會怎麼變化，看右邊這張圖，x軸是Rs+Rc，y軸是Ctotal，中間的灰色橢圓是Si，紅色的點是還沒加上Rc的Rs corner，藍色的是Rs+Rc corner，Cbest,RCbest搭配Rc下降所以往左偏移，Cworst,RCworst搭配Rc上升所以往右偏移，藍色的點圍起來的圖形也會更接近Si的橢圓，Si是橢圓是因為所有製程的variation總合起來會是常態分佈，加上via的corner之後我們的model更能反應Si的狀況
