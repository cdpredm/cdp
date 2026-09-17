# -*- coding: utf-8 -*-
import os, re
import gen_legal as G
esc = G.esc; page = G.page; switcher = G.switcher; OUT = G.OUT; JS = G.JS; DOCS = G.DOCS; SUB = G.SUB

# ================= MGA KASABWAT (Art 242) =================
KAS_BODY = '''      <section class="legal-part" id="kasabwat">
        <span class="part-label">Pananagutan</span>
        <h2 class="part-title">Mga Kasabwat at Pakikisabwat</h2>
        <div class="part-flourish"><span>✦</span></div>

        <div class="articulo" id="art-242">
          <span class="articulo-num">Artikulo 242 — <span class="art-title">Mga Uri ng Kasabwat</span></span>
          <p>Para sa wastong pagtatalaga ng pananagutan, ang mga taong nakikibahagi sa isang krimen ay uuriin ayon sa kanilang layunin, gawa, lawak ng pakikilahok, at naging ambag sa pagkakagawa ng krimen.</p>
          <p>Ang mga sumusunod ang mga pangunahing uri ng kasabwat:</p>
        </div>

        <div class="titulo" id="ks-1">
          <h3 class="titulo-head"><span class="diamond">I.</span>Pangunahing Kasabwat</h3>
          <div class="articulo">
            <p>Ang sinumang may mahalagang papel sa pagpaplano, pag-uutos, pamamahala, o pagpapatupad ng krimen, bagaman maaaring hindi siya mismo ang gumawa ng huling kilos na bumuo sa krimen.</p>
            <p><strong>Pananagutan:</strong> Maaaring patawan ng kaparusahan na kapantay o isang antas na mababa kaysa sa pangunahing salarin, depende sa bigat ng kanyang naging papel.</p>
          </div>
        </div>

        <div class="titulo" id="ks-2">
          <h3 class="titulo-head"><span class="diamond">II.</span>Aktibong Kasabwat</h3>
          <div class="articulo">
            <p>Ang taong may tuwirang pakikilahok sa pagsasagawa ng krimen, ngunit hindi itinuturing na pangunahing gumawa nito. Kabilang dito ang taong:</p>
            <ul>
              <li>tumulong sa pag-atake;</li>
              <li>nagsilbing bantay;</li>
              <li>humarang sa mga maaaring pumigil sa krimen;</li>
              <li>tumulong sa pagkuha o pagdala ng bagay na ninakaw;</li>
              <li>o nagsagawa ng ibang mahalagang kilos upang maisakatuparan ang krimen.</li>
            </ul>
            <p><strong>Pananagutan:</strong> Isang antas na mas mababa kaysa sa pangunahing salarin, maliban kung ibang parusa ang tahasang itinakda ng batas.</p>
          </div>
        </div>

        <div class="titulo" id="ks-3">
          <h3 class="titulo-head"><span class="diamond">III.</span>Tagapag-udyok</h3>
          <div class="articulo">
            <p>Ang taong nanghikayat, nag-utos, nagbanta, nangako ng gantimpala, o gumamit ng ibang paraan upang hikayatin ang isang tao na gumawa ng krimen.</p>
            <p>Kung mapatutunayang ang kanyang panghihikayat ang pangunahing dahilan kung bakit isinagawa ang krimen, maaari siyang papanagutin nang halos kapantay ng mismong gumawa nito.</p>
            <p><strong>Pananagutan:</strong> Maaaring kapantay ng pangunahing salarin kung ang kanyang pag-uudyok ang tuwirang naging sanhi ng krimen; kung hindi, isang antas na mas mababa.</p>
          </div>
        </div>

        <div class="titulo" id="ks-4">
          <h3 class="titulo-head"><span class="diamond">IV.</span>Tagapaglaan</h3>
          <div class="articulo">
            <p>Ang taong sadyang nagbigay o naglaan ng anumang bagay na kinakailangan sa paggawa ng krimen, kabilang ang:</p>
            <ul>
              <li>sandata;</li><li>bala;</li><li>sasakyan;</li><li>kagamitan;</li><li>salapi;</li><li>tirahan o lugar;</li><li>impormasyon;</li><li>o iba pang paraan.</li>
            </ul>
            <p>Hindi magiging pananagutan ang simpleng pagbibigay ng isang bagay kung walang kaalaman na ito ay gagamitin sa krimen.</p>
            <p><strong>Pananagutan:</strong> Dalawang antas na mas mababa kaysa sa pangunahing salarin, maliban kung ang kanyang tulong ay mahalaga o kailangang-kailangan sa pagkakagawa ng krimen.</p>
          </div>
        </div>

        <div class="titulo" id="ks-5">
          <h3 class="titulo-head"><span class="diamond">V.</span>Tagapagbantay</h3>
          <div class="articulo">
            <p>Ang taong sadyang nagmamasid sa paligid, nagbababala sa mga kasabwat, o pumipigil sa mga awtoridad o ibang tao habang isinasagawa ang krimen.</p>
            <p><strong>Pananagutan:</strong> Isa hanggang dalawang antas na mas mababa kaysa sa pangunahing salarin, ayon sa bigat ng kanyang pakikilahok.</p>
          </div>
        </div>

        <div class="titulo" id="ks-6">
          <h3 class="titulo-head"><span class="diamond">VI.</span>Tagapagtago o Tagapagkubli</h3>
          <div class="articulo">
            <p>Ang taong, matapos maisagawa ang krimen, ay sadyang tumulong sa salarin upang:</p>
            <ul>
              <li>makatakas;</li><li>makapagtago;</li><li>maiwasan ang paghuli;</li><li>maitago ang sandata;</li><li>maitago o sirain ang ebidensiya; o</li><li>maitago ang mga bagay na bunga ng krimen.</li>
            </ul>
            <p>Kung napatunayang bago pa man maganap ang krimen ay kasali na siya sa pagpaplano, hindi siya ituturing na simpleng tagapagkubli lamang at maaari siyang managot bilang kasabwat.</p>
            <p><strong>Pananagutan:</strong> Dalawa hanggang tatlong antas na mas mababa kaysa sa pangunahing salarin.</p>
          </div>
        </div>

        <div class="titulo" id="art-242b">
          <h3 class="titulo-head"><span class="diamond">◆</span>Artikulo 242-B — Mga Antas ng Kaparusahan</h3>
          <div class="articulo"><p>Upang maging malinaw ang pagpapataw ng parusa, ang mga sumusunod na antas ay maaaring gamitin:</p></div>
          <div class="table-scroll">
            <table class="penalty-table">
              <thead><tr><th>Antas</th><th>Uri ng Pakikilahok</th><th>Kaparusahan</th></tr></thead>
              <tbody>
                <tr><td class="pen-name">I</td><td>Pangunahing Kasabwat</td><td class="pen-time">Kapantay o −1 antas</td></tr>
                <tr><td class="pen-name">II</td><td>Aktibong Kasabwat</td><td class="pen-time">−1 antas</td></tr>
                <tr><td class="pen-name">III</td><td>Tagapag-udyok</td><td class="pen-time">Kapantay hanggang −1 antas</td></tr>
                <tr><td class="pen-name">IV</td><td>Tagapaglaan</td><td class="pen-time">−2 antas</td></tr>
                <tr><td class="pen-name">V</td><td>Tagapagbantay</td><td class="pen-time">−1 hanggang −2 antas</td></tr>
                <tr><td class="pen-name">VI</td><td>Tagapagkubli</td><td class="pen-time">−2 hanggang −3 antas</td></tr>
              </tbody>
            </table>
          </div>
          <div class="articulo"><p>Ang pagbaba ng antas ng kaparusahan ay hindi nangangahulugang awtomatikong walang pananagutan ang kasabwat. Ang Hukuman ang magtatakda ng wastong parusa batay sa kabuuan ng mga ebidensiya.</p></div>
        </div>

        <div class="titulo" id="art-242c">
          <h3 class="titulo-head"><span class="diamond">◆</span>Artikulo 242-C — Pinagsamang Pananagutan</h3>
          <div class="articulo">
            <p>Kung dalawa o higit pang tao ang napatunayang may iisang layunin at kusang pagkakaisa upang maisagawa ang krimen, maaaring papanagutin ang bawat isa ayon sa kanyang sariling naging papel.</p>
            <p>Ang kawalan ng direktang pakikilahok sa mismong sandali ng krimen ay hindi sapat upang maalis ang pananagutan kung mapatutunayang may naunang kasunduan at makabuluhang ambag sa pagkakagawa nito.</p>
          </div>
        </div>

        <div class="titulo" id="art-242d">
          <h3 class="titulo-head"><span class="diamond">◆</span>Artikulo 242-D — Pagpapabigat ng Pananagutan</h3>
          <div class="articulo">
            <p>Maaaring itaas ng Hukuman ang kaparusahan sa loob ng itinakdang saklaw kung ang kasabwat ay:</p>
            <ul>
              <li>gumamit ng dahas o pananakot;</li>
              <li>gumamit ng sandata;</li>
              <li>nagsamantala sa katayuan o tungkulin sa Pamahalaan;</li>
              <li>nanguna sa pagbuo ng sabwatan;</li>
              <li>gumamit ng mga menor de edad upang maisagawa ang krimen;</li>
              <li>nagbanta sa mga saksi;</li>
              <li>nagtangkang sirain o itago ang ebidensiya; o</li>
              <li>paulit-ulit na nakilahok sa katulad na mga krimen.</li>
            </ul>
          </div>
        </div>

        <div class="titulo" id="art-242e">
          <h3 class="titulo-head"><span class="diamond">◆</span>Artikulo 242-E — Pagpapagaan ng Pananagutan</h3>
          <div class="articulo">
            <p>Maaaring ibaba ng Hukuman ang parusa kung ang kasabwat ay:</p>
            <ul>
              <li>kusang umatras bago maisagawa ang krimen;</li>
              <li>nagtangkang pigilan ang krimen;</li>
              <li>kusang nagsiwalat ng mahalagang impormasyon sa mga awtoridad;</li>
              <li>tumulong sa paghuli sa pangunahing salarin;</li>
              <li>kusang nagsauli ng mga bagay na bunga ng krimen; o</li>
              <li>nagbigay ng mahalagang tulong sa paglilitis.</li>
            </ul>
            <p>Ang mga nasabing kalagayan ay hindi awtomatikong nagpapawalang-bisa sa pananagutan, ngunit maaaring maging batayan sa pagpapagaan ng parusa.</p>
          </div>
        </div>

        <div class="titulo" id="art-242f">
          <h3 class="titulo-head"><span class="diamond">◆</span>Artikulo 242-F — Kailangang Patunay</h3>
          <div class="articulo">
            <p>Ang simpleng pagiging kaibigan, kamag-anak, kasamahan, miyembro ng isang pangkat, o pagkakaroon ng ugnayan sa pangunahing salarin ay hindi sapat upang ituring ang isang tao bilang kasabwat.</p>
            <p>Kinakailangan na mapatunayan ang alinman sa mga sumusunod:</p>
            <ul>
              <li>(a) may sinadyang pakikilahok;</li>
              <li>(b) may kaalaman sa krimeng isinasagawa;</li>
              <li>(c) may kusang pagbibigay ng tulong; o</li>
              <li>(d) may naunang kasunduan o pagkakaisa upang maisagawa ang krimen.</li>
            </ul>
            <p>Ang bawat akusado ay mananatiling walang sala hanggang sa mapatunayan ang kanyang pananagutan alinsunod sa mga tuntunin ng paglilitis ng Ciudad de Paseo.</p>
          </div>
        </div>
      </section>'''

KAS_TOC = '''        <ul>
          <li><a href="#art-242">Art. 242 — Mga Uri ng Kasabwat</a></li>
          <li><a href="#ks-1">I. Pangunahing Kasabwat</a></li>
          <li><a href="#ks-2">II. Aktibong Kasabwat</a></li>
          <li><a href="#ks-3">III. Tagapag-udyok</a></li>
          <li><a href="#ks-4">IV. Tagapaglaan</a></li>
          <li><a href="#ks-5">V. Tagapagbantay</a></li>
          <li><a href="#ks-6">VI. Tagapagkubli</a></li>
          <li><a href="#art-242b">Art. 242-B — Mga Antas</a></li>
          <li><a href="#art-242c">Art. 242-C — Pinagsama</a></li>
          <li><a href="#art-242d">Art. 242-D — Pagpapabigat</a></li>
          <li><a href="#art-242e">Art. 242-E — Pagpapagaan</a></li>
          <li><a href="#art-242f">Art. 242-F — Patunay</a></li>
        </ul>'''
open(os.path.join(OUT,"kasabwat.html"),"w",encoding="utf-8").write(
  page("kasabwat.html","Mga Kasabwat","Pananagutan","Mga Kasabwat at Pakikisabwat", KAS_TOC, KAS_BODY))
print("wrote kasabwat.html")

# ================= LEGAL BOOK HUB =================
def card(href,title,desc):
    return '            <a class="card" href="%s"><h3>%s</h3><p>%s</p></a>' % (href, esc(title), esc(desc))

GROUPS = [
 ("Saligang Batas", [
   ("saligang-batas.html","Saligang Batas","Ang pinakamataas na batas — soberanya, karapatan, sangay ng pamahalaan."),
 ]),
 ("Código Penal", [
   ("legal.html","Código Penal (Pangkalahatan)","Preambulo, mga parusa, Aklat I–II — pangkalahatang probisyon."),
   ("krimen-estado.html","Krimen Laban sa Estado","Art. 121–130 — panlabas na seguridad."),
   ("krimen-saligang.html","Krimen Laban sa Saligang Batas","Art. 131–140."),
   ("krimen-kaayusan.html","Krimen Laban sa Kaayusan","Art. 141–146."),
   ("pamemeke.html","Kasinungalingan at Pamemeke","Art. 147–155."),
   ("kalusugan.html","Kalusugang Pampubliko","Art. 156–162 — paglilibing at kalusugan."),
   ("pagsusugal.html","Pagsusugal","Art. 163–168."),
   ("kawani.html","Mga Kawani ng Pamahalaan","Art. 169–176."),
   ("krimen-tao.html","Krimen Laban sa Tao","Art. 177–186."),
   ("krimen-puri.html","Kalinisan ng Puri","Art. 187–196."),
   ("krimen-dangal.html","Krimen Laban sa Dangal","Art. 197–202."),
   ("krimen-sibil-katayuan.html","Sibil na Katayuan","Art. 203–208."),
   ("krimen-kalayaan.html","Kalayaan at Seguridad","Art. 209–216."),
   ("krimen-ari-arian.html","Krimen Laban sa Ari-arian","Art. 217–224."),
   ("kapabayaan.html","Kapabayaan","Art. 225–230."),
   ("magagaan.html","Magagaan na Paglabag","Art. 231–241 — faltas."),
   ("kasabwat.html","Mga Kasabwat","Art. 242 — pakikisabwat at pananagutan."),
 ]),
 ("Código Sibil", [
   ("codigo-sibil.html","Código Sibil","Aklat I–V — kontrata, ari-arian, danyos, pamana."),
 ]),
 ("Código Administratibo", [
   ("codigo-administratibo.html","Código Administratibo","Aklat I–IX — tungkulin at pananagutan ng mga opisyal."),
 ]),
]
hub_sections = []
for gname, cards in GROUPS:
    hub_sections.append('        <h3 class="hub-group">%s</h3>' % esc(gname))
    hub_sections.append('        <div class="cards-grid">')
    hub_sections.extend(card(h,t,d) for (h,t,d) in cards)
    hub_sections.append('        </div>')
hub_cards = "\n".join(hub_sections)

hub = '''<!DOCTYPE html>
<html lang="tl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Legal Book — Ciudad de Paseo</title>
  <meta name="description" content="Legal Book ng Ciudad de Paseo — ang kalipunan ng mga batas: Saligang Batas, Código Penal, Código Sibil, at Código Administratibo." />
  <link rel="icon" type="image/png" href="PASEO.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Rye&family=Cinzel:wght@400;600;700;900&family=Special+Elite&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="legal.css" />
  <style>
    .hub-group { font-family: var(--font-head); color: var(--gold-bright); font-size: 1.3rem; letter-spacing: 0.03em; margin: 40px 0 6px; padding-bottom: 8px; border-bottom: 1px solid var(--border); }
    .hub-wrap .cards-grid { margin-top: 18px; }
    .hub-wrap .card { text-align: left; text-decoration: none; display: block; }
    .hub-wrap .card h3 { margin-bottom: 8px; }
  </style>
</head>
<body>
  <div class="paper-overlay" aria-hidden="true"></div>
  <header class="legal-topbar">
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <img src="PASEO.png" alt="Ciudad de Paseo" class="brand-logo" />
        <span class="brand-text">
          <span class="brand-title">Ciudad de Paseo</span>
          <span class="brand-sub">Legal Book · Aklat ng Batas</span>
        </span>
      </a>
      <a href="index.html" class="back-link">← Balik sa Website</a>
    </div>
  </header>
%s
  <div class="legal-cover">
    <img src="PASEO.png" alt="Ciudad de Paseo" />
    <p class="legal-kicker">Aklat ng Batas</p>
    <h1 class="legal-title">Legal Book</h1>
    <p class="legal-sub">%s</p>
  </div>
  <div class="hub-wrap">
    <div class="container" style="padding:44px 0 90px;">
      <p class="prose center" style="max-width:760px;margin:0 auto 10px;color:var(--ink-dim);font-size:1.1rem;">
        Ang opisyal na kalipunan ng mga batas ng Ciudad de Paseo. Piliin ang aklat na nais mong basahin.
      </p>
%s
    </div>
  </div>
  <footer class="legal-foot">Legal Book · Ciudad de Paseo · Est. 2024 — Mabuhay ang Batas ng Bayan</footer>
</body>
</html>
''' % (switcher("legal-index.html"), esc(SUB), hub_cards)
open(os.path.join(OUT,"legal-index.html"),"w",encoding="utf-8").write(hub)
print("wrote legal-index.html")

# ================= UPDATE existing pages' switcher + backlink =================
for f in ["legal.html","saligang-batas.html"]:
    p = os.path.join(OUT,f)
    s = open(p,encoding="utf-8").read()
    s = re.sub(r'  <nav class="legal-switch">.*?</nav>', switcher(f), s, count=1, flags=re.S)
    s = s.replace('<a href="index.html" class="back-link">← Balik sa Website</a>',
                  '<a href="legal-index.html" class="back-link">📚 Legal Book</a>')
    open(p,"w",encoding="utf-8").write(s)
    print("updated switcher in", f)

print("ALL DONE")
