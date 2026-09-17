# -*- coding: utf-8 -*-
import os, re
import gen_legal as G
esc = G.esc; page = G.page; switcher = G.switcher; OUT = G.OUT

# ---------- block renderer for code articles ----------
def blocks_html(blocks, indent="          "):
    out = []
    for b in blocks:
        if b[0] == "p":
            out.append('%s<p>%s</p>' % (indent, esc(b[1])))
        elif b[0] == "ul":
            out.append('%s<ul>' % indent)
            for it in b[1]:
                out.append('%s  <li>%s</li>' % (indent, esc(it)))
            out.append('%s</ul>' % indent)
    return "\n".join(out)

def code_body(aklats):
    out = []
    for (aid, label, title, arts, raw) in aklats:
        out.append('      <section class="legal-part" id="%s">' % aid)
        out.append('        <span class="part-label">%s</span>' % esc(label))
        out.append('        <h2 class="part-title">%s</h2>' % esc(title))
        out.append('        <div class="part-flourish"><span>✦</span></div>')
        for (num, atitle, blocks) in arts:
            out.append('        <div class="articulo" id="art-%s">' % num)
            out.append('          <span class="articulo-num">Artikulo %s — <span class="art-title">%s</span></span>' % (num, esc(atitle)))
            out.append(blocks_html(blocks))
            out.append('        </div>')
        if raw:
            out.append(raw)
        out.append('      </section>')
    return "\n".join(out)

def code_toc(aklats):
    lis = ["        <ul>"]
    for (aid, label, title, arts, raw) in aklats:
        lis.append('          <li>')
        lis.append('            <a class="top" href="#%s">%s</a>' % (aid, esc(label + " — " + title)))
        if arts:
            lis.append('            <ul class="sub">')
            for (num, atitle, blocks) in arts:
                lis.append('              <li><a href="#art-%s">Art. %s — %s</a></li>' % (num, num, esc(atitle)))
            lis.append('            </ul>')
        lis.append('          </li>')
    lis.append("        </ul>")
    return "\n".join(lis)

# ================= CÓDIGO SIBIL =================
SIBIL = [
 ("cs-a1","Aklat I","Mga Pangkalahatang Alituntunin",[
   ("1","Saklaw",[("p","Ang kasong sibil ay tumutukoy sa mga alitang hindi kriminal, kung saan ang layunin ay kabayaran, pagtupad sa kasunduan, o pagbabalik ng ari-arian, at hindi pagpaparusa.")]),
   ("2","Sino ang Maaaring Magsampa",[("p","Maaaring magsampa ng kasong sibil ang:"),("ul",["sinumang mamamayan","may-ari ng ari-arian","kasosyo sa negosyo","tagapagmana","sinumang napinsala ng gawa ng iba"])]),
   ("3","Pamantayan ng Katibayan",[("p","Ang hukuman ay magpapasya batay sa mas mabigat na ebidensiya (preponderance of evidence), at hindi sa pamantayang “beyond reasonable doubt.”")]),
   ("4","Layunin ng Hatol",[("p","Maaaring iutos ng hukuman ang:"),("ul",["pagbabayad ng danyos","pagtupad ng kasunduan","pagbabalik ng ari-arian","pagpapatigil ng isang gawain (injunction)"])]),
 ],""),
 ("cs-a2","Aklat II","Mga Kontrata at Utang",[
   ("5","Bisa ng Kontrata",[("p","Ang isang kasunduan ay may bisa kung may:"),("ul",["pahintulot ng magkabilang panig","malinaw na bagay o serbisyo","kapalit o bayad"]),("p","Ang kasunduang pasalita ay may bisa kung may sapat na saksi.")]),
   ("6","Paglabag sa Kontrata",[("p","Ang sinumang hindi tumupad sa kasunduan ay mananagot sa:"),("ul",["kabayaran sa pinsala","bayad sa nawalang kita","gastos sa paglilitis"])]),
   ("7","Utang",[("p","Ang may utang ay dapat magbayad sa itinakdang panahon."),("p","Kung hindi makabayad, maaaring ipag-utos ng hukuman ang:"),("ul",["pagbabayad nang hulugan","pagkumpiska ng ari-arian"]),("p","Hindi maaaring ipakulong ang may utang maliban kung may panlilinlang.")]),
   ("8","Panlilinlang",[("p","Kung ang utang ay nakuha sa pamamagitan ng panlilinlang o pekeng pangako, ito ay maaaring maging kasong kriminal bukod sa pananagutang sibil.")]),
 ],""),
 ("cs-a3","Aklat III","Ari-arian",[
   ("9","Pagmamay-ari",[("p","Ang sinumang may hawak ng lupa, bahay, hayop, o kagamitan at napatunayang kanya ay kikilalaning may-ari.")]),
   ("10","Ilegal na Pag-angkin",[("p","Ang pagkuha o paggamit ng ari-arian ng iba nang walang pahintulot ay nagbibigay sa may-ari ng karapatang:"),("ul",["bawiin ang ari-arian","maningil ng danyos"])]),
   ("11","Hangganan ng Lupa",[("p","Sa alitang may kinalaman sa hangganan:"),("ul",["unang pagbabatayan ang kasulatan","kung wala, ang testimonya ng mga saksi","kung wala pa rin, ang matagal na pag-okupa"])]),
 ],""),
 ("cs-a4","Aklat IV","Pinsala at Danyos",[
   ("12","Pananagutan",[("p","Ang sinumang makapinsala sa tao o ari-arian, kahit walang intensyon ngunit dulot ng kapabayaan, ay mananagot sa danyos.")]),
   ("13","Uri ng Danyos",[("p","Maaaring ipagkaloob ng hukuman ang:"),("ul",["aktuwal na danyos (nasirang ari-arian)","nawalang kita","danyos moral (kahihiyan o matinding abala)"])]),
   ("14","Pananagutan ng May-ari",[("p","Ang may-ari ng mga sumusunod ay mananagot sa pinsalang dulot nito kung may kapabayaan:"),("ul",["kabayo","baka","karwahe","negosyo"])]),
 ],""),
 ("cs-a5","Aklat V","Pamilya at Pamana",[
   ("15","Mana",[("p","Sa pagkamatay ng isang tao:"),("ul",["ang asawa ang unang may karapatan","susunod ang mga anak","kung wala, ang kapatid o ibang kamag-anak"])]),
   ("16","Hatiang Mana",[("p","Ang mana ay paghahatian nang pantay ng mga anak maliban kung may umiiral na testamento.")]),
   ("17","Testamento",[("p","Ang huling habilin ay kikilalanin kung:"),("ul",["may dalawang saksi","malinaw ang nilalaman","ginawa ng taong nasa matinong pag-iisip"])]),
 ],""),
]
open(os.path.join(OUT,"codigo-sibil.html"),"w",encoding="utf-8").write(
  page("codigo-sibil.html","Código Sibil","Batas Sibil","Código Sibil", code_toc(SIBIL), code_body(SIBIL)))
print("wrote codigo-sibil.html")

# ================= CÓDIGO ADMINISTRATIBO =================
OATH = '''        <div class="articulo">
          <p>Bago manungkulan, ang bawat opisyal ay manunumpa:</p>
          <blockquote style="margin:14px 0 0;padding:18px 22px;border-left:3px solid var(--gold);background:rgba(212,162,74,.08);border-radius:0 6px 6px 0;font-style:italic;color:var(--parchment);font-size:1.1rem;">“Ako ay maglilingkod nang tapat sa Bayang Sinilangan, ipatutupad ang batas nang walang takot o pabor, at hindi gagamitin ang aking kapangyarihan para sa pansariling pakinabang.”</blockquote>
        </div>'''
ADMIN = [
 ("ca-a1","Aklat I","Mga Pangkalahatang Tuntunin",[
   ("1","Saklaw",[("p","Ang Kodigong ito ay umiiral sa lahat ng lingkod-bayan ng Ciudad de Paseo, halal man o hinirang.")]),
   ("2","Mga Saklaw na Opisyal",[("p","Kabilang dito ang:"),("ul",["mga Gobernador","mga Alkalde at pinuno ng baryo","mga miyembro ng Konstabularyo","mga kawani ng hukuman","iba pang opisyal na itinalaga ng pamahalaan (hal. mga doktor)"])]),
   ("3","Katangian ng Tungkulin",[("p","Ang posisyon sa pamahalaan ay isang tiwala ng bayan at hindi isang pribadong pag-aari."),("p","Ang sinumang manunungkulan ay mananagot sa batas at sa mamamayan.")]),
 ],""),
 ("ca-a2","Aklat II","Mga Tungkulin ng Opisyal",[
   ("4","Pangunahing Tungkulin",[("p","Ang bawat opisyal ay dapat:"),("ul",["ipatupad ang batas","panatilihin ang katahimikan at kaayusan","protektahan ang buhay at ari-arian","igalang ang hukuman","sumunod sa mga legal na utos ng hukom"])]),
   ("5","Paggalang sa Hudikatura",[("p","Ang sinumang opisyal na:"),("ul",["tatangging sumunod sa subpoena, orden, o mandamiento (warrant)","hahadlang sa pagpapatupad ng legal na pag-aresto","makikialam sa proseso ng paglilitis"]),("p","ay maaaring managot sa administrative misconduct at contempt of court.")]),
 ],""),
 ("ca-a3","Aklat III","Mga Ipinagbabawal na Gawain",[
   ("6","Korapsyon",[("p","Mahigpit na ipinagbabawal ang:"),("ul",["pagtanggap ng suhol","paghingi ng bayad kapalit ng serbisyo","pagkuha ng ari-arian ng mamamayan nang walang pahintulot o kabayaran"])]),
   ("7","Pang-aabuso sa Kapangyarihan",[("p","Itinuturing na paglabag ang:"),("ul",["ilegal na pag-aresto","pagpapahirap o pananakit sa detenido","pananakot gamit ang posisyon","paggamit ng kapangyarihan sa pansariling alitan"])]),
   ("8","Pagpapabaya sa Tungkulin",[("p","Ang opisyal na:"),("ul",["sadyang hindi kikilos sa reklamo","tatangging tumulong sa mamamayan","iiwan ang tungkulin nang walang sapat na dahilan"]),("p","ay mananagot sa kapabayaan.")]),
 ],""),
 ("ca-a4","Aklat IV","Mga Kasong Administratibo",[
   ("9","Pagsisimula ng Reklamo",[("p","Ang sinumang mamamayan ay maaaring magsampa ng reklamo laban sa isang opisyal sa Hukuman o sa Kataas-taasang Hukuman.")]),
   ("10","Paunang Imbestigasyon",[("p","Susuriin ng Hukuman kung may sapat na batayan ang reklamo."),("p","Kung mayroon, ipapatawag ang opisyal upang magbigay ng paliwanag.")]),
   ("11","Preventive Suspension",[("p","Kung mabigat ang paratang, maaaring pansamantalang alisin sa tungkulin ang opisyal habang isinasagawa ang imbestigasyon.")]),
 ],""),
 ("ca-a5","Aklat V","Pagdinig at Pagpapasya",[
   ("12","Pagdinig",[("p","Magkakaroon ng pormal na pagdinig kung saan:"),("ul",["ihaharap ang ebidensya","maririnig ang panig ng depensa","maaaring magtanong ang hukom"])]),
   ("13","Pamantayan ng Katibayan",[("p","Ang desisyon ay ibabatay sa substantial evidence o malinaw at kapani-paniwalang patunay.")]),
 ],""),
 ("ca-a6","Aklat VI","Mga Parusa",[
   ("14","Mga Uri ng Parusa",[("p","Maaaring ipataw ang mga sumusunod:"),("ul",["Babala (Reprimand)","Multa","Suspensyon","Pagpapatalsik sa tungkulin (Dismissal)","Permanenteng pagbabawal sa panunungkulan"])]),
   ("15","Epekto ng Dismissal",[("p","Ang pinatalsik na opisyal ay:"),("ul",["agad mawawalan ng kapangyarihan","hindi na maaaring gumamit ng titulo o posisyon","kailangang isauli ang lahat ng kagamitan ng pamahalaan"])]),
 ],""),
 ("ca-a7","Aklat VII","Kaugnay sa Kasong Kriminal",[
   ("16","Hiwalay na Pananagutan",[("p","Ang kasong administratibo ay hiwalay sa kasong kriminal."),("p","Kahit mapawalang-sala sa kasong kriminal, maaari pa ring maparusahan sa kasong administratibo.")]),
 ],""),
 ("ca-a8","Aklat VIII","Pagsunod sa Utos ng Hukuman",[
   ("17","Pagtanggi sa Utos",[("p","Ang opisyal na sadyang tatanggi sa utos ng hukuman ay maaaring:"),("ul",["agad masuspinde","maaresto dahil sa contempt of court","matanggal sa tungkulin"])]),
 ],""),
 ("ca-a9","Aklat IX","Panunumpa ng Opisyal",[],OATH),
]
open(os.path.join(OUT,"codigo-administratibo.html"),"w",encoding="utf-8").write(
  page("codigo-administratibo.html","Código Administratibo","Batas Administratibo","Código Administratibo", code_toc(ADMIN), code_body(ADMIN)))
print("wrote codigo-administratibo.html")

# ================= MAGAGAAN NA PAGLABAG =================
def mg_art(n,t,pen,tm,fine):
    return ('        <div class="articulo" id="art-%s">\n'
            '          <span class="articulo-num">Artikulo %s — <span class="art-title">%s</span></span>\n'
            '          <div class="crime-meta">\n'
            '            <div class="crime-badge pen"><span class="cb-label">⚖️ Parusa</span><span class="cb-value">%s</span></div>\n'
            '            <div class="crime-badge"><span class="cb-label">⏱️ Tagal</span><span class="cb-value">%s</span></div>\n'
            '            <div class="crime-badge fine"><span class="cb-label">💰 Multa</span><span class="cb-value">%s</span></div>\n'
            '          </div>\n        </div>') % (n,n,esc(t),esc(pen),esc(tm),esc(fine))
def mg_plain(n,t,d):
    return ('        <div class="articulo" id="art-%s">\n'
            '          <span class="articulo-num">Artikulo %s — <span class="art-title">%s</span></span>\n'
            '          <p>%s</p>\n        </div>') % (n,n,esc(t),esc(d))

mg_titulos = [
 ("mg-t1","Titulo I — Mga Paglabag Laban sa Kaayusang Panlipunan",[
    mg_art("231","Magaan na Kaguluhan sa Publiko","Arresto Menor","60 min","$2,000"),
    mg_art("232","Paglabag sa Kapayapaan ng Komunidad","Arresto Mayor","120 min","$4,000")]),
 ("mg-t2","Titulo II — Mga Paglabag Laban sa Pampublikong Interes at Pamahalaang Bayan",[
    mg_art("233","Paglabag sa mga Ordinansa ng Bayan","Arresto Menor","60 min","$1,000"),
    mg_art("234","Pagtanggi sa Maliit na Utos ng Awtoridad","Arresto Mayor","120 min","$3,000")]),
 ("mg-t3","Titulo III — Mga Paglabag Laban sa Tao",[
    mg_art("235","Magaan na Pananakit (Slight Physical Injury)","Arresto Menor","60 min","$2,000"),
    mg_art("236","Pananakot (Light Threats)","Arresto Menor","60 min","$2,000")]),
 ("mg-t4","Titulo IV — Mga Paglabag Laban sa Ari-arian",[
    mg_art("237","Magaan na Pagnanakaw (Petty Theft)","Arresto Menor","60 min","$2,000"),
    mg_art("238","Magaan na Paninira ng Ari-arian","Arresto Mayor","120 min","$3,000")]),
 ("mg-t5","Titulo V — Mga Pangkalahatang Probisyon para sa mga Paglabag",[
    mg_plain("239","Paglalapat ng Parusa sa mga Paglabag","Ang mga paglabag ay pinaparusahan lamang kapag ganap na naisagawa, maliban kung may ibang itinatadhana ang batas."),
    mg_plain("240","Sabay-sabay na Paglabag","Kung may higit sa isang paglabag, ang parusa ay ipapataw ayon sa bawat pagkakasala, alinsunod sa batas."),
    mg_plain("241","Pagpapatawad ng Biktima","Sa mga paglabag, ang pagpapatawad ng biktima ay maaaring magpawala ng pananagutan kung pinahihintulutan ng batas.")]),
]
mg_body = ['      <section class="legal-part" id="magagaan">',
  '        <span class="part-label">Faltas</span>',
  '        <h2 class="part-title">Mga Magagaan na Paglabag</h2>',
  '        <div class="part-flourish"><span>✦</span></div>',
  '        <p class="legal-lead">Mga magagaan na paglabag (faltas) at ang kaukulang parusa (Artikulo 231–241).</p>']
for (tid,thead,arts) in mg_titulos:
    mg_body.append('        <div class="titulo" id="%s">' % tid)
    mg_body.append('          <h3 class="titulo-head"><span class="diamond">📖</span>%s</h3>' % esc(thead))
    mg_body.extend(arts)
    mg_body.append('        </div>')
mg_body.append('        <div class="court-note"><strong>Paalala:</strong> Maaaring bumaba ang multa depende sa pag-uusap ng mga hukom sa hatol.</div>')
mg_body.append('      </section>')
mg_toc = "        <ul>\n" + "".join('          <li><a href="#%s">%s</a></li>\n' % (tid, esc(thead)) for (tid,thead,_) in mg_titulos) + "        </ul>"
open(os.path.join(OUT,"magagaan.html"),"w",encoding="utf-8").write(
  page("magagaan.html","Mga Magagaan na Paglabag","Faltas","Mga Magagaan na Paglabag", mg_toc, "\n".join(mg_body)))
print("wrote magagaan.html")

print("CUSTOM CODE PAGES DONE")
