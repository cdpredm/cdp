# -*- coding: utf-8 -*-
import html, re, os

OUT = r"C:/xampp/htdocs/htdocs/cdpwebsite"
def esc(s): return html.escape(s, quote=False)

# ---- Document registry (order = switcher order) ----
DOCS = [
    ("legal-index.html", "📚 Index"),
    ("saligang-batas.html", "Saligang Batas"),
    ("legal.html", "Código Penal"),
    ("krimen-estado.html", "Krimen: Estado"),
    ("krimen-saligang.html", "Krimen: Saligang Batas"),
    ("krimen-kaayusan.html", "Krimen: Kaayusan"),
    ("pamemeke.html", "Pamemeke"),
    ("kalusugan.html", "Kalusugang Pampubliko"),
    ("pagsusugal.html", "Pagsusugal"),
    ("kawani.html", "Mga Kawani"),
    ("krimen-tao.html", "Krimen: Tao"),
    ("krimen-puri.html", "Kalinisan ng Puri"),
    ("krimen-dangal.html", "Dangal"),
    ("krimen-sibil-katayuan.html", "Sibil na Katayuan"),
    ("krimen-kalayaan.html", "Kalayaan at Seguridad"),
    ("krimen-ari-arian.html", "Ari-arian"),
    ("kapabayaan.html", "Kapabayaan"),
    ("magagaan.html", "Magagaan na Paglabag"),
    ("kasabwat.html", "Mga Kasabwat"),
    ("codigo-sibil.html", "Código Sibil"),
    ("codigo-administratibo.html", "Código Administratibo"),
]

JS = """
    (function () {
      var toggle = document.getElementById('tocToggle');
      var body = document.getElementById('tocBody');
      if (toggle && body) toggle.addEventListener('click', function () { body.classList.toggle('open'); });
      var tocLinks = document.querySelectorAll('.legal-toc a');
      tocLinks.forEach(function (a) {
        a.addEventListener('click', function () { if (window.innerWidth <= 900 && body) body.classList.remove('open'); });
      });
      var targets = [];
      tocLinks.forEach(function (a) {
        var id = a.getAttribute('href').slice(1);
        var el = id && document.getElementById(id);
        if (el) targets.push({ link: a, el: el });
      });
      function onScroll() {
        var pos = window.scrollY + 150, current = null;
        targets.forEach(function (t) {
          var top = t.el.getBoundingClientRect().top + window.scrollY;
          if (top <= pos) current = t;
        });
        tocLinks.forEach(function (a) { a.classList.remove('active'); });
        if (current) current.link.classList.add('active');
      }
      window.addEventListener('scroll', onScroll, { passive: true });
      onScroll();
    })();
"""

def switcher(active):
    pills = []
    for f, label in DOCS:
        cls = "doc-pill active" if f == active else "doc-pill"
        pills.append('      <a href="%s" class="%s">%s</a>' % (f, cls, label))
    return '  <nav class="legal-switch">\n    <div class="nav-inner">\n' + "\n".join(pills) + '\n    </div>\n  </nav>'

SUB = "Ciudad de Paseo · Bayan ng Alamat at Kasaysayan"

def page(file, page_title, kicker, doc_title, toc_html, body_html, back="legal-index.html", backlabel="📚 Legal Book", subtitle=SUB):
    return """<!DOCTYPE html>
<html lang="tl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>%s — Ciudad de Paseo | Legal Book</title>
  <link rel="icon" type="image/png" href="PASEO.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Rye&family=Cinzel:wght@400;600;700;900&family=Special+Elite&family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="stylesheet" href="legal.css" />
</head>
<body>
  <div class="paper-overlay" aria-hidden="true"></div>
  <header class="legal-topbar">
    <div class="nav-inner">
      <a href="index.html" class="brand">
        <img src="PASEO.png" alt="Ciudad de Paseo" class="brand-logo" />
        <span class="brand-text">
          <span class="brand-title">Ciudad de Paseo</span>
          <span class="brand-sub">Legal Book · %s</span>
        </span>
      </a>
      <a href="%s" class="back-link">%s</a>
    </div>
  </header>
%s
  <div class="legal-cover">
    <img src="PASEO.png" alt="Ciudad de Paseo" />
    <p class="legal-kicker">%s</p>
    <h1 class="legal-title">%s</h1>
    <p class="legal-sub">%s</p>
  </div>
  <div class="legal-layout">
    <aside class="legal-toc">
      <button class="toc-toggle" id="tocToggle">☰ Talaan ng Nilalaman</button>
      <div class="toc-body" id="tocBody">
        <h4>Talaan ng Nilalaman</h4>
%s
      </div>
    </aside>
    <main class="legal-book">
%s
      <p class="legal-foot">%s · Ciudad de Paseo · Est. 2024</p>
    </main>
  </div>
  <script>%s</script>
</body>
</html>
""" % (esc(page_title), esc(doc_title), back, backlabel, switcher(file), esc(kicker),
       esc(doc_title), esc(subtitle), toc_html, body_html, esc(doc_title), JS)

# ---------- Uniform crime-list pages ----------
def crime_toc(arts):
    lis = "".join('          <li><a href="#art-%s">Art. %s — %s</a></li>\n' % (n, n, esc(t)) for (n, t, d, p, tm, f) in arts)
    return "        <ul>\n" + lis + "        </ul>"

def crime_body(kicker, title, intro, arts, note):
    out = ['      <section class="legal-part" id="krimen">',
           '        <span class="part-label">%s</span>' % esc(kicker),
           '        <h2 class="part-title">%s</h2>' % esc(title),
           '        <div class="part-flourish"><span>✦</span></div>',
           '        <p class="legal-lead">%s</p>' % esc(intro)]
    for (n, t, d, pen, tm, fine) in arts:
        out.append('        <div class="articulo" id="art-%s">' % n)
        out.append('          <span class="articulo-num">Artikulo %s — <span class="art-title">%s</span></span>' % (n, esc(t)))
        if d:
            out.append('          <p>%s</p>' % esc(d))
        out.append('          <div class="crime-meta">')
        out.append('            <div class="crime-badge pen"><span class="cb-label">⚖️ Parusa</span><span class="cb-value">%s</span></div>' % esc(pen))
        out.append('            <div class="crime-badge"><span class="cb-label">⏱️ Tagal</span><span class="cb-value">%s</span></div>' % esc(tm))
        out.append('            <div class="crime-badge fine"><span class="cb-label">💰 Multa</span><span class="cb-value">%s</span></div>' % esc(fine))
        out.append('          </div>')
        out.append('        </div>')
    if note:
        out.append('        <div class="court-note"><strong>Paalala:</strong> Maaaring bumaba ang multa depende sa pag-uusap ng mga hukom sa hatol.</div>')
    out.append('      </section>')
    return "\n".join(out)

CRIME_PAGES = [
 dict(file="krimen-estado.html", pill="Krimen: Estado", title="Mga Krimen Laban sa Estado",
      kicker="Panlabas na Seguridad",
      intro="Mga paglabag laban sa panlabas na seguridad at soberanya ng Ciudad de Paseo (Artikulo 121–130).",
      note=False, arts=[
   ("121","Pagtataksil (Treason)","","Reclusión Perpetua – Kamatayan","1,440 min","$4,000"),
   ("122","Pagpapasimula ng Digmaan laban sa Estado","","Reclusión Temporal – Perpetua","720 – 1,440 min","$4,000"),
   ("123","Pakikipagsabwatan sa Kaaway","","Prisión Mayor – Reclusión Temporal","480 – 720 min","$2,500"),
   ("124","Paniniktik (Espionage)","","Prisión Mayor – Reclusión Temporal","480 – 720 min","$2,500"),
   ("125","Pagbibigay Tulong sa Kaaway","","Prisión Correccional – Prisión Mayor","240 – 480 min","$2,500"),
   ("126","Pagpapahintulot sa Pagpasok ng Kaaway","","Reclusión Temporal","720 min","$2,500"),
   ("127","Paglabag sa Neutralidad","","Prisión Correccional","240 min","$2,000"),
   ("128","Pag-uudyok laban sa Estado sa Panahon ng Digmaan","","Prisión Mayor","480 min","$2,500"),
   ("129","Paglalantad ng mga Lihim ng Estado","","Prisión Correccional – Prisión Mayor","240 – 480 min","$5,000"),
   ("130","Iba pang mga Gawa laban sa Panlabas na Seguridad","","Arresto Mayor – Prisión Correccional","120 – 240 min","$2,500"),
 ]),
 dict(file="krimen-saligang.html", pill="Krimen: Saligang Batas", title="Mga Krimen Laban sa Saligang Batas",
      kicker="Batayang Batas",
      intro="Mga paglabag laban sa batayang batas, karapatan, at proseso ng Estado (Artikulo 131–140).",
      note=False, arts=[
   ("131","Paglabag sa mga Saligang Batas","Ang sinumang sadyang lumabag o sumira sa mga batayang batas ng Estado.","Reclusión Temporal","720 min","$4,000"),
   ("132","Pag-agaw ng Kapangyarihan ng Pamahalaan","Ang sinumang umangkin o gumamit ng kapangyarihang hindi ipinagkaloob sa kanya ng batas.","Reclusión Temporal – Perpetua","720 – 1,440 min","$4,000"),
   ("133","Ilegal na Pagpigil sa mga Karapatan ng Mamamayan","Ang sinumang magpigil o mag-alis ng mga karapatang itinatadhana ng batas.","Prisión Mayor","480 min","$2,000"),
   ("134","Pang-aabuso ng Kapangyarihan","Ang sinumang opisyal na lumampas sa kanyang kapangyarihan na nagdudulot ng pinsala sa mamamayan.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$4,000"),
   ("135","Paglabag sa Konstitusyonal na Proseso","Ang sinumang lalabag sa mga legal na proseso na itinakda ng batas o konstitusyon.","Prisión Correccional – Prisión Mayor","240 – 480 min","$2,500"),
   ("136","Ilegal na Pagpigil sa Malayang Pagpapahayag","Ang sinumang pipigil sa malayang pagpapahayag nang labag sa batas.","Prisión Correccional","240 min","$1,000"),
   ("137","Paglabag sa Karapatan sa Pagtitipon","Ang sinumang hahadlang sa lehitimong pagtitipon ng mga mamamayan.","Arresto Mayor – Prisión Correccional","120 – 240 min","$1,000"),
   ("138","Ilegal na Pag-aresto o Pagkakakulong","Ang sinumang manghuli o magkulong nang walang sapat na batayan sa batas.","Prisión Mayor","480 min","$2,000"),
   ("139","Paglabag sa Karapatan sa Ari-arian","Ang sinumang kukuha o sisira ng ari-arian nang walang legal na batayan.","Prisión Correccional","240 min","$1,000"),
   ("140","Iba pang Paglabag sa mga Saligang Batas","Anumang gawaing lumalabag sa batayang batas ng Estado na hindi saklaw ng mga naunang artikulo.","Arresto Menor – Arresto Mayor","60 – 120 min","$4,000"),
 ]),
 dict(file="krimen-kaayusan.html", pill="Krimen: Kaayusan", title="Mga Krimen Laban sa Kaayusan",
      kicker="Kaayusang Panlipunan",
      intro="Mga paglabag laban sa kaayusan at kapayapaan ng lipunan (Artikulo 141–146).",
      note=True, arts=[
   ("141","Rebelyon (Rebellion)","Ang sinumang mag-aalsa laban sa pamahalaan upang pabagsakin ang umiiral na kaayusan.","Reclusión Temporal","720 min","$4,000"),
   ("142","Sedisyon (Sedition)","Ang pag-aalsa o kaguluhan laban sa mga awtoridad nang hindi tuwirang layuning pabagsakin ang pamahalaan.","Prisión Mayor","480 min","$3,000"),
   ("143","Paglabag sa Kapayapaan (Public Disorder)","Ang sinumang magdulot ng kaguluhan o takot sa publiko sa pamamagitan ng karahasan o pananakot.","Prisión Correccional","240 min","$2,000"),
   ("144","Ilegal na Pagtitipon (Unlawful Assembly)","Ang pagtitipon ng mga tao na may layuning gumawa ng krimen o maghasik ng kaguluhan.","Arresto Mayor – Prisión Correccional","120 – 240 min","$1,000"),
   ("145","Ilegal na Samahan (Unlawful Association)","Ang pagtatatag o pagsali sa samahang may layuning labagin ang batas o kaayusan.","Prisión Correccional","240 min","$1,000"),
   ("146","Pagtanggi sa Awtoridad (Resistance and Disobedience)","Ang sinumang tatanggi o lalaban sa lehitimong utos ng awtoridad.","Arresto Mayor","120 min","$1,000"),
 ]),
 dict(file="pamemeke.html", pill="Pamemeke", title="Mga Kasinungalingan at Pamemeke",
      kicker="Panlilinlang",
      intro="Mga krimen ng pamemeke ng dokumento, salapi, at pahayag (Artikulo 147–155).",
      note=True, arts=[
   ("147","Pamemeke ng mga Opisyal na Dokumento","Ang sinumang gagawa o magpapalsipika ng opisyal na dokumento ng pamahalaan.","Prisión Mayor","480 min","$2,000"),
   ("148","Pamemeke ng mga Pampublikong Tala","Ang pagbabago o pamemeke ng mga talaan ng pamahalaan.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$4,000"),
   ("149","Pamemeke ng mga Pribadong Dokumento","Ang sinumang magpapalsipika ng pribadong kasulatan upang makapanlinlang.","Prisión Correccional","240 min","$3,000"),
   ("150","Paggamit ng Pekeng Dokumento","Ang sinumang gagamit ng dokumentong alam niyang peke.","Prisión Correccional – Prisión Mayor","240 – 480 min","$1,500"),
   ("151","Pamemeke ng Pera o Salapi","Ang paggawa o pagpapakalat ng pekeng pera o salapi.","Reclusión Temporal","720 min","$4,000"),
   ("152","Pamemeke ng Selyo o Tatak ng Pamahalaan","Ang sinumang gagawa o gagamit ng pekeng selyo o tatak ng Estado.","Prisión Mayor","480 min","$3,000"),
   ("153","Pagsisinungaling sa Opisyal na Pahayag","Ang pagbibigay ng maling impormasyon sa isang opisyal na dokumento o pahayag.","Prisión Correccional","240 min","$1,000"),
   ("154","Pagbabago ng Tunay na Dokumento","Ang sinumang magbabago ng nilalaman ng tunay na dokumento upang manlinlang.","Prisión Mayor","480 min","$2,500"),
   ("155","Iba pang Uri ng Pamemeke","Anumang uri ng pamemeke na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$1,000"),
 ]),
 dict(file="kalusugan.html", pill="Kalusugang Pampubliko", title="Paglilibing at Kalusugang Pampubliko",
      kicker="Kalusugang Pampubliko",
      intro="Paglabag sa mga batas hinggil sa paglilibing, paglalapastangan sa mga libingan, at mga krimen laban sa kalusugang pampubliko (Artikulo 156–162).",
      note=True, arts=[
   ("156","Paglabag sa mga Batas ng Paglilibing","Ang sinumang lalabag sa mga itinakdang batas o regulasyon ukol sa wastong paglilibing ng mga bangkay.","Arresto Mayor","120 min","$4,000"),
   ("157","Paglapastangan sa Libingan (Violation of Sepulchers)","Ang sinumang sisira, dudungisan, o lalapastangan sa libingan o puntod.","Prisión Correccional","240 min","$5,000"),
   ("158","Paglabag sa Katawan ng Yumao","Ang sinumang gagawa ng labag sa batas na aksyon sa bangkay, kabilang ang paglipat o pagkuha nito nang walang pahintulot.","Prisión Correccional","240 min","$5,000"),
   ("159","Pagkalat ng Nakahahawang Sakit","Ang sinumang sadyang magpapakalat ng sakit na mapanganib sa kalusugan ng publiko.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$4,000"),
   ("160","Paglabag sa mga Batas Pangkalusugan","Ang sinumang lalabag sa mga regulasyon na itinakda upang protektahan ang kalusugan ng publiko.","Prisión Correccional","240 min","$5,000"),
   ("161","Paggawa o Pagbebenta ng Mapanganib na Produkto","Ang sinumang gagawa, magbebenta, o magpapakalat ng produktong nakasasama sa kalusugan ng publiko.","Prisión Mayor","480 min","$2,000"),
   ("162","Iba pang Paglabag laban sa Kalusugang Pampubliko","Anumang gawaing naglalagay sa panganib sa kalusugan ng publiko na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$4,000"),
 ]),
 dict(file="pagsusugal.html", pill="Pagsusugal", title="Pagsusugal at mga Uri Nito",
      kicker="Sugal",
      intro="Mga krimen na may kaugnayan sa ilegal na pagsusugal (Artikulo 163–168).",
      note=True, arts=[
   ("163","Ilegal na Pagsusugal","Ang sinumang lalahok sa pagsusugal na hindi pinahihintulutan ng batas.","Arresto Menor","60 min","$2,000"),
   ("164","Pamamahala ng Ilegal na Pagsusugal","Ang sinumang mag-oorganisa, magpapatakbo, o mamamahala ng ilegal na pagsusugal.","Prisión Correccional","240 min","$5,000"),
   ("165","Pagmamay-ari ng Lugar para sa Pagsusugal","Ang sinumang magbibigay o magpapahintulot ng lugar para sa ilegal na pagsusugal.","Prisión Correccional","240 min","$5,000"),
   ("166","Ilegal na Raffle","Ang pagsasagawa ng raffle o katulad na laro ng swerte nang walang pahintulot.","Arresto Mayor","120 min","$4,000"),
   ("167","Pandaraya sa Pagsusugal o Raffle","Ang sinumang gagamit ng pandaraya upang manalo o manipulahin ang resulta ng laro.","Prisión Correccional – Prisión Mayor","240 – 480 min","$1,000"),
   ("168","Pagtatago o Pagprotekta sa Ilegal na Pagsusugal","Ang sinumang magtatago, magbibigay proteksyon, o tutulong upang makaiwas sa batas ang ilegal na pagsusugal.","Arresto Mayor – Prisión Correccional","120 – 240 min","$5,000"),
 ]),
 dict(file="kawani.html", pill="Mga Kawani", title="Mga Pagkakasala ng mga Kawani ng Pamahalaan",
      kicker="Tungkulin ng Pamahalaan",
      intro="Mga pagkakasalang ginagawa ng mga kawani ng pamahalaan sa pagganap ng kanilang tungkulin (Artikulo 169–176).",
      note=True, arts=[
   ("169","Pang-aabuso sa Kapangyarihan (Abuse of Authority)","Ang sinumang kawani ng pamahalaan na lalampas sa kanyang kapangyarihan at magdudulot ng pinsala.","Prisión Mayor","480 min","$4,000"),
   ("170","Ilegal na Pag-aresto o Detensyon","Ang sinumang kawani na manghuhuli o magdedetine nang walang sapat na batayan sa batas.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$5,000"),
   ("171","Paglabag sa Karapatan ng mga Bilanggo","Ang sinumang opisyal na lalabag sa karapatan ng mga nakakulong.","Prisión Correccional","240 min","$5,000"),
   ("172","Korapsyon (Bribery)","Ang pagtanggap ng suhol kapalit ng pabor o aksyon sa tungkulin.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$5,000"),
   ("173","Pagtanggi sa Tungkulin (Dereliction of Duty)","Ang sinumang kawani na sadyang hindi gampanan ang kanyang tungkulin.","Prisión Correccional","240 min","$5,000"),
   ("174","Pagbubunyag ng Lihim ng Tungkulin","Ang sinumang kawani na maglalantad ng kumpidensyal na impormasyon.","Prisión Correccional – Prisión Mayor","240 – 480 min","$3,000"),
   ("175","Malversation o Paglustay ng Pondo ng Pamahalaan","Ang paggamit o paglustay ng pondo ng pamahalaan para sa pansariling kapakinabangan.","Reclusión Temporal","720 min","$5,000"),
   ("176","Iba pang Paglabag ng mga Kawani ng Pamahalaan","Anumang paglabag na hindi saklaw ng mga naunang artikulo ngunit may kaugnayan sa tungkulin.","Arresto Mayor – Prisión Correccional","120 – 240 min","$5,000"),
 ]),
 dict(file="krimen-tao.html", pill="Krimen: Tao", title="Mga Krimen Laban sa Tao",
      kicker="Buhay at Katawan",
      intro="Mga krimen laban sa buhay at katawan ng tao (Artikulo 177–186).",
      note=True, arts=[
   ("177","Pagpatay (Homicide)","Ang sinumang pumatay ng kapwa tao nang walang mga kwalipikadong kalagayan.","Reclusión Temporal","720 min","$5,000"),
   ("178","Pagpaslang (Murder)","Pagpatay na may kasamang panlilinlang, kalupitan, o planadong paraan.","Reclusión Perpetua – Kamatayan","1,440 min","$5,000"),
   ("179","Parricide (Pagpatay sa Kamag-anak)","Pagpatay sa magulang, anak, asawa, o malapit na kamag-anak.","Parusang Kamatayan","Agarang ipatutupad","$5,000"),
   ("180","Physical Injuries (Malubhang Pananakit)","Pagdudulot ng malubhang pinsala sa katawan ng ibang tao.","Prisión Mayor","480 min","$3,000"),
   ("181","Less Serious Physical Injuries","Pagdudulot ng hindi gaanong malubhang pinsala.","Prisión Correccional","240 min","$1,000"),
   ("182","Slight Physical Injuries","Magaan na pananakit o pinsala.","Arresto Mayor","120 min","$1,000"),
   ("183","Pagtangkang Pagpatay (Attempted Homicide/Murder)","Pagkilos na naglalayong pumatay ngunit hindi natupad.","Prisión Mayor","480 min","$2,000"),
   ("184","Pagpapabaya na Nagdulot ng Kamatayan (Negligence)","Pagkamatay ng isang tao dahil sa kapabayaan o kakulangan sa pag-iingat.","Prisión Correccional","240 min","$1,000"),
   ("185","Pagpapakamatay at Pagtulong Dito","Ang sinumang tutulong o mag-uudyok sa pagpapakamatay ng iba.","Prisión Mayor","480 min","$2,000"),
   ("186","Iba pang Krimen laban sa Tao","Anumang krimen laban sa buhay at katawan na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$4,000"),
 ]),
 dict(file="krimen-puri.html", pill="Kalinisan ng Puri", title="Mga Krimen Laban sa Kalinisan ng Puri",
      kicker="Moralidad at Puri",
      intro="Mga krimen laban sa kalinisan ng puri at moralidad (Artikulo 187–196).",
      note=True, arts=[
   ("187","Panggagahasa (Rape)","Ang sinumang makikipagtalik sa iba sa pamamagitan ng dahas, pananakot, o panlilinlang.","Reclusión Temporal – Perpetua","720 – 1,440 min","$4,000"),
   ("188","Acts of Lasciviousness (Malalaswang Gawa)","Ang paggawa ng malaswang kilos laban sa isang tao nang walang pahintulot.","Prisión Mayor","480 min","$4,000"),
   ("189","Seduction (Panlilinlang sa Kababaihan)","Ang panlilinlang upang makamit ang pakikipagtalik sa isang babae.","Prisión Correccional","240 min","$1,000"),
   ("190","Abduction (Pagdukot na may Layuning Sekswal)","Ang pagdukot sa isang tao upang pagsamantalahan o abusuhin.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$5,000"),
   ("191","Consented Abduction","Pagdukot na may pahintulot ngunit may layuning malaswa o labag sa moralidad.","Prisión Correccional","240 min","$5,000"),
   ("192","Adultery (Pakikiapid ng Babae)","Ang pakikipagtalik ng may asawa sa ibang lalaki.","Prisión Correccional","240 min","$5,000"),
   ("193","Concubinage (Pakikiapid ng Lalaki)","Ang pakikipagtalik ng lalaking may asawa sa ibang babae sa paraang labag sa batas.","Prisión Correccional","240 min","$5,000"),
   ("194","Corruption of Minors","Ang sinumang magpapasok o maghihikayat ng menor de edad sa malaswang gawain.","Reclusión Temporal","720 min","$5,000"),
   ("195","White Slave Trade / Prostitution Exploitation","Ang pagsasamantala sa prostitusyon o pagrekrut para sa malaswang gawain.","Reclusión Temporal","720 min","$5,000"),
   ("196","Iba pang Krimen laban sa Kalinisan ng Puri","Anumang krimen na lumalabag sa moralidad at puri na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$5,000"),
 ]),
 dict(file="krimen-dangal.html", pill="Dangal", title="Mga Krimen Laban sa Dangal",
      kicker="Dangal at Reputasyon",
      intro="Mga krimen laban sa dangal at reputasyon ng tao (Artikulo 197–202).",
      note=True, arts=[
   ("197","Paninirang-Puri (Libel)","Ang sinumang maglalathala o magpapahayag ng maling paratang na sumisira sa dangal ng iba.","Prisión Correccional","240 min","$5,000"),
   ("198","Paninirang-Puri sa Pamamagitan ng Salita (Slander)","Ang pagsasabi ng mapanirang pahayag laban sa isang tao.","Arresto Mayor","120 min","$5,000"),
   ("199","Mabigat na Paninirang-Puri (Grave Slander)","Ang malubhang anyo ng paninirang-puri na nagdudulot ng malaking pinsala sa reputasyon.","Prisión Correccional","240 min","$1,000"),
   ("200","Panlalait (Oral Defamation)","Ang tahasang pang-iinsulto o paglapastangan sa dangal ng iba.","Arresto Menor – Arresto Mayor","60 – 120 min","$4,000"),
   ("201","Paglalantad ng Pribadong Buhay (Public Disclosure of Private Facts)","Ang paglalantad ng pribadong impormasyon na nakasisira sa reputasyon ng isang tao.","Prisión Correccional","240 min","$5,000"),
   ("202","Iba pang Paglabag laban sa Dangal","Anumang gawaing sumisira sa dangal o reputasyon na hindi saklaw ng mga naunang artikulo.","Arresto Menor – Prisión Correccional","60 – 240 min","$5,000"),
 ]),
 dict(file="krimen-sibil-katayuan.html", pill="Sibil na Katayuan", title="Mga Krimen Laban sa Sibil na Katayuan ng Tao",
      kicker="Sibil na Katayuan",
      intro="Mga krimen laban sa sibil na katayuan ng tao (Artikulo 203–208).",
      note=True, arts=[
   ("203","Pagsisinungaling sa Sibil na Katayuan","Ang sinumang magpapahayag o gagamit ng maling impormasyon tungkol sa kanyang sibil na kalagayan.","Prisión Correccional","240 min","$1,000"),
   ("204","Ilegal na Pagpapalit ng Bata (Substitution of Children)","Ang pagpapalit o pagtatago ng tunay na pagkakakilanlan ng isang bata.","Reclusión Temporal","720 min","$2,000"),
   ("205","Pagpapanggap sa Ibang Tao (Usurpation of Civil Status)","Ang sinumang gagamit ng identidad ng ibang tao upang manlinlang.","Prisión Mayor","480 min","$4,000"),
   ("206","Ilegal na Pagpaparehistro","Ang pagpaparehistro ng maling impormasyon sa mga opisyal na tala ng kapanganakan, kasal, o kamatayan.","Prisión Correccional – Prisión Mayor","240 – 480 min","$1,000"),
   ("207","Paglabag sa mga Batas ng Kasal","Ang sinumang lalabag sa mga legal na kondisyon ng kasal (hal. bigamy o illegal marriage).","Prisión Mayor","480 min","$3,000"),
   ("208","Iba pang Paglabag sa Sibil na Kalagayan","Anumang gawaing lumalabag sa sibil na katayuan ng isang tao na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$5,000"),
 ]),
 dict(file="krimen-kalayaan.html", pill="Kalayaan at Seguridad", title="Mga Krimen Laban sa Kalayaan at Seguridad",
      kicker="Kalayaan at Seguridad",
      intro="Mga krimen laban sa kalayaan at seguridad ng tao (Artikulo 209–216).",
      note=True, arts=[
   ("209","Ilegal na Pagkakakulong (Illegal Detention)","Ang sinumang manghuli o magkulong ng tao nang walang legal na batayan.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$4,000"),
   ("210","Kidnapping o Pagdukot","Ang pagkuha o pagdetine ng tao laban sa kanyang kalooban.","Reclusión Temporal – Perpetua","720 – 1,440 min","$4,000"),
   ("211","Grave Threats (Matinding Pananakot)","Ang pagbabanta na magdudulot ng malubhang pinsala sa tao o ari-arian.","Prisión Mayor","480 min","$3,000"),
   ("212","Light Threats (Magaan na Pananakot)","Ang pagbabanta na hindi kasingbigat ng grave threats.","Arresto Mayor","120 min","$5,000"),
   ("213","Coercion (Pamimilit)","Ang sapilitang pagpapagawa o pagpigil sa isang tao laban sa kanyang kalooban.","Prisión Correccional","240 min","$5,000"),
   ("214","Unlawful Arrest","Ang sinumang magsasagawa ng pag-aresto nang walang legal na awtoridad.","Prisión Mayor","480 min","$2,000"),
   ("215","Violation of Domicile","Ang pagpasok sa tahanan ng iba nang walang pahintulot o legal na basehan.","Prisión Correccional","240 min","$2,000"),
   ("216","Iba pang Paglabag laban sa Kalayaan at Seguridad","Anumang gawaing lumalabag sa kalayaan at seguridad ng tao na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$2,000"),
 ]),
 dict(file="krimen-ari-arian.html", pill="Ari-arian", title="Mga Krimen Laban sa Ari-arian",
      kicker="Ari-arian",
      intro="Mga krimen laban sa ari-arian (Artikulo 217–224).",
      note=True, arts=[
   ("217","Pagnanakaw (Theft)","Ang sinumang kukuha ng ari-arian ng iba nang walang pahintulot at walang dahas.","Prisión Correccional","240 min","$2,000"),
   ("218","Pagnanakaw na may Dahas (Robbery)","Ang pagkuha ng ari-arian na may kasamang dahas o pananakot.","Prisión Mayor","480 min","$4,000"),
   ("219","Robbery with Violence against Persons","Pagnanakaw na may kasamang pananakit o pagbabanta sa tao.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$4,000"),
   ("220","Estafa (Swindling/Fraud)","Ang panlilinlang upang makuha ang ari-arian o pera ng iba.","Prisión Correccional – Prisión Mayor","240 – 480 min","$1,000"),
   ("221","Malicious Mischief (Paninira ng Ari-arian)","Sadyang pagsira o pagdulot ng pinsala sa ari-arian ng iba.","Prisión Correccional","240 min","$2,000"),
   ("222","Arson (Panununog)","Ang sinumang magsusunog ng ari-arian ng iba.","Reclusión Temporal","720 min","$3,000"),
   ("223","Qualified Theft","Pagnanakaw na may kasamang abuso ng tiwala o espesyal na kalagayan.","Prisión Mayor","480 min","$2,000"),
   ("224","Iba pang Krimen laban sa Ari-arian","Anumang krimen laban sa ari-arian na hindi saklaw ng mga naunang artikulo.","Arresto Mayor – Prisión Correccional","120 – 240 min","$4,000"),
 ]),
 dict(file="kapabayaan.html", pill="Kapabayaan", title="Pabaya o Walang Ingat na Kapabayaan",
      kicker="Kapabayaan",
      intro="Mga krimen ng kapabayaan at kakulangan sa pag-iingat (Artikulo 225–230).",
      note=True, arts=[
   ("225","Labis na Kapabayaan na Nagdulot ng Kamatayan","Ang sinumang dahil sa matinding kapabayaan ay nakapagdulot ng kamatayan ng ibang tao.","Prisión Mayor – Reclusión Temporal","480 – 720 min","$5,000"),
   ("226","Labis na Kapabayaan na Nagdulot ng Malubhang Pinsala","Ang kapabayaan na nagresulta sa seryosong pinsala sa katawan.","Prisión Mayor","480 min","$3,000"),
   ("227","Labis na Kapabayaan na Nagdulot ng Pinsala sa Ari-arian","Ang kapabayaan na nagresulta sa pagkasira o pagkawala ng ari-arian.","Prisión Correccional","240 min","$4,000"),
   ("228","Karaniwang Kapabayaan","Ang kakulangan sa pag-iingat na hindi umabot sa antas ng reckless negligence.","Arresto Mayor","120 min","$5,000"),
   ("229","Karaniwang Kapabayaan ng mga Propesyonal","Ang kapabayaan ng isang taong may espesyal na tungkulin o propesyon (hal. manggagamot, inhinyero, opisyal).","Prisión Mayor","480 min","$4,000"),
   ("230","Iba pang Uri ng Kapabayaan","Anumang kapabayaan na hindi saklaw ng mga naunang artikulo.","Arresto Menor – Prisión Correccional","60 – 240 min","$4,000"),
 ]),
]

# ---------- Generate uniform crime pages ----------
for d in CRIME_PAGES:
    toc = crime_toc(d["arts"])
    body = crime_body(d["kicker"], d["title"], d["intro"], d["arts"], d["note"])
    open(os.path.join(OUT, d["file"]), "w", encoding="utf-8").write(
        page(d["file"], d["title"], d["kicker"], d["title"], toc, body))
    print("wrote", d["file"])

print("CRIME PAGES DONE")
