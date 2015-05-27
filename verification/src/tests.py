TESTS = {
    "Rank_01": [
        {"input": ["Fizz Buzz is x89 XX.", "checkio101"],
         "answer": "do2y7mt22kry94y2y2",
         "function_name": "encode"},
        {"input": ["do2y7mt22kry94y2y2", "checkio101"],
         "answer": "fizxzbuzzisx89xzxz",
         "function_name": "decode"},

        {"input": ["How are you?", "hello"],
         "answer": "ea2imb1ht0",
         "function_name": "encode"},

        {"input": ["ea2imb1ht0", "hello"],
         "answer": "howareyouz",
         "function_name": "decode"},

        {"input": ["My name is Alex!!!", "alexander"],
         "answer": "i1dlkxjqlexn",
         "function_name": "encode"},

        {"input": ["i1dlkxjqlexn", "alexander"],
         "answer": "mynameisalex",
         "function_name": "decode"},

        {"input": ["Who are you?", "human"],
         "answer": "rnvftc1jd5",
         "function_name": "encode"},

        {"input": ["rnvftc1jd5", "human"],
         "answer": "whoareyouz",
         "function_name": "decode"},

        {"input": ["ATTACK AT DAWN", "general"],
         "answer": 'ewwektewhnua',
         "function_name": "encode"},

        {"input": ["ewwektewhnua", "general"],
         "answer": 'attackatdawn',
         "function_name": "decode"},

        {"input": ["The quick, brown fox jumps over a lazy dog.", "nobody"],
         "answer": 'vfikwgejntasbcnzmrpqzeshwnqb2oybe1',
         "function_name": "encode"},

        {"input": [
            "A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart. I am alone, and feel the charm of existence in this spot, which was created for the bliss of souls like mine. I am so happy, my dear friend, so absorbed in the exquisite sense of mere tranquil existence, that I neglect my talents. I should be incapable of drawing a single stroke at the present moment; and yet I feel that I never was a greater artist than now. When, while the lovely valley teems with vapour around me, and the meridian sun strikes the upper surface of the impenetrable foliage of my trees, and but a few stray gleams steal into the inner sanctuary",
            "xyzqwerty"],
         "answer": 'czpokdfl4u3ddxohgtnhmddhzssple3dleokpolivtzsbgdxlp4uofsdagd3d3exydnpalhokmlilsbfmhzjjbijzsipzegbgnzeinsxkzbtbgtnrnpozdsakxxsagwdnhtllixykodypaqkmaijlelsmbzjjbjzdndtzddyrklbagqdoflelpkll1mlofsdogszhbnlnicnmwvtkdbtlfkqsalpbclptcdkhoagxyxyx1kogbd3zs3dlisydxath0x1foxykodypaydnhbgszfmwdgvtgrnzsdmkoin4urcqkpacnbcsxlirtczhohtokmhsxmdblsdbaagwsdx3dmanpsymah0teydjgxyxsagbahoy3xdzcndftzddytbtakoryagh0opeyzjzszjfoydkzmp3ymx0tursxtgxyyspegbg0cnl1tbbl0ltszdsaagysxdkbhbol0lmdbfsdmdkz2lswdl4fhrdwliagqknszsydtbroxkpmhbkylivtatxyd3h0rcvrrhxemdtbtmsxtnlemdzdofmambkzhoszdlh0da0rtx',
         "function_name": "encode"},

        {"input": [
            "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and pain can procure him some great pleasure",
            "nobody"],
         "answer": 'dtwfu1tuczqmiqbrbadsey3ij0t0icukewwbskacognbgbcodscjcahmkfowvsiooyjviqwedcqyca3itonsonoyq3fqmfhwhodsnidkqmfsioj4enrdsbl0ifvotugknoog2jdsoyvfiofrwdt0ioeicaeubevffhscbwczqmnscsbevffssvvfvfgkowsftnwgmbcsbegvqdycyqqhocrzronzbocsckfeutagtkeqkznsywaeouqmiotvscfwzktlofinvtfcwfvkkfowvsfovuofinvtfseyzkvibybobsjoaseyruykvstvhkkfowvscsbweaonj0pbcoenrdsfxjbozkmwcoeftuiywbscczusgkfkhviqbctmobwnidcaewvfcsiooaboiseykbshzevjvstvkznsogwesctunzbdwbcaqycabefwzktlofinvtfcwfvkiqodvuofinvtkej4inwebobqpbecxj1utunoefzej4grwcariceisbfqnoymiqcjnojvnevsfigqzekgcuiovlkfowvsk5',
         "function_name": "encode"},

        {"input": [
            "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country",
            "data"],
         "answer": 'gdyldscsdzcdijlthncxlvalnvuhbgmugdylvlnaktbp0udukbuwqidmgbtmaepovmmtuhgbhndxdqo1dbktdohoabk3auxamcsdbdabkt4ro1bkotqvqisgxfzmvlxbvfhibteuhndembualihnaxaqtmbhawdmdskamdmhstkapbdtmtzsdmryo1dxmtqaertradlhmpxud1hnbkwlmdedtmarwnqmkbvgcuhbnhktqtedurzgy4xdkaofdmgbhbgvcmdstagvaqtbjbbp0uduz0',
         "function_name": "encode"},

        {"input": [
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.",
            "goodmorming"],
         "answer": 'jmeprghwvdmdjmgwoxcoawamhyfewauvpeborqgxfmhncpoxbfafbaamivrdmdqmdsjcnrawmdjmoefafbcgnttn',
         "function_name": "encode"},

        {"input": [
            "One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment.",
            "iddqd"],
         "answer": 'poflpllqunvjglknfhplviltbvrhfglptzlpwqslctcmhiltjfhm0uafdlylmexmqotepllfqdogeyijqdmuvhovx3lciphsklldoglsi1poeavilnnvlmcejibihcmqdejfsemzfieavehiqbseussmfjkinvmiylfjeycppvpqlss4ysqefvs4amlfqbmqqdsaifqc1ixkjfyemulvsdktetkisdpotujfijctqdunvbvecoim1iipfsrav1kldsqoitksflfilkbqzslvseifmhhdl0nplfmu',
         "function_name": "encode"},

        {"input": [
            "gdyldscsdzcdijlthncxlvalnvuhbgmugdylvlnaktbp0udukbuwqidmgbtmaepovmmtuhgbhndxdqo1dbktdohoabk3auxamcsdbdabkt4ro1bkotqvqisgxfzmvlxbvfhibteuhndembualihnaxaqtmbhawdmdskamdmhstkapbdtmtzsdmryo1dxmtqaertradlhmpxud1hnbkwlmdedtmarwnqmkbvgcuhbnhktqtedurzgy4xdkaofdmgbhbgvcmdstagvaqtbjbbp0uduz0",
            "data"],
         "answer": 'farfarawaybehindthewordmountainsfarfromthecountriesvokaliaandconsonantiatherelivetheblindtextsseparatedtheyliveinboxokmarksgroverightatxthecoastofthesemanticsalargelanguageoceanasmallrivernamedxdudenflowsbytheirplaceandsuppliesitwiththenecesxsaryregelialiaitisaparadisematiccountryz',
         "function_name": "decode"},


        {"input": [
            "jmeprghwvdmdjmgwoxcoawamhyfewauvpeborqgxfmhncpoxbfafbaamivrdmdqmdsjcnrawmdjmoefafbcgnttn",
            "goodmorming"],
         "answer": 'loremipsumdolorsitametconsectetueradipiscingelitaeneancomxmodoligulaegetdoloraeneanmassa',
         "function_name": "decode"},
        {"input": [
            "poflpllqunvjglknfhplviltbvrhfglptzlpwqslctcmhiltjfhm0uafdlylmexmqotepllfqdogeyijqdmuvhovx3lciphsklldoglsi1poeavilnnvlmcejibihcmqdejfsemzfieavehiqbseussmfjkinvmiylfjeycppvpqlss4ysqefvs4amlfqbmqqdsaifqc1ixkjfyemulvsdktetkisdpotujfijctqdunvbvecoim1iipfsrav1kldsqoitksflfilkbqzslvseifmhhdl0nplfmu",
            "iddqd"],
         "answer": 'onemorningwhengregorsamsawokefromtroubledxdreamshefoundhimselftransformedinhisbedintoahorxribleverminhelayonhisarmourlikebackandifheliftedhisheadalitxtlehecouldseehisbrownbellyslightlydomedanddividedbyarchesintostifxfsectionsthebedxdingwashardlyabletocoveritandsexemedreadytoslideoffanymoment',
         "function_name": "decode"},
        {"input": ["vfikwgejntasbcnzmrpqzeshwnqb2oybe1", "nobody"],
         "answer": 'thequickbrownfoxjumpsoveralazydogz',
         "function_name": "decode"},
    ]
}
