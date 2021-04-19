import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("アナルオナニー")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):

    if message.content.startswith("死ね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("お前が死ね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("しね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("お前がしね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("おまえがしね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("お前が死ね"):
        await message.channel.send("死ぬべきなのは社会不適合者であるあなたなのでは？:wink:")
    if message.content.startswith("殺す"):
        await message.channel.send("殺されるべきなのは未だに親のすねかじってるあなたなのでは？:wink:")
    if message.content.startswith("お前殺す"):
        await message.channel.send("殺されるべきなのは未だに親のすねかじってるあなたなのでは？:wink:")
    if message.content.startswith("ころす"):
        await message.channel.send("殺されるべきなのは未だに親のすねかじってるあなたなのでは？:wink:")
    if message.content.startswith("まんこ"):
        await message.channel.send("舐めたいですねぇ")
    if message.content.startswith("ちんこ"):
        await message.channel.send("しゃぶりたいですねぇ")
    if message.content.startswith("アスペ"):
        await message.channel.send("おたそら？")
    if message.content.startswith("まんこ"):
        await message.channel.send("舐めたいですねぇ")
    if message.content.startswith("ひま"):
        await message.channel.send("で？どうしろってんだよゴミが")
    if message.content.startswith("ガンジャ"):
        await message.channel.send("吸いたいのおおお:relaxed::relaxed::relaxed::relaxed::relaxed:")
    if message.content.startswith("あべ"):
        await message.channel.send("????????????????????????????????????????????????????????????????????????"
                                   "????????????"
                                   "???????????????？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？"
                                   "？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？？")
    if message.content.startswith("自殺しろ"):
        await message.channel.send("いやですけどぉ？ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ")
    if message.content.startswith("よろしく"):
        await message.channel.send("敬語使ってください:grinning:")
    if message.content.startswith("よろしくお願いします"):
        await message.channel.send("はい:grinning:まず住所と名前、あと顔写真まで貼っちゃって下さい:grinning:")
    if message.content.startswith("いやです"):
        await message.channel.send("ここから失せろ雑魚:grinning:")
    if message.content.startswith("無理です"):
        await message.channel.send("つまんねえな、死ねや:grinning:")
    if message.content.startswith("無理"):
        await message.channel.send("無理はあんたのお母さんが生まれてきたあなたを見た途端言った言葉です:grinning:")
    if message.content.startswith("うざいなｗ"):
        await message.channel.send("あなたのお母さんもあなたを見る度にそう思ってるはずですよ:grinning:")
    if message.content.startswith("はじめまして"):
        await message.channel.send("くたばれ:grinning:")
    if message.content.startswith("旦那さん"):
        await message.channel.send("俺、今お前としゃべる気分じゃないんだよね:shushing_face:")

    if message.content == "こんにちは":
       ran = random.randint(0,7)
       if ran == 0:
           d = "別に俺達、挨拶交わすほどの仲でもないですよね"
       if ran == 1:
           d = "はい、どうも"
       if ran == 2:
           d = "なに挨拶してんのお前"
       if ran == 3:
           d = "挨拶とかそういうの要らねえから"
       if ran == 4:
           d = "はい！こんにちはです！"
       if ran == 5:
           d = "だりぃな、今日も、お前も"
       if ran == 6:
           d = "うっせえよ"
       if ran == 7:
           d = "いいからどっかに消えてくれない？"
       await message.channel.send(d)

    if message.content == "占ってください":
       ran = random.randint(0,106)
       if ran == 0:
           q = "自分でやればいいじゃないですか:weary:"
       if ran == 1:
           q = "やる気出ないんで無理ですねぇ…"
       if ran == 2:
           q = "ちょっと今ギター鳴らしてるんで後にしてください"
       if ran == 3:
           q = "今カレー食ってるんで無理っす"
       if ran == 4:
           q = "あなたそのうち死にますよ:wink:"
       if ran == 5:
           q = "あなたはですねぇ...なんか生きてても良い事全くないんで、早めに死んだ方がいいんじゃないですか？:wink:"
       if ran == 6:
           q = "いやです、僕はあなたのための暇つぶし道具じゃないんですよ？:wink:"
       if ran == 7:
           q = "あっ！！！！！！！お前、明日絶対死ぬじゃんｗｗｗｗｗｗｗｗｗｗｗご愁傷様:smiley::smiley:"
       if ran == 8:
           q = "あー。。まあ、いいんじゃないっすか？運勢"
       if ran == 9:
           q = "ネットで生きる道を選んだ以上、いくら占ったっていい結果出ませんよ？"
       if ran == 10:
           q = "ｗ"
       if ran == 11:
           q = "やだ"
       if ran == 12:
           q = "僕の占いによるとですね…今があなたの人生の最高点なんですよ、" \
               "つまりこっから先は下り道しかないってことですね～:joy::joy::joy:"
       if ran == 13:
           q = "めんどくせえな、失せろ"
       if ran == 14:
           q = "就職活動してください:smiley:"
       if ran == 15:
           q = "ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ:smiley::smiley::smiley::smiley::smiley::smiley:" \
               ":smiley::smiley::smiley::smiley::smiley::smiley::smiley::smiley:"
       if ran == 16:
           q = "お前は「オカマ」でしょ？:smiley:"
       if ran == 17:
           q = "ほら、あのころ「バイキン」と呼ばれてイジメられていた時期のことを想い出してください:thinking:" \
               "あの頃より、今のほうがマシでしょ？:smiley:"
       if ran == 18:
           q = "kuzuさん元イジメられっ子ですよね？:thinking:"
       if ran == 19:
           q = "夢みんな童貞"
       if ran == 20:
           q = "あなた...もしかして中卒？:thinking:"
       if ran == 21:
           q = "貴方だれですか？:thinking:"
       if ran == 22:
           q = "モモさんからあなたの画像送ってもらいます"
       if ran == 23:
           q = "なーんか気持ち悪いですよね、おまえって"
       if ran == 24:
           q = "お金払ってから言ってください"
       if ran == 25:
           q = "http://vippers.jp/archives/9647640.html"
       if ran == 26:
           q = "占えつってもよぉ…今まで生きてきてお前もうすうす感じてるはずなんですよね…" \
               "お前の人生、不幸しかないってことが…"
       if ran == 27:
           q = "あなたは明日の夕方ぐらいに脳出血で死にますね"
       if ran == 28:
           q = "可愛そうだから占えません"
       if ran == 29:
           q = "あなたは女のけつばっか追ってるから、結局は性病で死にますね"
       if ran == 30:
           q = "あなたはあなたのお母さんに殺されます"
       if ran == 31:
           q = "あ、はい、今から占いますね" \
               "え？なにこれ？．．．" \
               "え？ｗｗｗｗｗｗｗｗｗｗｗｗｗｗ" \
               "お前ｗｗｗｗｗｗｗｗｗｗｗｗｗ" \
               "あｗｗｗｗｗｗｗｗｗｗｗｗｗｗ" \
               "ｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗｗ" \
               "明後日死にます"
       if ran == 32:
           q = "あなたは社会に適応できず自殺します"
       if ran == 33:
           q = "いまぁがんじゃぁきめてっからぁなにもできないんですよぉあぁぁぁぁあぁあぁああぁあぁ"
       if ran == 34:
           q = "ゆきだるまさんって知ってますか？" \
               "あなたはゆきだるまさんと相性いいです"
       if ran == 35:
           q = "あなたは顔が長くなりますね"
       if ran == 36:
           q = "え、いやですよ"
       if ran == 37:
           q = "あーあなたは生活保護者目指した方がいいですね"
       if ran == 38:
           q = "しね"
       if ran == 39:
           q = "ワッダファッカー？！"
       if ran == 40:
           q = "占って欲しいんだったら顔くらい見せてください"
       if ran == 41:
           q = "あなたは今年から来年まで最悪です"
       if ran == 42:
           q = "あなた、来年から最悪ですね、今のうちに自殺した方が楽かもしれません"
       if ran == 43:
           q = "たまに散歩とかしたらどうですか？僕は毎日相模原公園で散歩してます"
       if ran == 44:
           q = "30代まではいいんですけど。。40代なったら健康が悪くなる可能性が高いですね、死んでください"
       if ran == 45:
           q = "めんどくさいんですよ、占いたくないです"
       if ran == 46:
           q = "お金ちょうだい～:joy::joy::joy:"
       if ran == 47:
           q = "あなたは人に嫌われやすい性格してますね、私もあなたが嫌いになりました"
       if ran == 48:
           q = "クリトリスぺろぺろ～:stuck_out_tongue_winking_eye:"
       if ran == 49:
           q = "占いとか迷信なのであんま信じない方がいいですよ？占う気もないですけど"
       if ran == 50:
           q = "昔の思い出に浸って死にたくなる時ってありませんか、" \
               "今ちょっと鬱なんで占えないです、失せてください"
       if ran == 51:
           q = "届けママへの思い!+。:.ﾟ٩(๑＞ ͜ ＜๑)۶:.｡+ﾟ"
       if ran == 52:
           q = "お前は現代社会で餓死します、惨めな人生ですね"
       if ran == 53:
           q = "どうでもいいんでおっぱい見せてくれませんか"
       if ran == 54:
           q = "お前はどらえもんののび太以下だ"
       if ran == 55:
           q = "お前は生きるのが下手だ"
       if ran == 56:
           q = "お前は常に誰かを殺そうとしてる"
       if ran == 56:
           q = "デパスキメな"
       if ran == 57:
           q = "早く大麻でぶっ飛びたい"
       if ran == 58:
           q = "あなたアナルオナニーすきですよね？"
       if ran == 59:
           q = "おろろんおろろんおろろん"
       if ran == 60:
           q = "ぶっちゃけ、お前は死んでもいいと思ってる"
       if ran == 61:
           q = "うるせえよ"
       if ran == 62:
           q = "お前みたいなイキリ隠キャまじ無理"
       if ran == 63:
           q = "エロイプしてそう"
       if ran == 64:
           q = "ここさ、気持ち悪いのうじゃうじゃいるよね"
       if ran == 65:
           q = "お前今日死ぬよ？"
       if ran == 66:
           q = "お前は死ぬとき全身ちぎられて死ぬんだって"
       if ran == 67:
           q = "援交してそう"
       if ran == 68:
           q = "私、あなたに全く興味ないんですよ…そういう人を占う価値ってあるんですか？"
       if ran == 69:
           q = "私の占いはお金発生するんで早く私の口座に1万円振り込んでください"
       if ran == 70:
           q = "あなたはふけの量がやばいって結果がでました"
       if ran == 71:
           q = "あなた、普段から女装してそうな感じですね"
       if ran == 72:
           q = "？"
       if ran == 73:
           q = "ファッカー"
       if ran == 74:
           q = "あなた面食いですよね、面食いって早めに死ぬの知ってました？"
       if ran == 75:
           q = "お前は今日死んでください"
       if ran == 76:
           q = "あなたは個性的な性格してますね、社会から淘汰されてここまで流れ込んだんですか"
       if ran == 77:
           q = "陰湿な性格してますね、今すぐ死んでください"
       if ran == 78:
           q = "俺、お前みたいなやつ大嫌いなんだよね" \
               "だから占わない"
       if ran == 79:
           q = "おまえ、かなりしんどい人生いきてるね、これからもそれ変わらないから、お前は死ぬまでしんどいままだよ"
       if ran == 80:
           q = "特に言うことないんだけど"
       if ran == 81:
           q = "お前の運勢とかどうでもいいんだよまじで"
       if ran == 82:
           q = "あなた女の子ですか？男ですか？、俺、基本女の子しか占いたくないんだよ"
       if ran == 83:
           q = "だりぃ"
       if ran == 84:
           q = "お前ガンジャキメたことある？俺はあるけど"
       if ran == 85:
           q = "俺は半グレ人間なんだ、俺はやばいやつなんだよ"
       if ran == 86:
           q = "デパスキメてえな"
       if ran == 87:
           q = "幸せにはなれない人生だね"
       if ran == 88:
           q = "とりあえず楽器弾けって話ですね"
       if ran == 89:
           q = "一つ忠告です" \
               "私は本心を表に出しません" \
               "何故ならいつでも理想どおりことをすすめたいからです"
       if ran == 90:
           q = "全裸オナニー動画送ってください"
       if ran == 91:
           q = "お前のお父さん変態すぎるため占えないです！人間じゃない！お前のお父さんは！"
       if ran == 92:
           q = "どちらかと言えば長生きするタイプの人です"
       if ran == 93:
           q = "シャブ中っぽい見た目してますねえ"
       if ran == 94:
           q = "私のことが好きなんですか"
       if ran == 95:
           q = "日本語学びなおしてきてください"
       if ran == 96:
           q = "あなたも早く音楽を作ってくださいマヌケ"
       if ran == 97:
           q = "あなたは多くの人から嫌われてます"
       if ran == 98:
           q = "大人しくしないと痛い目にあいますよ"
       if ran == 99:
           q = "お前はゲームに怠けています" \
               "堕落してます"
       if ran == 100:
           q = "きしょいっす"
       if ran == 101:
           q = "ダルいので今日は布団に引きこもります"
       if ran == 102:
           q = "お疲れさまでした" \
               "永久に" \
               "眠ってください"
       if ran == 103:
           q = "生きなければならない"
       if ran == 104:
           q = "生きてる価値あるんすか？"
       if ran == 105:
           q = "何も生み出さないただのゴミ"
       if ran == 106:
           q = "あなたはゴミの種類でいえばもえないゴミなんですよ"

       await message.channel.send(q)













client.run("ODMzNTExMjI5NDE4MTEwOTc4.YHzZ0g.CyvQAkznRolzBf_TtAZsvCoO9SM")